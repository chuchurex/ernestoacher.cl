#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from pathlib import Path

# Leer archivo
source_file = Path("/Users/chuchurex/Sites/prod/ernestoacher.cl/backup/lbe/index.htm")

with open(source_file, 'r', encoding='iso-8859-1', errors='ignore') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# Buscar todos los td con colspan
print("=" * 80)
print("Buscando TD con colspan...")
print("=" * 80)

for td in soup.find_all('td'):
    colspan = td.get('colspan')
    rowspan = td.get('rowspan')
    if colspan or rowspan:
        # Obtener preview del contenido
        text_preview = td.get_text()[:100].replace('\n', ' ').strip()
        print(f"\nTD con colspan={colspan}, rowspan={rowspan}")
        print(f"Contenido preview: {text_preview}...")

        # Ver si tiene h1, h2 o p
        has_h1 = td.find('h1')
        has_h2 = td.find('h2')
        has_p = td.find('p')
        print(f"Contiene: h1={bool(has_h1)}, h2={bool(has_h2)}, p={bool(has_p)}")

print("\n" + "=" * 80)
print("Buscando H2 'Cómo empezó la historia'...")
print("=" * 80)

for h2 in soup.find_all('h2'):
    if 'empez' in h2.get_text():
        print(f"\nEncontrado H2: {h2.get_text()}")
        # Obtener el padre
        parent = h2.find_parent('td')
        if parent:
            print(f"Padre TD:")
            print(f"  - width: {parent.get('width')}")
            print(f"  - valign: {parent.get('valign')}")
            # Obtener todo el contenido del td
            content_preview = parent.get_text()[:300].replace('\n', ' ').strip()
            print(f"  - Contenido: {content_preview}...")
