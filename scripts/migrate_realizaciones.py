#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import shutil

def create_realizaciones_jsons():
    """Crear archivos JSON para Realizaciones Recientes"""

    os.makedirs('data/realizaciones', exist_ok=True)

    # JSON para index
    index_data = {
        "title": "Realizaciones recientes",
        "links": [
            {"title": "Humor con Acher", "url": "../humorconachis/santiago.html"},
            {"title": "La orquesta va al colegio", "url": "colegio.html"}
        ]
    }

    with open('data/realizaciones/index.json', 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # JSON para colegio
    colegio_data = {
        "title": "La orquesta va al colegio",
        "content": [
            "Cuando los directivos de la orquesta de la Universidad de Concepción me pidieron un proyecto para el ciclo de conciertos educacionales del 2004 presenté \"La orquesta va al colegio\", un esquema en el que yo hacía de \"maestro de ceremonias\" y dialogaba con un locutor \"en off\". En la primera parte utilizábamos proyecciones y mostrábamos una sinfónica \"por dentro\", instrumentos, sonidos, agrupaciones, etc. En la segunda parte mostrábamos la evolución en el proceso de aprendizaje, desde los cantitos infantiles hasta obras \"de repertorio\", marcábamos las distintas fases disfrazando a los músicos con \"sombreros\" típicos de la distintas edades, desde \"guaguas\" (con gorritos de bebé, una escena memorable...), pasando por niños (con gorras jockey, visera para atrás), luego adolescentes (con la visera para adelante) y fiinalmente adultos (con sombrero, hombres y mujeres...) Y hubo de todo, desde \"La sorpresa\" hasta la \"Obertura 1812\", desde cueca hasta rock, guiños y bromas, el \"Arroz con leche\" que aparecía por todos lados, el inefable Jaime Cofré que siempre \"metía la pata\" y recibía un \"chipote chillón\"... En fin, creo que lo didáctico y lo entretenido estuvo bien servido. Y además, para variar, los que estábamos en el escenario nos divertimos mucho..."
        ]
    }

    with open('data/realizaciones/colegio.json', 'w', encoding='utf-8') as f:
        json.dump(colegio_data, f, ensure_ascii=False, indent=2)

    print("✅ JSONs creados")

def copy_images():
    """Copiar imágenes desde backup"""

    os.makedirs('images/realizaciones', exist_ok=True)

    backup_dir = 'backup/rr/gfx/'
    images_dir = 'images/realizaciones/'

    if os.path.exists(backup_dir):
        for file in os.listdir(backup_dir):
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                src = os.path.join(backup_dir, file)
                dst = os.path.join(images_dir, file)
                if os.path.isfile(src):
                    shutil.copy2(src, dst)

    print("✅ Imágenes copiadas")

def create_html_pages():
    """Crear páginas HTML"""

    os.makedirs('realizaciones', exist_ok=True)

    # Plantilla para index.html
    index_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Realizaciones recientes - Ernesto Acher">
    <title>Realizaciones recientes - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-realizaciones">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>Realizaciones recientes</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li class="active">- Índice</li>
                            <li><a href="colegio.html">- La orquesta va al colegio</a></li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <h2><a href="../humorconachis/santiago.html">Humor con Acher</a></h2>
                    <h2><a href="colegio.html">La orquesta va al colegio</a></h2>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('realizaciones/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    # Plantilla para colegio.html
    colegio_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="La orquesta va al colegio - Ernesto Acher">
    <title>La orquesta va al colegio - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-realizaciones">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>Realizaciones recientes</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li><a href="index.html">- Índice</a></li>
                            <li class="active">- La orquesta va al colegio</li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <h2>La orquesta va al colegio</h2>

                    <p>Cuando los directivos de la orquesta de la Universidad de Concepción me pidieron un proyecto para el ciclo de conciertos educacionales del 2004 presenté "La orquesta va al colegio", un esquema en el que yo hacía de "maestro de ceremonias" y dialogaba con un locutor "en off". En la primera parte utilizábamos proyecciones y mostrábamos una sinfónica "por dentro", instrumentos, sonidos, agrupaciones, etc. En la segunda parte mostrábamos la evolución en el proceso de aprendizaje, desde los cantitos infantiles hasta obras "de repertorio", marcábamos las distintas fases disfrazando a los músicos con "sombreros" típicos de la distintas edades, desde "guaguas" (con gorritos de bebé, una escena memorable...), pasando por niños (con gorras jockey, visera para atrás), luego adolescentes (con la visera para adelante) y fiinalmente adultos (con sombrero, hombres y mujeres...) Y hubo de todo, desde "La sorpresa" hasta la "Obertura 1812", desde cueca hasta rock, guiños y bromas, el "Arroz con leche" que aparecía por todos lados, el inefable Jaime Cofré que siempre "metía la pata" y recibía un "chipote chillón"... En fin, creo que lo didáctico y lo entretenido estuvo bien servido. Y además, para variar, los que estábamos en el escenario nos divertimos mucho...</p>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('realizaciones/colegio.html', 'w', encoding='utf-8') as f:
        f.write(colegio_html)

    print("✅ Páginas HTML creadas")

def main():
    print("📦 Migrando Realizaciones Recientes...")
    print()

    print("📄 Creando archivos JSON...")
    create_realizaciones_jsons()
    print()

    print("📷 Copiando imágenes...")
    copy_images()
    print()

    print("📝 Creando páginas HTML...")
    create_html_pages()
    print()

    print("✅ Migración de Realizaciones completada!")

if __name__ == '__main__':
    main()
