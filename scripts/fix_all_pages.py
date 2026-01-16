#!/usr/bin/env python3
"""
Script mejorado para corregir TODAS las páginas HTML incluyendo index.html
"""
import os
import json
from pathlib import Path

base_dir = Path("/Users/chuchurex/Sites/prod/ernestoacher.cl")

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

def extract_content_simple(html_file):
    """Extrae contenido de los archivos JSON en lugar de HTML"""
    # Buscar el JSON correspondiente
    page_name = html_file.stem
    section_dir = html_file.parent.name
    json_file = base_dir / "data" / section_dir / f"{page_name}.json"

    if json_file.exists():
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('content', '')

    return ""

def fix_all_lesluthiers():
    """Corrige todas las páginas de Les Luthiers"""
    ll_dir = base_dir / "lesluthiers"
    print("🔧 Corrigiendo páginas de Les Luthiers...")

    # Lista de todas las páginas HTML que existen
    html_files = list(ll_dir.glob("*.html"))

    for html_file in html_files:
        page_name = html_file.stem
        json_file = base_dir / "data" / "lesluthiers" / f"{page_name}.json"

        if not json_file.exists():
            print(f"  ⚠️  No existe JSON para {page_name}, saltando...")
            continue

        # Leer datos del JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        title = data['title']
        content = data['content']

        # Determinar back URL
        if page_name == "index":
            back_url = "../lesluthiers.html"
            back_text = "Les Luthiers"
        else:
            back_url = "index.html"
            back_text = "Les Luthiers"

        # Crear nuevo HTML
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

def fix_all_labanda():
    """Corrige todas las páginas de La Banda Elástica"""
    lbe_dir = base_dir / "labandaelastica"
    print("\n🔧 Corrigiendo páginas de La Banda Elástica...")

    # Lista de todas las páginas HTML que existen
    html_files = list(lbe_dir.glob("*.html"))

    for html_file in html_files:
        page_name = html_file.stem
        json_file = base_dir / "data" / "labandaelastica" / f"{page_name}.json"

        if not json_file.exists():
            print(f"  ⚠️  No existe JSON para {page_name}, saltando...")
            continue

        # Leer datos del JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        title = data['title']
        content = data['content']

        # Determinar back URL
        if page_name == "index":
            back_url = "../labandaelastica.html"
            back_text = "La Banda Elástica"
        else:
            back_url = "index.html"
            back_text = "La Banda Elástica"

        # Crear nuevo HTML
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
    print("CORRECCIÓN COMPLETA DE NAVEGACIÓN")
    print("=" * 60)

    fix_all_lesluthiers()
    fix_all_labanda()

    print("\n" + "=" * 60)
    print("✅ PROCESO COMPLETADO")
    print("=" * 60)
