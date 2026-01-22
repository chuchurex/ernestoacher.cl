# 🎨 Guía de Estilos - Sitio Ernesto Acher

**Actualizado:** 14 de enero de 2026

Esta guía explica cómo modificar los estilos CSS del sitio de forma segura y eficiente.

---

## 🏗️ Arquitectura CSS

El sitio usa un **sistema CSS unificado** basado en Sass que compila todos los estilos en un solo archivo.

```
Todos los HTML → css/app.css ← Compilado desde scss/app.scss
```

### ✅ Lo Importante

- **NUNCA edites** `css/app.css` directamente
- **SIEMPRE modifica** archivos `.scss` en la carpeta `scss/`
- Después de modificar, **compila** con: `npm run sass:build`

---

## 📁 Estructura de Archivos Sass

```
scss/
├── app.scss                    ← PUNTO DE ENTRADA (importa todo)
│
├── _variables.scss             ← VARIABLES GLOBALES (colores, tamaños, etc.)
├── _mixins.scss                ← FUNCIONES REUTILIZABLES
│
├── base/
│   ├── _reset.scss             ← Reset CSS básico
│   ├── _typography.scss        ← Tipografías y fuentes
│   └── ../
│
├── layout/
│   ├── _header.scss            ← Header/logo (portada)
│   ├── _main.scss              ← Layout principal y elipse
│   └── _footer.scss            ← Footer global
│
├── components/
│   ├── _menu.scss              ← Menús de portada (lateral)
│   ├── _carousel.scss          ← Carrusel de proyectos
│   ├── _ernesto-photo.scss     ← Foto de Ernesto
│   ├── _sidebar.scss           ← Sidebar de interiores (30%)
│   └── _content.scss           ← Contenido de interiores
│
├── pages/
│   ├── _anecdotario.scss       ← Estilos específicos de anecdotario
│   └── _lesluthiers.scss       ← Estilos específicos de Les Luthiers
│
└── utilities/
    └── _helpers.scss           ← Clases de utilidad
```

---

## 🎯 Casos de Uso Comunes

### 1. Cambiar un Color

**Ejemplo:** Cambiar el color del vino de la elipse

```scss
// Edita: scss/_variables.scss

$color-wine: #6B1C23;  // ← Cambia este valor
$color-wine-dark: #4A1117;
```

**Después:**
```bash
npm run sass:build
```

### 2. Modificar la Portada (index.html)

La portada usa estos archivos principalmente:

```
scss/layout/_header.scss         # Logo y header
scss/layout/_main.scss           # Elipse y layout general
scss/components/_menu.scss       # Menús laterales
scss/components/_carousel.scss   # Carrusel central
```

**Ejemplo:** Cambiar tamaño de la elipse

```scss
// Edita: scss/layout/_main.scss

.ellipse-container {
  width: 100%;
  max-width: 1200px;  // ← Cambia este valor
  height: 90vh;       // ← O este
}
```

### 3. Modificar Páginas Interiores

Las páginas interiores (lesluthiers.html, etc.) usan:

```
scss/components/_sidebar.scss    # Barra lateral
scss/components/_content.scss    # Área de contenido
scss/pages/_lesluthiers.scss     # Estilos específicos
```

**Ejemplo:** Cambiar ancho del sidebar

```scss
// Edita: scss/_variables.scss

$sidebar-width: 30%;  // ← Cambia este valor
$content-width: 60%;  // ← Ajusta proporcionalmente
```

### 4. Agregar Estilos Nuevos

**Opción A:** Si es un componente nuevo
```bash
# Crea archivo nuevo
touch scss/components/_mi-componente.scss

# Agrega al archivo principal
# Edita: scss/app.scss
# Agrega: @use 'components/mi-componente';
```

**Opción B:** Si es específico de una página
```scss
// Agrega al archivo existente
// Por ejemplo en: scss/pages/_lesluthiers.scss

.mi-clase-nueva {
  color: $color-text;
  padding: $spacing-lg;
}
```

---

## 🔧 Comandos Útiles

### Compilar CSS una vez
```bash
npm run sass:build
```

### Modo desarrollo (compila automáticamente al guardar)
```bash
npm run sass:watch
```

### Ver qué archivos usan qué CSS
```bash
# Portada
grep "app.css" index.html

# Interiores
grep "app.css" lesluthiers.html
```

---

