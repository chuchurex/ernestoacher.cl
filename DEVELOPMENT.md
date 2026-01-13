# Guía de Desarrollo - ernestoacher.cl

## Configuración de Desarrollo con Sass

Este proyecto usa **Sass** para un CSS más organizado y mantenible, con **live-server** para desarrollo con recarga automática.

---

## Comandos Disponibles

### 🚀 Desarrollo (Recomendado)
```bash
npm run dev
```
Este comando:
- Compila Sass automáticamente cuando detecta cambios
- Levanta servidor local en `http://localhost:3000`
- Recarga el navegador automáticamente al guardar cambios
- Mantiene archivos CSS con formato legible y source maps

### 🔨 Solo compilar Sass (watch mode)
```bash
npm run sass:watch
```
Compila Sass a CSS cada vez que guardas cambios en archivos `.scss`

### 🌐 Solo servidor local
```bash
npm run serve
```
Levanta live-server en puerto 3000 sin compilar Sass

### 📦 Build para producción
```bash
npm run build
```
Compila Sass a CSS minificado sin source maps (listo para deployment)

---

## Estructura de Sass

```
scss/
├── styles.scss              # Archivo principal (importa todo)
├── _variables.scss          # Variables: colores, fuentes, breakpoints
├── _mixins.scss             # Funciones reutilizables
├── base/
│   ├── _reset.scss          # Reset CSS
│   └── _typography.scss     # Tipografías base
├── layout/
│   ├── _header.scss         # Header y logo
│   ├── _main.scss           # Layout principal y elipse
│   └── _footer.scss         # Footer
├── components/
│   ├── _menu.scss           # Menús (principal y media)
│   ├── _carousel.scss       # Carrusel central
│   └── _ernesto-photo.scss  # Foto de Ernesto
└── utilities/
    └── _helpers.scss        # Clases de utilidad
```

---

## Variables Disponibles

### Colores
```scss
$color-background: #0d0d0d;
$color-wine: #6B1C23;
$color-wine-dark: #4A1117;
$color-text: #ffffff;
$color-text-dim: #cccccc;
$color-silver: #d4d4d4;
```

### Breakpoints
```scss
$breakpoint-xl: 1200px;
$breakpoint-lg: 992px;
$breakpoint-md: 768px;
$breakpoint-sm: 576px;
```

### Uso de breakpoints
```scss
.elemento {
  width: 100%;

  @include respond-to('md') {
    width: 50%; // Aplica en pantallas <= 768px
  }
}
```

---

## Mixins Útiles

### Responsive
```scss
@include respond-to('md') {
  // Estilos para <= 768px
}
```

### Transiciones
```scss
@include smooth-transition(all, $transition-normal);
```

### Centrado absoluto
```scss
@include absolute-center;
```

### Text glow
```scss
@include text-glow(rgba(255,255,255,0.3));
```

### Underline effect
```scss
@include underline-effect($color-silver, left);
```

---

## Workflow Recomendado

1. **Iniciar desarrollo:**
   ```bash
   npm run dev
   ```

2. **Editar archivos en `scss/`** (NO en `css/`)
   - Los cambios se compilan automáticamente
   - El navegador se recarga solo

3. **Antes de commitear:**
   ```bash
   npm run build
   ```
   - Genera CSS minificado para producción

4. **Commit y push:**
   ```bash
   git add .
   git commit -m "Descripción de cambios"
   git push
   ```

---

## Notas Importantes

- ⚠️ **NO edites archivos en `/css/`** - edita solo archivos en `/scss/`
- Los archivos CSS se generan automáticamente desde Sass
- Los archivos `.css.map` NO se suben a producción (están en .gitignore)
- `package-lock.json` NO se sube a git (está en .gitignore)
- `node_modules/` NO se sube a git (está en .gitignore)

---

## Troubleshooting

### El servidor no inicia
```bash
# Reinstalar dependencias
rm -rf node_modules
npm install
```

### Los cambios de Sass no se reflejan
```bash
# Detener npm run dev (Ctrl+C)
# Borrar CSS generado
rm -rf css/styles.css css/styles.css.map
# Volver a iniciar
npm run dev
```

### Puerto 3000 ocupado
Edita `package.json`:
```json
"serve": "live-server --port=8080 ..."
```

---

## Archivos que NO se commitean

- `node_modules/` - Dependencias npm
- `*.css.map` - Source maps de Sass
- `package-lock.json` - Lock file de npm
- `.env` - Variables de entorno

---

## Próximos pasos de desarrollo

1. Agregar imágenes reales al proyecto
2. Implementar páginas internas
3. Rescatar contenido del Web Archive
4. Optimizar responsive en diferentes dispositivos

---

*Guía actualizada: 13 enero 2026*
