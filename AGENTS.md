# ernestoacher.cl - Sitio homenaje a Ernesto Acher (1947-2024)

Músico, compositor, director y humorista argentino. Miembro de Les Luthiers (1971-1986).
Sitio original: http://www.ernestoacher.com/ (rescatado de archive.org).

## Stack y Deploy

- **Motor**: Node.js + Handlebars templates + Dart Sass (SCSS)
- **Hosting**: Cloudflare Pages — deploy automático al pushear a `main`
- **Directorio de deploy**: `public/` (se versiona en git, CF lo sirve directo)
- **NO hay** wrangler.toml, _redirects ni _headers — es un sitio estático puro
- **Dominio**: ernestoacher.cl
- **Repo**: github.com/chuchurex/ernestoacher.cl

## Comandos

```bash
npm run build        # Build completo (HTML + SCSS + copiar assets)
npm run dev          # Build + servidor local en http://localhost:3012
npm run sass:watch   # Watch SCSS (desarrollo de estilos)
npm run validate     # Validar enlaces internos
npm run clean        # Limpiar public/
```

## Estructura de archivos

```
src/
├── content/           # HTML crudo de cada página (sin layout)
│   ├── lesluthiers/   # Subdirectorios por sección (fotos, años, discos)
│   ├── quorum/
│   ├── veladas/
│   └── *.html         # Páginas raíz (galerias, contacto, etc.)
├── data/
│   ├── site.json      # Config global (meta, carousel, menuMedia, footer)
│   ├── navigation.json # Sidebar + headers (source of truth de navegación)
│   └── sections/      # Un JSON por página (~103 archivos)
├── scss/
│   ├── app.scss       # Entry point — importa todo con @use
│   ├── _variables.scss
│   ├── _mixins.scss
│   ├── base/          # reset, typography
│   ├── layout/        # header, main, interior, footer
│   ├── components/    # menu, carousel, sidebar, content, nav-right, etc.
│   ├── sections/      # Estilos por sección (13 archivos)
│   └── utilities/     # helpers
└── templates/
    ├── base.html          # DOCTYPE + head + body (wrapper)
    ├── page-home.html     # Layout home (carousel + foto + menu media)
    ├── page-interior.html # Layout interior (sidebar + content + nav-right)
    └── partials/          # sidebar, header, nav-right, icon

scripts/build.js    # Build principal (clase SiteBuilder)
images/             # Fotos de contenido (17 subdirectorios)
assets/images/      # Imágenes de diseño (banners, logos, headers)
galerias/           # Galerías de fotos
js/                 # main.js, components.js
public/             # OUTPUT del build (generado, pero versionado para CF)
```

## Cómo funciona el build (scripts/build.js)

El `SiteBuilder` genera HTML combinando 3 fuentes por página:

1. **Plantilla** (`src/templates/`) — layout HTML (base → interior/home)
2. **Datos** (`src/data/sections/{id}.json`) — título, bodyClass, meta
3. **Contenido** (`src/content/{id}.html`) — HTML crudo del body

### Tipos de páginas que genera:

| Tipo | Método | Ejemplo |
|------|--------|---------|
| Home | `buildHomePage()` | index.html |
| Sección con submenú | `buildPage()` + `buildSubPage()` | lesluthiers.html + /lesluthiers/fotos.html |
| Página simple | `buildSimplePage()` | galerias.html, contacto.html |
| Página adicional | `buildSimplePage()` | lesluthiers-disco2.html |
| Subdirectorio | `buildSimplePage()` | lesluthiers/1971.html (id: lesluthiers-1971) |

### Convención de IDs para subdirectorios:
- ID `lesluthiers-1971` → busca contenido en `src/content/lesluthiers/1971.html`
- ID `lesluthiers-f_ll5` → busca contenido en `src/content/lesluthiers/f_ll5.html`
- La conversión: el primer `-` se convierte en `/` si el segundo segmento es numérico o empieza con `f_`

### Listas de páginas en build.js (IMPORTANTE):
Las páginas a generar están hardcodeadas en 3 arrays dentro de `buildAll()`:
- `menuMediaPages` — páginas del menú media del home
- `additionalPages` — páginas extra sin submenú
- `subDirPages` — páginas en subdirectorios

**Al agregar una página nueva, HAY QUE agregarla al array correspondiente en build.js.**

## Navegación (src/data/navigation.json)

Tres bloques:

### `sidebar` — Menú lateral izquierdo (secciones principales)
```json
{
  "id": "lesluthiers",
  "label": "Les Luthiers",
  "url": "/lesluthiers.html",
  "headerImage": "/images/headers/ll-header.jpg",
  "subPages": [
    { "label": "Comienzo", "url": "/lesluthiers.html", "default": true },
    { "label": "Espectáculos", "url": "/lesluthiers/espectaculos.html" }
  ]
}
```

