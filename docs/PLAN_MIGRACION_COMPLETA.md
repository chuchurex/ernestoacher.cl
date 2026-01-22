# Plan de Migración Completa - ernestoacher.com.ar → ernestoacher.cl

**Fecha:** 15 de enero de 2026
**Objetivo:** Migrar todo el contenido del sitio original a la nueva plataforma

## 📊 Estado Actual

### Contenido en Backup
- **238 archivos HTML** distribuidos en 13 secciones
- **485 imágenes** (JPG, GIF, PNG)
- Estructura completa del sitio original

### Ya Integrado ✅
- Anecdotario (19 anécdotas)
- Imágenes básicas (carrusel, secciones, galerías: 151 imágenes)
- Páginas índice (Discografía, Partituras, Galerías, Links, Contacto)
- Sistema de componentes (sidebar, header)
- Estilos SCSS modulares

## 🎯 Secciones Pendientes de Migración

### 1️⃣ ALTA PRIORIDAD (Contenido principal)

#### Les Luthiers (`ll/` - 16 archivos HTML)
- index.htm (página principal)
- Espectáculos, discografía, fotos
- Integrar con sistema actual de menú

#### La Banda Elástica (`lbe/` - 10 archivos HTML)
- index.htm (página principal)
- Espectáculos, discografía, fotos, videos
- Similar estructura a Les Luthiers

#### Humor con Achís (`hca/` - 3 archivos HTML)
- index.htm (unipersonal)
- Fotos relacionadas

#### Veladas Espeluznantes (`ve/` - 4 archivos HTML)
- index.htm (conciertos de música humor)
- Fotos relacionadas

### 2️⃣ MEDIA PRIORIDAD (Proyectos específicos)

#### Offside Chamber Orchestra (`ocho/` - 2 archivos HTML)
- index.htm
- Información del proyecto

#### Gershwin (`hg/` - 1 archivo HTML)
- index.htm (Homenaje a Gershwin)

#### Los Animales de la Música (`ladm/` - 2 archivos HTML)
- index.htm (concierto para niños)

#### De Todo como en Botica (`dtodo/` - 4 archivos HTML)
- index.htm
- Otros proyectos

### 3️⃣ BAJA PRIORIDAD (Administrativo/Histórico)

#### Realizaciones Recientes (`rr/` - 2 archivos HTML)
- Proyectos recientes (contenido potencialmente desactualizado)

#### Nuevos Proyectos (`proyectos/` - 1 archivo HTML)
- Proyectos en desarrollo

#### Menú de Conciertos (`menu/` - 1 archivo HTML)
- Programación de conciertos

### 4️⃣ CONTENIDO MULTIMEDIA

#### Discografía Detallada (`discos/` - 10 archivos HTML)
- Páginas individuales de discos
- Integrar con discografia.html actual

#### Galerías Completas (`galerias/` - 162 archivos HTML!)
- 162 páginas de galerías de fotos
- 327 imágenes asociadas
- Requiere estrategia especial (posible generación automática)

## 🔄 Estrategia de Migración

### Fase 1: Extracción y Limpieza de Datos
**Herramienta:** Scripts Python automatizados

1. Extraer contenido de todos los HTML
2. Limpiar markup antiguo (tablas, frames)
3. Convertir a UTF-8
4. Generar JSONs estructurados por sección

### Fase 2: Generación de Páginas
**Herramienta:** Scripts Node.js + Templates

1. Crear templates HTML reutilizables
2. Generar páginas con diseño moderno
3. Mantener componentes sidebar/header
4. Aplicar estilos SCSS consistentes

### Fase 3: Integración de Imágenes
**Proceso:**

1. Copiar imágenes a estructura organizada
2. Optimizar tamaños si es necesario
3. Actualizar rutas en HTML generado
4. Verificar carga correcta

### Fase 4: Actualización de Navegación
**Cambios:**

1. Actualizar menú sidebar con nuevas secciones
2. Completar enlaces del header flotante
3. Agregar navegación interna entre páginas relacionadas
4. Breadcrumbs donde sea necesario

## 📋 Plan de Ejecución Detallado

### Orden Sugerido de Implementación

