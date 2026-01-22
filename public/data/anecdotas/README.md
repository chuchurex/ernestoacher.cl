# Anécdotas - Datos JSON

Este directorio contiene todas las anécdotas extraídas del sitio antiguo en formato JSON estructurado.

## Contenido

- **19 archivos JSON individuales**: Una anécdota por archivo
- **1 archivo índice** (`index.json`): Índice completo organizado por categorías

## Estructura de cada archivo JSON

```json
{
  "id": "zanotti",
  "title": "(Les Luthiers) Zanotti",
  "cleanTitle": "Zanotti",
  "category": "Les Luthiers",
  "content": "<p>Contenido HTML limpio...</p>"
}
```

### Campos:

- **id**: Identificador único basado en el nombre del archivo original
- **title**: Título original con prefijo de categoría (si aplica)
- **cleanTitle**: Título sin prefijo, solo el nombre de la anécdota
- **category**: Categoría de la anécdota (Les Luthiers, La Banda Elástica, Gershwin, General)
- **content**: Contenido HTML limpio preservando párrafos y formato básico

## Archivo índice (index.json)

El archivo `index.json` contiene:

```json
{
  "total": 19,
  "categories": {
    "Les Luthiers": [array de anécdotas],
    "La Banda Elástica": [array de anécdotas],
    "Gershwin": [array de anécdotas],
    "General": [array de anécdotas]
  },
  "all": [array completo de todas las anécdotas]
}
```

## Categorías

### Les Luthiers (7 anécdotas)
- Historia de Don Rodrigo
- Pucho y el souvenir
- Tarzán y el telón
- La inundación
- Viaje accidentado
- Una ventana...
- Zanotti

### La Banda Elástica (4 anécdotas)
- Carlitos y la trompeta
- Flores negras
- Halloween
- Era más blanda que el agua...

### Gershwin (2 anécdotas)
- El mejor clarinetista
- Volados…

### General (6 anécdotas)
- Algún proyecto?
- Catástrofe
- Qué le anda pasando, m'hijo?
- El estreno de Molloy
- La estatua de Pushkin
- Debut en Rosario

## Uso en JavaScript

### Cargar índice completo:
```javascript
fetch('data/anecdotas/index.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Total de anécdotas: ${data.total}`);
    console.log('Categorías:', Object.keys(data.categories));
  });
```

### Cargar anécdota individual:
```javascript
fetch('data/anecdotas/zanotti.json')
  .then(response => response.json())
  .then(anecdota => {
    console.log(anecdota.cleanTitle);
    document.querySelector('#content').innerHTML = anecdota.content;
  });
```

### Listar anécdotas por categoría:
```javascript
fetch('data/anecdotas/index.json')
  .then(response => response.json())
  .then(data => {
    const lesLuthiers = data.categories['Les Luthiers'];
    lesLuthiers.forEach(anecdota => {
      console.log(`${anecdota.id}: ${anecdota.cleanTitle}`);
    });
  });
```

## Formato del contenido HTML

El campo `content` contiene HTML limpio con:
- Tags de párrafo `<p>`
- Tags de formato: `<b>`, `<i>`, `<em>`, `<strong>`
- Saltos de línea: `<br>`
- Enlaces: `<a href="...">`

Los textos están en UTF-8 con caracteres Unicode correctamente convertidos.

## Regenerar datos

Si necesitas regenerar los datos desde los archivos HTML originales:

```bash
# Extraer anécdotas desde archivos HTML
python3 scripts/extract_anecdotas.py

# Crear índice y agregar categorías
python3 scripts/create_anecdotas_index.py
```

## Archivos fuente

Los archivos HTML originales se encuentran en:
`/Users/chuchurex/Sites/prod/ernestoacher.cl/backup/anecdotario/`
