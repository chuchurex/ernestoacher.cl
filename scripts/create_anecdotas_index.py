#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from pathlib import Path

def extract_category_and_clean_title(title):
    """Extrae la categoría del título y devuelve el título limpio"""

    # Detectar categorías por prefijos
    if title.startswith("(Les Luthiers)"):
        return "Les Luthiers", title.replace("(Les Luthiers)", "").strip()
    elif title.startswith("(La Banda Elástica)"):
        return "La Banda Elástica", title.replace("(La Banda Elástica)", "").strip()
    elif title.startswith("(Gershwin"):
        return "Gershwin", title.split(")", 1)[1].strip()
    else:
        return "General", title

def main():
    data_dir = Path('/Users/chuchurex/Sites/prod/ernestoacher.cl/data/anecdotas')

    anecdotas = []

    # Leer todos los archivos JSON
    for json_file in sorted(data_dir.glob('*.json')):
        if json_file.name == 'index.json':
            continue

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extraer categoría y limpiar título
        category, clean_title = extract_category_and_clean_title(data['title'])

        # Actualizar el archivo JSON con la categoría y título limpio
        data['category'] = category
        data['cleanTitle'] = clean_title

        # Guardar el archivo actualizado
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # Agregar al índice
        anecdotas.append({
            'id': data['id'],
            'title': data['title'],
            'cleanTitle': clean_title,
            'category': category
        })

        print(f"Procesado: {json_file.name}")
        print(f"  Categoría: {category}")
        print(f"  Título original: {data['title']}")
        print(f"  Título limpio: {clean_title}")
        print()

    # Organizar por categorías
    categories = {}
    for anecdota in anecdotas:
        cat = anecdota['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(anecdota)

    # Crear el índice
    index = {
        'total': len(anecdotas),
        'categories': categories,
        'all': anecdotas
    }

    # Guardar el índice
    index_file = data_dir / 'index.json'
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"Índice creado: {index_file}")
    print(f"Total de anécdotas: {len(anecdotas)}")
    print(f"\nPor categoría:")
    for cat, items in categories.items():
        print(f"  {cat}: {len(items)}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
