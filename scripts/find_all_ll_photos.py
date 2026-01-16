#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from bs4 import BeautifulSoup

# All page numbers that exist in backup
page_numbers = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21,
                23, 24, 26, 27, 28, 33, 35, 36, 37, 38, 41, 43, 44, 45, 46, 47, 48, 50, 51]

all_photos = []

for num in page_numbers:
    filepath = f'backup/galerias/f_ll{num}.htm'

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='iso-8859-1') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            # Find the large image
            img = soup.find('img', src=lambda x: x and 'fotos/' in x and x.endswith('.jpg'))
            if img:
                img_src = img['src'].replace('fotos/', '')
                img_src = img_src.replace('%F1', 'n')  # Fix encoding

                # Get thumbnail name
                thumb_name = img_src.replace('.jpg', '_jpg.jpg')

                # Find description
                p_tag = soup.find('p')
                description = p_tag.get_text(strip=True) if p_tag else ''

                all_photos.append({
                    'page_num': num,
                    'image': img_src,
                    'thumb': thumb_name,
                    'description': description
                })

                print(f"f_ll{num}: {img_src}")
                if description:
                    print(f"  Desc: {description[:60]}...")

print(f"\n=== Total: {len(all_photos)} photos ===")
