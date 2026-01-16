#!/usr/bin/env python3
"""
Script para procesar archivos HTML antiguos de Les Luthiers
y generar páginas modernas con estructura JSON
"""

import os
import json
import re
from pathlib import Path
from html.parser import HTMLParser
import html

# Directorios
BASE_DIR = Path("/Users/chuchurex/Sites/prod/ernestoacher.cl")
BACKUP_DIR = BASE_DIR / "backup/ll"
DATA_DIR = BASE_DIR / "data/lesluthiers"
OUTPUT_DIR = BASE_DIR / "lesluthiers"
IMAGES_DIR = BASE_DIR / "images/ll"

# Archivos a procesar
FILES_TO_PROCESS = [
    ("index.htm", "Les Luthiers - Comienzo", "index.html"),
    ("espect.htm", "Espectáculos", "espectaculos.html"),
    ("discos.htm", "Discografía", "discografia.html"),
    ("fotos.htm", "Fotos - Parte 1", "fotos.html"),
    ("fotos2.htm", "Fotos - Parte 2", "fotos2.html"),
    ("videos.htm", "Videos", "videos.html"),
    ("1971.htm", "Opus Pi (1971)", "1971.html"),
    ("1972.htm", "Recital '72 - Opus Pi II (1972)", "1972.html"),
    ("1975.htm", "Recital '75 (1975)", "1975.html"),
    ("1976.htm", "Viejos Fracasos (1976)", "1976.html"),
    ("1977.htm", "Mastropiero que Nunca (1977)", "1977.html"),
    ("1979.htm", "Muchas Gracias de Nada (1979)", "1979.html"),
    ("1981.htm", "Luthierías (1981)", "1981.html"),
    ("1985.htm", "Humor Dulce Hogar (1985)", "1985.html"),
    ("1986.htm", "Recital en el Teatro Colón (1986)", "1986.html"),
]


class ContentExtractor(HTMLParser):
    """Extractor personalizado de contenido HTML"""

    def __init__(self):
        super().__init__()
        self.in_content = False
        self.in_h1 = False
        self.in_h2 = False
        self.in_h3 = False
        self.in_h5 = False
        self.in_h6 = False
        self.in_p = False
        self.in_a = False
        self.in_td = False
        self.in_table = 0
        self.in_strong = False
        self.in_em = False
        self.current_tag = None
        self.content_parts = []
        self.images = []
        self.depth = 0
        self.found_h1 = False
        self.current_attrs = {}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.current_attrs = attrs_dict

        # Detectar inicio de contenido
        if tag == 'h1':
            self.in_h1 = True
            self.found_h1 = True
            self.in_content = True
            self.content_parts.append('<h1>')
        elif tag == 'h2' and self.in_content:
            self.in_h2 = True
            self.content_parts.append('<h2>')
        elif tag == 'h3' and self.in_content:
            self.in_h3 = True
            self.content_parts.append('<h3>')
        elif tag == 'h5' and self.in_content:
            self.in_h5 = True
            self.content_parts.append('<h5>')
        elif tag == 'h6' and self.in_content:
            self.in_h6 = True
            self.content_parts.append('<h6>')
        elif tag == 'p' and self.in_content:
            self.in_p = True
            self.content_parts.append('<p>')
        elif tag == 'br' and self.in_content:
            self.content_parts.append('<br>')
        elif tag == 'strong' and self.in_content:
            self.in_strong = True
            self.content_parts.append('<strong>')
        elif tag == 'em' and self.in_content:
            self.in_em = True
            self.content_parts.append('<em>')
        elif tag == 'a' and self.in_content:
            href = attrs_dict.get('href', '')
            # Limpiar enlaces
            if href and not href.startswith('javascript:') and not href.startswith('#'):
                # Convertir enlaces internos
                if href.endswith('.htm'):
                    href = href.replace('.htm', '.html')
                self.in_a = True
                self.content_parts.append(f'<a href="{href}">')
        elif tag == 'img' and self.in_content:
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', '')
            width = attrs_dict.get('width', '')
            height = attrs_dict.get('height', '')
            align = attrs_dict.get('align', '')

            if src and 'spacer.gif' not in src:
                # Actualizar ruta de imagen
                if src.startswith('gfx/'):
                    src = '../images/ll/' + src.replace('gfx/', '')
                elif src.startswith('../ll/gfx/'):
                    src = src.replace('../ll/gfx/', '../images/ll/')
                elif 'gfx/' in src:
                    src = '../images/ll/' + src.split('gfx/')[-1]

                self.images.append(src)

                # Construir tag de imagen con atributos
                img_attrs = [f'src="{src}"']
                if alt:
                    img_attrs.append(f'alt="{html.escape(alt)}"')
                if width:
                    img_attrs.append(f'width="{width}"')
                if height:
                    img_attrs.append(f'height="{height}"')
                if align:
                    img_attrs.append(f'class="align-{align}"')

                self.content_parts.append(f'<img {" ".join(img_attrs)}>')
        elif tag == 'table':
            self.in_table += 1
        elif tag == 'td' and self.in_content and self.in_table > 0:
            self.in_td = True

    def handle_endtag(self, tag):
        if tag == 'h1' and self.in_h1:
            self.in_h1 = False
            self.content_parts.append('</h1>')
        elif tag == 'h2' and self.in_h2:
            self.in_h2 = False
            self.content_parts.append('</h2>')
        elif tag == 'h3' and self.in_h3:
            self.in_h3 = False
            self.content_parts.append('</h3>')
        elif tag == 'h5' and self.in_h5:
            self.in_h5 = False
            self.content_parts.append('</h5>')
        elif tag == 'h6' and self.in_h6:
            self.in_h6 = False
            self.content_parts.append('</h6>')
        elif tag == 'p' and self.in_p:
            self.in_p = False
            self.content_parts.append('</p>')
        elif tag == 'strong' and self.in_strong:
            self.in_strong = False
            self.content_parts.append('</strong>')
        elif tag == 'em' and self.in_em:
            self.in_em = False
            self.content_parts.append('</em>')
        elif tag == 'a' and self.in_a:
            self.in_a = False
            self.content_parts.append('</a>')
        elif tag == 'table':
            self.in_table -= 1
        elif tag == 'td':
            self.in_td = False

    def handle_data(self, data):
        if self.in_content and (self.in_h1 or self.in_h2 or self.in_h3 or self.in_h5 or self.in_h6 or self.in_p or self.in_a):
            # Limpiar y normalizar el texto
            text = data.strip()
            if text:
                # Convertir entidades HTML
                text = html.unescape(text)
                self.content_parts.append(text)

    def get_content(self):
        content = ''.join(self.content_parts)
        # Limpiar espacios múltiples
        content = re.sub(r'\s+', ' ', content)
        # Limpiar párrafos vacíos
        content = re.sub(r'<p>\s*</p>', '', content)
        content = re.sub(r'<p>\s*&nbsp;\s*</p>', '', content)
        # Agregar saltos de línea después de tags de bloque
        content = content.replace('</h1>', '</h1>\n')
        content = content.replace('</h2>', '</h2>\n')
        content = content.replace('</h3>', '</h3>\n')
        content = content.replace('</p>', '</p>\n')
        return content.strip()


