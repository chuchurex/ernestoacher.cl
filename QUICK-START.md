# 🚀 Quick Start - Ernesto Acher

## ⚡ Inicio Rápido

```bash
# 1. Build del sitio
npm run build

# 2. Iniciar servidor (puerto 3012)
npm run dev

# 3. Abrir en navegador
open http://localhost:3012
```

---

## 🔧 Comandos Principales

### Build y Deploy

```bash
# Build completo (HTML + CSS + Assets)
npm run build

# Build + Validación de enlaces
npm start
```

### Desarrollo

```bash
# Servidor simple (puerto 3012)
npm run dev

# Solo servidor (sin rebuild)
npm run dev:serve
```

### SCSS

```bash
# Compilar CSS una vez
npm run sass:build

# Watch mode para CSS (recompila al guardar)
npm run sass:watch
```

### Validación

```bash
# Validar todos los enlaces
npm run validate
```

---

## 📝 Flujo de Trabajo Típico

### Para editar contenido:

```bash
# 1. Editar archivo de contenido
vim src/content/lesluthiers.html

# 2. Rebuild
npm run build

# 3. Ver cambios
# Recargar http://localhost:3012 en navegador
```

### Para agregar nueva sección:

```bash
# 1. Crear configuración
vim src/data/sections/nuevaseccion.json

# 2. Agregar a navegación
vim src/data/navigation.json

# 3. Crear contenido
vim src/content/nuevaseccion.html

# 4. Rebuild
npm run build

# 5. Ver resultado
# Abrir http://localhost:3012/nuevaseccion.html
```

### Para modificar estilos:

```bash
# 1. Editar SCSS
vim src/scss/sections/_lesluthiers.scss

# 2. Compilar CSS
npm run sass:build

# 3. Ver cambios
# Recargar navegador (Cmd+R)
```

---

## 🌐 URLs de Desarrollo

### Sitio principal
- **URL**: http://localhost:3012
- **Puerto**: 3012 (según convención del equipo)

### Páginas generadas
- http://localhost:3012/lesluthiers.html
- http://localhost:3012/labandaelastica.html
- http://localhost:3012/humorconachis.html
- http://localhost:3012/veladas.html
- http://localhost:3012/offside.html
- http://localhost:3012/gershwin.html
- http://localhost:3012/animales.html
- http://localhost:3012/detodo.html
- http://localhost:3012/realizaciones.html
- http://localhost:3012/proyectos.html
- http://localhost:3012/menuconciertos.html

---

## 🐛 Solución de Problemas

### El servidor no levanta

```bash
# Verificar si el puerto está ocupado
lsof -ti:3012

# Si está ocupado, liberar
kill -9 $(lsof -ti:3012)

# Reintentar
npm run dev
```

### Los cambios no se reflejan

```bash
# Limpiar y reconstruir
npm run clean
npm run build
```

### Error en build

```bash
# Ver error completo
npm run build

# Si es error de SCSS
npm run sass:build

# Si es error de HTML
npm run build:html
```

---

## 📁 Archivos Clave

### Para editar contenido:
- `src/content/*.html` → Contenido de páginas

### Para editar navegación:
- `src/data/navigation.json` → Menús y estructura

### Para editar estilos:
- `src/scss/` → Todos los estilos

### Para configurar secciones:
- `src/data/sections/*.json` → Config de cada sección

---

## 💡 Tips

### Rebuild rápido
```bash
# Solo HTML (más rápido)
npm run build:html

# Solo CSS (más rápido)
npm run sass:build
```

### Ver estructura generada
```bash
# Listar páginas generadas
ls -lh public/*.html

# Ver tamaño del CSS
ls -lh public/css/app.css
```

### Validar antes de commitear
```bash
# Siempre validar antes de git commit
npm start
```

---

## 🎯 Estado Actual

✅ **11 páginas generadas** correctamente
✅ **CSS compilado** (`public/css/app.css`)
✅ **Assets copiados** (imágenes, JS)
✅ **Servidor corriendo** en puerto 3012

### Contenido actual:
- ✅ Les Luthiers (contenido completo)
- ⚠️ Otras 10 secciones (placeholder)

Para migrar contenido de otras secciones, copiar HTML desde archivos antiguos a `src/content/[seccion].html`

---

## 📚 Más Información

- **README.md** → Documentación completa
- **NUEVA-ARQUITECTURA.md** → Resumen de implementación
- **PUERTO.md** → Info del puerto 3012

---

*Última actualización: 16 Enero 2026*
