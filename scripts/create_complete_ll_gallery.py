#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup

# All page numbers that exist
page_numbers = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21,
                23, 24, 26, 27, 28, 33, 35, 36, 37, 38, 41, 43, 44, 45, 46, 47, 48, 50, 51]

def extract_thumb_info(page_num):
    """Extract thumbnail info from backup HTML"""
    filepath = f'backup/galerias/f_ll{page_num}.htm'

    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r', encoding='iso-8859-1') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

        # Find the large image
        img = soup.find('img', src=lambda x: x and 'fotos/' in x and x.endswith('.jpg'))
        if img:
            img_src = img['src'].replace('fotos/', '')
            img_src = img_src.replace('%F1', 'n')  # Fix encoding

            # Get thumbnail name
            thumb_name = img_src.replace('.jpg', '_jpg.jpg')

            # Check thumbnail dimensions from backup
            width = img.get('width', '100')
            height = img.get('height', '100')

            # Estimate thumbnail dimensions (usually max 100px)
            try:
                w = int(width)
                h = int(height)
                if w > h:
                    thumb_width = 100
                    thumb_height = int(h * 100 / w)
                else:
                    thumb_height = 100
                    thumb_width = int(w * 100 / h)
            except:
                thumb_width = 100
                thumb_height = 100

            return {
                'page_num': page_num,
                'thumb': thumb_name,
                'width': thumb_width,
                'height': thumb_height
            }

    return None

# Extract all photos
all_photos = []
for num in page_numbers:
    photo = extract_thumb_info(num)
    if photo:
        all_photos.append(photo)

print(f"Extracted {len(all_photos)} photos")

# Generate gallery HTML
rows = []
current_row = []

for i, photo in enumerate(all_photos):
    cell = f'<td><a href="f_ll{photo["page_num"]}.html"><img src="../galerias/fotos/{photo["thumb"]}" width="{photo["width"]}" height="{photo["height"]}" alt="Les Luthiers"></a></td>'
    current_row.append(cell)

    # Complete row with 4 columns
    if len(current_row) == 4:
        rows.append('<tr>\n                                ' + '\n                                '.join(current_row) + '\n                            </tr>')
        current_row = []

# Add final row with remaining cells (pad with empty cells)
if current_row:
    while len(current_row) < 4:
        current_row.append('<td>&nbsp;</td>')
    rows.append('<tr>\n                                ' + '\n                                '.join(current_row) + '\n                            </tr>')

table_html = '\n                            '.join(rows)

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fotos - Les Luthiers - Ernesto Acher</title>
    <meta name="description" content="Fotos - Les Luthiers">
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-lesluthiers">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>Les Luthiers</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li><a href="index.html">- Comienzo</a></li>
                            <li><a href="espectaculos.html">- Espectáculos</a></li>
                            <li><a href="discografia.html">- Discografía</a></li>
                            <li class="active">- Fotos</li>
                            <li><a href="videos.html">- Videos</a></li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <div class="photo-gallery">
                        <table>
                            {table_html}
                        </table>
                    </div>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>
'''

# Write gallery
with open('lesluthiers/fotos.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Gallery created with {len(all_photos)} photos in {len(rows)} rows")