def read_html_file(file_path):
    """Lee un archivo HTML con codificación ISO-8859-1"""
    try:
        with open(file_path, 'r', encoding='iso-8859-1') as f:
            return f.read()
    except Exception as e:
        print(f"Error leyendo {file_path}: {e}")
        return None


def extract_content(html_content):
    """Extrae el contenido principal del HTML antiguo"""
    parser = ContentExtractor()
    parser.feed(html_content)
    return parser.get_content(), list(set(parser.images))


def generate_html_page(title, content, breadcrumb_text="Les Luthiers"):
    """Genera una página HTML moderna"""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Les Luthiers - Ernesto Acher</title>
    <meta name="description" content="{title} - Les Luthiers">
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-lesluthiers">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="section-header">
                    <p><a href="index.html">← {breadcrumb_text}</a></p>
                </div>
                <div class="section-content">
                    {content}
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>"""


def process_files():
    """Procesa todos los archivos"""

    # Crear directorios
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    all_pages = []
    total_images = set()

    print("Procesando archivos de Les Luthiers...\n")

    for source_file, title, output_file in FILES_TO_PROCESS:
        source_path = BACKUP_DIR / source_file

        if not source_path.exists():
            print(f"⚠️  Archivo no encontrado: {source_file}")
            continue

        print(f"📄 Procesando: {source_file}")

        # Leer contenido HTML
        html_content = read_html_file(source_path)
        if not html_content:
            continue

        # Extraer contenido
        content, images = extract_content(html_content)

        if not content:
            print(f"   ⚠️  No se pudo extraer contenido")
            continue

        # Guardar JSON
        json_data = {
            "id": output_file.replace('.html', ''),
            "source": source_file,
            "title": title,
            "content": content,
            "images": images
        }

        json_path = DATA_DIR / output_file.replace('.html', '.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

        # Generar HTML moderno
        html_output = generate_html_page(title, content)
        html_path = OUTPUT_DIR / output_file
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

        all_pages.append({
            "id": json_data["id"],
            "title": title,
            "file": output_file,
            "images_count": len(images)
        })

        total_images.update(images)

        print(f"   ✓ Generado: {output_file}")
        print(f"   ✓ Imágenes encontradas: {len(images)}")

    # Generar índice
    index_data = {
        "section": "lesluthiers",
        "title": "Les Luthiers",
        "pages": all_pages,
        "total_pages": len(all_pages),
        "total_images": len(total_images)
    }

    index_path = DATA_DIR / "index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"✓ Procesamiento completado")
    print(f"{'='*60}")
    print(f"Páginas generadas: {len(all_pages)}")
    print(f"Imágenes únicas referenciadas: {len(total_images)}")
    print(f"\nArchivos generados:")
    print(f"  - Directorio de datos: {DATA_DIR}")
    print(f"  - Directorio HTML: {OUTPUT_DIR}")
    print(f"  - Índice general: {index_path}")

    # Listar todas las páginas generadas
    print(f"\nPáginas HTML generadas:")
    for page in all_pages:
        print(f"  - {page['file']} ({page['title']})")

    return all_pages, total_images


if __name__ == "__main__":
    process_files()
