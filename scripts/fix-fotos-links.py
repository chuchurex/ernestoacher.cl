#!/usr/bin/env python3
"""
Fix internal navigation links in fotos pages.
Changes absolute paths like /f_ll5.html to relative paths like f_ll5.html
"""

from pathlib import Path
import re

def fix_fotos_links(content):
    """Fix links in fotos content"""
    # Fix f_ll*.html links to be relative instead of absolute
    content = re.sub(r'href="/f_(ll\d+)\.html"', r'href="f_\1.html"', content)

    # Fix /fotos.html to point to parent directory (lesluthiers-fotos.html)
    content = content.replace('href="/fotos.html"', 'href="../lesluthiers-fotos.html"')

    return content

def main():
    fotos_dir = Path('src/content/lesluthiers')

    # Process all f_ll*.html files
    fotos_files = sorted(fotos_dir.glob('f_ll*.html'))

    print(f"🔧 Procesando {len(fotos_files)} archivos de fotos...")

    for file_path in fotos_files:
        content = file_path.read_text(encoding='utf-8')
        fixed_content = fix_fotos_links(content)

        if content != fixed_content:
            file_path.write_text(fixed_content, encoding='utf-8')
            print(f"  ✓ {file_path.name}")
        else:
            print(f"  - {file_path.name} (sin cambios)")

    print(f"\n✅ Completado: {len(fotos_files)} archivos procesados")

if __name__ == '__main__':
    main()