### `headerPrimary` — Iconos del header superior
Inicio, Links, Actualizaciones, Mapa del sitio, Contacto

### `headerSecondary` — Links secundarios del header
Discografía, Anecdotario, Pregunte nomás, Partituras, Galerías

## Cómo agregar una nueva sección completa

1. **Crear JSON** en `src/data/sections/{id}.json`:
```json
{
  "id": "nueva",
  "title": "Nueva Sección",
  "bodyClass": "page-nueva",
  "meta": {
    "description": "Descripción",
    "keywords": "palabras clave"
  }
}
```

2. **Crear contenido** en `src/content/{id}.html` (HTML crudo sin layout)

3. **Agregar a navigation.json** → en `sidebar[]` con subPages

4. **Agregar a build.js** → en el array correspondiente (`additionalPages` o `menuMediaPages`)

5. **Opcional: SCSS** → crear `src/scss/sections/_nueva.scss` y agregar `@use` en `app.scss`

6. **Build**: `npm run build`

## Cómo agregar una subpágina a sección existente

1. Crear JSON en `src/data/sections/{seccion}-{subpagina}.json`
2. Crear contenido en `src/content/{seccion}/{subpagina}.html`
3. Agregar en `navigation.json` → dentro de `subPages[]` de la sección
4. Agregar el ID a `additionalPages` o `subDirPages` en `build.js`

## Secciones actuales

| Sección | ID nav | Archivos principales |
|---------|--------|---------------------|
| Les Luthiers | lesluthiers | 14 espectáculos (1971-1986), 7 discos, 40+ fotos |
| La Banda Elástica | labanda | espectáculos, discografía, fotos, videos, audio |
| Unipersonal (Humor con Achis) | unipersonal | fotos, santiago |
| Conciertos de música humor | conciertos | bromas, videos, fotos |
| Offside Chamber Orchestra | offside | fotos |
| Homenaje a Gershwin | gershwin | — |
| Los animales de la música | animales | videos |
| De todo como en botica | detodo | juntos, qm, habia |
| Realizaciones recientes | realizaciones | colegio |
| Nuevos proyectos | nuevos | — |
| Menú de conciertos | menuconciertos | — |
| Quorum | quorum | disco, fotos, audio |
| En Serio | enserio | — |
| Los Rincones de Acher | lrda | — |

**Páginas sueltas**: discografia, anecdotario, anecdotario-modular, partituras, galerias, links, contacto, pnm (Pregunte nomás)

## SCSS — Convenciones

- Usa `@use` (Dart Sass), NO `@import`
- Variables en `_variables.scss`, mixins en `_mixins.scss`
- Cada sección tiene body class `page-{id}` (definida en el JSON)
- Banners de sección: `assets/images/{seccion}-banner.png` (1020x271px, fondo negro)
- Los banners se aplican en `src/scss/components/_content.scss`

## Banners de secciones

Patrón CSS:
```scss
.page-{seccion} .content-header {
  background-image: url('../assets/images/{seccion}-banner.png');
}
```
Tamaño: 1020x271px, formato PNG, fondo negro (#000).

## Tipografías

Google Fonts cargadas en `base.html`:
- Cormorant Garamond (serif, títulos)
- Inter (sans-serif, UI)
- Lora (serif, cuerpo)
- Playfair Display (serif, display)

## .gitignore — Notas importantes

- `public/` SÍ se versiona (CF Pages lo despliega directo)
- `*.json` está ignorado EXCEPTO `package.json`, `src/data/**/*.json` y `data/**/*.json`
- `trash/` ignorado
- `.env` ignorado

## Dependencias (todas devDependencies)

- handlebars ^4.7.8 — Motor de plantillas
- sass ^1.97.2 — Compilador SCSS
- fs-extra ^11.2.0 — File system
- chalk ^4.1.2 — Colores en consola
- cheerio ^1.0.0-rc.12 — Parsing HTML
- serve (npx) — Servidor local

## Symlinks en src/content/

- `conciertos.html` → `veladas.html`
- `labanda.html` → `labandaelastica.html`
- `nuevos.html` → `proyectos.html`

Estos existen porque el ID de navegación difiere del nombre de archivo.

## Errores comunes

- **"No se encontró contenido"**: Falta el HTML en `src/content/`. El build genera la página igual con placeholder.
- **Página nueva no se genera**: No está en los arrays de `build.js` (`menuMediaPages`, `additionalPages` o `subDirPages`).
- **SCSS no compila**: Verificar sintaxis y que el `@use` esté en `app.scss`.
- **Cambios no en producción**: Verificar commit + push. CF despliega en 1-2 min.
- **Puerto 3012 ocupado**: `npm run dev:serve` mata el proceso automáticamente.
