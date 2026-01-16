# Continuación de Migración - Ernesto Acher Website

**Fecha de creación:** 15 de enero de 2026
**Contexto:** Migración completa del sitio ernestoacher.com.ar a ernestoacher.cl

## 📋 Estado Actual del Proyecto

### ✅ Secciones Completadas (2/13)

#### 1. Les Luthiers ✅
- **Ubicación:** `/lesluthiers/` + `/lesluthiers.html` (raíz)
- **Archivos:** 15 páginas HTML
- **Datos:** 15 JSON en `/data/lesluthiers/`
- **Imágenes:** 108 imágenes en `/images/ll/` (2.1 MB)
- **Estilos:** `scss/pages/_lesluthiers.scss`
- **Estado:** 100% completo con navegación corregida

**Estructura de archivos:**
```
lesluthiers/
├── index.html (← ../lesluthiers.html)
├── espectaculos.html
├── discografia.html
├── fotos.html
├── fotos2.html
├── videos.html
├── 1971.html (Opus Pi)
├── 1972.html (Recital '72)
├── 1975.html (Recital '75)
├── 1976.html (Viejos Fracasos)
├── 1977.html (Mastropiero que Nunca)
├── 1979.html (Muchas Gracias de Nada)
├── 1981.html (Luthierías)
├── 1985.html (Humor Dulce Hogar)
└── 1986.html (Teatro Colón)
```

#### 2. La Banda Elástica ✅
- **Ubicación:** `/labandaelastica/` + `/labandaelastica.html` (raíz)
- **Archivos:** 10 páginas HTML
- **Datos:** 11 JSON en `/data/labandaelastica/`
- **Imágenes:** 10 imágenes en `/images/lbe/`
- **Estilos:** `scss/pages/_banda-elastica.scss`
- **Estado:** 100% completo con navegación corregida

**Estructura de archivos:**
```
labandaelastica/
├── index.html (← ../labandaelastica.html)
├── espectaculos.html
├── discografia.html
├── fotos.html
├── videos.html
├── audio.html
├── e1.html (Espectáculo 1 - 1988)
├── e2.html (Espectáculo 2 - 1989)
├── e3.html (Espectáculo 3 - 1991)
└── e4.html (Espectáculo 4 - 1992)
```

#### 3. Anecdotario ✅ (completado en sesión anterior)
- **Ubicación:** `/anecdotas/` + `/anecdotario-modular.html`
- **Archivos:** 19 páginas HTML
- **Datos:** 20 JSON en `/data/anecdotas/`
- **Estilos:** `scss/pages/_anecdotario.scss`

### 📊 Progreso General

**Completado:** 2 secciones principales + Anecdotario
**Pendiente:** 11 secciones
**Total archivos migrados:** ~44 páginas HTML, ~350 imágenes

---

## 🎯 Patrón de Migración Establecido

### Template HTML Estándar

