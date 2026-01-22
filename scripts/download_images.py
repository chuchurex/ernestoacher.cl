#!/usr/bin/env python3
"""
Script para descargar imágenes del sitio ernestoacher.com desde Wayback Machine
Usa CDX API para encontrar URLs disponibles de imágenes
"""

import requests
import os
import time
from pathlib import Path

# Configuración
WAYBACK_CDX_API = "http://web.archive.org/cdx/search/cdx"
WAYBACK_DOWNLOAD = "https://web.archive.org/web/"
DOMAIN = "ernestoacher.com"
TIMESTAMP_START = "20090401"
TIMESTAMP_END = "20090930"

# Directorio de salida
OUTPUT_DIR = Path(__file__).parent.parent / "backup"

# Extensiones de imagen a descargar
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.gif', '.png', '.bmp']

def get_image_urls(path_prefix):
    """
    Obtiene URLs de imágenes disponibles en Wayback Machine para un path específico
    """
    print(f"\n🔍 Buscando imágenes en: {path_prefix}")

    params = {
        'url': f'{DOMAIN}/{path_prefix}*',
        'matchType': 'prefix',
        'from': TIMESTAMP_START,
        'to': TIMESTAMP_END,
        'output': 'json',
        'fl': 'timestamp,original,mimetype,statuscode',
        'filter': 'statuscode:200',
        'collapse': 'original'
    }

    try:
        response = requests.get(WAYBACK_CDX_API, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        if not data or len(data) < 2:
            print(f"  ⚠️  No se encontraron resultados")
            return []

        # Filtrar solo imágenes
        image_urls = []
        for row in data[1:]:  # Skip header row
            timestamp, original_url, mimetype, statuscode = row

            # Verificar si es una imagen por extensión o mimetype
            is_image = (
                any(original_url.lower().endswith(ext) for ext in IMAGE_EXTENSIONS) or
                (mimetype and 'image' in mimetype.lower())
            )

            if is_image:
                image_urls.append((timestamp, original_url))

        print(f"  ✓ Encontradas {len(image_urls)} imágenes")
        return image_urls

    except Exception as e:
        print(f"  ✗ Error en CDX API: {e}")
        return []

def download_image(timestamp, original_url, output_path):
    """
    Descarga una imagen desde Wayback Machine
    """
    wayback_url = f"{WAYBACK_DOWNLOAD}{timestamp}id_/{original_url}"

    try:
        # Verificar si ya existe
        if output_path.exists():
            print(f"  ⊘ Ya existe: {output_path.name}")
            return True

        # Crear directorio si no existe
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Descargar
        response = requests.get(wayback_url, timeout=30, stream=True)
        response.raise_for_status()

        # Guardar
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"  ✓ Descargado: {output_path.name}")
        return True

    except Exception as e:
        print(f"  ✗ Error descargando {original_url}: {e}")
        return False

def download_section_images(section_name, path_prefix):
    """
    Descarga todas las imágenes de una sección específica
    """
    print(f"\n{'='*60}")
    print(f"📦 SECCIÓN: {section_name}")
    print(f"{'='*60}")

    # Obtener URLs de imágenes
    image_urls = get_image_urls(path_prefix)

    if not image_urls:
        print(f"  ⚠️  No hay imágenes para descargar en esta sección")
        return 0

    # Descargar cada imagen
    downloaded = 0
    for i, (timestamp, original_url) in enumerate(image_urls, 1):
        # Construir path de salida
        # Extraer la ruta relativa después del dominio
        relative_path = original_url.replace(f'http://{DOMAIN}/', '').replace(f'https://{DOMAIN}/', '')
        output_path = OUTPUT_DIR / relative_path

        print(f"\n  [{i}/{len(image_urls)}] {relative_path}")

        if download_image(timestamp, original_url, output_path):
            downloaded += 1

        # Delay para no saturar el servidor
        time.sleep(0.5)

    print(f"\n  📊 Total descargado: {downloaded}/{len(image_urls)}")
    return downloaded

def main():
    """
    Función principal
    """
    print("="*60)
    print("🖼️  DESCARGA DE IMÁGENES - ERNESTO ACHER")
    print("="*60)
    print(f"Fuente: {DOMAIN}")
    print(f"Período: {TIMESTAMP_START[:4]}-{TIMESTAMP_START[4:6]} a {TIMESTAMP_END[:4]}-{TIMESTAMP_END[4:6]}")
    print(f"Destino: {OUTPUT_DIR}")

    # Secciones a descargar (prioridad)
    sections = [
        ("Assets generales", "asset"),
        ("Les Luthiers", "ll"),
        ("La Banda Elástica", "lbe"),
        ("Humor con Achís", "hca"),
        ("Veladas", "ve"),
        ("Offside", "ocho"),
        ("Homenaje a Gershwin", "hg"),
        ("Los animales de la música", "ladm"),
        ("De todo como en botica", "dtodo"),
        ("Realizaciones recientes", "rr"),
        ("Nuevos proyectos", "proyectos"),
        ("Menú de conciertos", "menu"),
    ]

    total_downloaded = 0

    for section_name, path_prefix in sections:
        downloaded = download_section_images(section_name, path_prefix)
        total_downloaded += downloaded

    # Resumen final
    print("\n" + "="*60)
    print("📊 RESUMEN FINAL")
    print("="*60)
    print(f"Total de imágenes descargadas: {total_downloaded}")
    print(f"Ubicación: {OUTPUT_DIR}")
    print("\n✅ Descarga completada")

if __name__ == "__main__":
    main()
