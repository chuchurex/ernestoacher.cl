#!/bin/bash
# ==============================================
# Banner Assembler - Reconstruye banners originales
# desde slices de tabla Dreamweaver/Fireworks
# ==============================================
# Uso: ./scripts/assemble-banner.sh <seccion> <output>
#
# Secciones: ll, lbe, hca, ve
#
# Ensambla los slices con sus offsets verticales correctos
# y recorta la cortina roja decorativa

SECTION="${1:-lbe}"
OUTPUT="${2:-assets/images/${SECTION}-banner.png}"
SLICES_DIR="/tmp/banners/${SECTION}"

echo "🎨 Banner Assembler - Sección: ${SECTION}"

if [ ! -d "$SLICES_DIR" ]; then
    echo "❌ No se encontró directorio de slices: $SLICES_DIR"
    exit 1
fi

# Geometría de la tabla original:
# Las piezas del banner van escalonadas verticalmente.
# Offsets Y relativos al inicio de la zona del banner:
#   t3 = Y:0  (inicio)
#   t4 = Y:7  (fila 3 tiene height parcial de 7px antes de t4)
#   t5 = Y:24 (t4 tiene 17px de height visible)
#   t6 = Y:37 (t5 tiene 13px antes)
#   t7 = Y:39 (t6 tiene 2px antes)
#   t8 = Y:54 (t7 tiene 15px antes)
#   t9 = Y:71 (t8 tiene 17px antes)

# Orden horizontal de columnas en la foto:
# c6(39) | c7(166) | c11(98) | c12(53) | c14(45) | c15(39) | c17(23) | c18(68)
# (c2 y c5 son elementos de navegación/decoración, no foto)

# Calcular ancho total del banner (solo piezas de foto)
# y crear canvas negro del tamaño correcto

# Definir piezas según sección (orden horizontal y offset Y)
# Formato: archivo,offset_x,offset_y
case "$SECTION" in
    ll)
        PIECES=(
            "i_t6_c6.jpg,0,37"
            "i_t3_c7.jpg,39,0"
            "i_t3_c11.jpg,205,0"
            "i_t4_c12.jpg,303,7"
            "i_t5_c14.jpg,356,24"
        )
        CANVAS_W=401
        CANVAS_H=124
        ;;
    lbe)
        PIECES=(
            "i_t6_c6.jpg,0,37"
            "i_t3_c7.jpg,39,0"
            "i_t3_c11.jpg,205,0"
            "i_t4_c12.jpg,303,7"
            "i_t5_c14.jpg,356,24"
            "i_t7_c15.jpg,401,39"
            "i_t8_c17.jpg,440,54"
        )
        CANVAS_W=463
        CANVAS_H=124
        ;;
    hca)
        PIECES=(
            "i_t6_c6.jpg,0,37"
            "i_t3_c7.jpg,39,0"
            "i_t3_c11.jpg,205,0"
            "i_t4_c12.jpg,303,7"
            "i_t5_c14.jpg,356,24"
            "i_t7_c15.jpg,401,39"
        )
        CANVAS_W=440
        CANVAS_H=124
        ;;
    ve)
        PIECES=(
            "i_t6_c6.jpg,0,37"
            "i_t3_c7.jpg,39,0"
            "i_t3_c11.jpg,205,0"
            "i_t4_c12.jpg,303,7"
            "i_t5_c14.jpg,356,24"
            "i_t7_c15.jpg,401,39"
            "i_t8_c17.jpg,440,54"
            "i_t9_c18.jpg,463,71"
        )
        CANVAS_W=531
        CANVAS_H=124
        ;;
    *)
        echo "❌ Sección desconocida: $SECTION"
        echo "   Opciones: ll, lbe, hca, ve"
        exit 1
        ;;
esac

echo "   Canvas: ${CANVAS_W}x${CANVAS_H}"
echo "   Piezas: ${#PIECES[@]}"

# Crear canvas negro y posicionar cada pieza
CMD="magick -size ${CANVAS_W}x${CANVAS_H} xc:black"
for piece in "${PIECES[@]}"; do
    IFS=',' read -r file x y <<< "$piece"
    if [ -f "${SLICES_DIR}/${file}" ]; then
        CMD+=" ${SLICES_DIR}/${file} -geometry +${x}+${y} -composite"
        echo "   ✓ ${file} → +${x}+${y}"
    else
        echo "   ⚠ No encontrado: ${file}"
    fi
done
CMD+=" ${OUTPUT}"

# Ejecutar
eval $CMD

if [ -f "$OUTPUT" ]; then
    DIMS=$(magick identify -format "%wx%h" "$OUTPUT")
    echo ""
    echo "✨ Banner ensamblado: ${OUTPUT} (${DIMS})"
else
    echo "❌ Error al crear el banner"
    exit 1
fi
