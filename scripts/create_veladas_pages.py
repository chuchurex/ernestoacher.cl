#!/usr/bin/env python3
"""
Script para crear páginas HTML de Veladas Espeluznantes
"""

import json
from pathlib import Path

# Template HTML base
TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Veladas Espeluznantes - Ernesto Acher</title>
    <meta name="description" content="{title} - Veladas Espeluznantes">
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-veladas">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>Veladas Espeluznantes</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li{active_index}>- Comienzo</li>
                            <li{active_bromas}>- Bromas/Juegos</li>
                            <li{active_videos}>- Videos</li>
                            <li{active_fotos}>- Fotos</li>
                        </ul>
                    </nav>
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
'''

def create_active_marker(page_name, active_page):
    """Crea el atributo class="active" si la página coincide"""
    if page_name == active_page:
        return ' class="active"'
    return '><a href="' + page_name + '.html"'

def create_index_page():
    """Crea la página index.html"""
    content = '''                    <h2>Cómo empezó la historia...</h2>

                    <img src="../images/ve/main.jpg" alt="Veladas Espeluznantes" class="content-image-right">

                    <p>La historia de las "Veladas" es en realidad la confluencia de dos cosas distintas. La primera es "Juegos", un disco de bromas Y juegos musicales, cuya idea inicial surgió un día, no recuerdo si en el '85 o el '86, en que silbando el principio de la 40 de Mozart de pronto el silbido se me fue para el tango "El choclo". Me dio un ataque de risa y me puse a hacer un boceto con sintetizadores, lo llevé al teatro para hacérselo oir a los compañeros de Les Luthiers y debo decir que no les causó la más mínima gracia. Desilusionado, lo guardé en un cajón pero tiempo después, ya fuera del grupo, volví a escucharlo y no solamente me volvió a dar risa, sino que empezaron a ocurrírseme otras "asociaciones" tanto o más graciosas (como la "Pequeña música hebrea") o de puro juego musical (como "Borodin, bangles and beads"). Y el disco se grabó en abril de 1987 con una orquesta "de juguete" con la que grabábamos y regrabábamos hasta "parecer" una sinfónica y con la colaboración de amigos de muchos años como el Zurdo Roizner, Baby López Furst, etc. (Ver discografía)</p>

                    <p>La otra punta de las "Veladas" fue la experiencia con el maestro Calderón cuando me estrenó el poema sinfónico "Molloy" con la Filarmónica de Buenos Aires (1980). Además de haber quedado muy contento por el estupendo trabajo de Marcela Magín como solista de viola y por el apoyo de la orquesta, quedé muy impresionado por la manera en que Calderón había "mejorado" la obra desde la dirección. Más de diez años después hice algún intento por estudiar dirección orquestal pero no le encotraba la vuelta, hasta que a fines del '92 conocí a Carlos Calleja, un tipazo y un gran maestro. En un par de charlas me hizo "asomar" al meollo del asunto y me vino el entusiasmo. Casualmente o no, uno nunca sabe, unos meses después me llamó Hugo Vitantonio desde Rosario y me propuso hacer un concierto sinfónico de música humor, partiendo de las bromas de "Juegos". A fines del '93 estrené la primera versión en Rosario de las "Veladas Espeluznantes" y ya no me acuerdo cuantas veces las hice porque fue en un montón de lugares y otro montón de versiones diferentes. Y sigue funcionando...</p>'''

    html = TEMPLATE.format(
        title='Comienzo',
        active_index=' class="active"',
        active_bromas='><a href="bromas.html"',
        active_videos='><a href="videos.html"',
        active_fotos='><a href="fotos.html"',
        content=content
    )

    with open('veladas/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ veladas/index.html creado")

def create_bromas_page():
    """Crea la página bromas.html"""
    content = '''                    <h2>Bromas y Juegos Musicales</h2>

                    <p>Contenido de bromas y juegos musicales...</p>'''

    html = TEMPLATE.format(
        title='Bromas y Juegos',
        active_index='><a href="index.html"',
        active_bromas=' class="active"',
        active_videos='><a href="videos.html"',
        active_fotos='><a href="fotos.html"',
        content=content
    )

    with open('veladas/bromas.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ veladas/bromas.html creado")

def create_videos_page():
    """Crea la página videos.html"""
    content = '''                    <h2>Videos</h2>

                    <p>Videos de las Veladas Espeluznantes...</p>'''

    html = TEMPLATE.format(
        title='Videos',
        active_index='><a href="index.html"',
        active_bromas='><a href="bromas.html"',
        active_videos=' class="active"',
        active_fotos='><a href="fotos.html"',
        content=content
    )

    with open('veladas/videos.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ veladas/videos.html creado")

def create_fotos_page():
    """Crea la página fotos.html"""
    content = '''                    <h2>Fotos</h2>

                    <div class="photo-gallery">
                        <p>Galería de fotos de las Veladas Espeluznantes...</p>
                    </div>'''

    html = TEMPLATE.format(
        title='Fotos',
        active_index='><a href="index.html"',
        active_bromas='><a href="bromas.html"',
        active_videos='><a href="videos.html"',
        active_fotos=' class="active"',
        content=content
    )

    with open('veladas/fotos.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ veladas/fotos.html creado")

# Crear todas las páginas
print("Creando páginas HTML para Veladas Espeluznantes...")
create_index_page()
create_bromas_page()
create_videos_page()
create_fotos_page()
print("\n✅ Todas las páginas HTML creadas correctamente")
