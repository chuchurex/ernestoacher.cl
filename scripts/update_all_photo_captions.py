#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
from bs4 import BeautifulSoup

# Mapping of image filenames to their descriptions
photo_captions = {
    'll_ch76alm1.jpg': 'Almuerzo en Santiago, 1976. Al fondo, Marcos y Daniel. A la derecha, Susy Rabinovich, Carlos y Virginia Núñez, Pilar Díaz (esposa de Adolfo Flores). A la izquierda, Fernando Rosas y Rubén Scarone.',
    'll_ch76alm2.jpg': 'Almuerzo en Santiago, 1976. Fernando Rosas, Rubén Scarone, Jorge Maronna, Tito Diz, Chiche Aisemberg, Marcos Mundstock.',
    'll_ch76cadolf3.jpg': 'Con Adolfo Flores, Santiago, 1976.',
    'll_alejo1.jpg': 'Tocando "Pepper Clemens" en una gira a Mar del Plata, con Alejo Elijovich en reemplazo de López Puccio (hepatitis).',
    'll_bolero.jpg': 'Cantando el "Bolero de de los celos " en Radio Municipal, programa de Emilio Stevanovich.',
    'll_cn_cipe.jpg': 'Noche de estreno en el Coliseo: Carlos Núñez y Cipe Lincovsky',
    'll_ea_brito.jpg': 'Con el sello del Gusano Brito, excepcional fotógrafo. Caracas, 1973.',
    'll_cnea.jpg': 'En una entrevista, con Carlos Núñez.',
    'll_enscolon2.jpg': 'Ensayando "Las majas del bergantín" en el Teatro Colón, 1986.',
    'll_enscolon5.jpg': 'Ensayo general de "Las majas del bergantín" en el Teatro Colón, 1986.',
    'll_funcolon3.jpg': 'Saludando en el Teatro Colón, 1986.',
    'll_funcolon5.jpg': '"Kathy, la reina del saloon" en el Teatro Colón, 1986.',
    'll_funcolon9.jpg': 'Con Haydée Francia, Delia Galán y Saritela Castellvi, antes de la función del Teatro Colón, 1986.',
    'll_gabrrossettoea.jpg': 'Noche de estreno en el Coliseo: con Gabriela Acher y Cecilia Rosetto.',
    'll_gallinita2.jpg': 'Y por qué, eh? Por qué?…',
    'll_gila.jpg': 'Con el querido Miguel Gila en los camarines del Teatro Alcalá, Madrid, 1983. A la derecha, Juanito García Caffi.',
    'll_kathy2.jpg': 'En "Kathy, la reina del saloon".',
    'll_francia1.jpg': 'En el parador de Francia, frente a "La fusita", Punta del Este, verano de 1973. Parados: Gerardo Masana, Vladimiro y Francia, Carlos Núñez, Marcos Mundstock y Josefina. Sentados: Susy Mendelievich, Daniel Rabinovich, moi y Carlos López Puccio.',
    'll_oppibolero.jpg': '"Bolero de Mastropiero" en el escenario (???) de La cebolla, 1971, cuando éramos cinco. Moi, Jorge, Daniel, Carlitos y Pucho.',
    'll_gero72_2.jpg': 'Tocando en la playa... Punta del Este, 1973. Pucho, Gerardo, Daniel, moi, Jorge y Carlitos. Gentileza de Sebastián Padilla.',
    'll_vientosgit.jpg': 'El saludo de "Vientos gitanos", Teatro Odeón, 1975.',
    'll_serrat_ch1.jpg': 'Una fiesta para Joan Manuel Serrat en casa de Ciche Aisemberg.',
    'll_serrat_t.jpg': 'Visitas en el Coliseo: Joan Manuel Serrat',
    'll_sabato.jpg': 'Visitas en el Coliseo: Ernesto Sábato.',
    'll_sabatnegro.jpg': 'Noche de estreno en el Coliseo: Menchi Sabat y el Negro Fontanarrosa.',
    'll_partido.jpg': 'En el Teatro Coliseo, mirando un partido por TV. A la derecha de Daniel, Rudy Chernicoff y a mi izquierda Hugo Guerrero Martinheitz.',
    'll_mirtha.jpg': 'Recuerdo de un almuerzo con Mirtha Legrand.',
    'll_makanoa1.jpg': 'Carlos Núñez dándole a los cocos en "Makanoa".',
    'll_lasmajas.jpg': 'Ay! Qué mareo… (La majas del bergantín)',
    'll_landritorres.jpg': 'Noche de estreno en el Coliseo: Luis Landriscina y Jaime Torres.'
}

print("Step 1: Copying new photos from inbox/fotos to galerias/fotos")
copied = 0
for img_name in photo_captions.keys():
    src = f'inbox/fotos/{img_name}'
    dest = f'galerias/fotos/{img_name}'

    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"  ✓ Copied {img_name}")
        copied += 1
    else:
        print(f"  ✗ Missing: {img_name}")

print(f"\nCopied {copied} photos")

print("\nStep 2: Updating photo captions in HTML pages")

# Find all HTML pages that use these images
updated = 0
for html_file in os.listdir('lesluthiers'):
    if html_file.startswith('f_ll') and html_file.endswith('.html'):
        filepath = f'lesluthiers/{html_file}'

        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        # Find the image
        img_tag = soup.find('img', src=lambda x: x and 'galerias/fotos/' in x)
        if img_tag:
            img_src = img_tag['src']
            img_name = img_src.split('/')[-1]

            # Check if we have a caption for this image
            if img_name in photo_captions:
                # Find or create caption paragraph
                caption_tag = soup.find('p', class_='photo-caption')

                if caption_tag:
                    # Update existing caption
                    caption_tag.string = photo_captions[img_name]
                else:
                    # Add caption if missing
                    photo_display = soup.find('div', class_='photo-display')
                    if photo_display:
                        new_caption = soup.new_tag('p', **{'class': 'photo-caption'})
                        new_caption.string = photo_captions[img_name]
                        photo_display.append(new_caption)

                # Save updated HTML
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(soup.prettify()))

                print(f"  ✓ Updated {html_file}: {img_name}")
                updated += 1

print(f"\n✅ Updated {updated} HTML pages with correct captions")
