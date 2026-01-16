#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read bookmarks file
with open('/Users/chuchurex/Desktop/bookmarks_16_01_26.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all archive.org URLs for f_ll photos
urls = re.findall(r'HREF="(https://web\.archive\.org/web/\d+/http://www\.ernestoacher\.com/galerias/f_ll\d+\.htm)"', content)

# Parse and organize
photo_urls = {}
for url in urls:
    # Extract photo number
    match = re.search(r'f_ll(\d+)\.htm', url)
    if match:
        num = int(match.group(1))
        photo_urls[num] = url

# Sort by number
sorted_urls = sorted(photo_urls.items())

print(f"Found {len(sorted_urls)} photo URLs\n")

# Save to file
with open('archive_photo_urls.txt', 'w') as f:
    for num, url in sorted_urls:
        f.write(f"{num}\t{url}\n")
        print(f"f_ll{num}: {url}")

print(f"\n✅ URLs saved to archive_photo_urls.txt")