Todas las páginas interiores usan esta estructura:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {section_name} - Ernesto Acher</title>
    <meta name="description" content="{title} - {section_name}">
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-{section-class}">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="section-header">
                    <p><a href="{back_url}">← {back_text}</a></p>
                </div>
                <div class="section-content">
                    {content}
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>
```

### Navegación Consistente

1. **Página raíz** (ej: `lesluthiers.html`)
   - Tiene menú flotante derecho con navegación
   - Clase body: `page-{section}`
   - Link a `/lesluthiers/index.html`

2. **index.html interior** (ej: `/lesluthiers/index.html`)
   - Navegación: `← {Section}` → `../lesluthiers.html`
   - Contenido principal de la sección

3. **Páginas internas** (ej: `/lesluthiers/espectaculos.html`)
   - Navegación: `← {Section}` → `index.html`
   - Contenido específico

### Proceso de Migración (10 pasos)

1. ✅ **Extraer contenido** de `backup/{section}/` usando subagent
2. ✅ **Limpiar HTML** (remover tables, spacers, navegación antigua)
3. ✅ **Convertir encoding** ISO-8859-1 → UTF-8
4. ✅ **Generar archivos JSON** en `/data/{section}/`
5. ✅ **Crear páginas HTML** usando template estándar
6. ✅ **Copiar imágenes SIN modificar** a `/images/{section}/`
7. ✅ **Actualizar rutas** en HTML (`../images/{section}/`)
8. ✅ **Crear SCSS** en `scss/pages/_{section}.scss`
9. ✅ **Integrar menú** (ya está en `data/menus.json`)
10. ✅ **Compilar CSS** (`sass scss/app.scss css/app.css`)

**⏱️ Tiempo estimado por sección:** ~10-15 minutos

---

## 📁 Secciones Pendientes (11 restantes)

### Prioridad ALTA (5 secciones)

#### 1. Humor con Achís (hca/)
- **Archivos fuente:** `backup/hca/` (3 HTML)
- **Objetivo:** `/humorconachis/` + `/humorconachis.html`
- **Ya existe:** `humorconachis.html` y `humorconachis-fotos.html` en raíz
- **Imágenes:** ~15 en `backup/hca/gfx/`
- **SCSS:** Crear `scss/pages/_humor-con-achis.scss`

#### 2. Veladas Espeluznantes (ve/)
- **Archivos fuente:** `backup/ve/` (4 HTML)
- **Objetivo:** `/veladas/` + `/veladas.html`
- **Ya existe:** `veladas.html` y `veladas-fotos.html` en raíz
- **Imágenes:** ~20 en `backup/ve/gfx/`
- **SCSS:** Crear `scss/pages/_veladas.scss`

#### 3. Offside (ocho/)
- **Archivos fuente:** `backup/ocho/` (2 HTML)
- **Objetivo:** `/offside/` + `/offside.html`
- **Ya existe:** `offside.html` en raíz
- **Imágenes:** ~5 en `backup/ocho/gfx/`
- **SCSS:** Crear `scss/pages/_offside.scss`

#### 4. Gershwin (hg/)
- **Archivos fuente:** `backup/hg/` (1 HTML)
- **Objetivo:** `/gershwin/` + `/gershwin.html`
- **Ya existe:** `gershwin.html` en raíz
- **Imágenes:** ~10 en `backup/hg/gfx/`
- **SCSS:** Crear `scss/pages/_gershwin.scss`

#### 5. Los Animales de la Música (ladm/)
- **Archivos fuente:** `backup/ladm/` (2 HTML)
- **Objetivo:** `/animales/` + `/animales.html`
- **Ya existe:** `animales.html` en raíz
- **Imágenes:** ~8 en `backup/ladm/gfx/`
- **SCSS:** Crear `scss/pages/_animales.scss`

### Prioridad MEDIA (4 secciones)

#### 6. De Todo como en Botica (dtodo/)
- **Archivos fuente:** `backup/dtodo/` (4 HTML)
- **Objetivo:** `/detodo/` + `/detodo-juntos.html`
- **Ya existe:** `detodo-juntos.html` en raíz
- **Imágenes:** ~12 en `backup/dtodo/gfx/`
- **SCSS:** Crear `scss/pages/_detodo.scss`

#### 7. Discografía Detallada (discos/)
- **Archivos fuente:** `backup/discos/` (10 HTML)
- **Objetivo:** `/discografia/` (ya existe página índice)
- **Ya existe:** `discografia.html` en raíz
- **Imágenes:** ~30 en `backup/discos/gfx/`
- **SCSS:** Ya existe `scss/pages/_discografia.scss` (verificar)

#### 8. Partituras (partituras/)
- **Archivos fuente:** `backup/partituras/` (si existe)
- **Objetivo:** `/partituras/` (ya existe página índice)
- **Ya existe:** `partituras.html` en raíz
- **SCSS:** Verificar si necesita estilos específicos

#### 9. Links (links/)
- **Archivos fuente:** `backup/links/` (si existe)
- **Objetivo:** Expandir `/links.html` existente
- **Ya existe:** `links.html` en raíz (8 links externos)
- **Estado:** Revisar si necesita más contenido

### Prioridad BAJA (2 secciones)

#### 10. Galerías (galerias/)
- **Archivos fuente:** `backup/galerias/` (162 HTML!!!)
- **Objetivo:** `/galerias/` con estrategia especial
- **Ya existe:** `galerias.html` en raíz
- **Imágenes:** ~350 en `backup/galerias/fotos/`
- **SCSS:** Ya existe `scss/pages/_galerias.scss`
- **⚠️ IMPORTANTE:** Requiere estrategia diferente (lightbox, galería dinámica)

#### 11. Varios (rr, proyectos, menu)
- **Archivos fuente:** `backup/rr/`, `backup/proyectos/`, etc.
- **Objetivo:** Páginas sueltas según contenido
- **Cantidad:** 3-5 archivos HTML

---

## 🗂️ Inventario de Archivos Backup

### Directorios en backup/

```
backup/
├── ll/          ✅ COMPLETADO (Les Luthiers)
├── lbe/         ✅ COMPLETADO (La Banda Elástica)
├── hca/         ⏳ PENDIENTE (Humor con Achís - 3 HTML)
├── ve/          ⏳ PENDIENTE (Veladas - 4 HTML)
├── ocho/        ⏳ PENDIENTE (Offside - 2 HTML)
├── hg/          ⏳ PENDIENTE (Gershwin - 1 HTML)
├── ladm/        ⏳ PENDIENTE (Animales - 2 HTML)
├── dtodo/       ⏳ PENDIENTE (De Todo - 4 HTML)
├── discos/      ⏳ PENDIENTE (Discografía - 10 HTML)
├── galerias/    ⏳ PENDIENTE (Galerías - 162 HTML)
├── rr/          ⏳ PENDIENTE (Resto - varios)
└── otros/       ⏳ PENDIENTE (Revisar contenido)
```

### Total Estimado
- **HTML:** ~195 archivos pendientes
- **Imágenes:** ~135 imágenes pendientes (sin contar galerías)
- **Galerías:** ~350 imágenes adicionales

---

## 🔧 Scripts y Herramientas Creadas

### Scripts Disponibles

1. **`/scripts/fix_all_pages.py`**
   - Corrige estructura HTML de todas las páginas
   - Regenera desde JSON con template consistente
   - Usado en auditoría de LL y LBE

2. **`/scripts/migrate_lbe.py`** (referencia)
   - Migración de La Banda Elástica
   - Patrón replicable para otras secciones

3. **Scripts pendientes de crear:**
   - Migración automatizada por sección
   - Generador de SCSS base para nuevas secciones

### Comandos Útiles

```bash
# Compilar SCSS
sass scss/app.scss css/app.css

