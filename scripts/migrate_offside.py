#!/usr/bin/env python3
"""
Script completo para migrar Offside Chamber Orchestra
"""

import json
import os

# 1. CREAR JSONs
print("📄 Creando archivos JSON...")

index_data = {
    "title": "Offside Chamber Orchestra",
    "subtitle": "",
    "mainImage": "main.jpg",
    "content": [
        {
            "type": "paragraph",
            "text": 'Cuando tuve que ponerme a aprender a toda máquina como demonios se hacía para "mover" una orquesta y poder dirigir la primera versión de las "Veladas" se me ocurrió armar un "octeto de entrenamiento" (flauta, clarinete, corno, cuarteto de cuerdas y contrabajo). Ensayábamos con todas las partituras "reducidas", en el Teatro del Globo gracias al buenazo de Cacho Carcavallo y más que nada gracias a la infinita paciencia y buena voluntad de los músicos que me acompañaron en la aventura. Me acuerdo solamente de algunos (Elías Gurevich, Marcelo Bru, Gabriel Pinette, Luis Tauriello, Fernando Chiappero) y pido disculpas por la mala memoria, tal vez algún alma caritativa que lea esto me acerque más datos.'
        },
        {
            "type": "paragraph",
            "text": 'El hecho es que a fines del ´94 la idea de tocar repertorio sinfónico en reducción me volvió a rondar y armé una sinfónica en miniatura con flauta, oboe, dos clarinetes, fagot, dos cornos, trompeta, trombón, bajo/percusión, guitarra/percusión, cuatro primeros violines, tres segundos, dos violas, dos cellos y contrabajo, con la posibilidad de "estrenarla" en una fiesta empresaria. El programa incluía algunos "juegos", obras serias (Faure, Dvorak y otros), anécdotas, en fin, toda una apuesta... Como es habitual, tocamos después de la cenay el clima general, como a veces sucede en estos eventos, no parecía ser muy favorable, sobre todo teniendo en cuenta que "abríamos" con un vals de Johann Strauss y no precisamente uno de los más movidos (Rosas del Sud). Creo que los ganamos con la sorpresa, al principio estaban como desconcertados pero al tercer tema "estaban adentro" y cuando cerramos con la "Pequeña música hebrea" aplaudían subidos a las mesas...'
        },
        {
            "type": "paragraph",
            "text": 'Al año siguiente hicimos unas cuantas presentaciones y llegamos a hacer una temporadita en la reapertura del Teatro Lassalle, pero era lógico que tuviera corta duración, éramos veintitres y yo en un tiempo en que todo grupo musical de más de tres comenzaba a ser un exotismo. De todos modos valió la pena, nos divertimos mucho, hicimos buena música y hasta nos dimos el lujo de cerrar el ciclo haciendo de bis, y con dos cantantes, las tres arias del final del primer acto de "La Bohème".'
        }
    ]
}

fotos_data = {
    "title": "Offside Chamber Orchestra",
    "subtitle": "Fotos",
    "photos": []
}

with open('data/offside/index.json', 'w', encoding='utf-8') as f:
    json.dump(index_data, f, ensure_ascii=False, indent=2)

with open('data/offside/fotos.json', 'w', encoding='utf-8') as f:
    json.dump(fotos_data, f, ensure_ascii=False, indent=2)

print("✅ JSONs creados")

# 2. COPIAR IMÁGENES
print("\n📷 Copiando imágenes...")
os.system('cp backup/ocho/gfx/*.jpg images/offside/ 2>/dev/null')
os.system('ls -1 images/offside/*.jpg 2>/dev/null | wc -l')
print("✅ Imágenes copiadas")

# 3. CREAR PÁGINAS HTML
print("\n📝 Creando páginas HTML...")

TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Offside Chamber Orchestra - Ernesto Acher</title>
    <meta name="description" content="{title} - Offside Chamber Orchestra">
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-offside">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>Offside Chamber Orchestra</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li{active_index}>- Comienzo</li>
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

# index.html
index_content = '''                    <img src="../images/offside/main.jpg" alt="Offside Chamber Orchestra" class="content-image-right">

                    <p>Cuando tuve que ponerme a aprender a toda máquina como demonios se hacía para "mover" una orquesta y poder dirigir la primera versión de las "Veladas" se me ocurrió armar un "octeto de entrenamiento" (flauta, clarinete, corno, cuarteto de cuerdas y contrabajo). Ensayábamos con todas las partituras "reducidas", en el Teatro del Globo gracias al buenazo de Cacho Carcavallo y más que nada gracias a la infinita paciencia y buena voluntad de los músicos que me acompañaron en la aventura. Me acuerdo solamente de algunos (Elías Gurevich, Marcelo Bru, Gabriel Pinette, Luis Tauriello, Fernando Chiappero) y pido disculpas por la mala memoria, tal vez algún alma caritativa que lea esto me acerque más datos.</p>

                    <p>El hecho es que a fines del ´94 la idea de tocar repertorio sinfónico en reducción me volvió a rondar y armé una sinfónica en miniatura con flauta, oboe, dos clarinetes, fagot, dos cornos, trompeta, trombón, bajo/percusión, guitarra/percusión, cuatro primeros violines, tres segundos, dos violas, dos cellos y contrabajo, con la posibilidad de "estrenarla" en una fiesta empresaria. El programa incluía algunos "juegos", obras serias (Faure, Dvorak y otros), anécdotas, en fin, toda una apuesta... Como es habitual, tocamos después de la cenay el clima general, como a veces sucede en estos eventos, no parecía ser muy favorable, sobre todo teniendo en cuenta que "abríamos" con un vals de Johann Strauss y no precisamente uno de los más movidos (Rosas del Sud). Creo que los ganamos con la sorpresa, al principio estaban como desconcertados pero al tercer tema "estaban adentro" y cuando cerramos con la "Pequeña música hebrea" aplaudían subidos a las mesas...</p>

                    <p>Al año siguiente hicimos unas cuantas presentaciones y llegamos a hacer una temporadita en la reapertura del Teatro Lassalle, pero era lógico que tuviera corta duración, éramos veintitres y yo en un tiempo en que todo grupo musical de más de tres comenzaba a ser un exotismo. De todos modos valió la pena, nos divertimos mucho, hicimos buena música y hasta nos dimos el lujo de cerrar el ciclo haciendo de bis, y con dos cantantes, las tres arias del final del primer acto de "La Bohème".</p>'''

index_html = TEMPLATE.format(
    title='Comienzo',
    active_index=' class="active"',
    active_fotos='><a href="fotos.html"',
    content=index_content
)

with open('offside/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# fotos.html
fotos_content = '''                    <h2>Fotos</h2>

                    <div class="photo-gallery">
                        <p>Galería de fotos de Offside Chamber Orchestra...</p>
                    </div>'''

fotos_html = TEMPLATE.format(
    title='Fotos',
    active_index='><a href="index.html"',
    active_fotos=' class="active"',
    content=fotos_content
)

with open('offside/fotos.html', 'w', encoding='utf-8') as f:
    f.write(fotos_html)

print("✅ Páginas HTML creadas")
print("\n✅ Migración de Offside completada!")
