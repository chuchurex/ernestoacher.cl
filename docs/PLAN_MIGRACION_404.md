# 🔍 Plan de Migración de Páginas Faltantes (404s)

**Fecha**: 18 Enero 2026
**Estado actual**: 197 enlaces rotos detectados
**Objetivo**: Identificar, clasificar y migrar todas las páginas que causan 404

---

## 📊 Análisis de Enlaces Rotos

### 1. Detectar Todos los 404s

**Script de análisis**:
```bash
npm run validate 2>&1 | grep "→" | grep -v "✓" | grep -oE "/[^\"]+\.html" | sort -u > missing-pages.txt
```

### 2. Categorizar Páginas Faltantes

Basado en el análisis inicial, las páginas se dividen en:

#### A. Páginas Únicas del Sitio Principal
```
/anecdotario.html           - Versión antigua del anecdotario
/actualizaciones.html       - Página de actualizaciones/novedades
/mapa.html                  - Mapa del sitio
```

#### B. Subdirectorio: anecdotas/
```
/anecdotas/drodrigo.html
/anecdotas/zanotti.html
/anecdotas/ll03.html
/anecdotas/ll04.html
/anecdotas/ll05.html
/anecdotas/ll06.html
/anecdotas/ll35.html
/anecdotas/fnegras.html
/anecdotas/carlitosy.html
/anecdotas/lbe01.html
/anecdotas/lbe18.html
/anecdotas/volados.html
/anecdotas/mejor_clari.html
/anecdotas/rosario.html
/anecdotas/molloy.html
/anecdotas/algun_proy.html
/anecdotas/mhijo.html
/anecdotas/catastrofe.html
/anecdotas/pushkin.html
```
**Estimado**: ~50-100 anécdotas individuales

#### C. Enlaces Especiales/Inválidos
```
/mailto:eracher@gmail.com   - Mailto mal formado
index.html                  - Link relativo sin /
/sidebar.html              - Componente (no debe ser accesible)
```

#### D. Páginas de Galería/Especiales
```
/lesluthiers/1971.html      - Páginas por año
/lesluthiers/1972.html
...
/lesluthiers/f_ll*.html     - Páginas de fotos individuales
```

---

## 🎯 Estrategia de Migración

### FASE 1: Inventario Completo
**Objetivo**: Saber exactamente qué páginas existen y cuáles faltan

**Tareas**:
1. Crear script de análisis que:
   - Extraiga todos los enlaces únicos rotos del validador
   - Los clasifique por tipo/directorio
   - Cuente cuántos hay en cada categoría
   - Verifique cuáles existen en `archive/html-original/`

**Entregable**: `INVENTARIO_404.md` con listado completo categorizado

**Script propuesto**:
```python
#!/usr/bin/env python3
# scripts/analyze-404s.py

import subprocess
import re
from pathlib import Path
from collections import defaultdict

# Ejecutar validación
result = subprocess.run(['npm', 'run', 'validate'],
                       capture_output=True, text=True)

# Extraer enlaces rotos
broken_links = re.findall(r'→ (/[^\n]+\.html)', result.stderr)
unique_links = sorted(set(broken_links))

# Clasificar
categories = defaultdict(list)
for link in unique_links:
    if link.startswith('/anecdotas/'):
        categories['anecdotas'].append(link)
    elif link.startswith('/lesluthiers/'):
        categories['lesluthiers_especiales'].append(link)
    elif link.startswith('/labandaelastica/'):
        categories['labanda_especiales'].append(link)
    elif '/' not in link[1:]:
        categories['root'].append(link)
    else:
        categories['otros'].append(link)

# Verificar existencia en archive
archive_path = Path('archive/html-original')
for category, links in categories.items():
    print(f"\n## {category.upper()} ({len(links)} páginas)")
    for link in links[:10]:  # Primeras 10
        filename = link[1:]  # Quitar /
        exists = (archive_path / filename).exists()
        status = '✓ EXISTE' if exists else '✗ NO EXISTE'
        print(f"  {status} {link}")
    if len(links) > 10:
        print(f"  ... y {len(links) - 10} más")
```

---

### FASE 2: Decisión de Alcance
**Objetivo**: Decidir qué páginas migrar y cuáles ignorar

**Criterios de decisión**:

| Tipo | Acción | Razón |
|------|--------|-------|
| Páginas principales únicas | ✅ MIGRAR | Importantes para funcionalidad |
| Anecdotario modular vs antiguo | ⚠️ EVALUAR | Puede haber duplicación |
| Subdirectorio anecdotas/ | ✅ MIGRAR | Contenido único |
| Páginas especiales de fotos | ⚠️ EVALUAR | Ver si son necesarias |
| Enlaces malformados | ❌ IGNORAR | Errores del HTML original |
| Componentes internos | ❌ IGNORAR | No son páginas accesibles |