# Ver estructura de backup
ls -la backup/

# Contar archivos HTML en una sección
find backup/hca -name "*.html" | wc -l

# Listar imágenes en una sección
ls -lh backup/hca/gfx/
```

---

## 🎨 Arquitectura CSS Actual

### SCSS Modular

```scss
scss/
├── app.scss (archivo principal)
├── _variables.scss
├── _mixins.scss
├── base/
│   ├── _reset.scss
│   ├── _typography.scss
│   └── _base.scss
├── layout/
│   ├── _header.scss
│   ├── _main.scss
│   └── _footer.scss
├── components/
│   ├── _menu.scss
│   ├── _carousel.scss
│   ├── _sidebar.scss
│   ├── _content.scss
│   └── _arc-decoration.scss
└── pages/
    ├── _anecdotario.scss       ✅
    ├── _lesluthiers.scss        ✅
    ├── _banda-elastica.scss     ✅
    ├── _galerias.scss           ✅
    ├── _links.scss              ✅
    ├── _contacto.scss           ✅
    ├── _humor-con-achis.scss    ⏳ CREAR
    ├── _veladas.scss            ⏳ CREAR
    ├── _offside.scss            ⏳ CREAR
    ├── _gershwin.scss           ⏳ CREAR
    ├── _animales.scss           ⏳ CREAR
    └── _detodo.scss             ⏳ CREAR
