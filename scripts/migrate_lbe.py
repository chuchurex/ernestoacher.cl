#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
import html
import shutil
from pathlib import Path
from bs4 import BeautifulSoup

# Rutas base
BASE_DIR = Path("/Users/chuchurex/Sites/prod/ernestoacher.cl")
BACKUP_DIR = BASE_DIR / "backup/lbe"
DATA_DIR = BASE_DIR / "data/labandaelastica"
IMAGES_SRC_DIR = BACKUP_DIR / "gfx"
IMAGES_DEST_DIR = BASE_DIR / "images/lbe"
OUTPUT_DIR = BASE_DIR / "labandaelastica"

# Mapeo de archivos
FILE_MAPPING = {
    'index.htm': 'index.html',
    'espect.htm': 'espectaculos.html',
    'discos.htm': 'discografia.html',
    'fotos.htm': 'fotos.html',
    'videos.htm': 'videos.html',
    'audio.htm': 'audio.html',
    'e1.htm': 'e1.html',
    'e2.htm': 'e2.html',
    'e3.htm': 'e3.html',
    'e4.htm': 'e4.html'
}

# Títulos para cada página
PAGE_TITLES = {
    'index': 'La Banda Elástica',
    'espectaculos': 'Espectáculos',
    'discografia': 'Discografía',
    'fotos': 'Fotos',
    'videos': 'Videos',
    'audio': 'Audio',
    'e1': 'El show de la Banda Elástica',
    'e2': 'La Banda Elástica \'89',
    'e3': '3a. Edición',
    'e4': 'Perché mi piace'
}


def clean_html_content(soup):
    """Limpia el HTML antiguo y extrae solo el contenido relevante"""

    # Eliminar scripts y elementos no deseados
    for tag in soup(['script', 'style', 'object', 'embed', 'param']):
        tag.decompose()

    # Eliminar imágenes spacer y d2 spacers
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 'spacer.gif' in src or 'd2/' in src:
            img.decompose()

    # Estrategia: buscar el td principal con colspan="15" y rowspan="10"
    main_td = None
    for td in soup.find_all('td'):
        if td.get('colspan') == '15' and td.get('rowspan') == '10':
            main_td = td
            break

    if not main_td:
        # Fallback: buscar por contenido específico
        for td in soup.find_all('td'):
            if td.find('h2') or (td.find('h5') and td.find('p')):
                text = td.get_text()
                if len(text) > 200:  # Debe tener contenido sustancial
                    main_td = td
                    break

    if not main_td:
        return ""

    # Crear un nuevo soup con solo el contenido del td principal
    content_soup = BeautifulSoup(str(main_td), 'html.parser')

    # Eliminar toda la navegación
    for nav in content_soup.find_all('div', id='navegacion'):
        nav.decompose()

    # Eliminar todas las tablas que solo contienen navegación
    for table in content_soup.find_all('table'):
        # Verificar si es una tabla de navegación
        text_content = table.get_text()
        nav_keywords = ['Comienzo', 'Espectáculos', 'Discografía', 'Fotos', 'Videos', 'Audio']

        # Si tiene estos keywords pero no tiene contenido sustancial, es navegación
        has_nav = any(keyword in text_content for keyword in nav_keywords)
        has_content_tags = table.find('h2') or table.find('h5') or table.find('p')

        if has_nav and not has_content_tags:
            table.decompose()

    # Buscar el td con el contenido real (normalmente width="457")
    content_td = None
    for td in content_soup.find_all('td'):
        if td.get('width') in ['457', '421']:  # Anchos típicos del contenido
            # Verificar que tenga contenido real
            if td.find('h2') or td.find('h5') or td.find('p'):
                content_td = td
                break

    if content_td:
        # Usar solo este td
        content_soup = BeautifulSoup(str(content_td), 'html.parser')

    # Eliminar atributos obsoletos
    for tag in content_soup.find_all(True):
        allowed_attrs = ['href', 'src', 'alt', 'class', 'id', 'target', 'align']
        attrs_to_remove = [attr for attr in tag.attrs if attr not in allowed_attrs]
        for attr in attrs_to_remove:
            del tag[attr]

    # Obtener el HTML limpio
    clean_content = str(content_soup)

    # Eliminar wrappers de td
    clean_content = re.sub(r'</?td[^>]*>', '', clean_content)

    # Eliminar tablas vacías o de layout
    clean_content = re.sub(r'<table[^>]*>\s*</table>', '', clean_content)

    # Limpiar espacios múltiples
    clean_content = re.sub(r'\n\s*\n', '\n\n', clean_content)
    clean_content = re.sub(r'  +', ' ', clean_content)

    return clean_content.strip()


