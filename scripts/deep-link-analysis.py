#!/usr/bin/env python3
"""
Análisis profundo de enlaces rotos - Navega por todas las páginas y verifica cada enlace
"""

import re
from pathlib import Path
from collections import defaultdict
from urllib.parse import urljoin, urlparse

def extract_links_from_html(html_file):
    """Extrae todos los enlaces href de un archivo HTML"""
    try:
        content = html_file.read_text(encoding='utf-8')
        # Buscar todos los href
        links = re.findall(r'href=["\']([^"\']+)["\']', content)
        return links
    except Exception as e:
        print(f"Error leyendo {html_file}: {e}")
        return []

def normalize_link(link, source_page):
    """Normaliza un enlace relativo a absoluto"""
    # Ignorar enlaces externos, mailto, tel, #anchors
    if any(link.startswith(x) for x in ['http://', 'https://', 'mailto:', 'tel:', '#', 'javascript:']):
        return None

    # Eliminar anchors
    link = link.split('#')[0]
    if not link or link == '/':
        return None

    # Si es absoluto (empieza con /), usar directamente
    if link.startswith('/'):
        return link

    # Si es relativo, resolver desde la página fuente
    source_dir = Path(source_page).parent
    if source_dir == Path('.'):
        resolved = f"/{link}"
    else:
        resolved = f"/{source_dir}/{link}"

    # Limpiar ../ y ./
    parts = resolved.split('/')
    clean_parts = []
    for part in parts:
        if part == '..':
            if clean_parts:
                clean_parts.pop()
        elif part and part != '.':
            clean_parts.append(part)

    return '/' + '/'.join(clean_parts) if clean_parts else '/'

def check_link_exists(link, public_dir):
    """Verifica si un enlace existe en el directorio public"""
    # Convertir link a path
    if link.startswith('/'):
        link = link[1:]

    file_path = public_dir / link

    # Verificar si existe como archivo
    if file_path.exists():
        return True

    # Si no tiene extensión, probar con .html
    if not file_path.suffix:
        html_path = public_dir / f"{link}.html"
        if html_path.exists():
            return True

    return False

