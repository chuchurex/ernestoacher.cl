#!/usr/bin/env python3
"""
Script para corregir la navegación de todas las páginas HTML de Les Luthiers y La Banda Elástica
"""
import os
import json
from pathlib import Path

base_dir = Path("/Users/chuchurex/Sites/prod/ernestoacher.cl")

# Template HTML base para páginas interiores
def create_page_template(section_class, section_name, title, content, back_url, back_text):
    """Crea el template HTML para una página interior"""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {section_name} - Ernesto Acher</title>
    <meta name="description" content="{title} - {section_name}">
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="{section_class}">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="section-header">
                    <p><a href="{back_url}">← {back_text}</a></p>
                </div>
                <div class="section-content">
{content}
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>
"""

def extract_content(html_content):
    """Extrae solo el contenido entre <body> y </body>, limpiando estructura"""
    import re

    # Buscar contenido dentro de section-content o main-content
    match = re.search(r'<div class="section-content">(.*?)</div>\s*</main>', html_content, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Si no encuentra section-content, busca main-content
    match = re.search(r'<main class="main-content">(.*?)</main>', html_content, re.DOTALL)
    if match:
        content = match.group(1).strip()
        # Limpiar section-header si existe
        content = re.sub(r'<div class="section-header">.*?</div>', '', content, flags=re.DOTALL)
        # Limpiar content-header-title si existe
        content = re.sub(r'<div class="content-header-title">.*?</div>', '', content, flags=re.DOTALL)
        # Limpiar section-content wrapper si existe
        content = re.sub(r'<div class="section-content">\s*', '', content)
        content = re.sub(r'\s*</div>\s*$', '', content)
        return content.strip()

    return html_content

def fix_lesluthiers_pages():
    """Corrige todas las páginas de Les Luthiers"""
    ll_dir = base_dir / "lesluthiers"
    data_dir = base_dir / "data" / "lesluthiers"

    print("🔧 Corrigiendo páginas de Les Luthiers...")

    # Leer todos los JSON files
    json_files = list(data_dir.glob("*.json"))
    json_files = [f for f in json_files if f.name not in ["catalog.json", "index.json"]]

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        page_id = data['id']
        title = data['title']

        # Determinar el nombre del archivo HTML
        if page_id == 'index':
            html_file = ll_dir / "index.html"
        elif page_id == 'espectaculos':
            html_file = ll_dir / "espectaculos.html"
        elif page_id == 'discografia':
            html_file = ll_dir / "discografia.html"
        elif page_id == 'fotos':
            html_file = ll_dir / "fotos.html"
        elif page_id == 'fotos2':
            html_file = ll_dir / "fotos2.html"
        elif page_id == 'videos':
            html_file = ll_dir / "videos.html"
        else:
            # Espectáculos por año
            html_file = ll_dir / f"{page_id}.html"

        if not html_file.exists():
            print(f"  ⚠️  {html_file.name} no existe, saltando...")
            continue

        # Leer el contenido existente
        with open(html_file, 'r', encoding='utf-8') as f:
            old_content = f.read()

        # Extraer solo el contenido relevante
        content = extract_content(old_content)

        # Crear nuevo HTML con template correcto
        if page_id == 'index':
            back_url = "../lesluthiers.html"
            back_text = "Les Luthiers"
        else:
            back_url = "index.html"
            back_text = "Les Luthiers"

        new_html = create_page_template(
            section_class="page-lesluthiers",
            section_name="Les Luthiers",
            title=title.replace("Les Luthiers - ", ""),
            content=content,
            back_url=back_url,
            back_text=back_text
        )

        # Guardar
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_html)

        print(f"  ✅ {html_file.name}")

def fix_labanda_pages():
    """Corrige todas las páginas de La Banda Elástica"""
    lbe_dir = base_dir / "labandaelastica"
    data_dir = base_dir / "data" / "labandaelastica"

    print("\n🔧 Corrigiendo páginas de La Banda Elástica...")

    # Leer todos los JSON files
    json_files = list(data_dir.glob("*.json"))
    json_files = [f for f in json_files if f.name not in ["catalog.json", "index.json"]]

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        page_id = data['id']
        title = data['title']

        # Determinar el nombre del archivo HTML
        if page_id == 'index':
            html_file = lbe_dir / "index.html"
        elif page_id == 'espectaculos':
            html_file = lbe_dir / "espectaculos.html"
        elif page_id == 'discografia':
            html_file = lbe_dir / "discografia.html"
        elif page_id == 'fotos':
            html_file = lbe_dir / "fotos.html"
        elif page_id == 'videos':
            html_file = lbe_dir / "videos.html"
        elif page_id == 'audio':
            html_file = lbe_dir / "audio.html"
        else:
            # Espectáculos e1, e2, e3, e4
            html_file = lbe_dir / f"{page_id}.html"

        if not html_file.exists():
            print(f"  ⚠️  {html_file.name} no existe, saltando...")
            continue

        # Leer el contenido existente
        with open(html_file, 'r', encoding='utf-8') as f:
            old_content = f.read()

        # Extraer solo el contenido relevante
        content = extract_content(old_content)

        # Crear nuevo HTML con template correcto
        if page_id == 'index':
            back_url = "../labandaelastica.html"
            back_text = "La Banda Elástica"
        else:
            back_url = "index.html"
            back_text = "La Banda Elástica"

        new_html = create_page_template(
            section_class="page-banda-elastica",
            section_name="La Banda Elástica",
            title=title.replace("La Banda Elástica - ", "").replace("La Banda Elástica", "Inicio"),
            content=content,
            back_url=back_url,
            back_text=back_text
        )

        # Guardar
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_html)

        print(f"  ✅ {html_file.name}")

if __name__ == "__main__":
    print("=" * 60)
    print("CORRECCIÓN DE NAVEGACIÓN - ERNESTO ACHER")
    print("=" * 60)

    fix_lesluthiers_pages()
    fix_labanda_pages()

    print("\n" + "=" * 60)
    print("✅ PROCESO COMPLETADO")
    print("=" * 60)