## 📋 Variables Más Importantes

Estas variables están en `scss/_variables.scss`:

### Colores
```scss
// Portada
$color-wine: #6B1C23;           // Elipse color vino
$color-background: #0d0d0d;     // Fondo negro
$color-text: #ffffff;           // Texto blanco

// Interiores
$color-bg-dark: rgb(16, 14, 27);     // Fondo sidebar
$color-bg-content: rgb(204, 204, 204); // Fondo contenido
$color-link: #000099;                  // Enlaces
```

### Tipografías
```scss
$font-logo: 'Great Vibes', cursive;        // Logo portada
$font-menu: 'Crimson Text', Georgia, serif; // Menús
$font-body: Georgia, 'Times New Roman', serif; // Contenido
```

### Layout
```scss
$sidebar-width: 30%;     // Ancho sidebar interiores
$content-width: 60%;     // Ancho contenido interiores
$spacing-lg: 20px;       // Espaciado grande
$spacing-xl: 30px;       // Espaciado extra grande
```

### Breakpoints (responsive)
```scss
$breakpoint-md: 768px;   // Tablets
$breakpoint-lg: 992px;   // Desktop
$breakpoint-xl: 1200px;  // Desktop grande
```

---

## ⚠️ Reglas de Oro

### ✅ HACER

1. **Modificar archivos .scss** en la carpeta `scss/`
2. **Usar variables** definidas en `_variables.scss`
3. **Compilar después** de cada cambio
4. **Testear** en navegador después de compilar
5. **Hacer commit** de los archivos .scss Y .css

### ❌ NO HACER

1. **NO editar** `css/app.css` directamente
2. **NO editar** `css/styles.css` o `css/main.css` (obsoletos)
3. **NO crear** archivos CSS sueltos
4. **NO duplicar** estilos que ya existen
5. **NO olvidar** compilar después de modificar

---

## 🐛 Solución de Problemas

### Problema: Los cambios no se ven

**Solución:**
```bash
# 1. Verifica que compilaste
npm run sass:build

# 2. Limpia caché del navegador
# Chrome/Firefox: Cmd+Shift+R (Mac) o Ctrl+Shift+R (Windows)

# 3. Verifica que el HTML usa app.css
grep "app.css" index.html
```

### Problema: Error al compilar

**Errores comunes:**

1. **"Undefined variable"**
   - Falta agregar `@use '../variables' as *;` al inicio del archivo

2. **"@use rules must be written before"**
   - Los `@use` deben estar ANTES de cualquier código CSS

3. **"File not found"**
   - Verifica la ruta relativa del import

---

## 📝 Flujo de Trabajo Recomendado

1. **Identifica** qué quieres cambiar
2. **Localiza** el archivo SCSS correspondiente (ver estructura arriba)
3. **Edita** el archivo .scss
4. **Compila** con `npm run sass:build`
5. **Refresca** el navegador (Cmd+Shift+R)
6. **Verifica** que el cambio funcionó
7. **Commit** de los cambios

```bash
git add scss/ css/app.css
git commit -m "Update styles: [descripción del cambio]"
git push
```

---

## 🎓 Ejemplo Completo

**Objetivo:** Cambiar el color de los menús de gris a azul

### Paso 1: Identificar archivo
Los menús están en `scss/components/_menu.scss`

### Paso 2: Editar variable
```scss
// En scss/_variables.scss
$color-text-muted: #3366cc;  // Era #999
```

### Paso 3: Compilar
```bash
npm run sass:build
```

### Paso 4: Verificar
Abre el navegador y refresca (Cmd+Shift+R)

### Paso 5: Commit
```bash
git add scss/_variables.scss css/app.css
git commit -m "Change menu color to blue"
```

---

## 📚 Recursos Adicionales

- **Sass Documentation:** https://sass-lang.com/documentation
- **CSS Grid Guide:** https://css-tricks.com/snippets/css/complete-guide-grid/
- **Flexbox Guide:** https://css-tricks.com/snippets/css/a-guide-to-flexbox/

---

## 🆘 Ayuda

Si algo no funciona o tienes dudas:

1. Revisa esta guía
2. Verifica que compilaste correctamente
3. Revisa la consola del navegador (F12) por errores
4. Verifica que el archivo HTML usa `css/app.css`

---

**Última actualización:** 14 de enero de 2026
**Autor:** @chuchurex
