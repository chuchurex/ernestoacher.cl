#!/usr/bin/env python3
"""
Script para agregar menú page-nav-right a todas las páginas interiores de cada sección
"""

import os
import re
from pathlib import Path

# Definir los menús para cada sección
SECTION_MENUS = {
    'lesluthiers': {
        'title': 'Les Luthiers',
        'items': [
            {'label': 'Comienzo', 'href': 'index.html'},
            {'label': 'Espectáculos', 'href': 'espectaculos.html'},
            {'label': 'Discografía', 'href': 'discografia.html'},
            {'label': 'Fotos', 'href': 'fotos.html'},
            {'label': 'Videos', 'href': 'videos.html'},
        ]
    },
    'labandaelastica': {
        'title': 'La Banda Elástica',
        'items': [
            {'label': 'Comienzo', 'href': 'index.html'},
            {'label': 'Espectáculos', 'href': 'espectaculos.html'},
            {'label': 'Discografía', 'href': 'discografia.html'},
            {'label': 'Fotos', 'href': 'fotos.html'},
            {'label': 'Videos', 'href': 'videos.html'},
            {'label': 'Audio', 'href': 'audio.html'},
        ]
    },
    'humorconachis': {
        'title': 'Humor, con Acher',
        'items': [
            {'label': 'Comienzo', 'href': 'index.html'},
            {'label': 'Fotos', 'href': 'fotos.html'},
            {'label': 'Santiago', 'href': 'santiago.html'},
        ]
    }
}

def generate_menu_html(section_name, current_file):
    """Genera el HTML del menú para una sección específica"""
    menu_data = SECTION_MENUS[section_name]

    menu_html = f'''                <div class="content-header-title">
                    <h1>{menu_data['title']}</h1>
                    <nav class="page-nav-right">
                        <ul>
'''

    for item in menu_data['items']:
        # Determinar si es la página actual
        is_active = item['href'] == current_file
        if is_active:
            menu_html += f'                            <li class="active">- {item["label"]}</li>\n'
        else:
            menu_html += f'                            <li><a href="{item["href"]}">- {item["label"]}</a></li>\n'

    menu_html += '''                        </ul>
                    </nav>
                </div>
'''

    return menu_html

def process_html_file(filepath, section_name):
    """Procesa un archivo HTML para agregar el menú page-nav-right"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraer el nombre del archivo
    current_file = os.path.basename(filepath)

    # Verificar si ya tiene el menú page-nav-right
    if 'page-nav-right' in content:
        print(f"  ⏭️  {current_file} - Ya tiene menú page-nav-right")
        return False

    # Generar el nuevo menú
    menu_html = generate_menu_html(section_name, current_file)

    # Reemplazar la estructura actual
    # Buscar el patrón: <div class="section-header">...</div> seguido de <div class="section-content">
    pattern = r'(<div class="section-header">.*?</div>\s*<div class="section-content">)'

    # Crear el nuevo header con menú
    replacement = f'{menu_html}\n                <div class="section-content">'

    # Hacer el reemplazo
    new_content = re.sub(
        r'<div class="section-header">.*?</div>\s*<div class="section-content">',
        replacement,
        content,
        flags=re.DOTALL
    )

    # Verificar si se hizo algún cambio
    if new_content == content:
        print(f"  ⚠️  {current_file} - No se pudo agregar menú (patrón no encontrado)")
        return False

    # Guardar el archivo modificado
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✅ {current_file} - Menú agregado")
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
        if process_html_file(html_file, section_name):
            modified_count += 1

    print(f"   Total modificados: {modified_count}/{len(html_files)}")

def main():
    """Función principal"""
    print("=" * 60)
    print("Agregando menú page-nav-right a páginas interiores")
    print("=" * 60)

    # Procesar cada sección
    for section_name in SECTION_MENUS.keys():
        process_section(section_name)

    print("\n" + "=" * 60)
    print("✅ Proceso completado")
    print("=" * 60)

if __name__ == '__main__':
    main()