**Entregable**: Lista priorizada de páginas a migrar

---

### FASE 3: Migración Automatizada
**Objetivo**: Migrar páginas en lotes usando scripts

**Enfoque**:

#### 3A. Script de Extracción Batch
```python
#!/usr/bin/env python3
# scripts/migrate-batch.py

import sys
from pathlib import Path

def migrate_pages(page_list_file, category):
    """
    Migra un lote de páginas de archive/ a src/

    Args:
        page_list_file: Archivo con lista de páginas (una por línea)
        category: Categoría para organizar (ej: 'anecdotas')
    """
    pages = Path(page_list_file).read_text().splitlines()

    for page_path in pages:
        # Extraer contenido
        # Crear JSON de sección
        # Guardar en src/content/
        pass

# Uso:
# python scripts/migrate-batch.py missing-anecdotas.txt anecdotas
```

#### 3B. Actualizar build.js
Agregar soporte para subdirectorios:
```javascript
// En buildAll()
const specialDirs = ['anecdotas', 'lesluthiers', 'labandaelastica'];
for (const dir of specialDirs) {
  const pagesInDir = await getSpecialPages(dir);
  for (const page of pagesInDir) {
    await buildSimplePage(`${dir}/${page}`);
  }
}
```

---

### FASE 4: Validación y Limpieza
**Objetivo**: Asegurar que todas las migraciones funcionan

**Tareas**:
1. Ejecutar `npm run validate` después de cada batch
2. Verificar visualmente páginas migradas
3. Corregir paths de imágenes/enlaces si es necesario
4. Actualizar contadores en PLAN_REFACTORIZACION.md

---

## 📋 Checklist de Implementación

### Pre-requisitos
- [ ] Crear `scripts/analyze-404s.py`
- [ ] Ejecutar análisis y generar `INVENTARIO_404.md`
- [ ] Revisar inventario y decidir alcance

### Migración por Categoría

#### Páginas Root Prioritarias
- [ ] `/anecdotario.html` (si diferente de anecdotario-modular)
- [ ] `/actualizaciones.html`
- [ ] `/mapa.html`

#### Subdirectorio anecdotas/
- [ ] Contar total de páginas
- [ ] Crear script de migración batch
- [ ] Migrar primeras 10 como prueba
- [ ] Migrar resto si prueba exitosa

#### Páginas Especiales lesluthiers/
- [ ] Páginas por año (1971-1986)
- [ ] Páginas de fotos (f_ll*.html)
- [ ] Evaluar si son necesarias todas

#### Limpieza Final
- [ ] Corregir enlaces malformados en contenido
- [ ] Ignorar componentes internos en validación
- [ ] Actualizar documentación

---

## 🎯 Resultado Esperado

**Meta**: Reducir errores de validación de **197 → <50**

**Criterio de éxito**:
- ✅ Todas las páginas principales accesibles
- ✅ Subdirectorios de contenido (anecdotas/) migrados
- ✅ Solo errores de enlaces opcionales/antiguos
- ✅ Build sin warnings

**Páginas esperadas al final**:
```
Actual: 41 páginas
+ Root especiales: 3 páginas
+ Anecdotas: ~50 páginas
+ Especiales LL: ~20 páginas
= TOTAL: ~114 páginas
```

---

## 🚀 Orden de Ejecución Recomendado

```bash
# FASE 1: Análisis
python3 scripts/analyze-404s.py > INVENTARIO_404.md

# FASE 2: Revisar inventario
cat INVENTARIO_404.md

# FASE 3: Migración progresiva
python3 scripts/migrate-batch.py missing-root.txt root
npm run build && npm run validate

python3 scripts/migrate-batch.py missing-anecdotas.txt anecdotas
npm run build && npm run validate

# FASE 4: Verificación final
npm run validate
git commit -m "Migración completa de páginas 404"
```

---

## 📝 Notas Importantes

1. **No todas las páginas necesitan migrarse**: Algunas pueden ser versiones antiguas o duplicadas
2. **Priorizar por uso**: Migrar primero las páginas más enlazadas
3. **Batch processing**: Migrar en lotes para facilitar testing
4. **Commits incrementales**: Commitear después de cada categoría migrada
5. **Rollback disponible**: Archivos originales en `archive/` por si acaso

---

**Última actualización**: 18 Enero 2026
**Próximo paso**: Ejecutar FASE 1 - Inventario Completo
