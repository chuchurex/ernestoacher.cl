# Plan de Rediseño - Sitio Ernesto Acher 2026

## Objetivo
Recrear el sitio completo conservando la estructura y contenido original pero con diseño moderno 2026 a pantalla completa.

## Estructura Original Detectada

### Secciones Principales
1. **Les Luthiers** (`/ll/`)
2. **La Banda Elástica** (`/lbe/`)
3. **Discografía** (`/discos/`)
4. **Anecdotario** (✓ YA HECHO)
5. **Partituras** (`/partituras/`)
6. **Galerías** (`/galerias/`)
7. **Homenaje a Gershwin** (`/hg/`)
8. **Los Animales de la Música** (`/ladm/`)
9. **Offside Chamber Orchestra** (`/ocho/`)
10. **Veladas** (`/ve/`)
11. **Realizaciones Recientes** (`/rr/`)
12. **De Todo como en botica** (`/dtodo/`)
13. **Contacto** (`/contacto/`)

## Diseño Propuesto 2026

### Layout Principal
```
┌─────────────────────────────────────────────┐
│  HEADER: Logo Ernesto Acher (Grande)       │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────┐  ┌─────────────────────┐    │
│  │          │  │                     │    │
│  │  MENÚ    │  │   CONTENIDO         │    │
│  │  STICKY  │  │   PRINCIPAL         │    │
│  │          │  │                     │    │
│  │          │  │                     │    │
│  └──────────┘  └─────────────────────┘    │
│                                             │
├─────────────────────────────────────────────┤
│  FOOTER: Actualizado, Contacto              │
└─────────────────────────────────────────────┘
```

### Características Diseño
- **Pantalla completa** (viewport 100%)
- **Menú lateral sticky** (siempre visible al scroll)
- **Tipografía moderna**: Great Vibes + Crimson Text
- **Fondo oscuro elegante** (como el original pero mejorado)
- **Animaciones sutiles** CSS3
- **Totalmente responsive**
- **Navegación fluida** (scroll suave)

### Sistema de Colores
```css
--color-bg: #0a0a0f;          /* Fondo oscuro principal */
--color-bg-light: #1a1a2e;    /* Fondo secciones */
--color-primary: #d4af37;      /* Dorado (botones, acentos) */
--color-text: #e8e8e8;         /* Texto principal */
--color-text-dim: #a0a0a0;     /* Texto secundario */
--color-border: #2a2a3e;       /* Bordes */
```

## Prioridades de Implementación

### Fase 1: Estructura Base (HOY)
1. ✓ Anecdotario (completado)
2. Crear template base con menú lateral
3. Crear páginas para cada sección principal
4. Sistema de navegación funcional

### Fase 2: Contenido
1. Descargar contenido de cada sección desde Wayback
2. Extraer y procesar texto
3. Procesar imágenes y multimedia
4. Integrar en páginas modernas

### Fase 3: Refinamiento
1. Animaciones y transiciones
2. Optimización de imágenes
3. Testing responsive
4. Ajustes finales

## Archivo de Estilos Globales

Crear `/css/site-2026.css` con:
- Variables CSS
- Reset/normalize
- Tipografía
- Layout grid
- Componentes reutilizables
- Utilidades

## Componentes Reutilizables

1. **Header Global**
   - Logo grande
   - Ribbon decorativo

2. **Sidebar Menu**
   - Sticky positioning
   - Animaciones hover
   - Indicador de sección activa

3. **Content Container**
   - Max-width para legibilidad
   - Padding responsive
   - Typography system

4. **Card Component**
   - Para galerías, discografía
   - Hover effects
   - Responsive grid

5. **Footer**
   - Links de navegación
   - Información de contacto
   - Fecha de actualización

## Tecnologías

- HTML5 semántico
- CSS3 (Grid, Flexbox, Custom Properties)
- JavaScript vanilla (mínimo, solo para interactividad)
- Sin frameworks pesados
- Optimizado para performance

## Próximos Pasos Inmediatos

1. Crear template base HTML
2. Crear sistema de estilos CSS
3. Implementar menú lateral sticky
4. Crear páginas para cada sección
5. Descargar y procesar contenido restante
