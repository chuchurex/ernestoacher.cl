#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from bs4 import BeautifulSoup

def extract_photos_from_gallery(filepath):
    """Extract all photo links from a gallery page"""
    photos = []

    with open(filepath, 'r', encoding='iso-8859-1') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

        # Find all links to photo pages
        for link in soup.find_all('a', href=re.compile(r'../galerias/f_ll\d+\.htm')):
            img = link.find('img')
            if img and 'src' in img.attrs:
                # Extract page number
                page_match = re.search(r'f_ll(\d+)\.htm', link['href'])
                if page_match:
                    page_num = int(page_match.group(1))

                    # Extract thumbnail info
                    thumb_src = img['src'].replace('../galerias/fotos/', '')
                    thumb_src = thumb_src.replace('%F1', 'n')  # Fix encoding

                    width = img.get('width', '100')
                    height = img.get('height', '100')

                    photos.append({
                        'page_num': page_num,
                        'thumb': thumb_src,
                        'width': width,
                        'height': height
                    })

    return photos

def main():
    # Extract from both pages
    photos_page1 = extract_photos_from_gallery('backup/ll/fotos.htm')
    photos_page2 = extract_photos_from_gallery('backup/ll/fotos2.htm')

    # Combine and deduplicate
    all_photos = {}
    for photo in photos_page1 + photos_page2:
        all_photos[photo['page_num']] = photo

    # Sort by page number
    sorted_photos = sorted(all_photos.values(), key=lambda x: x['page_num'])

    print(f"Total unique photos found: {len(sorted_photos)}\n")

    print("Photos from fotos.htm (page 1):")
    for photo in photos_page1:
        print(f"  f_ll{photo['page_num']}: {photo['thumb']} ({photo['width']}x{photo['height']})")

    print(f"\nPhotos from fotos2.htm (page 2):")
    for photo in photos_page2:
        print(f"  f_ll{photo['page_num']}: {photo['thumb']} ({photo['width']}x{photo['height']})")

    print(f"\n=== SUMMARY ===")
    print(f"Total photos in fotos.htm: {len(photos_page1)}")
    print(f"Total photos in fotos2.htm: {len(photos_page2)}")
    print(f"Unique photos (combined): {len(sorted_photos)}")

    # Save list for gallery generation
    with open('photo_list.txt', 'w') as f:
        for photo in sorted_photos:
            f.write(f"{photo['page_num']}\t{photo['thumb']}\t{photo['width']}\t{photo['height']}\n")

    print(f"\nPhoto list saved to photo_list.txt")

if __name__ == '__main__':
    main()
