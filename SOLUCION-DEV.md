# 🔧 Solución al Problema de `npm run dev`

## 🎯 Problema Resuelto

Antes, `npm run dev` fallaba si el puerto 3012 estaba ocupado con error:
```
OSError: [Errno 48] Address already in use
```

## ✅ Solución Implementada

Creado script robusto `scripts/dev-server.sh` que:

1. **Verifica puerto**: Detecta si 3012 está ocupado
2. **Libera automáticamente**: Mata proceso si es necesario
3. **Ejecuta build**: Con mensajes limpios (sin warnings de SASS)
4. **Inicia servidor**: De forma segura
5. **Maneja Ctrl+C**: Limpia puerto al salir

## 🚀 Uso

```bash
# Ahora simplemente ejecuta:
npm run dev
```

El script automáticamente:
- ✅ Libera puerto 3012 si está ocupado
- ✅ Ejecuta build completo
- ✅ Inicia servidor
- ✅ Muestra URL clara: http://localhost:3012
- ✅ Captura Ctrl+C para detener limpiamente

## 📝 Características

### Mensajes Claros
```
🚀 Iniciando servidor de desarrollo para ernestoacher.cl

⚠️  Puerto 3012 ocupado. Liberando...
✅ Puerto 3012 liberado

📦 Ejecutando build...
✅ Build completado

🌐 Iniciando servidor en puerto 3012...
   URL: http://localhost:3012

   Presiona Ctrl+C para detener el servidor
```

### Filtrado de Warnings
Los warnings de deprecación de SASS se ocultan automáticamente para mantener output limpio.

### Limpieza Automática
Al presionar Ctrl+C:
```
🛑 Deteniendo servidor...
✅ Servidor detenido
```

## 🔧 Comandos Disponibles

```bash
# Servidor de desarrollo (recomendado)
npm run dev

# Build sin servidor
npm run build

# Solo servidor (sin build)
npm run dev:serve

# Validar enlaces
npm run validate
```

## 📁 Archivos Modificados

1. **scripts/dev-server.sh** (NUEVO)
   - Script bash robusto
   - Manejo de puerto ocupado
   - Limpieza automática

2. **package.json**
   - `"dev": "./scripts/dev-server.sh"`
   - Usa script en lugar de comando directo

## 🎯 Ventajas

✅ **A prueba de errores**: No falla si puerto ocupado
✅ **Limpio**: Sin warnings molestos
✅ **Informativo**: Mensajes claros del proceso
✅ **Seguro**: Limpia puerto al salir
✅ **Simple**: Un solo comando para todo

## 🐛 Solución de Problemas

Si aún falla:

```bash
# 1. Verificar que script sea ejecutable
chmod +x scripts/dev-server.sh

# 2. Liberar puerto manualmente
kill -9 $(lsof -ti:3012)

# 3. Ejecutar script directamente
./scripts/dev-server.sh
```

---

**Fecha**: 16 Enero 2026
**Estado**: ✅ Funcionando
