# 🏗️ Plan de Refactorización - Arquitectura Modular Completa

**Fecha**: 16 Enero 2026
**Estado Actual**: Sitio funcionando con arquitectura híbrida
**Objetivo**: Migrar a sistema de templates Handlebars manteniendo diseño exacto

---

## 📊 Estado Actual (Commit: 7133b27)

### ✅ Lo que funciona:
- Sitio completo con diseño original
- Puerto 3012 configurado y registrado
- Sistema de build robusto (`npm run dev`)
- CSS compilado desde `scss/`
- Servidor Python sirviendo desde `public/`

### 🔧 Arquitectura Actual (Híbrida):

```
Raíz:
├── index.html              → Portada (estático)
├── *.html                  → 11 páginas (estáticos)
├── scss/                   → SASS (compila a public/css/)
├── images/                 → Imágenes
├── assets/                 → Foto principal Ernesto
├── js/                     → JavaScript (components.js)
├── components/             → header.html, sidebar.html (carga dinámica JS)
└── data/                   → menus.json

Preparado (no usado aún):
├── src/
│   ├── templates/          → Plantillas Handlebars
│   ├── data/               → JSON centralizados
│   ├── content/            → Contenido HTML separado
│   └── scss/               → SASS modular
└── scripts/
    ├── build.js            → Generador de páginas
    └── validate-links.js   → Validador de enlaces
```

---

## 🎯 Objetivo Final

Migrar a arquitectura 100% basada en templates donde:
1. **Todas las páginas** se generan desde plantillas Handlebars
2. **Todo el contenido** viene de archivos JSON + HTML separados
3. **Portada incluida** también generada desde template
4. **Diseño idéntico** al ojo humano (pixel-perfect)
5. **Mantenibilidad extrema** - cambio global = 1 archivo

---

## 📋 Plan de Migración por Fases

### ✅ FASE 0: Preparación (COMPLETADA)

- [x] Sistema de build funcionando
- [x] Puerto 3012 configurado
- [x] Estructura `src/` creada
- [x] Templates base creados
- [x] Script dev-server.sh robusto
- [x] Commit del estado actual

---

### 🔄 FASE 1: Migrar Contenido HTML a src/content/

**Objetivo**: Extraer contenido de páginas HTML a archivos separados

**Agente recomendado**: `general-purpose`

**Tareas**:
1. Leer cada página HTML en raíz (11 archivos)
2. Extraer solo el contenido `<main>` (sin estructura)
3. Guardar en `src/content/[seccion].html`
4. Verificar que imágenes usen rutas absolutas (`/images/`)

**Páginas a migrar**:
- lesluthiers.html → src/content/lesluthiers.html
- labandaelastica.html → src/content/labandaelastica.html
- humorconachis.html → src/content/humorconachis.html
- veladas.html → src/content/veladas.html
- offside.html → src/content/offside.html
- gershwin.html → src/content/gershwin.html
- animales.html → src/content/animales.html
- detodo.html → src/content/detodo.html
- realizaciones.html → src/content/realizaciones.html
- proyectos.html → src/content/proyectos.html
- menuconciertos.html → src/content/menuconciertos.html

**Criterio de éxito**:
- 11 archivos en `src/content/`
- Solo contenido HTML (sin `<head>`, `<body>`, estructura)
- Rutas de imágenes absolutas

**Prompt sugerido**:
```
Necesito extraer el contenido HTML de las 11 páginas principales del sitio.

Para cada archivo [nombre].html en la raíz:
1. Lee el archivo
2. Extrae solo el contenido dentro de <main class="main-content">
3. Asegúrate que las rutas de imágenes sean absolutas (/images/...)
4. Guarda en src/content/[nombre].html

Páginas: lesluthiers, labandaelastica, humorconachis, veladas, offside,
gershwin, animales, detodo, realizaciones, proyectos, menuconciertos

No modifiques el contenido, solo extráelo.
```

---

### 🔄 FASE 2: Actualizar navigation.json con Contenido Real

