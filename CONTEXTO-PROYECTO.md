# Contexto del Proyecto: Sitio Homenaje Ernesto Acher

## Resumen Ejecutivo

Ernesto Acher falleció recientemente (finales 2025). El usuario (chuchu/chuchurex) trabajó con él en su sitio web original en 2004 y lo actualizó en 2008. El dominio `ernestoacher.com` fue tomado por spammers (sitio de apuestas indonesio "AreaSlots"). Se decidió crear `ernestoacher.cl` como sitio homenaje, recreando fielmente el sitio original de 2008.

---

## Información del Dominio Original

### ernestoacher.com (TOMADO)
- **Registrado originalmente**: 15 abril 2004
- **Expira**: 15 abril 2026
- **Registrar**: GoDaddy.com, LLC
- **Estado actual**: Usado por sitio de gambling indonesio
- **Bloqueos**: client delete/renew/transfer/update prohibited (no quieren venderlo fácilmente)

### Nuevo dominio
- **ernestoacher.cl** - Comprado por el usuario
- **Hosting**: Cloudflare Pages
- **Repositorio**: https://github.com/chuchurex/ernestoacher.cl

---

## Sitio Original (Web Archive)

### URL de referencia
```
https://web.archive.org/web/20080729145131/http://ernestoacher.com/
```

### Tecnología original
- **Flash** (ahora funciona con Ruffle emulator en Web Archive)
- 214 capturas disponibles desde julio 2004 hasta noviembre 2025

