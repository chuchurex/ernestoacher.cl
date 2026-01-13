#!/bin/bash
# =============================================================================
# Deploy script para ernestoacher.cl
# Sube el sitio a Hostinger vía rsync
# =============================================================================

# Cargar variables de entorno
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "Error: Archivo .env no encontrado"
    exit 1
fi

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Deploying ernestoacher.cl ===${NC}"

# Verificar que las variables existen
if [ -z "$UPLOAD_HOST" ] || [ -z "$UPLOAD_USER" ] || [ -z "$UPLOAD_DIR" ]; then
    echo -e "${RED}Error: Faltan variables de entorno${NC}"
    exit 1
fi

# Archivos a subir
FILES_TO_SYNC=(
    "index.html"
    "css/"
    "js/"
    "assets/"
    "favicon.ico"
)

echo -e "${BLUE}Subiendo archivos...${NC}"

# Usar rsync con SSH
sshpass -p "$UPLOAD_PASS" rsync -avz \
    --port=$UPLOAD_PORT \
    --progress \
    --delete \
    --exclude='.git' \
    --exclude='.env' \
    --exclude='node_modules' \
    --exclude='deploy.sh' \
    --exclude='README.md' \
    --exclude='CONTEXTO-PROYECTO.md' \
    -e "ssh -p $UPLOAD_PORT" \
    ./ ${UPLOAD_USER}@${UPLOAD_HOST}:${UPLOAD_DIR}/

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Deploy exitoso${NC}"
    echo -e "${GREEN}✓ Sitio disponible en: https://${DOMAIN}${NC}"

    # Opcional: Purgar cache de Cloudflare
    if [ ! -z "$CF_ZONE_ID" ]; then
        echo -e "${BLUE}Purgando cache de Cloudflare...${NC}"
        curl -X POST "https://api.cloudflare.com/client/v4/zones/${CF_ZONE_ID}/purge_cache" \
            -H "X-Auth-Email: ${CF_EMAIL}" \
            -H "X-Auth-Key: ${CF_API_KEY}" \
            -H "Content-Type: application/json" \
            --data '{"purge_everything":true}'
        echo -e "${GREEN}✓ Cache purgado${NC}"
    fi
else
    echo -e "${RED}✗ Error en deploy${NC}"
    exit 1
fi
