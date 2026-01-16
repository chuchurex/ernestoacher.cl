#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import shutil

def create_gershwin_jsons():
    """Crear archivos JSON para Gershwin"""

    # Crear directorio data/gershwin si no existe
    os.makedirs('data/gershwin', exist_ok=True)

    # JSON para index
    index_data = {
        "title": "Gershwin, el hombre que amamos",
        "sections": [
            {
                "heading": "Primera versión",
                "content": [
                    "En una visita de Lalo Schifrin a Buenos Aires, en 1997, me encontré con Baby López Furst y Jorge Navarro, a quienes hacía un tiempo que no veía, y unas semanas más tarde nos citamos con Jorge a tomar café y recordar viejos tiempos. Justo por esa época me propusieron armar un ciclo de tres conciertos de \"fusión\" para una fundación y propuse, con una orquesta sinfónica como base, un concierto de tango con Jairo y Rodolfo Mederos, uno de jazz con el dúo de pianos Jorge Navarro-Baby López Furst y un tercero con cantantes haciendo fragmentos de comedia musical.",
                    "Mientras esperaba la respuesta me quedé pensando que al concierto de jazz, que iba a ser sobre la base de standards, le faltaba un remate que tuviera \"punch\", hasta que un día se me ocurrió que sería fantástico hacer una versión jazzeada de \"Rhapsody in blue\". Me encontré con Jorge en un bar y cuando empecé a contarle la idea se puso como loco y empezó a saltar y a gritar su conocido \"No... no... no puede ser...\" Yo estaba desconcertado y por un instante pensé \"Se enojó... no le gustó...\" Cuando se calmó, me explicó que la excitación era porque hacía seis meses que él y Baby estaban pensando en lo mismo, incluso lo habían comentado con Pedro Ignacio Calderón, pero no avanzaban porque no sabían quien podría animarse a escribir la versión. Con todo el entusiasmo, le dije que me animaba y además él a su vez me propuso que el programa fuera dedicado sólo a Gershwin. Hasta tenían el nombre \"Gershwin, el hombre que amamos\", obviamente una paráfrasis de su tema más conocido, y acepté enseguida porque me pareció una idea brillante. Al final, el ciclo no se concretó pero no quisimos dejar caer la idea, y a través de la gestión Rafael Pereyra conseguimos a Hiram Walker como sponsor (para whisky Premium). Baby y yo nos pusimos a trabajar como locos en los arreglos y hasta llegué a hacer una primera versión jazzeada de la \"Rhapsody\" para dúo de pianos, que Jorge y Baby estrenaron en el show que hacían en \"Opera prima\". Nunca dejaré de lamentar que no haya quedado grabación de esa versión...",
                    "Más tarde y con todo el apoyo de Alberto Alonso y el querido Parmigiani (jefe de escenario) estrenamos en el Teatro Avenida (1.000 asientos!!). Con todo el susto del mundo anunciamos dos funciones (y eran en martes...) pero apenas se abrió la boletería, las entradas volaron. Para hacerla corta, hicimos ocho funciones a sala repleta y tuvimos que parar porque yo tenía compromiso de unos conciertos en Caracas. Pero conseguimos repetir el ciclo al año siguiente, también en el Avenida, y además lo presentamos en Córdoba, en Santa Fe, en Mar del Plata y en São Paulo (Brasil). Se grabó en audio y video, hubo contactos para presentarlo en EEUU, hubo proyectos de una segunda versión que incluía el Concierto en Fa, en fin, daba para mucho más pero la prematura y lamentada muerte de Baby cerró este capítulo. Lo he dicho muchas veces, y sigo sintiéndolo: de las muchas, muchísimas noches de felicidad y alegría que tuve la suerte de vivir en el escenario, si tuviera que elegir una, sin dudas elegiría una de esas noches de \"Gershwin\" en el Avenida. Era puro placer estar ahí, con esos musicazos y con Jorge y Baby produciendo tanta belleza."
                ]
            },
            {
                "heading": "Segunda versión",
                "content": [
                    "Y la vida siempre da revancha... A principios del 2006 tuvimos el ofrecimiento de reeditar el homenaje a Gershwin. Lo hablamos mucho con Jorge y decidimos hacerlo con orquesta y trío, porque teníamos nostalgia de esas noches y porque pensamos que era una manera de mantener vivo el recuerdo y la magia de los arreglos de Baby. Esta nueva versión se estrenó en Mendoza en el festival \"Los caminos del vino\". A mediados de año nos ofrecieron hacerlo en el Teatro Colón, y a pesar de estar muy \"sobre la hora\" y otros inconvenientes, hicimos dos funciones a sala repleta. Fueron dos noches de mucha felicidad en las que sólo lamentamos la ausencia del querido Baby. Como tantas veces sucede, nos quedamos con ganas de más y en noviembre nos animamos a dos funciones en el Teatro Coliseo, esta vez con la grabación a cargo del inefable Carlos Piriz. Se hizo algunas veces más, en el Parque 3 de febrero, en el Festival de Jazz de Campana, a fines de marzo lo haremos en Tucumán. El proyecto sigue vivo, y tanto que el 18 de abril lo haremos en el Teatro Opera de Buenos Aires, presentando el CD editado por Acqua Records."
                ]
            }
        ],
        "image": "images/gershwin/main.jpg",
        "image_alt": "Gershwin - El hombre que amamos"
    }

    with open('data/gershwin/index.json', 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    print("✅ JSONs creados")

def copy_images():
    """Copiar imágenes desde backup"""

    # Crear directorio images/gershwin si no existe
    os.makedirs('images/gershwin', exist_ok=True)

    # Copiar imágenes JPG
    backup_dir = 'backup/hg/gfx/'
    images_dir = 'images/gershwin/'

    images = ['i_t3_c11.jpg', 'i_t3_c7.jpg', 'i_t4_c12.jpg', 'i_t5_c14.jpg']

    for img in images:
        src = os.path.join(backup_dir, img)
        dst = os.path.join(images_dir, img)
        if os.path.exists(src):
            shutil.copy2(src, dst)

    # La imagen main.jpg no existe en el backup, la vamos a buscar en otro lugar
    # o crear un placeholder si no la encontramos

    print("✅ Imágenes copiadas")

def create_html_pages():
    """Crear páginas HTML"""

    # Crear directorio gershwin si no existe
    os.makedirs('gershwin', exist_ok=True)

    # Plantilla para index.html
    index_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Gershwin, el hombre que amamos - Ernesto Acher">
    <title>Gershwin, el hombre que amamos - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-gershwin">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>Gershwin, el hombre que amamos</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li class="active">- Comienzo</li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <img src="../images/gershwin/main.jpg" alt="Gershwin - El hombre que amamos" class="content-image-right">

                    <h2>Primera versión</h2>

                    <p>En una visita de Lalo Schifrin a Buenos Aires, en 1997, me encontré con Baby López Furst y Jorge Navarro, a quienes hacía un tiempo que no veía, y unas semanas más tarde nos citamos con Jorge a tomar café y recordar viejos tiempos. Justo por esa época me propusieron armar un ciclo de tres conciertos de "fusión" para una fundación y propuse, con una orquesta sinfónica como base, un concierto de tango con Jairo y Rodolfo Mederos, uno de jazz con el dúo de pianos Jorge Navarro-Baby López Furst y un tercero con cantantes haciendo fragmentos de comedia musical.</p>

                    <p>Mientras esperaba la respuesta me quedé pensando que al concierto de jazz, que iba a ser sobre la base de standards, le faltaba un remate que tuviera "punch", hasta que un día se me ocurrió que sería fantástico hacer una versión jazzeada de "Rhapsody in blue". Me encontré con Jorge en un bar y cuando empecé a contarle la idea se puso como loco y empezó a saltar y a gritar su conocido "No... no... no puede ser..." Yo estaba desconcertado y por un instante pensé "Se enojó... no le gustó..." Cuando se calmó, me explicó que la excitación era porque hacía seis meses que él y Baby estaban pensando en lo mismo, incluso lo habían comentado con Pedro Ignacio Calderón, pero no avanzaban porque no sabían quien podría animarse a escribir la versión. Con todo el entusiasmo, le dije que me animaba y además él a su vez me propuso que el programa fuera dedicado sólo a Gershwin. Hasta tenían el nombre "Gershwin, el hombre que amamos", obviamente una paráfrasis de su tema más conocido, y acepté enseguida porque me pareció una idea brillante. Al final, el ciclo no se concretó pero no quisimos dejar caer la idea, y a través de la gestión Rafael Pereyra conseguimos a Hiram Walker como sponsor (para whisky Premium). Baby y yo nos pusimos a trabajar como locos en los arreglos y hasta llegué a hacer una primera versión jazzeada de la "Rhapsody" para dúo de pianos, que Jorge y Baby estrenaron en el show que hacían en "Opera prima". Nunca dejaré de lamentar que no haya quedado grabación de esa versión...</p>

                    <p>Más tarde y con todo el apoyo de Alberto Alonso y el querido Parmigiani (jefe de escenario) estrenamos en el Teatro Avenida (1.000 asientos!!). Con todo el susto del mundo anunciamos dos funciones (y eran en martes...) pero apenas se abrió la boletería, las entradas volaron. Para hacerla corta, hicimos ocho funciones a sala repleta y tuvimos que parar porque yo tenía compromiso de unos conciertos en Caracas. Pero conseguimos repetir el ciclo al año siguiente, también en el Avenida, y además lo presentamos en Córdoba, en Santa Fe, en Mar del Plata y en São Paulo (Brasil). Se grabó en audio y video, hubo contactos para presentarlo en EEUU, hubo proyectos de una segunda versión que incluía el Concierto en Fa, en fin, daba para mucho más pero la prematura y lamentada muerte de Baby cerró este capítulo. Lo he dicho muchas veces, y sigo sintiéndolo: de las muchas, muchísimas noches de felicidad y alegría que tuve la suerte de vivir en el escenario, si tuviera que elegir una, sin dudas elegiría una de esas noches de "Gershwin" en el Avenida. Era puro placer estar ahí, con esos musicazos y con Jorge y Baby produciendo tanta belleza.</p>

                    <h2>Segunda versión</h2>

                    <p>Y la vida siempre da revancha... A principios del 2006 tuvimos el ofrecimiento de reeditar el homenaje a Gershwin. Lo hablamos mucho con Jorge y decidimos hacerlo con orquesta y trío, porque teníamos nostalgia de esas noches y porque pensamos que era una manera de mantener vivo el recuerdo y la magia de los arreglos de Baby. Esta nueva versión se estrenó en Mendoza en el festival "Los caminos del vino". A mediados de año nos ofrecieron hacerlo en el Teatro Colón, y a pesar de estar muy "sobre la hora" y otros inconvenientes, hicimos dos funciones a sala repleta. Fueron dos noches de mucha felicidad en las que sólo lamentamos la ausencia del querido Baby. Como tantas veces sucede, nos quedamos con ganas de más y en noviembre nos animamos a dos funciones en el Teatro Coliseo, esta vez con la grabación a cargo del inefable Carlos Piriz. Se hizo algunas veces más, en el Parque 3 de febrero, en el Festival de Jazz de Campana, a fines de marzo lo haremos en Tucumán. El proyecto sigue vivo, y tanto que el 18 de abril lo haremos en el Teatro Opera de Buenos Aires, presentando el CD editado por Acqua Records.</p>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('gershwin/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    print("✅ Páginas HTML creadas")

def main():
    print("📦 Migrando Gershwin...")
    print()

    print("📄 Creando archivos JSON...")
    create_gershwin_jsons()
    print()

    print("📷 Copiando imágenes...")
    copy_images()
    print()

    print("📝 Creando páginas HTML...")
    create_html_pages()
    print()

    print("✅ Migración de Gershwin completada!")

if __name__ == '__main__':
    main()
