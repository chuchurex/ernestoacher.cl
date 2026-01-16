#!/usr/bin/env python3
"""
Script para migrar la sección Veladas Espeluznantes
"""

import os
import json
import re
from pathlib import Path

def clean_html_entities(text):
    """Convierte entidades HTML a caracteres UTF-8"""
    entities = {
        '&oacute;': 'ó',
        '&aacute;': 'á',
        '&eacute;': 'é',
        '&iacute;': 'í',
        '&uacute;': 'ú',
        '&ntilde;': 'ñ',
        '&uuml;': 'ü',
        '&#8220;': '"',
        '&#8221;': '"',
        '&acute;': '´',
        '&amp;': '&',
        '&nbsp;': ' ',
    }
    for entity, char in entities.items():
        text = text.replace(entity, char)
    return text

def extract_content_from_html(filepath):
    """Extrae el contenido principal de un archivo HTML del backup"""
    with open(filepath, 'r', encoding='iso-8859-1') as f:
        content = f.read()

    # Limpiar entidades HTML
    content = clean_html_entities(content)

    # Extraer título
    title_match = re.search(r'<h1>([^<]+)</h1>', content)
    title = title_match.group(1) if title_match else "Veladas Espeluznantes"

    # Extraer contenido entre <p> tags
    paragraphs = re.findall(r'<p>(.+?)</p>', content, re.DOTALL)

    # Limpiar cada párrafo de tags HTML internos (excepto <img>)
    cleaned_paragraphs = []
    for p in paragraphs:
        # Mantener imágenes pero extraer su info
        img_match = re.search(r'<img[^>]*src="([^"]+)"[^>]*>', p)
        if img_match:
            # Si tiene imagen, la guardamos aparte
            continue
        # Remover otros tags HTML
        cleaned = re.sub(r'<[^>]+>', '', p)
        cleaned = cleaned.strip()
        if cleaned:
            cleaned_paragraphs.append(cleaned)

    return {
        'title': title,
        'paragraphs': cleaned_paragraphs
    }

# Crear JSON para index
print("Generando data/veladas/index.json...")
index_data = {
    "title": "Veladas Espeluznantes",
    "subtitle": "Cómo empezó la historia...",
    "mainImage": "main.jpg",
    "content": [
        {
            "type": "paragraph",
            "text": 'La historia de las "Veladas" es en realidad la confluencia de dos cosas distintas. La primera es "Juegos", un disco de bromas Y juegos musicales, cuya idea inicial surgió un día, no recuerdo si en el ´85 o el ´86, en que silbando el principio de la 40 de Mozart de pronto el silbido se me fue para el tango "El choclo". Me dio un ataque de risa y me puse a hacer un boceto con sintetizadores, lo llevé al teatro para hacérselo oir a los compañeros de Les Luthiers y debo decir que no les causó la más mínima gracia. Desilusionado, lo guardé en un cajón pero tiempo después, ya fuera del grupo, volví a escucharlo y no solamente me volvió a dar risa, sino que empezaron a ocurrírseme otras "asociaciones" tanto o más graciosas (como la "Pequeña música hebrea") o de puro juego musical (como "Borodin, bangles and beads"). Y el disco se grabó en abril de 1987 con una orquesta "de juguete" con la que grabábamos y regrabábamos hasta "parecer" una sinfónica y con la colaboración de amigos de muchos años como el Zurdo Roizner, Baby López Furst, etc. (Ver discografía)'
        },
        {
            "type": "paragraph",
            "text": 'La otra punta de las "Veladas" fue la experiencia con el maestro Calderón cuando me estrenó el poema sinfónico "Molloy" con la Filarmónica de Buenos Aires (1980). Además de haber quedado muy contento por el estupendo trabajo de Marcela Magín como solista de viola y por el apoyo de la orquesta, quedé muy impresionado por la manera en que Calderón había "mejorado" la obra desde la dirección. Más de diez años después hice algún intento por estudiar dirección orquestal pero no le encotraba la vuelta, hasta que a fines del ´92 conocí a Carlos Calleja, un tipazo y un gran maestro. En un par de charlas me hizo "asomar" al meollo del asunto y me vino el entusiasmo. Casualmente o no, uno nunca sabe, unos meses después me llamó Hugo Vitantonio desde Rosario y me propuso hacer un concierto sinfónico de música humor, partiendo de las bromas de "Juegos". A fines del ´93 estrené la primera versión en Rosario de las "Veladas Espeluznantes" y ya no me acuerdo cuantas veces las hice porque fue en un montón de lugares y otro montón de versiones diferentes. Y sigue funcionando...'
        }
    ]
}

with open('data/veladas/index.json', 'w', encoding='utf-8') as f:
    json.dump(index_data, f, ensure_ascii=False, indent=2)

# Crear JSONs simples para otras páginas
print("Generando data/veladas/bromas.json...")
bromas_data = {
    "title": "Veladas Espeluznantes",
    "subtitle": "Bromas y Juegos",
    "content": []
}
with open('data/veladas/bromas.json', 'w', encoding='utf-8') as f:
    json.dump(bromas_data, f, ensure_ascii=False, indent=2)

print("Generando data/veladas/fotos.json...")
fotos_data = {
    "title": "Veladas Espeluznantes",
    "subtitle": "Fotos",
    "photos": []
}
with open('data/veladas/fotos.json', 'w', encoding='utf-8') as f:
    json.dump(fotos_data, f, ensure_ascii=False, indent=2)

print("Generando data/veladas/videos.json...")
videos_data = {
    "title": "Veladas Espeluznantes",
    "subtitle": "Videos",
    "videos": []
}
with open('data/veladas/videos.json', 'w', encoding='utf-8') as f:
    json.dump(videos_data, f, ensure_ascii=False, indent=2)

print("✅ Archivos JSON creados correctamente")
