#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
from bs4 import BeautifulSoup

# Process all downloaded HTML files
photo_captions = {}
temp_dir = 'temp_archive'

print("Processing downloaded archive.org pages...")

for filename in os.listdir(temp_dir):
    if filename.startswith('f_ll') and filename.endswith('.htm'):
        filepath = os.path.join(temp_dir, filename)

        with open(filepath, 'r', encoding='iso-8859-1', errors='ignore') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            # Find description
            p_tag = soup.find('p')
            description = ''
            if p_tag:
                description = p_tag.get_text(strip=True)

            # Find image name
            img = soup.find('img', src=lambda x: x and 'fotos/' in x and x.endswith('.jpg'))
            if img and description:
                img_src = img['src']
                # Extract just the filename from archive.org path
                # Format: /web/TIMESTAMP/http://...fotos/FILENAME.jpg
                img_name = img_src.split('/')[-1].replace('%F1', 'n')
                photo_captions[img_name] = description
                print(f"  ✓ {filename}: {img_name}")
                print(f"    {description[:70]}...")

print(f"\nExtracted {len(photo_captions)} photo captions")

# Add the ll_francia1 caption manually
photo_captions['ll_francia1.jpg'] = 'En el parador de Francia, frente a "La fusita", Punta del Este, verano de 1973. Parados: Gerardo Masana, Vladimiro y Francia, Carlos Núñez, Marcos Mundstock y Josefina. Sentados: Susy Mendelievich, Daniel Rabinovich, moi y Carlos López Puccio.'

print("\n" + "="*70)
print("Step 1: Copying photos from inbox/fotos to galerias/fotos")

copied = 0
for img_name in photo_captions.keys():
    src = f'inbox/fotos/{img_name}'
    dest = f'galerias/fotos/{img_name}'

    if os.path.exists(src):
        if not os.path.exists(dest):
            shutil.copy2(src, dest)
            print(f"  ✓ Copied {img_name}")
            copied += 1
        else:
            print(f"  - {img_name} (already exists)")
    else:
        print(f"  ⚠ Missing in inbox: {img_name}")

print(f"\nCopied {copied} new photos")

print("\n" + "="*70)
print("Step 2: Updating HTML pages with captions")

# Find all photo HTML pages
updated = 0
for html_file in os.listdir('lesluthiers'):
    if html_file.startswith('f_ll') and html_file.endswith('.html'):
        filepath = f'lesluthiers/{html_file}'

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')

        # Find the image
        img_tag = soup.find('img', src=lambda x: x and 'galerias/fotos/' in x)
        if img_tag:
            img_src = img_tag['src']
            img_name = img_src.split('/')[-1]

            # Check if we have a caption for this image
            if img_name in photo_captions:
                caption_tag = soup.find('p', class_='photo-caption')

                if caption_tag:
                    # Update caption
                    old_text = caption_tag.get_text(strip=True)
                    new_text = photo_captions[img_name]

                    if old_text != new_text:
                        caption_tag.string = new_text

                        # Save updated HTML (preserve original formatting)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(str(soup))

                        print(f"  ✓ Updated {html_file}")
                        updated += 1
                    else:
                        print(f"  - {html_file} (already correct)")

print(f"\n✅ Updated {updated} HTML pages")
print(f"✅ Total captions in database: {len(photo_captions)}")