**Objetivo**: Expandir `src/data/navigation.json` con menús flotantes correctos

**Agente recomendado**: `general-purpose`

**Tareas**:
1. Para cada sección, leer el HTML original
2. Extraer el menú flotante derecho (`<nav class="page-nav-right">`)
3. Actualizar `subPages` en `src/data/navigation.json` con URLs correctas
4. Verificar que coincida con estructura real del sitio

**Ejemplo**:

Leer de `lesluthiers.html`:
```html
<nav class="page-nav-right">
    <ul>
        <li class="active">- Comienzo</li>
        <li><a href="lesluthiers/espectaculos.html">- Espectáculos</a></li>
        ...
    </ul>
</nav>
```

Actualizar en `src/data/navigation.json`:
```json
{
  "id": "lesluthiers",
  "label": "Les Luthiers",
  "url": "/lesluthiers.html",
  "subPages": [
    { "label": "Comienzo", "url": "/lesluthiers.html", "default": true },
    { "label": "Espectáculos", "url": "/lesluthiers/espectaculos.html" },
    ...
  ]
}
```

**Criterio de éxito**:
- `navigation.json` tiene menús flotantes completos para las 11 secciones
- URLs coinciden con archivos reales
- Campo `default: true` en página principal de cada sección

**Prompt sugerido**:
```
Necesito actualizar src/data/navigation.json con los menús flotantes correctos.

Para cada sección en navigation.json:
1. Lee el archivo HTML original ([seccion].html)
2. Busca <nav class="page-nav-right">
3. Extrae todos los items del menú
4. Actualiza el array "subPages" con las URLs correctas
5. Marca como "default: true" el primer item (sin URL)

Mantén el resto de la estructura intacta.
```

---

### 🔄 FASE 3: Generar Páginas desde Templates

**Objetivo**: Que `scripts/build.js` genere las 11 páginas desde templates

**Agente recomendado**: `general-purpose`

**Tareas**:
1. Verificar que `scripts/build.js` funciona correctamente
2. Ejecutar build: `npm run build`
3. Comparar HTML generado vs HTML original
4. Ajustar templates si hay diferencias visuales
5. Verificar que CSS se aplica correctamente

**Validación**:
- `public/[seccion].html` se genera correctamente
- Estructura HTML idéntica a original
- Sidebar se muestra
- Header se muestra
- Menú flotante derecho se muestra
- Contenido se inyecta correctamente

**Ajustes esperados**:
- Posibles diferencias en indentación (OK)
- Verificar que `bodyClass` sea correcto (ej: `page-lesluthiers`)
- Asegurar rutas absolutas en templates

**Criterio de éxito**:
- `npm run build` genera 11 páginas sin errores
- Visualmente idénticas al abrir en navegador
- Menús funcionan
- Enlaces funcionan

**Prompt sugerido**:
```
El sistema de templates está listo. Necesito:

1. Ejecutar npm run build
2. Verificar que se generan las 11 páginas en public/
3. Comparar visualmente una página generada vs la original
4. Si hay diferencias, ajustar templates en src/templates/

Páginas a verificar:
- public/lesluthiers.html (generado) vs lesluthiers.html (original)
- Verificar que sidebar, header, menú flotante y contenido se vean igual

Si algo falla, revisar:
- src/templates/base.html
- src/templates/page-interior.html
- src/templates/partials/*
```

---

### 🔄 FASE 4: Migrar Portada (index.html)

**Objetivo**: Crear template para la portada

**Agente recomendado**: `Plan` (planear primero) → `general-purpose` (implementar)

**Tareas**:
1. **Planear**: Analizar estructura de `index.html`
2. Crear `src/templates/page-home.html`
3. Extraer datos del carousel a `src/data/site.json`
4. Actualizar `scripts/build.js` para generar portada
5. Probar que se vea idéntica

