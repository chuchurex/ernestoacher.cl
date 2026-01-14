#!/bin/bash
#
# Download ALL remaining sections from Wayback Machine
# Comprehensive download of all Ernesto Acher website sections
#

set -e

BASE_DIR="/Users/chuchurex/Sites/prod/ernestoacher.cl/backup"
LOG_FILE="/Users/chuchurex/Sites/prod/ernestoacher.cl/all_sections_download.log"

# Initialize log
echo "=====================================================================" > "$LOG_FILE"
echo "ERNESTO ACHER WEBSITE - COMPLETE SECTION DOWNLOAD" >> "$LOG_FILE"
echo "=====================================================================" >> "$LOG_FILE"
echo "Started: $(date)" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
TOTAL_SUCCESS=0
TOTAL_FAIL=0
TOTAL_SIZE=0

# Function to download a page
download_page() {
    local section="$1"
    local filename="$2"
    local timestamp="$3"

    local url="https://web.archive.org/web/${timestamp}id_/http://www.ernestoacher.com/${section}/${filename}"
    local output_dir="${BASE_DIR}/${section}"
    local output_file="${output_dir}/${filename}"

    mkdir -p "$output_dir"

    echo "  Downloading ${filename} from ${timestamp}..."

    if curl -f -s -L --max-time 30 -o "$output_file" "$url" 2>/dev/null; then
        local size=$(wc -c < "$output_file" | tr -d ' ')
        echo -e "    ${GREEN}✓${NC} Saved ($size bytes)"
        echo "    ✓ ${section}/${filename} - Success ($size bytes)" >> "$LOG_FILE"
        return 0
    else
        echo -e "    ${RED}✗${NC} Failed"
        echo "    ✗ ${section}/${filename} - Failed" >> "$LOG_FILE"
        return 1
    fi
}

# Function to try multiple timestamps
try_multiple_timestamps() {
    local section="$1"
    local filename="$2"

    # Timestamps to try
    local timestamps=(
        "20090519200000"  # May 19, 2009
        "20090521184931"  # May 21, 2009
        "20090416022827"  # April 16, 2009
        "20091004221547"  # October 4, 2009
        "20090301000000"  # March 1, 2009
        "20090630000000"  # June 30, 2009
    )

    for timestamp in "${timestamps[@]}"; do
        if download_page "$section" "$filename" "$timestamp"; then
            return 0
        fi
        sleep 1
    done

    return 1
}

# Function to download a section
download_section() {
    local section="$1"
    local section_name="$2"

    echo ""
    echo "======================================================================"
    echo "SECTION: ${section_name} (${section}/)"
    echo "======================================================================"
    echo "" | tee -a "$LOG_FILE"
    echo "Section: ${section_name} (${section}/)" >> "$LOG_FILE"

    local section_success=0
    local section_fail=0

    # Standard pages to try
    local pages=(
        "index.htm"
        "espect.htm"
        "discos.htm"
        "fotos.htm"
        "videos.htm"
        "audio.htm"
    )

    # Also try numbered detail pages (like e1.htm, e2.htm, etc.)
    for i in {1..10}; do
        pages+=("e${i}.htm")
        pages+=("d${i}.htm")
        pages+=("f${i}.htm")
    done

    for page in "${pages[@]}"; do
        if try_multiple_timestamps "$section" "$page"; then
            ((section_success++))
            ((TOTAL_SUCCESS++))
        else
            ((section_fail++))
            ((TOTAL_FAIL++))
        fi
        sleep 2
    done

    echo ""
    echo "  Section Summary:"
    echo "    Success: ${section_success}"
    echo "    Failed: ${section_fail}"
    echo "" >> "$LOG_FILE"
    echo "  Summary: ${section_success} success, ${section_fail} failed" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
}

# Main execution
echo "======================================================================"
echo "ERNESTO ACHER WEBSITE - COMPLETE SECTION DOWNLOAD"
echo "======================================================================"
echo ""
echo "Downloading 9 sections from Wayback Machine"
echo "Time period: 2009 (May preferred)"
echo "Base directory: ${BASE_DIR}"
echo ""

# Download each section
download_section "hca" "Humor con Achís (Unipersonal)"
sleep 3

download_section "ve" "Veladas (Conciertos de música humor)"
sleep 3

download_section "ocho" "Offside Chamber Orchestra"
sleep 3

download_section "hg" "Homenaje a Gershwin"
sleep 3

download_section "ladm" "Los animales de la música"
sleep 3

download_section "dtodo" "De todo como en botica"
sleep 3

download_section "rr" "Realizaciones recientes"
sleep 3

download_section "proyectos" "Nuevos proyectos"
sleep 3

download_section "menu" "Menú de conciertos"

# Final summary
echo ""
echo "======================================================================"
echo "FINAL DOWNLOAD SUMMARY"
echo "======================================================================"
echo "Total files downloaded: ${TOTAL_SUCCESS}"
echo "Total files failed: ${TOTAL_FAIL}"
echo "All files saved to: ${BASE_DIR}"
echo ""

# Calculate total size
TOTAL_SIZE=$(find "$BASE_DIR" -type f -name "*.htm" -exec wc -c {} + | tail -1 | awk '{print $1}')
TOTAL_SIZE_MB=$(echo "scale=2; $TOTAL_SIZE / 1024 / 1024" | bc)
echo "Total size: ${TOTAL_SIZE} bytes (${TOTAL_SIZE_MB} MB)"
echo ""

# List downloaded directories
echo "Downloaded sections:"
for dir in "$BASE_DIR"/*/; do
    if [ -d "$dir" ]; then
        local dir_name=$(basename "$dir")
        local file_count=$(find "$dir" -name "*.htm" -type f | wc -l | tr -d ' ')
        echo "  - ${dir_name}/ (${file_count} files)"
    fi
done

echo ""
echo "======================================================================"
echo "Ended: $(date)" >> "$LOG_FILE"
echo ""
echo -e "${GREEN}Download complete!${NC}"
echo "Full log saved to: ${LOG_FILE}"