def analyze_all_pages():
    """Analiza todas las páginas HTML en public/"""
    public_dir = Path('public')
    archive_dir = Path('archive/html-original')

    # Encontrar todas las páginas HTML
    html_files = list(public_dir.rglob('*.html'))

    print("=" * 70)
    print("  ANÁLISIS PROFUNDO DE ENLACES ROTOS")
    print("=" * 70)
    print(f"\n📄 Analizando {len(html_files)} páginas HTML...\n")

    # Diccionarios para rastrear
    broken_links = defaultdict(list)  # link -> [páginas que lo referencian]
    all_links_found = set()
    pages_with_issues = defaultdict(int)

    # Analizar cada página
    for html_file in html_files:
        rel_path = html_file.relative_to(public_dir)
        links = extract_links_from_html(html_file)

        for link in links:
            normalized = normalize_link(link, str(rel_path))
            if not normalized:
                continue

            all_links_found.add(normalized)

            # Verificar si existe
            if not check_link_exists(normalized, public_dir):
                broken_links[normalized].append(str(rel_path))
                pages_with_issues[str(rel_path)] += 1

    # Ordenar por cantidad de referencias (más problemáticos primero)
    sorted_broken = sorted(broken_links.items(), key=lambda x: len(x[1]), reverse=True)

    print(f"🔍 Enlaces únicos encontrados: {len(all_links_found)}")
    print(f"❌ Enlaces rotos únicos: {len(broken_links)}")
    print(f"📄 Páginas con problemas: {len(pages_with_issues)}\n")

    # Categorizar enlaces rotos
    categories = {
        'discografia': [],
        'fotos': [],
        'anecdotas': [],
        'espectaculos': [],
        'videos': [],
        'audio': [],
        'años': [],
        'otros': []
    }

    for link, sources in sorted_broken:
        if '/anecdotas/' in link:
            categories['anecdotas'].append((link, sources))
        elif 'disco' in link:
            categories['discografia'].append((link, sources))
        elif 'foto' in link or 'f_ll' in link:
            categories['fotos'].append((link, sources))
        elif 'espectaculo' in link:
            categories['espectaculos'].append((link, sources))
        elif 'video' in link:
            categories['videos'].append((link, sources))
        elif 'audio' in link:
            categories['audio'].append((link, sources))
        elif any(year in link for year in ['1971', '1972', '1975', '1976', '1977', '1979', '1981', '1985', '1986']):
            categories['años'].append((link, sources))
        else:
            categories['otros'].append((link, sources))

    # Generar reporte
    report = []
    report.append("# 🔍 ANÁLISIS PROFUNDO DE ENLACES ROTOS\n")
    report.append(f"**Fecha**: {Path('INVENTARIO_404.md').stat().st_mtime}\n")
    report.append(f"**Páginas analizadas**: {len(html_files)}")
    report.append(f"**Enlaces únicos encontrados**: {len(all_links_found)}")
    report.append(f"**Enlaces rotos únicos**: {len(broken_links)}\n")
    report.append("---\n")

    # Reporte por categoría
    for cat_name, cat_links in categories.items():
        if not cat_links:
            continue

        report.append(f"\n## {cat_name.upper()}")
        report.append(f"**Total**: {len(cat_links)} enlaces rotos\n")

        for link, sources in cat_links[:30]:  # Primeros 30
            # Verificar si existe en archive
            archive_path = archive_dir / link[1:]  # Quitar /
            exists_in_archive = archive_path.exists()
            status = "✅ EN ARCHIVE" if exists_in_archive else "❌ NO EN ARCHIVE"

            report.append(f"\n### `{link}`")
            report.append(f"- **Estado**: {status}")
            report.append(f"- **Referencias**: {len(sources)} página(s)")
            report.append(f"- **Desde**: {', '.join(sources[:3])}")
            if len(sources) > 3:
                report.append(f"  *...y {len(sources) - 3} más*")

        if len(cat_links) > 30:
            report.append(f"\n*...y {len(cat_links) - 30} enlaces más en esta categoría*")

    # Top páginas con más problemas
    report.append("\n---\n")
    report.append("\n## 📊 PÁGINAS CON MÁS ENLACES ROTOS\n")
    top_pages = sorted(pages_with_issues.items(), key=lambda x: x[1], reverse=True)[:20]
    for page, count in top_pages:
        report.append(f"- **{page}**: {count} enlaces rotos")

    # Lista plana de todos los enlaces rotos para fácil referencia
    report.append("\n---\n")
    report.append("\n## 📋 LISTA COMPLETA DE ARCHIVOS FALTANTES\n")
    report.append("*Para buscar en archive.org:*\n")

    for link, sources in sorted_broken:
        archive_path = archive_dir / link[1:]
        if not archive_path.exists():
            report.append(f"- `{link}` (referenciado {len(sources)}x)")

    # Guardar reporte
    output_file = Path('ANALISIS_ENLACES_PROFUNDO.md')
    output_file.write_text('\n'.join(report), encoding='utf-8')

    print("=" * 70)
    print(f"✅ Reporte guardado en: {output_file}")
    print("=" * 70)

    # Mostrar resumen en consola
    print("\n📊 RESUMEN POR CATEGORÍA:\n")
    for cat_name, cat_links in categories.items():
        if cat_links:
            in_archive = sum(1 for link, _ in cat_links
                           if (archive_dir / link[1:]).exists())
            print(f"{cat_name.upper():20s} {len(cat_links):3d} enlaces "
                  f"({in_archive} en archive)")

    print("\n" + "=" * 70)

    return broken_links, categories

if __name__ == '__main__':
    analyze_all_pages()
