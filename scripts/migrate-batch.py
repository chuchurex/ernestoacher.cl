#!/usr/bin/env python3
"""
Migra un lote de páginas desde archive/html-original/ al sistema de templates.
"""

import sys
import re
import json
from pathlib import Path

def extract_content(html_file):
    """Extrae el contenido del <main> de un archivo HTML"""
    try:
        html = html_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  ❌ Error leyendo {html_file}: {e}")
        return None

    # Extraer main content
    match = re.search(r'<main class="main-content">(.*?)</main>', html, re.DOTALL)
    if not match:
        print(f"  ⚠️  No se encontró <main> en {html_file}")
        return None

    content = match.group(1).strip()

    # Convertir rutas relativas a absolutas
    content = re.sub(r'href="([^/"#])', r'href="/\1', content)
    content = re.sub(r'src="([^/"#])', r'src="/\1', content)
    content = re.sub(r'href="\.\./images/', r'href="/images/', content)
    content = re.sub(r'src="\.\./images/', r'src="/images/', content)
    content = re.sub(r'href="\.\.\/', r'href="/', content)
    content = re.sub(r'src="\.\.\/', r'src="/', content)

    return content

def extract_title(html_file):
    """Extrae el título de la página"""
    try:
        html = html_file.read_text(encoding='utf-8')
        match = re.search(r'<title>(.*?)</title>', html)
        if match:
            title = match.group(1)
            # Limpiar " - Ernesto Acher"
            title = re.sub(r'\s*-\s*Ernesto Acher\s*$', '', title)
            return title
    except:
        pass
    return None

def create_section_json(page_id, title, category=None):
    """Crea archivo JSON de sección"""
    section_data = {
        "id": page_id,
        "title": title or page_id.replace('-', ' ').title(),
        "bodyClass": f"page-{page_id}"
    }

    if category:
        section_data["category"] = category

    return section_data

def migrate_page(page_path, category=None, dry_run=False):
    """
    Migra una página individual

    Args:
        page_path: Ruta relativa de la página (ej: 'anecdotas/drodrigo.html')
        category: Categoría opcional para organización
        dry_run: Si True, solo muestra lo que haría sin escribir archivos
    """
    archive_file = Path('archive/html-original') / page_path
    if not archive_file.exists():
        print(f"  ❌ No existe: {archive_file}")
        return False

    # Determinar paths de salida
    page_id = page_path.replace('.html', '').replace('/', '-')
    content_output = Path('src/content') / page_path
    section_json = Path('src/data/sections') / f"{page_id}.json"

    print(f"  📄 Migrando: {page_path}")

    # Extraer contenido
    content = extract_content(archive_file)
    if not content:
        return False

    # Extraer título
    title = extract_title(archive_file)

    if dry_run:
        print(f"    ✓ Contenido extraído ({len(content)} chars)")
        print(f"    ✓ Título: {title or 'N/A'}")
        print(f"    → Content: {content_output}")
        print(f"    → JSON: {section_json}")
        return True

    # Crear directorios si no existen
    content_output.parent.mkdir(parents=True, exist_ok=True)
    section_json.parent.mkdir(parents=True, exist_ok=True)

    # Escribir contenido
    content_output.write_text(content, encoding='utf-8')

    # Escribir JSON
    section_data = create_section_json(page_id, title, category)
    section_json.write_text(json.dumps(section_data, indent=2, ensure_ascii=False), encoding='utf-8')

    print(f"    ✅ Migrado exitosamente")
    return True

def migrate_batch(page_list, category=None, dry_run=False):
    """
    Migra un lote de páginas

    Args:
        page_list: Lista de paths relativos (str o archivo)
        category: Categoría para todas las páginas
        dry_run: Modo de prueba
    """
    # Si es string, asumimos que es un archivo
    if isinstance(page_list, str):
        list_file = Path(page_list)
        if list_file.exists():
            pages = list_file.read_text().splitlines()
        else:
            pages = [page_list]
    else:
        pages = page_list

    # Filtrar líneas vacías y comentarios
    pages = [p.strip() for p in pages if p.strip() and not p.strip().startswith('#')]

    print(f"\n{'=' * 60}")
    print(f"  MIGRACIÓN EN BATCH")
    print(f"{'=' * 60}")
    print(f"Páginas a migrar: {len(pages)}")
    print(f"Categoría: {category or 'N/A'}")
    print(f"Modo: {'DRY RUN (prueba)' if dry_run else 'PRODUCCIÓN'}")
    print(f"{'=' * 60}\n")

    success_count = 0
    fail_count = 0

    for page in pages:
        try:
            if migrate_page(page, category, dry_run):
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"  ❌ Error en {page}: {e}")
            fail_count += 1

    print(f"\n{'=' * 60}")
    print(f"  RESUMEN")
    print(f"{'=' * 60}")
    print(f"✅ Exitosas: {success_count}")
    print(f"❌ Fallidas: {fail_count}")
    print(f"{'=' * 60}\n")

    if dry_run:
        print("⚠️  Modo DRY RUN - No se escribieron archivos")
        print("   Ejecutar sin --dry-run para aplicar cambios\n")

    return success_count, fail_count

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Migra páginas HTML del archivo al sistema de templates'
    )
    parser.add_argument(
        'pages',
        help='Archivo con lista de páginas o página individual'
    )
    parser.add_argument(
        '--category',
        help='Categoría para organización'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Modo de prueba (no escribe archivos)'
    )

    args = parser.parse_args()

    migrate_batch(args.pages, args.category, args.dry_run)

if __name__ == '__main__':
    main()