**Estructura de index.html**:
```html
<body>
  <div class="home-container">
    <header class="site-header">
      <h1 class="logo">Ernesto Acher</h1>
    </header>
    <main class="home-content">
      <div class="ellipse-container"><!-- SVG --></div>
      <nav class="menu-principal"><!-- 11 items --></nav>
      <section class="carousel-container"><!-- 7 slides --></section>
      <div class="ernesto-photo"><!-- Foto --></div>
      <nav class="menu-media"><!-- 6 items --></nav>
    </main>
    <footer class="site-footer"><!-- Footer --></footer>
  </div>
</body>
```

**Datos a extraer**:
- Carousel: 7 slides con imágenes, textos y links
- Menú principal: 11 items (ya está en navigation.json)
- Menú media: 6 items
- URL de foto de Ernesto

**Criterio de éxito**:
- `public/index.html` generado desde template
- Visualmente idéntico al original
- Carousel funciona
- Menús funcionan
- Elipse SVG se muestra correctamente

**Prompt sugerido** (usar con agente Plan primero):
```
Necesito crear un template para la portada (index.html).

Primero, analiza la estructura actual de index.html y crea un plan para:
1. Qué datos extraer a JSON (carousel, menús)
2. Qué estructura de template crear
3. Cómo modificar build.js para generar la portada

Luego implementa el plan asegurando que se vea idéntico al original.
```

---

### 🔄 FASE 5: Migrar Subpáginas

**Objetivo**: Generar páginas en subdirectorios (ej: `lesluthiers/espectaculos.html`)

**Agente recomendado**: `general-purpose`

**Tareas**:
1. Identificar todas las subpáginas existentes
2. Para cada subpágina:
   - Extraer contenido a `src/content/[seccion]/[subpagina].html`
   - Actualizar `src/data/sections/[seccion].json` con subpáginas
3. Modificar `scripts/build.js` para generar subdirectorios
4. Probar navegación entre páginas

**Subpáginas identificadas** (aproximadamente 40):
- lesluthiers/espectaculos.html
- lesluthiers/discografia.html
- lesluthiers/fotos.html
- lesluthiers/videos.html
- labandaelastica/discografia.html
- labandaelastica/episodios.html
- ... (ver archivos en subdirectorios)

**Criterio de éxito**:
- Todas las subpáginas se generan en `public/[seccion]/[subpagina].html`
- Navegación funciona
- Menú flotante marca correctamente la página activa

---

### 🔄 FASE 6: Eliminar Archivos Antiguos

**Objetivo**: Limpiar archivos HTML antiguos ya que todo se genera

**Agente recomendado**: Hacer manualmente o con `general-purpose`

**Tareas**:
1. Mover archivos HTML antiguos a `archive/`
2. Actualizar package.json - eliminar copia de HTML en build
3. Verificar que sitio funciona 100% generado
4. Commit final

**Archivos a archivar**:
- index.html (raíz)
- *.html (11 archivos raíz)
- Subdirectorios con HTML (lesluthiers/, labandaelastica/, etc.)

**Criterio de éxito**:
- No hay HTML en raíz ni subdirectorios (excepto `public/`)
- `npm run build` genera todo desde templates
- Sitio funciona perfectamente

---

### 🔄 FASE 7: Optimización Final

**Objetivo**: Mejorar sistema de build y validación

**Agente recomendado**: `general-purpose`

**Tareas**:
1. Ejecutar `npm run validate` y corregir enlaces rotos
2. Optimizar imágenes (opcional)
3. Agregar scripts para:
   - Crear nueva sección automáticamente
   - Agregar subpágina a sección existente
4. Documentar en README.md

**Criterio de éxito**:
- `npm run validate` pasa sin errores
- Scripts helper creados
- README.md actualizado con nueva arquitectura

---

## 🚀 Cómo Continuar en Nuevo Contexto

### 1. Abrir Claude Code

Abre una nueva ventana de Claude Code en el proyecto:
```bash
cd /Users/chuchurex/Sites/prod/ernestoacher.cl
code .
```

