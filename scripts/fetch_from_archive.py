#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import time
from bs4 import BeautifulSoup

# Read URLs from file
urls = {}
with open('archive_photo_urls.txt', 'r') as f:
    for line in f:
        num, url = line.strip().split('\t')
        urls[int(num)] = url

print(f"Found {len(urls)} URLs to fetch\n")

os.makedirs('temp_archive', exist_ok=True)

photo_data = {}
failed = []

for num in sorted(urls.keys()):
    url = urls[num]
    print(f"Fetching f_ll{num} from archive.org...")

    # Try to download with curl
    temp_file = f'temp_archive/f_ll{num}.htm'

    try:
        result = subprocess.run(
            ['curl', '-s', '-L', '--max-time', '30', url, '-o', temp_file],
            capture_output=True,
            timeout=35
        )

        if result.returncode == 0 and os.path.exists(temp_file):
            # Parse the downloaded HTML
            with open(temp_file, 'r', encoding='iso-8859-1', errors='ignore') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

                # Find the description paragraph
                p_tag = soup.find('p')
                description = ''
                if p_tag:
                    description = p_tag.get_text(strip=True)

                # Find the image
                img = soup.find('img', src=lambda x: x and 'fotos/' in x and x.endswith('.jpg'))
                img_name = ''
                img_url = ''

                if img:
                    img_src = img['src']
                    img_name = img_src.replace('fotos/', '').replace('%F1', 'n')

                    # Construct full image URL from archive.org
                    # Extract timestamp from the page URL
                    timestamp = url.split('/web/')[1].split('/')[0]
                    img_url = f"https://web.archive.org/web/{timestamp}/http://www.ernestoacher.com/galerias/fotos/{img_src.replace('fotos/', '')}"

                if img_name and description:
                    photo_data[num] = {
                        'image': img_name,
                        'description': description,
                        'img_url': img_url
                    }
                    print(f"  ✓ Found: {img_name}")
                    print(f"  📝 {description[:60]}...")
                else:
                    print(f"  ⚠ Incomplete data")
                    failed.append(num)
        else:
            print(f"  ✗ Download failed")
            failed.append(num)

    except Exception as e:
        print(f"  ✗ Error: {e}")
        failed.append(num)

    # Be nice to archive.org - wait between requests
    time.sleep(2)

print(f"\n{'='*60}")
print(f"Successfully fetched: {len(photo_data)}/{len(urls)}")
print(f"Failed: {len(failed)}")

if failed:
    print(f"\nFailed numbers: {failed}")

# Save the extracted data
if photo_data:
    print(f"\nSaving extracted data...")
    with open('extracted_photo_data.txt', 'w', encoding='utf-8') as f:
        for num in sorted(photo_data.keys()):
            data = photo_data[num]
            f.write(f"{num}\t{data['image']}\t{data['description']}\t{data['img_url']}\n")

    print(f"✅ Data saved to extracted_photo_data.txt")

    # Now download the images
    print(f"\nDownloading images...")
    downloaded = 0
    for num in sorted(photo_data.keys()):
        data = photo_data[num]
        img_name = data['image']
        img_url = data['img_url']

        dest = f"galerias/fotos/{img_name}"

        # Only download if we don't have it
        if not os.path.exists(dest):
            print(f"  Downloading {img_name}...")
            try:
                result = subprocess.run(
                    ['curl', '-s', '-L', '--max-time', '30', img_url, '-o', dest],
                    capture_output=True,
                    timeout=35
                )
                if result.returncode == 0:
                    print(f"    ✓ Downloaded")
                    downloaded += 1
                else:
                    print(f"    ✗ Failed")
            except:
                print(f"    ✗ Error")

            time.sleep(1)
        else:
            print(f"  ✓ {img_name} already exists")

    print(f"\n✅ Downloaded {downloaded} new images")
