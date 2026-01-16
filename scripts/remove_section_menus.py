#!/usr/bin/env python3
"""
Script para REMOVER el menú page-nav-right de todas las páginas interiores
dejándolo solo en las páginas raíz (lesluthiers.html, labandaelastica.html, etc.)
"""

import os
import re
from pathlib import Path

SECTIONS = ['lesluthiers', 'labandaelastica', 'humorconachis']

def remove_menu_from_file(filepath):
    """Remueve el menú page-nav-right de un archivo HTML"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verificar si tiene el menú page-nav-right
    if 'page-nav-right' not in content:
        print(f"  ⏭️  {os.path.basename(filepath)} - No tiene menú page-nav-right")
        return False

    # Detectar el título de la sección del h1
    title_match = re.search(r'<h1>([^<]+)</h1>', content)
    section_title = title_match.group(1) if title_match else "Volver"

    # Patrón para encontrar el bloque completo del menú page-nav-right
    # Desde <div class="content-header-title"> hasta el cierre </div>
    pattern = r'\s*<div class="content-header-title">.*?</nav>\s*</div>\s*'

    # Reemplazar con el header simple original
    replacement = f'''                <div class="section-header">
                    <p><a href="index.html">← {section_title}</a></p>
                </div>
'''

    # Hacer el reemplazo
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Verificar si se hizo algún cambio
    if new_content == content:
        print(f"  ⚠️  {os.path.basename(filepath)} - No se pudo remover menú (patrón no encontrado)")
        return False

    # Guardar el archivo modificado
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✅ {os.path.basename(filepath)} - Menú removido")
    return True

def process_section(section_name):
    """Procesa todas las páginas HTML de una sección"""

    section_dir = Path(section_name)

    if not section_dir.exists():
        print(f"❌ Directorio {section_name}/ no existe")
        return

    print(f"\n📁 Procesando sección: {section_name}/")

    # Obtener todos los archivos HTML en el directorio
    html_files = sorted(section_dir.glob('*.html'))

    modified_count = 0
    for html_file in html_files:
        if remove_menu_from_file(html_file):
            modified_count += 1

    print(f"   Total modificados: {modified_count}/{len(html_files)}")

def main():
    """Función principal"""
    print("=" * 60)
    print("Removiendo menú page-nav-right de páginas interiores")
    print("(El menú solo debe estar en páginas raíz)")
    print("=" * 60)

    # Procesar cada sección
    for section_name in SECTIONS:
        process_section(section_name)

    print("\n" + "=" * 60)
    print("✅ Proceso completado")
    print("=" * 60)

if __name__ == '__main__':
    main()
