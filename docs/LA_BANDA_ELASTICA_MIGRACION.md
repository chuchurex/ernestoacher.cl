# Migración de La Banda Elástica - Completada

## Fecha
15 de enero de 2026

## Resumen
Extracción y migración exitosa de todo el contenido de La Banda Elástica desde el backup siguiendo el mismo patrón usado para Les Luthiers.

## Ubicación del backup
`/Users/chuchurex/Sites/prod/ernestoacher.cl/backup/lbe/`

## Archivos procesados
- **index.htm** → Página principal con historia del grupo
- **espect.htm** → Listado de espectáculos
- **discos.htm** → Discografía
- **fotos.htm** → Galería de fotos
- **videos.htm** → Videos
- **audio.htm** → Audios
- **e1.htm** → El show de la Banda Elástica (1988-1989)
- **e2.htm** → La Banda Elástica '89 (1989-1990)
- **e3.htm** → 3a. Edición (1990-1992)
- **e4.htm** → Perche mi piace (1992)

## Estructura generada

### 1. Directorio de datos JSON
**Ubicación:** `/Users/chuchurex/Sites/prod/ernestoacher.cl/data/labandaelastica/`

**Archivos generados:**
- `index.json` - Página principal (2.4 KB)
- `espectaculos.json` - Espectáculos (871 B)
- `discografia.json` - Discografía (690 B)
- `fotos.json` - Fotos (4.6 KB)
- `videos.json` - Videos (1.6 KB)
- `audio.json` - Audios (168 B)
- `e1.json` - Espectáculo 1 (1.5 KB)
- `e2.json` - Espectáculo 2 (1.7 KB)
- `e3.json` - Espectáculo 3 (1.6 KB)
- `e4.json` - Espectáculo 4 (1.6 KB)
- `catalog.json` - Índice general con todas las páginas (1.0 KB)

Cada archivo JSON contiene:
```json
{
  "id": "nombre",
  "title": "Título de la página",
  "content": "HTML limpio",
  "images": ["array de imágenes"],
  "nav_links": {}
}
```

### 2. Páginas HTML modernas
**Ubicación:** `/Users/chuchurex/Sites/prod/ernestoacher.cl/labandaelastica/`

**Archivos generados:**
- `index.html` - Página principal (3.1 KB)
- `espectaculos.html` - Espectáculos (1.6 KB)
- `discografia.html` - Discografía (1.4 KB)
- `fotos.html` - Fotos (3.8 KB)
- `videos.html` - Videos (2.3 KB)
- `audio.html` - Audios (971 B)
- `e1.html` - Espectáculo 1 (2.3 KB)
- `e2.html` - Espectáculo 2 (2.5 KB)
- `e3.html` - Espectáculo 3 (2.4 KB)
- `e4.html` - Espectáculo 4 (2.3 KB)

Todas las páginas usan el template moderno con:
- Header y sidebar dinámicos (cargados vía JavaScript)
- Breadcrumbs de navegación (excepto index)
- Estructura responsive
- Clase `page-banda-elastica` para estilos específicos

### 3. Imágenes
**Ubicación:** `/Users/chuchurex/Sites/prod/ernestoacher.cl/images/lbe/`

**Imágenes copiadas (10):**
- `i_t3_c7.jpg` (4.1 KB)
- `i_t3_c11.jpg` (2.5 KB)
- `i_t4_c12.jpg` (1.7 KB)
- `i_t5_c14.jpg` (1.4 KB)
- `i_t5_c2.jpg` (854 B)
- `i_t6_c6.jpg` (1.2 KB)
- `i_t7_c15.jpg` (1.3 KB)
- `i_t8_c17.jpg` (632 B)
- `i_t12_c5.jpg` (432 B)
- `d2_r1_c2.gif` (277 B)

**Imágenes referenciadas pero faltantes:**
- `espc.jpg` - Referenciada en espectaculos.html pero no existe en backup
- `discos.jpg` - Ya existía previamente en images/lbe/ (32 KB)

