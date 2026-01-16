#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from bs4 import BeautifulSoup

def extract_photo_info():
    """Extract photo descriptions from backup HTML files"""
    backup_dir = 'backup/galerias'
    photo_info = []

    # Get all f_ll*.htm files
    files = sorted([f for f in os.listdir(backup_dir) if f.startswith('f_ll') and f.endswith('.htm')])

    for filename in files:
        filepath = os.path.join(backup_dir, filename)

        with open(filepath, 'r', encoding='iso-8859-1') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            # Find the image tag
            img = soup.find('img', src=lambda x: x and 'fotos/' in x and x.endswith('.jpg'))
            if img:
                img_src = img['src'].replace('fotos/', '')

                # Normalize filename - replace URL encoded characters
                img_src = img_src.replace('%F1', 'n')  # ñ URL encoded -> n

                # Find description in the <p> tag before the image
                desc_tag = soup.find('p')
                description = ''
                if desc_tag:
                    description = desc_tag.get_text(strip=True)

                photo_info.append({
                    'page_name': filename.replace('.htm', '.html'),
                    'image': img_src,
                    'description': description
                })

    return photo_info

def create_photo_page(photo_data, index, total):
    """Create individual photo page HTML"""

    # Determine prev/next
    prev_page = f"f_ll{index-1}.html" if index > 1 else None
    next_page = f"f_ll{index+1}.html" if index < total else None

    nav_html = '<div class="photo-nav">'
    if prev_page:
        nav_html += f'<a href="{prev_page}" class="nav-prev">← Anterior</a>'
    nav_html += f'<a href="fotos.html" class="nav-gallery">Volver a Galería</a>'
    if next_page:
        nav_html += f'<a href="{next_page}" class="nav-next">Siguiente →</a>'
    nav_html += '</div>'

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Les Luthiers - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-lesluthiers">
    <div id="header-container"></div>

    <div class="layout-container">
        <div id="sidebar-container"></div>

        <main class="main-content">
            <div class="section-content">
                <h1>Les Luthiers</h1>

                {nav_html}

                <div class="photo-display">
                    <img src="../galerias/fotos/{photo_data['image']}" alt="Les Luthiers">
                    {f'<p class="photo-caption">{photo_data["description"]}</p>' if photo_data['description'] else ''}
                </div>

                {nav_html}
            </div>
        </main>
    </div>

    <script src="../js/components.js"></script>
</body>
</html>
'''
    return html

def main():
    print("Extracting photo information...")
    photos = extract_photo_info()

    print(f"Found {len(photos)} photos")

    # Create lesluthiers directory if it doesn't exist
    os.makedirs('lesluthiers', exist_ok=True)

    # Create individual photo pages
    for i, photo in enumerate(photos, 1):
        page_name = photo['page_name']
        html = create_photo_page(photo, i, len(photos))

        output_path = os.path.join('lesluthiers', page_name)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"Created {output_path}")

    print(f"\n✅ Created {len(photos)} photo pages")

if __name__ == '__main__':
    main()
