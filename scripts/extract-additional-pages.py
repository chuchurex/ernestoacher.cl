#!/usr/bin/env python3
"""
Extrae páginas adicionales que no están en el script original
"""
import re
from pathlib import Path

# Páginas adicionales a migrar
pages = [
    'anecdotario.html',
    'humorconachis-fotos.html',
    'labandaelastica-discografia.html',
    'labandaelastica-fotos.html',
    'lesluthiers-discografia.html',
    'lesluthiers-fotos.html',
    'offside-fotos.html',
    'veladas-fotos.html'
]

for page in pages:
    input_file = Path(f'archive/html-original/{page}')
    output_file = Path(f'src/content/{page}')

    if not input_file.exists():
        print(f"⚠️  Saltando {page} (no existe)")
        continue

    html = input_file.read_text(encoding='utf-8')

    # Extract main content
    match = re.search(r'<main class="main-content">(.*?)</main>', html, re.DOTALL)

    if match:
        content = match.group(1).strip()
        # Convert relative URLs to absolute
        content = re.sub(r'href="([^/"#])', r'href="/\1', content)
        content = re.sub(r'src="([^/"#])', r'src="/\1', content)
        content = re.sub(r'href="\.\./images/', r'href="/images/', content)
        content = re.sub(r'src="\.\./images/', r'src="/images/', content)

        output_file.write_text(content, encoding='utf-8')
        print(f'✅ Extraído: {page}')
    else:
        print(f'❌ No se encontró main-content en {page}')

print('\n✅ Extracción de páginas adicionales completada')