Todas las rutas de imágenes fueron actualizadas a `../images/lbe/`

## Procesamiento realizado

### Limpieza de HTML
- Eliminación de tablas de layout antiguas
- Eliminación de navegación obsoleta (divs con id="navegacion")
- Eliminación de imágenes spacer.gif
- Eliminación de scripts, objetos Flash y elementos embed
- Preservación de contenido semántico (h1, h2, h5, p, img, a)

### Conversión de encoding
- Conversión de ISO-8859-1 a UTF-8
- Decodificación de entidades HTML (&aacute;, &eacute;, etc.)
- Conversión de caracteres especiales (comillas tipográficas, etc.)

### Actualización de rutas
- Imágenes: `gfx/imagen.jpg` → `../images/lbe/imagen.jpg`
- Enlaces internos: `archivo.htm` → `archivo.html`

## Contenido extraído

### Página principal (index.html)
Contiene la historia completa de cómo se formó La Banda Elástica en 1987-1988, incluyendo:
- Formación del grupo con Jorge Navarro, Juan Amaral, Pocho Lapouble, Carlos Costantini, Juan Carlos Bazán, Hugo Pierre, Ricardo Lew y Ernesto Acher
- Cambios en la formación (incorporación de Enrique Varela y el Zurdo Roizner)
- 6 meses de ensayos diarios
- Debut en el Teatro Nacional Cervantes el 18 de junio de 1988

### Espectáculos (espectaculos.html)
Listado de los 4 espectáculos principales:
1. **El show de la Banda Elástica** (1988-1989)
2. **La Banda Elástica '89** (1989-1990)
3. **3a. Edición** (1990-1992)
4. **Perche mi piace** (1992)

Cada espectáculo tiene su propia página detallada (e1.html, e2.html, e3.html, e4.html)

### Discografía (discografia.html)
3 discos publicados:
- **Volumen 1** (1990)
- **Volumen 2** (1991)
- **Perche Mi Piace** (1992)

### Galerías multimedia
- **Fotos** (fotos.html) - Galería de fotografías del grupo
- **Videos** (videos.html) - Videos de actuaciones
- **Audio** (audio.html) - Grabaciones de audio

## Script de migración
**Ubicación:** `/Users/chuchurex/Sites/prod/ernestoacher.cl/scripts/migrate_lbe.py`

El script realiza:
1. Creación de directorios de datos y salida
2. Copia de imágenes desde backup/lbe/gfx/
3. Procesamiento de cada archivo HTML:
   - Extracción de contenido principal
   - Limpieza de HTML antiguo
   - Conversión de encoding
   - Actualización de rutas
4. Generación de archivos JSON con metadatos
5. Generación de páginas HTML modernas
6. Creación de catalog.json con índice de todas las páginas

## Estado final
✅ **10 páginas HTML generadas**
✅ **11 archivos JSON generados** (10 páginas + 1 catálogo)
✅ **10 imágenes copiadas**
✅ **Contenido completo extraído y limpiado**
✅ **Encodings convertidos a UTF-8**
✅ **Rutas actualizadas correctamente**
✅ **Enlaces internos corregidos (.htm → .html)**

## Próximos pasos sugeridos
1. Agregar entrada de "La Banda Elástica" al menú de navegación
2. Crear estilos CSS específicos para `.page-banda-elastica`
3. Agregar la sección al sitemap
4. Buscar o recrear las imágenes faltantes (espc.jpg)
5. Revisar y ajustar el formato del HTML extraído si es necesario
6. Probar la navegación entre páginas

## Notas
- El patrón de migración es idéntico al usado para Les Luthiers
- Todas las páginas usan el mismo template HTML moderno
- El contenido preserva la estructura original (h2, h5, p, tablas)
- Los enlaces internos apuntan correctamente a .html
- Las imágenes faltantes no impedirán el funcionamiento del sitio