### Diseño visual del home
- **Fondo**: Negro (#0d0d0d)
- **Elemento central**: Elipse horizontal color "concho de vino" / burdeo (#6B1C23)
- **Logo**: "Ernesto Acher" en tipografía script/cursiva plateada, arriba centrado
- **Decoración bajo logo**: Cintas/pañuelo plateado decorativo
- **Foto de Ernesto**: A la derecha, dentro de la elipse, con chaleco rojo y camisa negra, dirigiendo con las manos
- **Menú principal**: Izquierda, texto blanco
- **Menú media**: Derecha, texto blanco

### Comportamiento original (Flash)
- Al hacer hover en ítems del menú, aparecía un preview del contenido en el centro
- El usuario quiere convertir esto en un **carrusel automático** que avanza mostrando previews, y el hover del menú controla qué slide se muestra

---

## Estructura de Menús

### Menú Principal (izquierda) - Proyectos/Shows
1. Les Luthiers
2. La Banda Elástica
3. Unipersonal
4. Conciertos de música humor
5. Offside Chamber Orchestra
6. Homenaje a Gershwin
7. Los animales de la música
8. De todo como en botica
9. Realizaciones recientes
10. Nuevos proyectos
11. Menú de conciertos

### Menú Media (derecha) - Contenido
1. Discografía
2. Anecdotario
3. Partituras
4. Links
5. Galerías
6. Contacto

### Footer
- Link a "Actualizaciones" con fecha de última actualización

---

## Contenido Disponible en Web Archive

### Anecdotario
- Historias de Les Luthiers: ll01.htm - ll35.htm
- Historias de La Banda Elástica: lbe01.htm - lbe27.htm
- Otras anécdotas: animales, carlitos, catastrofe, drodrigo, fnegras, mejor_clari, mhijo, molloy, pushkin, rosario, volados, zanotti

### Discografía (imágenes de carátulas disponibles)
- La Banda Elástica (lbe1.jpg, lbe2.jpg, lbe3.jpg)
- Les Luthiers (ll2.jpg - ll7.jpg)
- Gershwin (gershwin.jpg)
- Quorum (quorum.jpg)
- Juegos (juegos.jpg, juegos2.jpg)

### Galerías de Fotos
**Dibujos/Acuarelas de viajes:**
- antumalal, callbeso, cancun, caracas, casaraymont, cdlpaz, chartres (1-3), convleones, cpark (1-4), cuernavaca, curitiba, elcadillal, guaruja, iguazu (1-2), kensington, mexbaeza, mexjuarez, nieve, notredame, nybrooklyn, nycolumbus, nyguggen, nysexta, patera, pzabaratillo, pzapino, pzasroque, pzateatro, ronchamps (1-4), salamaya, schapelle, sfbahia, sfghirardelli, smainstituto, villavicencio, vistaalegre, yacanto

**Fotos de shows:**
- f_hca (1-2) - Homenaje Cámara de Arte
- f_hg (1-19) - Homenaje a Gershwin
- f_hp (1-7)
- f_lbe (1-32) - La Banda Elástica

### Videos (mpeg-4 zips)
- **Animales**: adlm-manuelita, adlm-moscardon, adlm-zorro
- **Banda**: lbe-cambalache, lbe-cottontail, lbe-historia, lbe-lunatucumana, lbe-perro, lbe-tiger_rag
- **Colegio**: colegio-1812, colegio-6a
- **Enserio**: retrato
- **Gershwin**: gg-but_not, gg-someone, gg-they_cant
- **Veladas**: ve-40choclos, ve-schumann

### Otros assets
- CSS: acher.css
- Favicon: favicon.ico
- Imágenes del menú en /menu/gfx/

---

## Decisiones de Diseño para la Recreación

### Tipografía
- **Logo "Ernesto Acher"**: Google Fonts "Great Vibes" (similar a la script original)
- **Menús**: Google Fonts "Crimson Text"
- **Textos**: Georgia (sistema)

### Colores (CSS Variables)
```css
--color-background: #0d0d0d;  /* Negro */
--color-wine: #6B1C23;        /* Concho de vino */
--color-wine-dark: #4A1117;   /* Vino oscuro */
--color-text: #ffffff;        /* Blanco */
--color-text-dim: #cccccc;    /* Gris claro */
--color-silver: #d4d4d4;      /* Plateado */
```

### Comportamiento del carrusel
- Auto-avanza cada 6 segundos
- Al hacer hover en ítem del menú principal → muestra ese slide
- Al salir del hover → continúa auto-play
- Navegación con flechas del teclado
- Efecto fade-in en transiciones

### Responsive
- Desktop: Layout de 3 columnas con grid
- Tablet: Ajustes de tamaño
- Mobile: Layout vertical, sin elipse

---

## Archivos Creados

```
/
├── index.html          # Página principal completa
├── css/
│   └── styles.css      # ~500 líneas de CSS
├── js/
│   └── main.js         # Carrusel y efectos (~150 líneas)
├── assets/
│   └── images/         # Carpeta vacía (agregar imágenes)
└── README.md           # Documentación del proyecto
```

---

## Tareas Pendientes

### Inmediatas
1. [ ] Agregar foto de Ernesto como `assets/images/ernesto-acher.png` (con fondo transparente)
2. [ ] Rescatar imágenes de preview del Web Archive para el carrusel
3. [ ] Probar localmente y ajustar CSS
4. [ ] Subir al repositorio GitHub
5. [ ] Conectar a Cloudflare Pages

### Futuras
- [ ] Implementar páginas internas de cada sección
- [ ] Rescatar todo el contenido del anecdotario
- [ ] Crear galería de fotos
- [ ] Agregar videos (embed YouTube o hosting propio)
- [ ] Sección de homenaje/in memoriam (opcional, el usuario decidirá después)

---

## URLs Útiles para Rescate de Assets

### Imágenes de preview (ejemplos)
```
https://web.archive.org/web/2008/http://www.ernestoacher.com/menu/gfx/i_t3_c7.jpg
https://web.archive.org/web/2008/http://www.ernestoacher.com/discos/gfx/lbe1.jpg
```

### CDX API para listar todos los archivos
```
https://web.archive.org/cdx/search/cdx?url=ernestoacher.com/*&output=text&fl=original&collapse=urlkey
```

### Página principal funcionando con Ruffle
```
https://web.archive.org/web/20080729145131/http://ernestoacher.com/
```

---

## Notas del Usuario

- El usuario (chuchu) trabajó personalmente con Ernesto Acher en el sitio original
- Quiere una "copia perfecta versión 2026" del sitio de 2008
- Por ahora NO quiere sección de homenaje adicional, solo la recreación fiel
- Puede continuar trabajando en Claude Code desde VSCode

---

## Contacto del Proyecto

- **Usuario**: chuchu
- **Email**: cmartinezg@uchile.cl
- **GitHub**: chuchurex
- **Repositorio**: https://github.com/chuchurex/ernestoacher.cl

---

*Documento generado: 13 enero 2026*
*Conversación: Cowork Mode - Claude*
