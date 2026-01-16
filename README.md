# 🎵 Ernesto Acher - Nueva Arquitectura Modular

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Arquitectura](#arquitectura)
- [Instalación](#instalación)
- [Comandos Disponibles](#comandos-disponibles)
- [Estructura de Archivos](#estructura-de-archivos)
- [Cómo Agregar Contenido](#cómo-agregar-contenido)
- [Sistema de Plantillas](#sistema-de-plantillas)
- [Ventajas de la Nueva Arquitectura](#ventajas)

---

## 🎯 Descripción

Sitio web de **Ernesto Acher** construido con un sistema modular basado en:
- **Plantillas Handlebars** para reutilización de componentes
- **Datos centralizados en JSON** como única fuente de verdad
- **Sistema de build automatizado** con validación de enlaces
- **SASS modular** con arquitectura escalable

**Versión**: 2.0.0
**Arquitectura**: Modular basada en plantillas

---

## 🏗️ Arquitectura

### Principios de Diseño

1. **Single Source of Truth**: Todos los datos en archivos JSON
2. **Separación de Responsabilidades**: Contenido, estructura, presentación y estilos separados
3. **Rutas Absolutas**: No más cálculos dinámicos frágiles
4. **Validación Automática**: Enlaces rotos se detectan en build time
5. **A Prueba de Errores**: Imposible crear inconsistencias

### Flujo de Trabajo

```
src/
├── data/          → Configuración y navegación
├── content/       → Contenido HTML de páginas
├── templates/     → Plantillas Handlebars reutilizables
└── scss/          → Estilos modulares

         ↓ npm run build ↓

public/            → Sitio generado listo para deploy
├── *.html         → Páginas generadas
├── css/           → CSS compilado
├── images/        → Imágenes copiadas
└── js/            → JavaScript copiado
```

---

## 🚀 Instalación

```bash
# 1. Instalar dependencias (si no están instaladas)
npm install

# 2. Primer build
npm run build
```

---

## ⚙️ Comandos Disponibles

### Comandos Principales

```bash
# Build completo (limpia, compila SCSS, genera HTML, copia assets)
npm run build

# Build + validación de enlaces
npm start

# Modo desarrollo (watch + live-reload)
npm run dev

# Validar enlaces rotos
npm run validate
```

### Comandos Individuales

```bash
# Solo HTML
npm run build:html

# Solo CSS
npm run sass:build

# Watch SCSS
npm run sass:watch

# Limpiar directorio public
npm run clean

# Copiar assets (imágenes, JS)
npm run copy:assets
```

---

## 📁 Estructura de Archivos

```
/ernestoacher.cl/
│
├── 📂 src/                          # FUENTE (donde editamos)
│   │
│   ├── 📂 data/                     # Datos centralizados
│   │   ├── site.json               # Configuración global
│   │   ├── navigation.json         # TODO el sistema de navegación
│   │   └── sections/               # Configuración por sección
│   │       ├── lesluthiers.json
│   │       ├── labanda.json
│   │       └── ...
│   │
│   ├── 📂 content/                  # Contenido HTML
│   │   ├── lesluthiers.html
│   │   ├── labanda.html
│   │   └── ...
│   │
│   ├── 📂 templates/                # Plantillas Handlebars
│   │   ├── base.html               # <head> + <body> wrapper
│   │   ├── page-interior.html      # Layout páginas interiores
│   │   └── partials/               # Componentes reutilizables
│   │       ├── sidebar.html
│   │       ├── header.html
│   │       ├── nav-right.html
│   │       └── icon.html
│   │
│   └── 📂 scss/                     # Estilos modulares
│       ├── app.scss                # Importador principal
│       ├── _variables.scss         # Variables globales
│       ├── _mixins.scss            # Mixins reutilizables
│       ├── base/                   # Reset, tipografía
│       ├── layout/                 # Layouts principales
│       ├── components/             # Componentes (sidebar, header)
│       └── sections/               # Estilos específicos por sección
│
├── 📂 scripts/                      # Sistema de build
│   ├── build.js                    # Generador de páginas
│   └── validate-links.js           # Validador de enlaces
│
├── 📂 public/                       # SALIDA (generado automáticamente)
│   ├── *.html                      # Páginas generadas
│   ├── css/app.css                 # CSS compilado
│   ├── images/                     # Imágenes copiadas
│   └── js/                         # JavaScript copiado
│
├── 📂 images/                       # Assets originales
├── 📂 js/                           # JavaScript original
│
├── package.json                     # Configuración NPM
└── README.md                        # Esta documentación
```

---

## ✏️ Cómo Agregar Contenido

### Agregar Nueva Sección Principal

**Ejemplo: Agregar sección "Tango Humor"**

#### 1. Crear configuración de sección

`src/data/sections/tangohumor.json`:
```json
{
  "id": "tangohumor",
  "title": "Tango Humor",
  "bodyClass": "page-tangohumor",
  "meta": {
    "description": "Tango Humor - Ernesto Acher",
    "keywords": "tango, humor, Ernesto Acher"
  }
}
```

#### 2. Agregar a navegación

Editar `src/data/navigation.json`, agregar en array `sidebar`:
```json
{
  "id": "tangohumor",
  "label": "Tango Humor",
  "url": "/tangohumor.html",
  "headerImage": "/images/headers/tangohumor.jpg",
  "subPages": [
    { "label": "Comienzo", "url": "/tangohumor.html", "default": true },
    { "label": "Fotos", "url": "/tangohumor/fotos.html" }
  ]
}
```

#### 3. Crear contenido

`src/content/tangohumor.html`:
```html
<h2>El origen del proyecto</h2>
<p>Contenido de la página...</p>
<img src="/images/tangohumor/foto1.jpg" alt="Descripción">
```

#### 4. (Opcional) Estilos específicos

`src/scss/sections/_tangohumor.scss`:
```scss
.page-tangohumor {
  // Estilos únicos solo para esta sección
  .special-element {
    color: $color-accent;
  }
}
```

Importar en `src/scss/app.scss`:
```scss
@use 'sections/tangohumor';
```

#### 5. Regenerar sitio

```bash
npm run build
```

**¡Listo!** La nueva sección está completamente integrada.

---

### Modificar Menús Globales

**Único archivo a editar**: `src/data/navigation.json`

```json
{
  "sidebar": [...],           // Menú izquierdo (secciones principales)
  "headerPrimary": [...],     // Menú con iconos (Inicio, Links, etc.)
  "headerSecondary": [...]    // Menú secundario (Discografía, Anecdotario)
}
```

Después de editar:
```bash
npm run build
```

Los menús se actualizan **automáticamente en todas las páginas**.

---

### Actualizar Contenido Existente

**Editar solo el archivo HTML de contenido:**

```bash
# Editar contenido
vim src/content/lesluthiers.html

# Regenerar
npm run build
```

No necesitas tocar ningún otro archivo. La estructura, menús y estilos se mantienen consistentes.

---

## ✅ Ventajas

### Antes (Arquitectura Antigua)

❌ 61 archivos HTML casi idénticos
❌ Cambiar header = editar 61 archivos
❌ Agregar sección = editar 10+ archivos
❌ Enlaces rotos frecuentes
❌ Rutas calculadas dinámicamente (frágiles)
❌ Menús en 3 lugares diferentes
❌ Alto riesgo de inconsistencias

### Ahora (Nueva Arquitectura)

✅ **4 plantillas reutilizables** (en lugar de 61 HTML)
✅ Cambiar header = **1 archivo** (`partials/header.html`)
✅ Agregar sección = **3 archivos** (JSON + contenido + opcional SCSS)
✅ **Validación automática** de enlaces rotos
✅ **Rutas absolutas** a prueba de errores
✅ Menús en **1 solo lugar** (`navigation.json`)
✅ **Imposible crear inconsistencias**

---

## 🔍 Validación de Enlaces

El sistema incluye un validador que verifica:
- Enlaces internos `<a href="...">`
- Imágenes `<img src="...">`
- Hojas de estilo `<link href="...">`
- Scripts `<script src="...">`

### Ejecutar validación

```bash
# Validar todo el sitio
npm run validate

# Build + validación automática
npm start
```

Si hay enlaces rotos, el build **falla** y muestra reporte detallado.

---

## 🛠️ Desarrollo

### Modo Watch (Recomendado)

```bash
npm run dev
```

Esto inicia:
1. **SASS watch**: Recompila CSS al guardar archivos `.scss`
2. **HTML watch**: Regenera páginas al editar datos/templates/contenido
3. **Live server**: Recarga navegador automáticamente

Abre: http://localhost:3012

### Build de Producción

```bash
# Build optimizado
npm run build

# Build + validación
npm start
```

---

## 📝 Notas Importantes

### Rutas Absolutas

**Siempre usar rutas desde raíz** con `/`:

```html
✅ Correcto:
<a href="/lesluthiers.html">Les Luthiers</a>
<img src="/images/ll/foto.jpg">

❌ Incorrecto:
<a href="lesluthiers.html">
<img src="../images/ll/foto.jpg">
```

### Contenido HTML

Los archivos en `src/content/` son **HTML puro**, no Handlebars.

### IDs de Secciones

Los IDs deben ser consistentes en:
1. `navigation.json` → `"id": "lesluthiers"`
2. `sections/lesluthiers.json` → `"id": "lesluthiers"`
3. `content/lesluthiers.html` → nombre de archivo

---

## 🎉 Resumen

La nueva arquitectura convierte el sitio en un **sistema modular, mantenible y a prueba de errores**.

**Para agregar contenido**:
1. Editar `src/data/navigation.json` (agregar entrada)
2. Crear `src/data/sections/[nombre].json` (configuración)
3. Crear `src/content/[nombre].html` (contenido)
4. Ejecutar `npm run build`

**¡Y listo!** Todo se integra automáticamente sin riesgo de errores.
