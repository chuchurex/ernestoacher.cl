#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import shutil

def create_animales_jsons():
    """Crear archivos JSON para Los Animales de la Música"""

    # Crear directorio data/animales si no existe
    os.makedirs('data/animales', exist_ok=True)

    # JSON para index
    index_data = {
        "title": "Los animales de la música",
        "sections": [
            {
                "heading": "Primera versión",
                "content": [
                    "Después de la experiencia del \"Colón Opera Concerto\", Jorge de la Vega y yo quedamos con ganas de hacer algún otro proyecto y café va, café viene, en la esquina de Canning y Cabello, se nos ocurrió hacer un concierto para chicos basado en música que estuviera dedicada, o que de algún modo hiciera alusión a animalitos. Y así comenzamos a anotar: \"El murciélago\", \"La pantera rosa\", \"El pájaro loco\", \"Tiburón\", \"Faivel\", \"El cóndor pasa\", \"El vuelo del moscardón\", \"Pájaro campana\", \"Pedro y el lobo\", \"El zorro\"... y por supuesto, cada nueva anotación era una carcajada por las cosas que se nos iban ocurriendo para la puesta en escena.",
                    "Creo que el mayor delirio fue cuando armamos el inventado viaje de \"Manuelita\", ese entrañable personaje de la aún más entrañable María Elena Walsh, haciéndola pasar por distintas épocas y toparse con diferentes compositores. Primero hacíamos cantar a toda la sala, chicos y grandes, y luego se escuchaba la \"cruza\" de Manuelita con Vivaldi (\"La primavera\"), con Beethoven (\"5a. sinfonía\"), con Tchaikovsky (\"Cascanueces\") y finalmente con Ravel (\"Bolero\"). La parte final era \"Teresa y el Oso\", el cuento sinfónico de Les Luthiers, con De la Vega como relator. También fuimos al Avenida, con el auspicio de la Fundación Konex y también fue un bombazo. También se repitió al año siguiente, ya sin el apoyo de Konex, y luego lo presentamos en Córdoba, pero la marcha se detuvo. Creo que \"Los animales de la música\" merecía mejor suerte..."
                ]
            },
            {
                "heading": "Segunda versión",
                "content": [
                    "Y la vida siempre da revancha... En el segundo semestre del 2005 hubo un retorno con algunas funciones en el Teatro Colón, y aunque las condiciones escénicas eran un tanto precarias (sólo se podía utilizar el proscenio) resultaron todo un éxito. Tanto es así que en el 2006 hicimos casi veinte funciones durante las vacaciones de invierno. Y a sala llena!",
                    "Los cambios en la segunda versión fueron el reemplazo de \"Manueleces\" (Manuelita-\"Cascanueces\"), por la \"Polka de Manuelita\" (Manuelita-\"Tritsch-tratsch polka\") y la supresión de \"Teresa y el Oso\", que hacía el programa demasiado largo, quedando el cierre a cargo del delirante paseo de Manuelita. El éxito fue impresionante, continuó durante 2007 en el Auditorio de Belgrano y ahora empieza a proyectarse fuera de Buenos Aires: el 14 de marzo lo presentaremos en Asunción (Paraguay) y hay gestiones adelantadas para el interior de Argentina."
                ]
            }
        ],
        "image": "images/animales/main.jpg",
        "image_alt": "Los animales de la música"
    }

    with open('data/animales/index.json', 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # JSON para videos
    videos_data = {
        "title": "Videos",
        "content": "Videos de Los animales de la música"
    }

    with open('data/animales/videos.json', 'w', encoding='utf-8') as f:
        json.dump(videos_data, f, ensure_ascii=False, indent=2)

    print("✅ JSONs creados")

def copy_images():
    """Copiar imágenes desde backup"""

    # Crear directorio images/animales si no existe
    os.makedirs('images/animales', exist_ok=True)

    # Copiar imágenes desde backup/ladm/gfx/
    backup_dir = 'backup/ladm/gfx/'
    images_dir = 'images/animales/'

    if os.path.exists(backup_dir):
        for file in os.listdir(backup_dir):
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                src = os.path.join(backup_dir, file)
                dst = os.path.join(images_dir, file)
                shutil.copy2(src, dst)

    # Copiar main.jpg si existe en images/ladm/
    if os.path.exists('images/ladm/main.jpg'):
        shutil.copy2('images/ladm/main.jpg', 'images/animales/main.jpg')

    print("✅ Imágenes copiadas")

def create_html_pages():
    """Crear páginas HTML"""

    # Crear directorio animales si no existe
    os.makedirs('animales', exist_ok=True)

    # Plantilla para index.html
    index_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Los animales de la música - Ernesto Acher">
    <title>Los animales de la música - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-animales">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>Los animales de la música</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li class="active">- Comienzo</li>
                            <li><a href="videos.html">- Videos</a></li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <img src="../images/animales/main.jpg" alt="Los animales de la música" class="content-image-right">

                    <h2>Primera versión</h2>

                    <p>Después de la experiencia del "Colón Opera Concerto", Jorge de la Vega y yo quedamos con ganas de hacer algún otro proyecto y café va, café viene, en la esquina de Canning y Cabello, se nos ocurrió hacer un concierto para chicos basado en música que estuviera dedicada, o que de algún modo hiciera alusión a animalitos. Y así comenzamos a anotar: "El murciélago", "La pantera rosa", "El pájaro loco", "Tiburón", "Faivel", "El cóndor pasa", "El vuelo del moscardón", "Pájaro campana", "Pedro y el lobo", "El zorro"... y por supuesto, cada nueva anotación era una carcajada por las cosas que se nos iban ocurriendo para la puesta en escena.</p>

                    <p>Creo que el mayor delirio fue cuando armamos el inventado viaje de "Manuelita", ese entrañable personaje de la aún más entrañable María Elena Walsh, haciéndola pasar por distintas épocas y toparse con diferentes compositores. Primero hacíamos cantar a toda la sala, chicos y grandes, y luego se escuchaba la "cruza" de Manuelita con Vivaldi ("La primavera"), con Beethoven ("5a. sinfonía"), con Tchaikovsky ("Cascanueces") y finalmente con Ravel ("Bolero"). La parte final era "Teresa y el Oso", el cuento sinfónico de Les Luthiers, con De la Vega como relator. También fuimos al Avenida, con el auspicio de la Fundación Konex y también fue un bombazo. También se repitió al año siguiente, ya sin el apoyo de Konex, y luego lo presentamos en Córdoba, pero la marcha se detuvo. Creo que "Los animales de la música" merecía mejor suerte...</p>

                    <h2>Segunda versión</h2>

                    <p>Y la vida siempre da revancha... En el segundo semestre del 2005 hubo un retorno con algunas funciones en el Teatro Colón, y aunque las condiciones escénicas eran un tanto precarias (sólo se podía utilizar el proscenio) resultaron todo un éxito. Tanto es así que en el 2006 hicimos casi veinte funciones durante las vacaciones de invierno. Y a sala llena!</p>

                    <p>Los cambios en la segunda versión fueron el reemplazo de "Manueleces" (Manuelita-"Cascanueces"), por la "Polka de Manuelita" (Manuelita-"Tritsch-tratsch polka") y la supresión de "Teresa y el Oso", que hacía el programa demasiado largo, quedando el cierre a cargo del delirante paseo de Manuelita. El éxito fue impresionante, continuó durante 2007 en el Auditorio de Belgrano y ahora empieza a proyectarse fuera de Buenos Aires: el 14 de marzo lo presentaremos en Asunción (Paraguay) y hay gestiones adelantadas para el interior de Argentina.</p>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('animales/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    # Plantilla para videos.html
    videos_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Videos - Los animales de la música">
    <title>Videos - Los animales de la música - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-animales">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>Los animales de la música</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li><a href="index.html">- Comienzo</a></li>
                            <li class="active">- Videos</li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <h2>Videos</h2>
                    <p>Próximamente se agregarán videos de Los animales de la música.</p>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('animales/videos.html', 'w', encoding='utf-8') as f:
        f.write(videos_html)

    print("✅ Páginas HTML creadas")

def main():
    print("📦 Migrando Los Animales de la Música...")
    print()

    print("📄 Creando archivos JSON...")
    create_animales_jsons()
    print()

    print("📷 Copiando imágenes...")
    copy_images()
    print()

    print("📝 Creando páginas HTML...")
    create_html_pages()
    print()

    print("✅ Migración de Los Animales completada!")

if __name__ == '__main__':
    main()
