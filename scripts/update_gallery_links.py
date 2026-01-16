#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from bs4 import BeautifulSoup

def extract_photo_mapping():
    """Extract mapping between photo files and page numbers"""
    backup_dir = 'backup/galerias'
    mapping = {}

    # Get all f_ll*.htm files
    files = [f for f in os.listdir(backup_dir) if f.startswith('f_ll') and f.endswith('.htm')]

    for filename in files:
        filepath = os.path.join(backup_dir, filename)

        with open(filepath, 'r', encoding='iso-8859-1') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            # Find the image tag
            img = soup.find('img', src=lambda x: x and 'fotos/' in x and x.endswith('.jpg'))
            if img:
                img_src = img['src'].replace('fotos/', '')
                page_num = filename.replace('f_ll', '').replace('.htm', '')
                mapping[img_src] = page_num

    return mapping

def main():
    # Extract mapping
    mapping = extract_photo_mapping()

    # Current gallery structure from fotos.html
    # We need to map the thumbnails we're using to the correct pages
    gallery_photos = [
        'll_explicado1_jpg.jpg',
        'll_explicado2_jpg.jpg',
        'll_gabrrossettoea_jpg.jpg',  # This is "ll_gabo2_jpg.jpg" in current file
        'll_gero72_jpg.jpg',
        'll_falmm_jpg.jpg',
        'll_los2mm_jpg.jpg',
        'll_cafepuerto1_jpg.jpg',
        'll_cuarteto_jpg.jpg',
        'll_benedetti_jpg.jpg',
        'll_fcolon2_jpg.jpg',
        'll_fcolon7_jpg.jpg',
        'll_fcolon8_jpg.jpg',
        'll_gallinita1_jpg.jpg',
        'll_gulevandia_jpg.jpg',
        'll_jm_ea_gm_jpg.jpg',
        'll_menotti_jpg.jpg',
        'll_osk_ek_jpg.jpg',
        'll_rey_enam_jpg.jpg',
        'll_añoralgias_jpg.jpg',
        'll_vinicius1_jpg.jpg',
        'll_tyo_grab_jpg.jpg'
    ]

    # Print mapping for reference
    print("Photo to page mapping:")
    for photo in gallery_photos:
        # Convert thumbnail name to full image name
        full_img = photo.replace('_jpg.jpg', '.jpg')
        if full_img in mapping:
            print(f"{photo} -> f_ll{mapping[full_img]}.html")
        else:
            print(f"{photo} -> NOT FOUND (searching...)")
            # Try without special chars
            alt_name = full_img.replace('añ', 'a%F1')
            if alt_name in mapping:
                print(f"  Found as {alt_name} -> f_ll{mapping[alt_name]}.html")

if __name__ == '__main__':
    main()