### 2. Leer Este Plan

En el nuevo contexto, primero lee:
```
@PLAN_REFACTORIZACION.md
```

### 3. Elegir Fase

Decide qué fase quieres comenzar (recomiendo: **FASE 1**)

### 4. Usar Agente Apropiado

**Para FASE 1** (Migrar contenido HTML):
```
Usa el agente: general-purpose

Prompt:
"Necesito ejecutar la FASE 1 del plan de refactorización.
Lee @PLAN_REFACTORIZACION.md y ejecuta todos los pasos de FASE 1.
Extrae el contenido de las 11 páginas HTML a src/content/"
```

**Para FASE 4** (Portada):
```
Usa el agente: Plan (primero)

Prompt:
"Necesito ejecutar la FASE 4 del plan de refactorización.
Lee @PLAN_REFACTORIZACION.md y crea un plan detallado para
migrar la portada (index.html) a sistema de templates."

Luego usa: general-purpose (para implementar)
```

### 5. Verificar en Cada Fase

Después de cada fase:
```bash
npm run build
npm run dev
# Abrir http://localhost:3012 y verificar visualmente
```

---

## 📝 Checklist de Progreso

Marca con `[x]` las fases completadas:

- [ ] FASE 1: Contenido HTML migrado a src/content/
- [ ] FASE 2: navigation.json actualizado con menús reales
- [ ] FASE 3: Páginas principales generadas desde templates
- [ ] FASE 4: Portada migrada a template
- [ ] FASE 5: Subpáginas migradas
- [ ] FASE 6: Archivos antiguos archivados
- [ ] FASE 7: Optimización y validación final

---

## 🎯 Resultado Final Esperado

```
ernestoacher.cl/
├── src/                        # FUENTE
│   ├── data/
│   │   ├── site.json          # Config global + carousel
│   │   ├── navigation.json    # Navegación completa
│   │   └── sections/          # 11 archivos JSON
│   ├── content/               # ~50 archivos HTML (contenido puro)
│   ├── templates/
│   │   ├── base.html
│   │   ├── page-home.html     # NUEVO
│   │   ├── page-interior.html
│   │   └── partials/
│   └── scss/                  # Estilos (sin cambios)
│
├── scripts/
│   ├── build.js               # Genera TODO el sitio
│   ├── validate-links.js
│   └── dev-server.sh
│
├── public/                    # GENERADO (todo desde src/)
│   ├── index.html            # ✓ Generado
│   ├── *.html                # ✓ 11 generados
│   ├── [seccion]/            # ✓ ~40 subpáginas generadas
│   ├── css/                  # ✓ Compilado
│   ├── images/               # ✓ Copiado
│   └── assets/               # ✓ Copiado
│
└── archive/                   # Archivos antiguos (backup)
    └── html-original/
```

**Comandos**:
```bash
npm run build   # Genera TODO desde src/
npm run dev     # Build + servidor puerto 3012
npm run validate # Valida enlaces
```

**Ventajas conseguidas**:
- ✅ Cambio global = 1 archivo
- ✅ Nueva sección = 3 archivos
- ✅ Validación automática
- ✅ Imposible crear inconsistencias
- ✅ Diseño idéntico pixel-perfect

---

## 💡 Tips para Nuevo Contexto

1. **Siempre lee primero**: `@PLAN_REFACTORIZACION.md`
2. **Una fase a la vez**: No saltes fases
3. **Verifica visualmente**: Después de cada cambio, abre en navegador
4. **Commitea cada fase**: `git commit` al terminar cada fase
5. **Usa agente correcto**: Plan para planear, general-purpose para implementar
6. **No modifiques diseño**: El objetivo es mantenerlo idéntico

---

**Último commit**: `7133b27` - Sitio funcionando con arquitectura híbrida
**Puerto**: 3012 (registrado en `/Sites/vigentes/dashboard/PORTS.md`)
**Branch**: `diseno2`

¡Buena suerte con la refactorización! 🚀