```

### Clases Body por Sección

```css
.page-lesluthiers       ✅
.page-banda-elastica    ✅
.page-anecdotario       ✅
.page-humor-con-achis   ⏳
.page-veladas           ⏳
.page-offside           ⏳
.page-gershwin          ⏳
.page-animales          ⏳
.page-detodo            ⏳
.page-galerias          ✅
.page-links             ✅
.page-contacto          ✅
```

---

## 📝 Componentes del Sistema

### Componentes Dinámicos

1. **Sidebar** (`components/sidebar.html`)
   - Se carga en `<div id="sidebar-container"></div>`
   - Menú desde `data/menus.json` → `sidebar[]`
   - Logo y navegación principal

2. **Header** (`components/header.html`)
   - Se carga en `<div id="header-container"></div>`
   - Menús desde `data/menus.json` → `headerPrimary[]` y `headerSecondary[]`
   - Navegación secundaria

3. **JavaScript** (`js/components.js`)
   - Carga componentes dinámicamente
   - Puebla menús desde JSON
   - Maneja clases activas

### Menú Principal (data/menus.json)

```json
{
  "sidebar": [
    { "id": "lesluthiers", "label": "Les Luthiers", "href": "lesluthiers.html" },
    { "id": "labanda", "label": "La Banda Elástica", "href": "labandaelastica.html" },
    { "id": "unipersonal", "label": "Unipersonal", "href": "humorconachis.html" },
    { "id": "conciertos", "label": "Conciertos de música humor", "href": "veladas.html" },
    { "id": "offside", "label": "Offside Chamber Orchestra", "href": "offside.html" },
    { "id": "gershwin", "label": "Homenaje a Gershwin", "href": "gershwin.html" },
    { "id": "animales", "label": "Los animales de la música", "href": "animales.html" },
    { "id": "detodo", "label": "De todo como en botica", "href": "detodo.html" },
    { "id": "realizaciones", "label": "Realizaciones recientes", "href": "realizaciones.html" },
    { "id": "nuevos", "label": "Nuevos proyectos", "href": "proyectos.html" },
    { "id": "menuconciertos", "label": "Menú de conciertos", "href": "menuconciertos.html" }
  ],
  "headerSecondary": [
    { "id": "discografia", "label": "Discografía", "href": "discografia.html" },
    { "id": "anecdotario", "label": "Anecdotario", "href": "anecdotario-modular.html" },
    { "id": "partituras", "label": "Partituras", "href": "partituras.html" },
    { "id": "galerias", "label": "Galerías", "href": "galerias.html" }
  ]
}
```

---

## ⚠️ Reglas CRÍTICAS para Migración

### Imágenes

**REGLA #1:** Las imágenes se copian **SIN MODIFICAR**

```bash
# ✅ CORRECTO
cp backup/hca/gfx/* images/hca/

# ❌ INCORRECTO (NO optimizar)
convert backup/hca/gfx/foto.jpg -quality 80 images/hca/foto.jpg
```

**Razón:** Usuario especificó: "las imágenes rescátalas tal como son, después en otro contexto las podremos mejorar de calidad"

### Encoding

**REGLA #2:** Siempre convertir de ISO-8859-1 a UTF-8

```python
# En scripts Python
with open(html_file, 'r', encoding='iso-8859-1') as f:
    content = f.read()

# Guardar en UTF-8
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)
```

### Navegación

**REGLA #3:** Mantener navegación coherente

```
Home → Sidebar "{Sección}" → {seccion}.html (raíz con menú flotante)
     → Link del menú → {seccion}/index.html
     → "← {Sección}" → {seccion}.html

{seccion}/index.html → Links internos → {seccion}/pagina.html
     → "← {Sección}" → index.html
```

### Estructura de Directorios

**REGLA #4:** Mantener organización consistente

```
ernestoacher.cl/
├── {seccion}.html              (página raíz con menú flotante)
├── {seccion}/                  (directorio de páginas)
│   ├── index.html             (back to ../{seccion}.html)
│   └── *.html                 (back to index.html)
├── data/{seccion}/            (datos JSON)
│   ├── index.json
│   ├── catalog.json
│   └── *.json
├── images/{seccion}/          (imágenes sin modificar)
│   └── *.jpg
└── scss/pages/_{seccion}.scss (estilos específicos)
```

---

## 🚀 Siguiente Paso Recomendado

### Iniciar con: Humor con Achís (hca/)

**Razón:** Es una sección pequeña (3 HTML) y sigue el mismo patrón de LL y LBE.

### Pasos para Nueva Sesión

1. **Explorar backup:**
   ```bash
   ls -la backup/hca/
   find backup/hca -name "*.html"
   ls -lh backup/hca/gfx/
   ```

2. **Usar Task tool con subagent_type='general-purpose':**
   ```
   Migrar sección Humor con Achís desde backup/hca/ siguiendo el patrón
   establecido en Les Luthiers:
   - Extraer 3 archivos HTML
   - Generar JSONs en data/humorconachis/
   - Copiar imágenes SIN modificar a images/hca/
   - Crear páginas HTML en humorconachis/
   - Template HTML consistente
   ```

3. **Crear SCSS:**
   - `scss/pages/_humor-con-achis.scss`
   - Importar en `scss/app.scss`
   - Compilar CSS

4. **Verificar navegación:**
   - Página raíz: `/humorconachis.html`
   - Index: `/humorconachis/index.html`
   - Páginas internas con navegación correcta

5. **Documentar:**
   - Crear `HUMORCONACHIS_COMPLETADO.md`

---

## 📚 Documentación Existente

- ✅ `PLAN_MIGRACION_COMPLETA.md` - Plan general inicial
- ✅ `LESLUTHIERS_COMPLETADO.md` - Resumen Les Luthiers
- ✅ `LABANDA_COMPLETADO.md` - Resumen La Banda Elástica
- ✅ `AUDITORIA_NAVEGACION_COMPLETADA.md` - Corrección navegación
- ✅ Este documento (`CONTINUACION_MIGRACION.md`)

---

## 🎯 Meta Final

Migrar **100% del contenido** de ernestoacher.com.ar a ernestoacher.cl:
- 13 secciones principales
- ~238 archivos HTML
- ~485 imágenes
- Navegación coherente
- Diseño moderno y responsive
- Encoding UTF-8
- Componentes dinámicos

**Progreso actual:** 2/13 secciones principales (15%) + Anecdotario

---

## 💡 Tips para Continuar

1. **Una sección a la vez:** No mezclar múltiples secciones
2. **Seguir el patrón:** LL y LBE son la referencia perfecta
3. **Verificar siempre:** Probar navegación después de cada migración
4. **Documentar:** Crear MD de resumen al terminar cada sección
5. **Galerías al final:** Dejar las 162 páginas de galerías para el final (requiere estrategia especial)

**Comando para verificar:**
```bash
# Abrir en navegador
open http://127.0.0.1:8080/{seccion}.html
```

---

**Creado:** 15/01/2026
**Última actualización:** 15/01/2026
**Siguiente paso:** Migrar Humor con Achís (hca/)
