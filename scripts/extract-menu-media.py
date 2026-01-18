#!/usr/bin/env python3
import re
from pathlib import Path

pages = ['galerias', 'discografia', 'anecdotario-modular', 'partituras', 'links', 'contacto']

for page in pages:
    input_file = Path(f'archive/html-original/{page}.html')
    output_file = Path(f'src/content/{page}.html')

    if not input_file.exists():
        print(f"⚠️  Saltando {page}.html (no existe)")
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
        print(f'✅ Extraído: {page}.html')
    else:
        print(f'❌ No se encontró main-content en {page}.html')

print('\n✅ Extracción completada')
