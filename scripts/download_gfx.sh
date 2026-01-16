#!/bin/bash
# Script para descargar imágenes de directorios gfx

DOMAIN="ernestoacher.com"
TIMESTAMP="20090601"  # Timestamp medio del rango
OUTPUT_DIR="backup"

# Función para descargar una imagen
download_image() {
    local path=$1
    local filename=$2
    local output_path="$OUTPUT_DIR/$path/$filename"

    # Crear directorio si no existe
    mkdir -p "$OUTPUT_DIR/$path"

    # Si ya existe, skip
    if [ -f "$output_path" ]; then
        echo "  ⊘ Ya existe: $filename"
        return 0
    fi

    # URL de Wayback Machine
    local wayback_url="https://web.archive.org/web/${TIMESTAMP}id_/http://${DOMAIN}/${path}/${filename}"

    # Descargar
    if curl -s -f -o "$output_path" "$wayback_url"; then
        echo "  ✓ Descargado: $filename"
        sleep 0.5
        return 0
    else
        echo "  ✗ Error: $filename"
        rm -f "$output_path" 2>/dev/null
        return 1
    fi
}

echo "================================"
echo "🖼️  DESCARGA DE IMÁGENES GFX"
echo "================================"

# Arrays de imágenes por directorio
declare -A images

# gfx raíz (compartido)
images[gfx]="spacer.gif"

# ll/gfx (Les Luthiers)
images[ll/gfx]="rodrigo.jpg discos.jpg espect.jpg escenassueltas.jpg lacola.jpg teresaeloso.jpg vientosgitanos.jpg i_t3_c11.jpg i_t3_c7.jpg i_t4_c12.jpg i_t5_c14.jpg i_t6_c6.jpg"

# Descargar por directorio
for dir in "${!images[@]}"; do
    echo ""
    echo "📁 $dir"
    echo "---"

    for img in ${images[$dir]}; do
        download_image "$dir" "$img"
    done
done

echo ""
echo "✅ Descarga completada"
