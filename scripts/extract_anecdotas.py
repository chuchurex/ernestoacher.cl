#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
from html.parser import HTMLParser
from pathlib import Path

class AnecdotaExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content_td = False
        self.in_h2 = False
        self.in_p = False
        self.td_depth = 0
        self.found_anecdotario_h1 = False
        self.title = ""
        self.content_parts = []
        self.current_p = []

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.td_depth += 1
            # Buscamos el td que contiene el contenido (después del h1 de Anecdotario)
            if self.found_anecdotario_h1 and not self.in_content_td:
                attrs_dict = dict(attrs)
                if attrs_dict.get('valign') == 'top':
                    self.in_content_td = True

        elif tag == 'h1':
            # Detectar cuando encontramos el h1 de Anecdotario
            pass

        elif tag == 'h2' and self.in_content_td:
            self.in_h2 = True

        elif tag == 'p' and self.in_content_td:
            self.in_p = True
            self.current_p = ['<p>']

        elif self.in_p:
            # Preservar tags dentro de párrafos (b, i, em, strong, br)
            if tag in ['b', 'i', 'em', 'strong', 'br']:
                self.current_p.append(f'<{tag}>')
            elif tag == 'a':
                attrs_dict = dict(attrs)
                if 'href' in attrs_dict:
                    self.current_p.append(f'<a href="{attrs_dict["href"]}">')
                else:
                    self.current_p.append('<a>')

    def handle_endtag(self, tag):
        if tag == 'td':
            self.td_depth -= 1
            if self.in_content_td and self.td_depth < 1:
                self.in_content_td = False

        elif tag == 'h2' and self.in_h2:
            self.in_h2 = False

        elif tag == 'p' and self.in_p:
            self.current_p.append('</p>')
            self.content_parts.append(''.join(self.current_p))
            self.current_p = []
            self.in_p = False

        elif self.in_p:
            if tag in ['b', 'i', 'em', 'strong', 'a']:
                self.current_p.append(f'</{tag}>')

    def handle_data(self, data):
        text = data.strip()
        if not text:
            return

        if text == 'Anecdotario':
            self.found_anecdotario_h1 = True

        elif self.in_h2:
            if self.title:
                self.title += " " + text
            else:
                self.title = text

        elif self.in_p:
            self.current_p.append(data)

    def get_result(self):
        return {
            'title': self.title.strip(),
            'content': '\n'.join(self.content_parts)
        }

def clean_html_entities(text):
    """Convierte entidades HTML a caracteres Unicode"""
    # Diccionario de entidades HTML comunes
    entities = {
        '&aacute;': 'á', '&eacute;': 'é', '&iacute;': 'í', '&oacute;': 'ó', '&uacute;': 'ú',
        '&Aacute;': 'Á', '&Eacute;': 'É', '&Iacute;': 'Í', '&Oacute;': 'Ó', '&Uacute;': 'Ú',
        '&ntilde;': 'ñ', '&Ntilde;': 'Ñ',
        '&uuml;': 'ü', '&Uuml;': 'Ü',
        '&iquest;': '¿', '&iexcl;': '¡',
        '&ldquo;': '"', '&rdquo;': '"', '&quot;': '"',
        '&lsquo;': "'", '&rsquo;': "'",
        '&nbsp;': ' ', '&amp;': '&',
        '&#8220;': '"', '&#8221;': '"',
        '&#8217;': "'",
    }

    result = text
    for entity, char in entities.items():
        result = result.replace(entity, char)

    return result

def extract_anecdota(html_file):
    """Extrae el contenido de una anécdota desde un archivo HTML"""
    try:
        with open(html_file, 'r', encoding='iso-8859-1') as f:
            html = f.read()

        parser = AnecdotaExtractor()
        parser.feed(html)
        result = parser.get_result()

        # Limpiar entidades HTML
        result['title'] = clean_html_entities(result['title'])
        result['content'] = clean_html_entities(result['content'])

        return result
    except Exception as e:
        print(f"Error procesando {html_file}: {str(e)}")
        return None

def generate_id_from_filename(filename):
    """Genera un ID a partir del nombre del archivo"""
    return Path(filename).stem

def main():
    backup_dir = Path('/Users/chuchurex/Sites/prod/ernestoacher.cl/backup/anecdotario')
    output_dir = Path('/Users/chuchurex/Sites/prod/ernestoacher.cl/data/anecdotas')

    # Asegurar que el directorio de salida existe
    output_dir.mkdir(parents=True, exist_ok=True)

    # Lista de archivos a procesar
    archivos = [
        'rosario.htm',
        'drodrigo.htm',
        'zanotti.htm',
        'molloy.htm',
        'll03.htm',
        'll04.htm',
        'll05.htm',
        'll06.htm',
        'll35.htm',
        'fnegras.htm',
        'carlitosy.htm',
        'lbe01.htm',
        'lbe18.htm',
        'volados.htm',
        'mejor_clari.htm',
        'catastrofe.htm',
        'pushkin.htm',
        # Agregar otros archivos que encontramos
        'algun_proy.htm',
        'mhijo.htm'
    ]

    processed = 0
    failed = 0

    for archivo in archivos:
        html_path = backup_dir / archivo

        if not html_path.exists():
            print(f"Advertencia: {archivo} no existe, saltando...")
            continue

        print(f"Procesando {archivo}...")
        result = extract_anecdota(html_path)

        if result and result['title']:
            # Generar ID desde el nombre del archivo
            anecdota_id = generate_id_from_filename(archivo)

            # Crear el objeto JSON
            anecdota_json = {
                'id': anecdota_id,
                'title': result['title'],
                'content': result['content']
            }

            # Guardar como JSON
            output_file = output_dir / f'{anecdota_id}.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(anecdota_json, f, ensure_ascii=False, indent=2)

            print(f"  ✓ Creado: {output_file.name}")
            print(f"    Título: {result['title']}")
            processed += 1
        else:
            print(f"  ✗ Falló la extracción")
            failed += 1

    print(f"\n{'='*60}")
    print(f"Resumen:")
    print(f"  Procesados exitosamente: {processed}")
    print(f"  Fallidos: {failed}")
    print(f"  Total: {processed + failed}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
