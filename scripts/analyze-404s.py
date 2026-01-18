#!/usr/bin/env python3
"""
Analiza los enlaces rotos detectados por el validador y genera un inventario categorizado.
"""

import subprocess
import re
from pathlib import Path
from collections import defaultdict

def run_validation():
    """Ejecuta npm run validate y captura salida"""
    print("🔍 Ejecutando validación de enlaces...\n")
    result = subprocess.run(
        ['npm', 'run', 'validate'],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    return result.stdout + result.stderr

def extract_broken_links(validation_output):
    """Extrae enlaces únicos rotos de la salida del validador"""
    # Buscar líneas con → seguido de URL
    broken_links = re.findall(r'→\s+(/[^\n\s]+\.html)', validation_output)
    # También buscar links relativos sin /
    relative_links = re.findall(r'→\s+([^/\n\s]+\.html)', validation_output)

    return sorted(set(broken_links)), sorted(set(relative_links))

def categorize_links(links):
    """Clasifica enlaces por tipo/directorio"""
    categories = defaultdict(list)

    for link in links:
        if link.startswith('/anecdotas/'):
            categories['anecdotas'].append(link)
        elif link.startswith('/lesluthiers/') and any(x in link for x in ['f_ll', '197', '198']):
            categories['lesluthiers_especiales'].append(link)
        elif link.startswith('/labandaelastica/') and any(x in link for x in ['e', 'disco']):
            categories['labanda_especiales'].append(link)
        elif link.startswith('/humorconachis/'):
            categories['humorconachis_especiales'].append(link)
        elif link.startswith('/veladas/'):
            categories['veladas_especiales'].append(link)
        elif link.startswith('/detodo/'):
            categories['detodo_especiales'].append(link)
        elif link.startswith('/realizaciones/'):
            categories['realizaciones_especiales'].append(link)
        elif link.startswith('/offside/'):
            categories['offside_especiales'].append(link)
        elif link.startswith('/animales/'):
            categories['animales_especiales'].append(link)
        elif link.count('/') == 1:  # Solo / al inicio
            categories['root'].append(link)
        else:
            categories['otros'].append(link)

    return categories

def check_archive_existence(links):
    """Verifica qué enlaces existen en archive/html-original/"""
    archive_path = Path('archive/html-original')
    results = {}

    for link in links:
        # Convertir /path/file.html -> path/file.html
        filepath = link[1:] if link.startswith('/') else link
        exists = (archive_path / filepath).exists()
        results[link] = exists

    return results

def generate_report(categories, archive_status, relative_links):
    """Genera reporte markdown del inventario"""
    report = []
    report.append("# 📊 INVENTARIO DE PÁGINAS 404\n")
    report.append(f"**Fecha**: {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}\n")

    total_links = sum(len(links) for links in categories.values())
    report.append(f"**Total de enlaces rotos únicos**: {total_links}\n")
    report.append(f"**Enlaces relativos (sin /)**: {len(relative_links)}\n")
    report.append("\n---\n")

    # Por cada categoría
    for category, links in sorted(categories.items()):
        exists_count = sum(1 for link in links if archive_status.get(link, False))
        report.append(f"\n## {category.upper().replace('_', ' ')}")
        report.append(f"**Total**: {len(links)} páginas")
        report.append(f"**Existen en archive**: {exists_count}/{len(links)}\n")

        # Mostrar primeras 15
        for i, link in enumerate(links[:15]):
            exists = archive_status.get(link, False)
            status = '✅ EXISTE' if exists else '❌ FALTA'
            report.append(f"{i+1}. {status} `{link}`")

        if len(links) > 15:
            report.append(f"\n*... y {len(links) - 15} páginas más*\n")

    # Enlaces relativos
    if relative_links:
        report.append("\n## ENLACES RELATIVOS (SIN /)")
        report.append(f"**Total**: {len(relative_links)} enlaces\n")
        for i, link in enumerate(relative_links[:10]):
            report.append(f"{i+1}. ⚠️  `{link}` (debería ser `/{link}`)")
        if len(relative_links) > 10:
            report.append(f"\n*... y {len(relative_links) - 10} más*\n")

    # Resumen de prioridades
    report.append("\n---\n")
    report.append("\n## 🎯 RESUMEN DE PRIORIDADES\n")

    priority_table = []
    priority_table.append("| Categoría | Páginas | En Archive | Prioridad | Acción |")
    priority_table.append("|-----------|---------|------------|-----------|--------|")

    priorities = {
        'root': ('ALTA', '✅ Migrar'),
        'anecdotas': ('MEDIA', '✅ Migrar en batch'),
        'lesluthiers_especiales': ('BAJA', '⚠️  Evaluar necesidad'),
        'labanda_especiales': ('BAJA', '⚠️  Evaluar necesidad'),
        'otros': ('BAJA', '❌ Ignorar')
    }

    for category, links in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
        exists_count = sum(1 for link in links if archive_status.get(link, False))
        priority, action = priorities.get(category, ('MEDIA', '⚠️  Revisar'))
        priority_table.append(
            f"| {category.replace('_', ' ')} | {len(links)} | {exists_count} | {priority} | {action} |"
        )

    report.extend(priority_table)

    return '\n'.join(report)

def main():
    print("=" * 60)
    print("  ANÁLISIS DE PÁGINAS 404")
    print("=" * 60)
    print()

    # Ejecutar validación
    output = run_validation()

    # Extraer enlaces rotos
    absolute_links, relative_links = extract_broken_links(output)
    print(f"✓ Enlaces absolutos rotos encontrados: {len(absolute_links)}")
    print(f"✓ Enlaces relativos encontrados: {len(relative_links)}\n")

    # Categorizar
    categories = categorize_links(absolute_links)
    print(f"✓ Categorías identificadas: {len(categories)}\n")

    # Verificar existencia en archive
    print("🔍 Verificando archivos en archive/html-original/...")
    all_links = absolute_links + [f"/{link}" for link in relative_links]
    archive_status = check_archive_existence(all_links)
    exists_total = sum(1 for exists in archive_status.values() if exists)
    print(f"✓ Archivos existentes: {exists_total}/{len(all_links)}\n")

    # Generar reporte
    print("📝 Generando reporte...")
    report = generate_report(categories, archive_status, relative_links)

    # Guardar
    output_file = Path('INVENTARIO_404.md')
    output_file.write_text(report, encoding='utf-8')
    print(f"✓ Reporte guardado: {output_file}\n")

    # Mostrar resumen en consola
    print("=" * 60)
    print("  RESUMEN")
    print("=" * 60)
    for category, links in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"{category.upper().replace('_', ' '):30s} {len(links):3d} páginas")
    print("=" * 60)
    print(f"\n✅ Análisis completado. Ver detalles en: INVENTARIO_404.md\n")

if __name__ == '__main__':
    main()
