#!/bin/bash
# Download La Banda Elástica content from Wayback Machine

BASE_DIR="/Users/chuchurex/Sites/prod/ernestoacher.cl/backup/lbe"
mkdir -p "$BASE_DIR"

echo "============================================================"
echo "La Banda Elástica Content Download"
echo "============================================================"
echo ""

SUCCESS=0
FAIL=0

download_page() {
    local filename="$1"
    local timestamp="$2"
    local url="https://web.archive.org/web/${timestamp}id_/http://www.ernestoacher.com/lbe/${filename}"
    local output="${BASE_DIR}/${filename}"

    echo "Downloading ${filename} from ${timestamp}..."

    if curl -s -f -L -o "$output" "$url"; then
        size=$(wc -c < "$output" | tr -d ' ')
        echo "  ✓ Saved to ${output} (${size} bytes)"
        ((SUCCESS++))
    else
        echo "  ✗ Error downloading ${filename}"
        ((FAIL++))
    fi

    sleep 2
}

# Download main pages
download_page "index.htm" "20090519200000"
download_page "espect.htm" "20090521184931"
download_page "discos.htm" "20090519200438"
download_page "fotos.htm" "20090416022827"
download_page "videos.htm" "20090519200443"
download_page "audio.htm" "20090519200433"

# Download spectacle detail pages
download_page "e1.htm" "20091004221547"
download_page "e2.htm" "20091004114718"
download_page "e3.htm" "20091004114723"
download_page "e4.htm" "20091004221617"

echo ""
echo "============================================================"
echo "DOWNLOAD SUMMARY"
echo "============================================================"
echo "Successfully downloaded: $SUCCESS"
echo "Failed: $FAIL"
echo ""
echo "All files saved to: ${BASE_DIR}"
echo ""

echo "Downloaded files:"
ls -lh "${BASE_DIR}"/*.htm 2>/dev/null | awk '{print "  - " $9 " (" $5 ")"}'