```
1. Les Luthiers (ll/) - Principal, más contenido
   ├── Extraer estructura
   ├── Generar páginas
   └── Integrar al menú

2. La Banda Elástica (lbe/) - Similar a LL
   ├── Reutilizar lógica de LL
   ├── Generar páginas
   └── Integrar al menú

3. Proyectos musicales (hca, ve, ocho, hg, ladm, dtodo)
   ├── Procesar en batch
   ├── Template común
   └── Generar todas juntas

4. Discografía detallada (discos/)
   ├── Integrar con discografia.html existente
   └── Generar páginas de discos individuales

5. Galerías (galerias/)
   ├── Estrategia especial (muchos archivos)
   ├── Posible lightbox/galería dinámica
   └── Considerar lazy loading

6. Resto (rr, proyectos, menu)
   ├── Contenido secundario
   └── Generar según necesidad
```

## 🛠️ Herramientas a Desarrollar

### Scripts de Extracción
```python
# extract_all_sections.py
- Procesar todas las secciones
- Generar JSONs estructurados
- Limpiar HTML antiguo
```

### Generadores de Páginas
```javascript
// generate_section_pages.js
- Template engine para cada tipo de sección
- Generación en batch
- Validación de enlaces
```

### Optimizador de Imágenes
```bash
# optimize_images.sh
- Redimensionar si es necesario
- Comprimir sin perder calidad
- Generar thumbnails para galerías
```

## 📊 Estimación de Archivos a Generar

| Sección | HTML Origen | HTML Destino | Imágenes |
|---------|-------------|--------------|----------|
| ll | 16 | 16 | ~50 |
| lbe | 10 | 10 | ~30 |
| hca | 3 | 3 | ~10 |
| ve | 4 | 4 | ~15 |
| ocho | 2 | 2 | ~15 |
| hg | 1 | 1 | ~5 |
| ladm | 2 | 2 | ~15 |
| dtodo | 4 | 4 | ~30 |
| rr | 2 | 2 | ~25 |
| proyectos | 1 | 1 | ~5 |
| menu | 1 | 1 | ~10 |
| discos | 10 | 10 | ~20 |
| galerias | 162 | 162* | 327 |
| **TOTAL** | **218** | **218** | **~557** |

*Las galerías podrían simplificarse con un sistema dinámico

## 🎨 Diseño y Estilos

### Componentes a Crear
- `.page-lesluthiers` - Estilos para sección LL
- `.page-banda-elastica` - Estilos para LBE
- `.page-proyecto` - Template genérico para proyectos
- `.gallery-grid` - Grid moderno para galerías
- `.disco-card` - Cards para discos individuales

### Características Comunes
- Sidebar dinámico (ya implementado)
- Header flotante (ya implementado)
- Navegación breadcrumb
- Enlaces "volver" consistentes
- Responsive design
- Lazy loading para imágenes

## ⚠️ Consideraciones Especiales

### Galerías (162 archivos)
**Opciones:**
1. **Migración completa:** Generar las 162 páginas individuales
2. **Sistema dinámico:** Crear galería JavaScript con datos JSON
3. **Híbrido:** Páginas principales + lightbox para fotos

**Recomendación:** Opción 3 (híbrido) para mejor UX y menos archivos

### Contenido Desactualizado
- Revisar "Realizaciones Recientes" y "Nuevos Proyectos"
- Considerar archivar o actualizar antes de publicar
- Marcar claramente fechas históricas

### Videos y Multimedia
- Verificar si los videos aún existen
- Considerar embed de YouTube si aplica
- Archivos MPEG-4 locales o streaming

## ✅ Criterios de Éxito

- [ ] Todo el contenido HTML migrado
- [ ] Todas las imágenes integradas y funcionando
- [ ] Navegación completa y funcional
- [ ] Diseño consistente en todas las páginas
- [ ] Responsive en mobile/tablet/desktop
- [ ] Performance optimizado (imágenes, lazy load)
- [ ] SEO básico (meta tags, títulos, descripciones)
- [ ] Sin enlaces rotos
- [ ] Encoding UTF-8 correcto en todo el sitio

## 🚀 Próximos Pasos Inmediatos

1. **Confirmar prioridades** con el usuario
2. **Empezar con Les Luthiers** (sección más importante)
3. **Desarrollar sistema de extracción** reutilizable
4. **Generar primeras páginas** como prueba de concepto
5. **Iterar** con el resto de secciones

---

**Nota:** Este es un proyecto grande pero sistemático. Con las herramientas adecuadas y procesamiento en batch, podemos completarlo eficientemente.
