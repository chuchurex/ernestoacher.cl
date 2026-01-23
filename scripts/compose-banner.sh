#!/bin/bash
# ==============================================
# Banner Composer - Compone banners panorámicos
# desde fotos individuales del archivo
# ==============================================
# Uso: ./scripts/compose-banner.sh <prefijo> <output> [num_fotos]
#
# Ejemplos:
#   ./scripts/compose-banner.sh lbe labandaelastica-banner 6
#   ./scripts/compose-banner.sh ll lesluthiers-banner 6
#   ./scripts/compose-banner.sh hp veladas-banner 4
#
# El script:
# 1. Busca fotos horizontales con el prefijo dado
# 2. Selecciona las N mejores (más anchas vs altas)
# 3. Las recorta a un alto uniforme centrado
# 4. Las une horizontalmente con fondo negro
# 5. Guarda el resultado en assets/images/

FOTOS_DIR="galerias/fotos"
OUTPUT_DIR="assets/images"
BANNER_HEIGHT=300  # Alto del recorte en px

PREFIX="${1:-lbe}"
OUTPUT_NAME="${2:-banner}"
NUM_FOTOS="${3:-6}"

echo "🎨 Banner Composer"
echo "   Prefijo: ${PREFIX}_*"
echo "   Output:  ${OUTPUT_DIR}/${OUTPUT_NAME}.png"
echo "   Fotos:   ${NUM_FOTOS}"
echo ""

# Buscar fotos horizontales (ancho > alto) con el prefijo
echo "📷 Buscando fotos horizontales con prefijo '${PREFIX}_'..."
CANDIDATES=()
while IFS= read -r line; do
    file=$(echo "$line" | cut -d' ' -f1)
    CANDIDATES+=("$file")
done < <(find "$FOTOS_DIR" -name "${PREFIX}_*.jpg" ! -name "*_jpg*" -exec sh -c '
    dims=$(magick identify -format "%w %h" "$1" 2>/dev/null)
    w=$(echo "$dims" | cut -d" " -f1)
    h=$(echo "$dims" | cut -d" " -f2)
    if [ "$w" -gt "$h" ] 2>/dev/null; then
        ratio=$(echo "scale=2; $w / $h" | bc)
        echo "$1 $ratio"
    fi
' _ {} \; | sort -t' ' -k2 -rn)

echo "   Encontradas: ${#CANDIDATES[@]} fotos horizontales"

if [ ${#CANDIDATES[@]} -lt "$NUM_FOTOS" ]; then
    echo "⚠️  Solo hay ${#CANDIDATES[@]} fotos disponibles, usando todas"
    NUM_FOTOS=${#CANDIDATES[@]}
fi

if [ ${#CANDIDATES[@]} -eq 0 ]; then
    echo "❌ No se encontraron fotos con prefijo '${PREFIX}_'"
    exit 1
fi

# Seleccionar las N fotos con mejor ratio (más panorámicas)
SELECTED=("${CANDIDATES[@]:0:$NUM_FOTOS}")

echo ""
echo "✅ Fotos seleccionadas:"
for f in "${SELECTED[@]}"; do
    dims=$(magick identify -format "%wx%h" "$f" 2>/dev/null)
    echo "   - $(basename $f) ($dims)"
done

# Crear directorio temporal
TMPDIR=$(mktemp -d)
echo ""
echo "🔧 Procesando fotos (recorte central a ${BANNER_HEIGHT}px de alto)..."

i=0
for f in "${SELECTED[@]}"; do
    # Redimensionar al alto del banner manteniendo proporción, luego recortar centro
    magick "$f" \
        -resize "x${BANNER_HEIGHT}" \
        -gravity center \
        -extent "x${BANNER_HEIGHT}" \
        "${TMPDIR}/part_${i}.png"
    i=$((i + 1))
done

# Unir horizontalmente con fondo negro
echo "🔗 Uniendo ${NUM_FOTOS} fotos horizontalmente..."
magick "${TMPDIR}"/part_*.png +append -background black -flatten "${OUTPUT_DIR}/${OUTPUT_NAME}.png"

# Mostrar resultado
RESULT_DIMS=$(magick identify -format "%wx%h" "${OUTPUT_DIR}/${OUTPUT_NAME}.png" 2>/dev/null)
echo ""
echo "✨ Banner creado: ${OUTPUT_DIR}/${OUTPUT_NAME}.png (${RESULT_DIMS})"
echo ""
echo "📋 Siguiente paso: Sube la resolución con Gemini AI usando este prompt:"
echo "   'Upscale this image to 4x resolution maintaining the photographic quality,"
echo "    preserve the black background, enhance facial details and lighting.'"

# Limpiar
rm -rf "$TMPDIR"
