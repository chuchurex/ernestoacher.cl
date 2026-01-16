#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from bs4 import BeautifulSoup

def extract_show_data(year):
    """Extract show data from backup HTML file"""
    filepath = f'backup/ll/{year}.htm'

    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r', encoding='iso-8859-1') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

        # Find the content area
        h2 = soup.find('h2')
        if not h2:
            return None

        # Extract title (text before <br>)
        title_parts = []
        for content in h2.contents:
            if content.name == 'br':
                break
            if isinstance(content, str):
                title_parts.append(content.strip())

        title = ' '.join(title_parts)

        # Find venue/date info (first h5 after h2 WITHOUT strong tag)
        venue = ''
        for h5 in h2.find_next_siblings('h5'):
            if not h5.find('strong'):
                # This is the venue, convert to plain text
                venue = h5.get_text(separator=' ', strip=True)
                break

        # Extract all songs (h5 with strong tags)
        songs = []
        for h5 in soup.find_all('h5'):
            strong = h5.find('strong')
            if strong:
                song_name = strong.get_text(strip=True)
                if song_name and song_name != '':
                    songs.append(song_name)

        return {
            'year': year,
            'title': f'{title}<br>{year}',
            'venue': venue,
            'songs': songs
        }

def create_show_html(data):
    """Create HTML page for a show"""

    songs_html = '\n'.join([f'                  <h5><strong>{song}</strong></h5>' for song in data['songs']])

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']} - Les Luthiers - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-lesluthiers">
    <div id="header-container"></div>

    <div class="layout-container">
        <div id="sidebar-container"></div>

        <main class="main-content">
            <div class="section-content">
                <h1>Les Luthiers</h1>

                <p><a href="espectaculos.html">← Volver a Espectáculos</a></p>

                <h2>{data['title']}</h2>

                <h5>{data['venue']}</h5>

                <h3>Repertorio</h3>

{songs_html}
            </div>
        </main>
    </div>

    <script src="../js/components.js"></script>
</body>
</html>
'''
    return html

def main():
    years = ['1971', '1972', '1975', '1976', '1977', '1979', '1981', '1985', '1986']

    os.makedirs('lesluthiers', exist_ok=True)

    for year in years:
        print(f"Processing {year}...")
        data = extract_show_data(year)

        if data:
            html = create_show_html(data)
            output_path = f'lesluthiers/{year}.html'

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)

            print(f"  ✓ Created {output_path}")
            print(f"    Title: {data['title']}")
            print(f"    Songs: {len(data['songs'])}")
        else:
            print(f"  ✗ Failed to extract data for {year}")

    print(f"\n✅ Migration complete!")

if __name__ == '__main__':
    main()
