#!/bin/bash

# Configuration
INPUT_DIR="inbox/fotos"
OUTPUT_DIR="inbox/fotos/optimized"
TARGET_WIDTH=1500

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to process a single image
process_image() {
    local input_file="$1"
    local base_name=$(basename "$input_file")
    local output_file="$OUTPUT_DIR/$base_name"

    echo "Processing $base_name..."

    convert "$input_file" \
        -filter Lanczos \
        -resize "${TARGET_WIDTH}x>" \
        -despeckle \
        -unsharp 0x1+1+0.05 \
        -quality 95 \
        -interlace Plane \
        "$output_file"
}

# Check if specific files are passed as arguments
if [ "$#" -gt 0 ]; then
    for file in "$@"; do
        process_image "$file"
    done
else
    # Process all jpg files in input directory
    for file in "$INPUT_DIR"/*.jpg; do
        process_image "$file"
    done
fi

echo "Done. Optimized images are in $OUTPUT_DIR"
