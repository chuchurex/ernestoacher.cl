# Ernesto Acher - Sitio Web Homenaje

Sitio web dedicado a la memoria del músico argentino Ernesto Acher (1947-2024).

**Versión**: 2.0.0
**Hosting**: Cloudflare Pages
**URL**: https://ernestoacher.cl

---

## Estructura del Proyecto

```
ernestoacher.cl/
│
├── src/                     # CÓDIGO FUENTE
│   ├── content/             # Contenido HTML de páginas
│   ├── data/                # Datos JSON (navegación, secciones)
│   ├── scss/                # Estilos SCSS modulares
│   │   ├── _variables.scss  # Variables globales
│   │   ├── _mixins.scss     # Mixins reutilizables
│   │   ├── base/            # Reset, tipografía
│   │   ├── components/      # Sidebar, content, carousel
│   │   ├── layout/          # Header, footer, interior
│   │   ├── sections/        # Estilos por sección
│   │   └── utilities/       # Helpers
│   └── templates/           # Plantillas Handlebars
│       └── partials/        # Parciales reutilizables
│
├── assets/                  # Imágenes del diseño (headers, logos)
├── images/                  # Fotos de contenido
├── galerias/                # Galerías de fotos
├── js/                      # JavaScript
├── components/              # Componentes HTML
├── data/                    # Datos para el build
│
├── scripts/                 # Scripts de build y utilidades
├── docs/                    # Documentación del proyecto
│
├── .claude/                 # Configuración Claude Code
├── package.json             # Dependencias npm
└── README.md                # Este archivo
```

**Nota**: `public/` es generado por el build y no se versiona.

---

## Comandos

```bash
# Instalar dependencias
npm install

# Build completo (genera sitio en public/)
npm run build

# Servidor de desarrollo (puerto 3012)
npx serve public -p 3012

# Watch de SCSS durante desarrollo
npm run sass:watch

# Validar enlaces rotos
npm run validate
```

---

## Flujo de Trabajo

1. Editar contenido en `src/content/`
2. Editar estilos en `src/scss/`
3. Ejecutar `npm run build`
4. Probar con `npx serve public -p 3012`
5. Commit y push a `main` → Deploy automático

---

## Arquitectura

### Principios

- **Single Source of Truth**: Datos en JSON, no duplicados
- **Plantillas Handlebars**: Reutilización de componentes
- **SCSS Modular**: Estilos organizados por responsabilidad
- **Rutas Absolutas**: Sin cálculos dinámicos frágiles
- **Validación Automática**: Enlaces rotos detectados en build

### Agregar Nueva Sección

1. Crear `src/data/sections/[nombre].json`
2. Agregar entrada en `src/data/navigation.json`
3. Crear `src/content/[nombre].html`
4. (Opcional) Crear `src/scss/sections/_[nombre].scss`
5. Ejecutar `npm run build`

---

## Tecnologías

- **Templates**: Handlebars
- **Estilos**: SCSS (Dart Sass)
- **Build**: Node.js scripts
- **Hosting**: Cloudflare Pages

---

## Documentación

Ver `docs/` para documentación detallada:

- `QUICK-START.md` - Inicio rápido
- `NUEVA-ARQUITECTURA.md` - Arquitectura del sistema
- `GUIA_ESTILOS.md` - Guía de estilos CSS
- `DEVELOPMENT.md` - Guía de desarrollo
