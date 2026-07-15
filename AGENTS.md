# ernestoacher.cl - Sitio homenaje a Ernesto Acher (1947-2024)

Músico, compositor, director y humorista argentino. Miembro de Les Luthiers (1971-1986).
Generador estático propio que reconstruye el sitio original (rescatado de archive.org) con arquitectura modular.

## Stack

- Node.js + Handlebars (plantillas) + Dart Sass (SCSS, con `@use`, no `@import`)
- Build propio en `scripts/build.js` (clase `SiteBuilder`)
- devDependencies: handlebars, sass, fs-extra, chalk, cheerio, npm-run-all, live-server, nodemon
- Salida en `public/` (se versiona en git)
- Fuentes Google (en `base.html`): Cormorant Garamond, Inter, Lora, Playfair Display

## Comandos

```bash
npm run build        # build.js + sass:build + copia images/assets/galerias/js/components/data a public/
npm run dev          # build + servidor local en http://localhost:3012 (libera el puerto si está ocupado)
npm run sass:build   # compila SCSS comprimido a public/css (sin source map)
npm run sass:watch   # watch SCSS expandido con source map
npm run validate     # valida enlaces internos (scripts/validate-links.js)
npm run clean        # borra y recrea public/
npm run start        # build + validate
```

Antes de commitear cambios del sitio: correr `npm run build` para verificar.

## Estructura

```
src/
├── content/        # HTML crudo por página (sin layout); subdirs por sección (lesluthiers/, quorum/, veladas/)
├── data/
│   ├── site.json         # config global (meta, carousel, menuMedia, footer)
│   ├── navigation.json   # source of truth de navegación
│   └── sections/         # un JSON por página (~103 archivos)
├── scss/           # app.scss (entry), _variables, _mixins, base/ layout/ components/ sections/ (13) utilities/
└── templates/      # base.html, page-home.html, page-interior.html, partials/
scripts/            # build.js, validate-links.js, deploy.sh + muchos scripts .py/.sh de migración (one-off)
images/ assets/images/ galerias/ js/ components/   # activos copiados a public/ en el build
public/             # OUTPUT del build (versionado)
```

Build: cada página combina plantilla (`src/templates`) + datos (`src/data/sections/{id}.json`) + contenido (`src/content/{id}.html`).
Métodos: `buildHomePage`, `buildPage`/`buildSubPage` (sección con submenú), `buildSimplePage` (páginas sueltas y subdirectorios).

Navegación (`src/data/navigation.json`), tres bloques:
- `sidebar` - menú lateral izquierdo (secciones principales, con `subPages`)
- `headerPrimary` - iconos header superior (Inicio, Links, Actualizaciones, Mapa del sitio, Contacto)
- `headerSecondary` - links secundarios (Discografía, Anecdotario, Pregunte nomás, Partituras, Galerías)

## Notas

- Las páginas a generar están hardcodeadas en 3 arrays dentro de `buildAll()` en `build.js`: `menuMediaPages`, `additionalPages`, `subDirPages`. Al agregar una página nueva HAY QUE sumarla al array correspondiente o no se genera.
- IDs de subdirectorio: el primer `-` se vuelve `/` si el segundo segmento es numérico o empieza con `f_` (ej: `lesluthiers-1971` → `src/content/lesluthiers/1971.html`).
- Agregar sección completa: JSON en `sections/{id}.json` + contenido en `content/{id}.html` + entrada en `navigation.json` + entrada en el array de `build.js` + (opcional) `scss/sections/_{id}.scss` con su `@use` en `app.scss`. Cada sección tiene body class `page-{id}` (en el JSON).
- Banners de sección: `assets/images/{seccion}-banner.png` (1020x271px, fondo negro), aplicados en `scss/components/_content.scss`.
- Symlinks en `src/content/` (el ID de nav difiere del nombre de archivo): `conciertos.html`→`veladas.html`, `labanda.html`→`labandaelastica.html`, `nuevos.html`→`proyectos.html`.
- `.gitignore`: `public/` SÍ se versiona; `*.json` ignorado EXCEPTO `package.json`, `src/data/**/*.json` y `data/**/*.json`; `trash/` y `.env` ignorados.
- Errores comunes: "No se encontró contenido" = falta HTML en `src/content/` (genera placeholder); página nueva no aparece = falta en los arrays de `build.js`; SCSS no compila = revisar sintaxis y el `@use` en `app.scss`.
- Deploy: hay dos rutas. Según la documentación previa, Cloudflare Pages despliega automáticamente al pushear a `main` sirviendo `public/`. Además existe `scripts/deploy.sh`, que sube por rsync/SSH a un host externo (variables `UPLOAD_HOST`, `UPLOAD_PORT`, `UPLOAD_USER`, `UPLOAD_PASS`, `UPLOAD_DIR`, `DOMAIN`) y opcionalmente purga la caché de Cloudflare (`CF_ZONE_ID`, `CLOUDFLARE_API_TOKEN`/`CF_API_KEY`, `CF_EMAIL`, `CF_ACCOUNT_ID`). Confirmar cuál es la vía activa antes de desplegar. Los valores reales viven en `.env` (gitignored); ver `.env.example` para la lista.
- No commitear ni pushear sin que el usuario lo pida explícitamente.
- Comunicarse siempre en español con el usuario.

## Infraestructura (deploy y datos SEO)

El deploy en Cloudflare y el acceso a datos SEO (Search Console / Analytics) usan credenciales
gestionadas localmente por el mantenedor, fuera del repositorio. No hay secretos versionados:
tokens y service accounts viven solo en el entorno local, nunca en el repo.
