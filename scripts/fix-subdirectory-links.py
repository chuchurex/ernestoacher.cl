#!/usr/bin/env python3
"""
Fix internal navigation links in subdirectory pages (años, fotos).
Changes absolute paths to correct relative paths.
"""

from pathlib import Path
import re

def fix_años_links(content):
    """Fix links in años content"""
    # Fix /espectaculos.html to point to parent directory
    content = content.replace('href="/espectaculos.html"', 'href="../lesluthiers-espectaculos.html"')

    return content

def main():
    # Fix años pages
    años_dir = Path('src/content/lesluthiers')
    años_files = [f for f in años_dir.glob('*.html') if f.stem.isdigit()]

    print(f"🔧 Procesando {len(años_files)} archivos de años...")

    for file_path in sorted(años_files):
        content = file_path.read_text(encoding='utf-8')
        fixed_content = fix_años_links(content)

        if content != fixed_content:
            file_path.write_text(fixed_content, encoding='utf-8')
            print(f"  ✓ {file_path.name}")
        else:
            print(f"  - {file_path.name} (sin cambios)")

    print(f"\n✅ Completado: {len(años_files)} archivos procesados")

if __name__ == '__main__':
    main()