def convert_encoding(text):
    """Convierte de ISO-8859-1 a UTF-8 y decodifica entidades HTML"""
    # Decodificar entidades HTML
    text = html.unescape(text)

    # Reemplazos adicionales de entidades comunes
    replacements = {
        '&aacute;': 'á',
        '&eacute;': 'é',
        '&iacute;': 'í',
        '&oacute;': 'ó',
        '&uacute;': 'ú',
        '&ntilde;': 'ñ',
        '&Aacute;': 'Á',
        '&Eacute;': 'É',
        '&Iacute;': 'Í',
        '&Oacute;': 'Ó',
        '&Uacute;': 'Ú',
        '&Ntilde;': 'Ñ',
        '&acute;': '´',
        '&#8220;': '"',
        '&#8221;': '"',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def extract_images(content):
    """Extrae las rutas de imágenes del contenido"""
    images = []
    soup = BeautifulSoup(content, 'html.parser')

    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src and 'spacer.gif' not in src:
            # Normalizar la ruta
            src = src.replace('gfx/', '').replace('../lbe/gfx/', '')
            if src:
                images.append(src)

    return images


def fix_image_paths(content):
    """Actualiza las rutas de imágenes en el contenido"""
    # Reemplazar rutas relativas a gfx
    content = re.sub(r'src="gfx/([^"]+)"', r'src="../images/lbe/\1"', content)
    content = re.sub(r'src="../lbe/gfx/([^"]+)"', r'src="../images/lbe/\1"', content)

    return content


def fix_internal_links(content):
    """Convierte enlaces .htm a .html"""
    # Convertir enlaces a archivos htm a html
    content = re.sub(r'href="([^"]*\.htm)"', r'href="\1l"', content)

    return content


def process_html_file(source_file, dest_id):
    """Procesa un archivo HTML y extrae su contenido"""

    print(f"Procesando {source_file}...")

    # Leer el archivo con encoding ISO-8859-1
    with open(source_file, 'r', encoding='iso-8859-1', errors='ignore') as f:
        content = f.read()

    # Parsear con BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Limpiar y extraer contenido
    clean_content = clean_html_content(soup)

    # Convertir encoding
    clean_content = convert_encoding(clean_content)

    # Extraer imágenes
    images = extract_images(clean_content)

    # Arreglar rutas de imágenes
    clean_content = fix_image_paths(clean_content)

    # Arreglar enlaces internos
    clean_content = fix_internal_links(clean_content)

    # Obtener título
    title = PAGE_TITLES.get(dest_id, dest_id)

    # Crear objeto JSON
    data = {
        'id': dest_id,
        'title': title,
        'content': clean_content,
        'images': images,
        'nav_links': {}
    }

    return data


def generate_html_page(data, is_index=False):
    """Genera una página HTML moderna desde los datos"""

    title = data['title']
    content = data['content']

    # Breadcrumb
    breadcrumb = ''
    if not is_index:
        breadcrumb = '<div class="section-header"><p><a href="index.html">← La Banda Elástica</a></p></div>'

    html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - La Banda Elástica - Ernesto Acher</title>
    <meta name="description" content="{title} - La Banda Elástica">
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-banda-elastica">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                {breadcrumb}
                <h1>{title}</h1>
                <div class="section-content">
                    {content}
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    return html_template


def copy_images():
    """Copia todas las imágenes del backup al destino"""

    print("\nCopiando imágenes...")

    # Crear directorio de destino
    IMAGES_DEST_DIR.mkdir(parents=True, exist_ok=True)

    copied_count = 0
    copied_files = []

    # Copiar todos los archivos de imagen
    for img_file in IMAGES_SRC_DIR.glob('*'):
        if img_file.is_file() and img_file.suffix.lower() in ['.jpg', '.jpeg', '.gif', '.png']:
            dest_file = IMAGES_DEST_DIR / img_file.name
            shutil.copy2(img_file, dest_file)
            copied_count += 1
            copied_files.append(img_file.name)
            print(f"  Copiado: {img_file.name}")

    return copied_count, copied_files


def main():
    """Función principal"""

    print("=" * 80)
    print("MIGRACIÓN DE LA BANDA ELÁSTICA")
    print("=" * 80)

    # Crear directorios
    print("\n1. Creando directorios...")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"  ✓ {DATA_DIR}")
    print(f"  ✓ {OUTPUT_DIR}")

    # Copiar imágenes
    print("\n2. Copiando imágenes...")
    images_count, images_list = copy_images()
    print(f"  ✓ {images_count} imágenes copiadas")

    # Procesar archivos HTML
    print("\n3. Procesando archivos HTML...")
    all_pages = []
    generated_files = []

    for source_file, dest_file in FILE_MAPPING.items():
        source_path = BACKUP_DIR / source_file

        if not source_path.exists():
            print(f"  ⚠ Archivo no encontrado: {source_file}")
            continue

        # Obtener ID sin extensión
        dest_id = dest_file.replace('.html', '')

        # Procesar archivo
        data = process_html_file(source_path, dest_id)

        # Guardar JSON
        json_file = DATA_DIR / f"{dest_id}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"  ✓ {source_file} → {json_file.name}")

        # Generar HTML
        is_index = (dest_id == 'index')
        html_content = generate_html_page(data, is_index)

        html_file = OUTPUT_DIR / dest_file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"  ✓ Generado: {dest_file}")

        all_pages.append({
            'id': dest_id,
            'title': data['title'],
            'file': dest_file
        })

        generated_files.append(dest_file)

    # Crear índice
    print("\n4. Creando índice...")
    index_data = {
        'section': 'labandaelastica',
        'title': 'La Banda Elástica',
        'pages': all_pages
    }

    index_file = DATA_DIR / 'catalog.json'
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    print(f"  ✓ {index_file}")

    # Resumen final
    print("\n" + "=" * 80)
    print("RESUMEN DE MIGRACIÓN")
    print("=" * 80)
    print(f"\n✓ Páginas generadas: {len(generated_files)}")
    for f in generated_files:
        print(f"  - {f}")

    print(f"\n✓ Imágenes copiadas: {images_count}")
    for img in images_list:
        print(f"  - {img}")

    print(f"\n✓ Archivos JSON generados: {len(all_pages)}")
    print(f"  - {DATA_DIR}")

    print(f"\n✓ Archivos HTML generados: {len(generated_files)}")
    print(f"  - {OUTPUT_DIR}")

    print("\n" + "=" * 80)
    print("MIGRACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 80)


if __name__ == '__main__':
    main()
