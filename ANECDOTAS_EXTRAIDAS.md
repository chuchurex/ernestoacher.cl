# Extracción de Anécdotas - Completada

## Resumen

Se han extraído exitosamente **19 anécdotas** del sitio antiguo y convertido a formato JSON estructurado.

## Ubicación de los archivos

- **Directorio de datos**: `/Users/chuchurex/Sites/prod/ernestoacher.cl/data/anecdotas/`
- **Scripts de procesamiento**: `/Users/chuchurex/Sites/prod/ernestoacher.cl/scripts/`

## Archivos generados

### 1. Archivos JSON individuales (19 anécdotas)

Cada archivo contiene:
- `id`: Identificador único (basado en nombre de archivo)
- `title`: Título original con categoría
- `cleanTitle`: Título sin prefijo de categoría
- `category`: Categoría de la anécdota
- `content`: Contenido HTML limpio (con párrafos y formato básico)

#### Por categoría:

**Les Luthiers (7 anécdotas):**
- `drodrigo.json` - Historia de Don Rodrigo
- `ll03.json` - Pucho y el souvenir
- `ll04.json` - Tarzán y el telón
- `ll05.json` - La inundación
- `ll06.json` - Viaje accidentado
- `ll35.json` - Una ventana...
- `zanotti.json` - Zanotti

**La Banda Elástica (4 anécdotas):**
- `carlitosy.json` - Carlitos y la trompeta
- `fnegras.json` - Flores negras
- `lbe01.json` - Halloween
- `lbe18.json` - Era más blanda que el agua...

**Gershwin (2 anécdotas):**
- `mejor_clari.json` - El mejor clarinetista
- `volados.json` - Volados…

**General (6 anécdotas):**
- `algun_proy.json` - Algún proyecto?
- `catastrofe.json` - Catástrofe
- `mhijo.json` - Qué le anda pasando, m'hijo?
- `molloy.json` - El estreno de Molloy
- `pushkin.json` - La estatua de Pushkin
- `rosario.json` - Debut en Rosario

### 2. Archivo índice

**`index.json`**: Contiene un índice completo con:
- Total de anécdotas
- Lista organizada por categorías
- Lista completa de todas las anécdotas

## Estructura de datos JSON

### Ejemplo de anécdota individual:

```json
{
  "id": "rosario",
  "title": "Debut en Rosario",
  "cleanTitle": "Debut en Rosario",
  "category": "General",
  "content": "<p>Acabo de hacer un concierto...</p>"
}
```

### Estructura del índice:

```json
{
  "total": 19,
  "categories": {
    "Les Luthiers": [...],
    "La Banda Elástica": [...],
    "Gershwin": [...],
    "General": [...]
  },
  "all": [...]
}
```

## Scripts creados

1. **`extract_anecdotas.py`**:
   - Extrae contenido de archivos HTML antiguos
   - Convierte entidades HTML a Unicode
   - Limpia y estructura el contenido
   - Genera archivos JSON individuales

2. **`create_anecdotas_index.py`**:
   - Lee todos los archivos JSON
   - Extrae categorías de los títulos
   - Crea títulos limpios sin prefijos
   - Genera archivo índice organizado

## Características del contenido extraído

- **Encoding**: UTF-8 (convertido desde ISO-8859-1)
- **Entidades HTML**: Convertidas a caracteres Unicode (á, é, í, ó, ú, ñ, etc.)
- **Formato preservado**: Se mantienen párrafos, negritas, cursivas, enlaces
- **Tags preservados**: `<p>`, `<b>`, `<i>`, `<em>`, `<strong>`, `<br>`, `<a>`

## Próximos pasos sugeridos

1. Crear páginas HTML individuales para cada anécdota
2. Crear página índice con navegación por categorías
3. Implementar diseño responsivo
4. Agregar navegación entre anécdotas
5. Integrar con el menú del sitio

## Archivos fuente originales

Los archivos HTML originales se encuentran en:
`/Users/chuchurex/Sites/prod/ernestoacher.cl/backup/anecdotario/`

## Notas técnicas

- Todos los archivos JSON usan `ensure_ascii=False` para preservar caracteres Unicode
- El contenido HTML está limpio pero mantiene la estructura semántica básica
- Las categorías se extraen automáticamente de los prefijos en los títulos
- El ID de cada anécdota se basa en el nombre del archivo original
