# Ernesto Acher - Sitio Homenaje

Recreación fiel del sitio web oficial de **Ernesto Acher** (versión 2008), como homenaje a este destacado músico, compositor, director y humorista argentino.

## Acerca de Ernesto Acher

Ernesto Acher (1947-2025) fue un artista multifacético argentino reconocido internacionalmente por su talento como músico, compositor, director de orquesta, actor y humorista. Fue miembro de **Les Luthiers** durante 17 años, y posteriormente desarrolló una prolífica carrera como solista con proyectos como **La Banda Elástica**, **Homenaje a Gershwin**, y sus famosas **Veladas** de música y humor.

## Sobre este Proyecto

Este sitio es una recreación del sitio web original de Ernesto Acher, originalmente desarrollado en Flash en 2004 y actualizado hasta 2008. El sitio original fue rescatado de [Web Archive](https://web.archive.org/web/20080729145131/http://ernestoacher.com/) y reconstruido con tecnologías web modernas.

**Dominio original**: ernestoacher.com (actualmente tomado por terceros)
**Nuevo dominio**: ernestoacher.cl

## Estructura del Proyecto

```
/
├── index.html          # Página principal (recreación del home Flash)
├── css/
│   └── styles.css      # Estilos (fondo negro, elipse burdeo, etc.)
├── js/
│   └── main.js         # JavaScript (carrusel interactivo)
├── assets/
│   └── images/         # Imágenes y assets
└── README.md           # Este archivo
```

## Características

- **Diseño fiel al original**: Fondo negro, elipse concho de vino, tipografía script plateada
- **Menú interactivo**: El menú principal controla un carrusel de contenido destacado
- **Responsive**: Adaptado para dispositivos móviles
- **Sin Flash**: Recreado con HTML5, CSS3 y JavaScript vanilla

## Secciones del Sitio

### Menú Principal (Proyectos)
- Les Luthiers
- La Banda Elástica
- Unipersonal
- Conciertos de música humor
- Offside Chamber Orchestra
- Homenaje a Gershwin
- Los animales de la música
- De todo como en botica
- Realizaciones recientes
- Nuevos proyectos
- Menú de conciertos

### Menú Media (Contenido)
- Discografía
- Anecdotario
- Partituras
- Galerías
- Contacto

## Paleta de Colores

| Color | Hex | Uso |
|-------|-----|-----|
| Negro | `#0d0d0d` | Fondo principal |
| Concho de vino | `#6B1C23` | Elipse decorativa |
| Blanco | `#ffffff` | Texto |
| Plateado | `#d4d4d4` | Logo y acentos |

## Tipografías

- **Logo**: Great Vibes (Google Fonts)
- **Menús**: Crimson Text (Google Fonts)
- **Textos**: Georgia (sistema)

## Despliegue

Configurado para **Cloudflare Pages**:
1. Conectar repositorio GitHub
2. Build command: (ninguno, es estático)
3. Build output directory: `/`

## Desarrollo Local

```bash
# Clonar repositorio
git clone https://github.com/chuchurex/ernestoacher.cl.git
cd ernestoacher.cl

# Servir localmente
python -m http.server 8000
# o
npx serve
```

## Créditos

- **Sitio original**: Desarrollado en 2004, actualizado 2008
- **Recreación 2026**: [chuchurex](https://github.com/chuchurex)
- **Contenido rescatado de**: Internet Archive Wayback Machine

## Licencia

Este es un proyecto de homenaje sin fines de lucro. Todos los derechos sobre la imagen, nombre y contenido de Ernesto Acher pertenecen a sus respectivos titulares.

---

*"Los arquitectos aplaudieron y los músicos guardaron respetuoso silencio..."* — Ernesto Acher
