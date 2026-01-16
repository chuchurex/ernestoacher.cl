#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import shutil

def create_detodo_jsons():
    """Crear archivos JSON para De Todo como en Botica"""

    # Crear directorio data/detodo si no existe
    os.makedirs('data/detodo', exist_ok=True)

    # JSON para index
    index_data = {
        "title": "De todo como en botica",
        "links": [
            {"title": "Juntos en concierto", "url": "juntos.html"},
            {"title": "Quinteto Maderas", "url": "qm.html"},
            {"title": "Había una vez un país", "url": "habia.html"}
        ]
    }

    with open('data/detodo/index.json', 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # JSON para juntos
    juntos_data = {
        "title": "Juntos en concierto",
        "content": [
            "A principios de la temporada de 1991 me ofrecieron la posibilidad de hacer un concierto fusionando a la \"Banda Elástica\" con la \"Camerata Bariloche\" en un ciclo de tres que se haría en el Teatro Opera de Buenos Aires. Creo que el entusiasmo de ambos lados fue definitorio porque, aunque el ciclo nunca se concretó (me suena conocido...), decidimos hacerlo de todas maneras, y en un par de semanas tuve listo un proyecto con las posibles obras \"en conjunto\" y los momentos de lucimiento individual para cada grupo.",
            "El esquema fue aceptado y me puse a trabajar en los arreglos, tomando obras de la Banda y agregando algunas de mis bromas y juegos musicales que calzaban justo con ambas formaciones y que venían muy bien al clima festivo que flotaba en la idea, y así nació \"Juntos en concierto\". Una vez terminados los arreglos, con la Banda nos pusimos a ensayar nuestras partes como locos, dado que íbamos a \"enfrentarnos\" al grupo de cámara más prestigioso de la Argentina y queríamos estar \"afiladísimos\". Comenzaron los ensayos en el coqueto duplex que tenía la Camerata y lo que no habíamos tenido en cuenta era que ellos tenían muchos ensayos y obligaciones con otros repertorios y la verdad es que no nos habían dedicado tiempo... en fin, que los primeros ensayos parecían una despedida de soltero. Pero enseguida todo el mundo se conectó, la cosa empezó a sonar y la máquina se puso en marcha. Además propuse que hubiera un presentador muy particular, que mezclara la tónica de presentación \"culta\" con el \"enfrentamiento\" de los dos grupos como si fuera un partido de fútbol. El querido y recordado Mario Grasso lo hizo maravillosamente, hubo intercambio de banderines, revoleo de moneda para el \"sorteo de lado\", con silbato y todo... La muy buena producción estuvo a cargo de Héctor Cavallero y, aun con el entusiasmo de todos los que estábamos involucrados, nunca imaginamos que el proyecto tendría la resonancia que tuvo. Se anunciaron dos funciones en el Opera (2.400 asientos!!!!) y terminamos haciendo cuatro a sala llena. Pero la cosa no paró ahí... Fue tal el \"ruido\", que a los pocos meses hicimos dos funciones repletas en el Luna Park (5.000 asientos!!!!). Hubo grabación y filmación de las funciones del Opera pero las calidades no fueron satisfactorias. El video llegó a editarse y sólo pude rescatar un par de ejemplares."
        ],
        "image": "images/detodo/juntos.jpg"
    }

    with open('data/detodo/juntos.json', 'w', encoding='utf-8') as f:
        json.dump(juntos_data, f, ensure_ascii=False, indent=2)

    # JSON para qm
    qm_data = {
        "title": "Quinteto Maderas",
        "content": [
            "Con Juan Carlos Bazán (clarinete) y Alfonso Ferramosca (clarinete y saxo tenor), dos talentosos músicos de jazz tradicional, nos conocemos desde los tiempos de la escuela secundaria, cuando éramos habitués del Hot Club de Buenos Aires. Después de muchos años los reencontré en las jam sessions de los sábados a la tarde en la casa de Alfonso Fassi (trompeta), con quien además nos conocíamos desde la escuela primaria; y con Bazán seguimos viéndonos socialmente y en Bix, un simpático boliche dedicado al jazz que desafortunadamente duró muy poco. En una fiesta de cumpleaños de Carlos Inzillo, un entusiasta e incansable difusor del jazz, coincidimos tres clarinetes: Juan Carlos Bazán, Beto Wassington y yo; nos pusimos a tocar \"en trio\" y fue tan divertido (e insólito) que la idea me quedó flotando. Tiempo después le propuse a Bazán armar un grupo y se prendieron el inefable Ferramosca, Fili Savloff en guitarra y Juan Francisco Rodríguez en contrabajo. Comenzamos a ensayar en la casa de Bazán en Belgrano y a los pocos meses el mismo Inzillo (quien si no?) nos invitó a presentarnos en su histórico ciclo de la Sala AB del Teatro San Martín (Buenos Aires) Nos preparamos mucho y, a pesar de algunos tropiezos, olvidos y otra peripecias, creo que salió bien y por suerte quedó el testimonio en video. Después inentamos seguir pero algo había cambiado y una cierta onda se había evaporado. Fue debut y despedida, como diría Chico Novarro, pero sin ninguna duda valió la pena."
        ]
    }

    with open('data/detodo/qm.json', 'w', encoding='utf-8') as f:
        json.dump(qm_data, f, ensure_ascii=False, indent=2)

    # JSON para habia
    habia_data = {
        "title": "Había una vez un país",
        "content": [
            "Estando ya radicado en Córdoba (2001) mi querido y talentoso amigo Gustavo Maldino me llamó para contarme que estaba preparando un espectáculo basado en las canciones de María Elena Walsh, con solistas, coro y banda sinfónica. El se haría cargo de los arreglos corales y yo de los arreglos para banda. Me encantó la idea y también la posibilidad de trabajar con Gustavo, y en el retiro y el paisaje de mi casa de La Cumbrecita me puse a trabajar con todo. En medio de este proceso, en octubre, me invitaron a dirigir por segunda vez en Concepción y al regresar comencé a pensar la posibilidad de la migración. En pleno terremoto politico y social empezaron los ensayos y el estreno fue el 30 de noviembre de 2001, apenas unos días antes de la estrepitosa caída del gobierno de De la Rúa. El espectáculo se llamaba \"Había una vez un país\"..."
        ]
    }

    with open('data/detodo/habia.json', 'w', encoding='utf-8') as f:
        json.dump(habia_data, f, ensure_ascii=False, indent=2)

    print("✅ JSONs creados")

def copy_images():
    """Copiar imágenes desde backup"""

    # Crear directorio images/detodo si no existe
    os.makedirs('images/detodo', exist_ok=True)

    # Copiar imágenes desde backup/dtodo/gfx/
    backup_dir = 'backup/dtodo/gfx/'
    images_dir = 'images/detodo/'

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

    # Crear directorio detodo si no existe
    os.makedirs('detodo', exist_ok=True)

    # Plantilla para index.html
    index_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="De todo como en botica - Ernesto Acher">
    <title>De todo como en botica - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-detodo">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>De todo como en botica</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li class="active">- Índice</li>
                            <li><a href="juntos.html">- Juntos en concierto</a></li>
                            <li><a href="qm.html">- Quinteto Maderas</a></li>
                            <li><a href="habia.html">- Había una vez un país</a></li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <h2><a href="juntos.html">Juntos en concierto</a></h2>
                    <h2><a href="qm.html">Quinteto Maderas</a></h2>
                    <h2><a href="habia.html">Había una vez un país</a></h2>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('detodo/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    # Plantilla para juntos.html
    juntos_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Juntos en concierto - De todo como en botica">
    <title>Juntos en concierto - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-detodo">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>De todo como en botica</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li><a href="index.html">- Índice</a></li>
                            <li class="active">- Juntos en concierto</li>
                            <li><a href="qm.html">- Quinteto Maderas</a></li>
                            <li><a href="habia.html">- Había una vez un país</a></li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <h2>Juntos en concierto</h2>

                    <img src="../images/detodo/juntos.jpg" alt="Juntos en concierto" class="content-image-center">

                    <p>A principios de la temporada de 1991 me ofrecieron la posibilidad de hacer un concierto fusionando a la "Banda Elástica" con la "Camerata Bariloche" en un ciclo de tres que se haría en el Teatro Opera de Buenos Aires. Creo que el entusiasmo de ambos lados fue definitorio porque, aunque el ciclo nunca se concretó (me suena conocido...), decidimos hacerlo de todas maneras, y en un par de semanas tuve listo un proyecto con las posibles obras "en conjunto" y los momentos de lucimiento individual para cada grupo.</p>

                    <p>El esquema fue aceptado y me puse a trabajar en los arreglos, tomando obras de la Banda y agregando algunas de mis bromas y juegos musicales que calzaban justo con ambas formaciones y que venían muy bien al clima festivo que flotaba en la idea, y así nació "Juntos en concierto". Una vez terminados los arreglos, con la Banda nos pusimos a ensayar nuestras partes como locos, dado que íbamos a "enfrentarnos" al grupo de cámara más prestigioso de la Argentina y queríamos estar "afiladísimos". Comenzaron los ensayos en el coqueto duplex que tenía la Camerata y lo que no habíamos tenido en cuenta era que ellos tenían muchos ensayos y obligaciones con otros repertorios y la verdad es que no nos habían dedicado tiempo... en fin, que los primeros ensayos parecían una despedida de soltero. Pero enseguida todo el mundo se conectó, la cosa empezó a sonar y la máquina se puso en marcha. Además propuse que hubiera un presentador muy particular, que mezclara la tónica de presentación "culta" con el "enfrentamiento" de los dos grupos como si fuera un partido de fútbol. El querido y recordado Mario Grasso lo hizo maravillosamente, hubo intercambio de banderines, revoleo de moneda para el "sorteo de lado", con silbato y todo... La muy buena producción estuvo a cargo de Héctor Cavallero y, aun con el entusiasmo de todos los que estábamos involucrados, nunca imaginamos que el proyecto tendría la resonancia que tuvo. Se anunciaron dos funciones en el Opera (2.400 asientos!!!!) y terminamos haciendo cuatro a sala llena. Pero la cosa no paró ahí... Fue tal el "ruido", que a los pocos meses hicimos dos funciones repletas en el Luna Park (5.000 asientos!!!!). Hubo grabación y filmación de las funciones del Opera pero las calidades no fueron satisfactorias. El video llegó a editarse y sólo pude rescatar un par de ejemplares.</p>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('detodo/juntos.html', 'w', encoding='utf-8') as f:
        f.write(juntos_html)

    # Plantilla para qm.html
    qm_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Quinteto Maderas - De todo como en botica">
    <title>Quinteto Maderas - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-detodo">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>De todo como en botica</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li><a href="index.html">- Índice</a></li>
                            <li><a href="juntos.html">- Juntos en concierto</a></li>
                            <li class="active">- Quinteto Maderas</li>
                            <li><a href="habia.html">- Había una vez un país</a></li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <h2>Quinteto Maderas</h2>

                    <p>Con Juan Carlos Bazán (clarinete) y Alfonso Ferramosca (clarinete y saxo tenor), dos talentosos músicos de jazz tradicional, nos conocemos desde los tiempos de la escuela secundaria, cuando éramos habitués del Hot Club de Buenos Aires. Después de muchos años los reencontré en las jam sessions de los sábados a la tarde en la casa de Alfonso Fassi (trompeta), con quien además nos conocíamos desde la escuela primaria; y con Bazán seguimos viéndonos socialmente y en Bix, un simpático boliche dedicado al jazz que desafortunadamente duró muy poco. En una fiesta de cumpleaños de Carlos Inzillo, un entusiasta e incansable difusor del jazz, coincidimos tres clarinetes: Juan Carlos Bazán, Beto Wassington y yo; nos pusimos a tocar "en trio" y fue tan divertido (e insólito) que la idea me quedó flotando. Tiempo después le propuse a Bazán armar un grupo y se prendieron el inefable Ferramosca, Fili Savloff en guitarra y Juan Francisco Rodríguez en contrabajo. Comenzamos a ensayar en la casa de Bazán en Belgrano y a los pocos meses el mismo Inzillo (quien si no?) nos invitó a presentarnos en su histórico ciclo de la Sala AB del Teatro San Martín (Buenos Aires) Nos preparamos mucho y, a pesar de algunos tropiezos, olvidos y otra peripecias, creo que salió bien y por suerte quedó el testimonio en video. Después inentamos seguir pero algo había cambiado y una cierta onda se había evaporado. Fue debut y despedida, como diría Chico Novarro, pero sin ninguna duda valió la pena.</p>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('detodo/qm.html', 'w', encoding='utf-8') as f:
        f.write(qm_html)

    # Plantilla para habia.html
    habia_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Había una vez un país - De todo como en botica">
    <title>Había una vez un país - Ernesto Acher</title>
    <link rel="stylesheet" href="../css/app.css">
</head>
<body class="page-detodo">
    <div class="site-container">
        <div id="sidebar-container"></div>
        <div class="content-wrapper">
            <div id="header-container"></div>
            <main class="main-content">
                <div class="content-header-title">
                    <h1>De todo como en botica</h1>
                    <nav class="page-nav-right">
                        <ul>
                            <li><a href="index.html">- Índice</a></li>
                            <li><a href="juntos.html">- Juntos en concierto</a></li>
                            <li><a href="qm.html">- Quinteto Maderas</a></li>
                            <li class="active">- Había una vez un país</li>
                        </ul>
                    </nav>
                </div>

                <div class="section-content">
                    <h2>Había una vez un país</h2>

                    <p>Estando ya radicado en Córdoba (2001) mi querido y talentoso amigo Gustavo Maldino me llamó para contarme que estaba preparando un espectáculo basado en las canciones de María Elena Walsh, con solistas, coro y banda sinfónica. El se haría cargo de los arreglos corales y yo de los arreglos para banda. Me encantó la idea y también la posibilidad de trabajar con Gustavo, y en el retiro y el paisaje de mi casa de La Cumbrecita me puse a trabajar con todo. En medio de este proceso, en octubre, me invitaron a dirigir por segunda vez en Concepción y al regresar comencé a pensar la posibilidad de la migración. En pleno terremoto politico y social empezaron los ensayos y el estreno fue el 30 de noviembre de 2001, apenas unos días antes de la estrepitosa caída del gobierno de De la Rúa. El espectáculo se llamaba "Había una vez un país"...</p>
                </div>
            </main>
        </div>
    </div>
    <script src="../js/components.js"></script>
</body>
</html>'''

    with open('detodo/habia.html', 'w', encoding='utf-8') as f:
        f.write(habia_html)

    print("✅ Páginas HTML creadas")

def main():
    print("📦 Migrando De Todo como en Botica...")
    print()

    print("📄 Creando archivos JSON...")
    create_detodo_jsons()
    print()

    print("📷 Copiando imágenes...")
    copy_images()
    print()

    print("📝 Creando páginas HTML...")
    create_html_pages()
    print()

    print("✅ Migración de De Todo completada!")

if __name__ == '__main__':
    main()
