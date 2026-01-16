#!/bin/bash

# Script para iniciar servidor de desarrollo de forma segura
# Maneja puerto ocupado y errores de build

PORT=3012
PROJECT_NAME="ernestoacher.cl"

echo "🚀 Iniciando servidor de desarrollo para $PROJECT_NAME"
echo ""

# Función para liberar puerto
free_port() {
    if lsof -ti:$PORT > /dev/null 2>&1; then
        echo "⚠️  Puerto $PORT ocupado. Liberando..."
        kill -9 $(lsof -ti:$PORT) 2>/dev/null
        sleep 1
        echo "✅ Puerto $PORT liberado"
    fi
}

# Función para limpiar al salir
cleanup() {
    echo ""
    echo "🛑 Deteniendo servidor..."
    kill -9 $(lsof -ti:$PORT) 2>/dev/null
    echo "✅ Servidor detenido"
    exit 0
}

# Capturar Ctrl+C
trap cleanup SIGINT SIGTERM

# Liberar puerto si está ocupado
free_port

# Ejecutar build
echo ""
echo "📦 Ejecutando build..."
echo ""

npm run build 2>&1 | grep -v "Deprecation Warning" | grep -v "DEPRECATION" | grep -v "More info"

if [ $? -ne 0 ]; then
    echo "❌ Error en el build"
    exit 1
fi

echo ""
echo "✅ Build completado"
echo ""

# Iniciar servidor
echo "🌐 Iniciando servidor en puerto $PORT..."
echo ""
echo "   URL: http://localhost:$PORT"
echo ""
echo "   Presiona Ctrl+C para detener el servidor"
echo ""

cd public && python3 -m http.server $PORT
