#!/usr/bin/env python3
"""
Script para descargar imágenes faltantes específicas del sitio ernestoacher.com
Enfocado en directorios gfx/ de cada sección
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

def get_available_images(path):
    """
    Obtiene URLs de imágenes disponibles en Wayback Machine para un path específico
    """
    print(f"  🔍 Consultando CDX API: {path}")

    params = {
        'url': f'{DOMAIN}/{path}',
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
            return []

        # Filtrar solo imágenes
        images = []
        for row in data[1:]:
            timestamp, original_url, mimetype, statuscode = row

            # Verificar si es imagen
            if any(original_url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.gif', '.png']) or \
               (mimetype and 'image' in mimetype.lower()):
                images.append((timestamp, original_url))

        return images

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return []

def download_image(timestamp, original_url, output_path):
    """
    Descarga una imagen desde Wayback Machine
    """
    wayback_url = f"{WAYBACK_DOWNLOAD}{timestamp}id_/{original_url}"

    try:
        # Verificar si ya existe
        if output_path.exists():
            return "exists"

        # Crear directorio
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Descargar
        response = requests.get(wayback_url, timeout=30, stream=True)
        response.raise_for_status()

        # Guardar
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return "downloaded"

    except Exception as e:
        return f"error: {e}"

def process_directory(dir_path, section_name):
    """
    Procesa un directorio específico
    """
    print(f"\n{'='*60}")
    print(f"📁 {section_name}")
    print(f"{'='*60}")

    images = get_available_images(dir_path)

    if not images:
        print(f"  ⚠️  No se encontraron imágenes")
        return 0, 0, 0

    downloaded = 0
    exists = 0
    errors = 0

    for i, (timestamp, original_url) in enumerate(images, 1):
        # Construir path de salida
        relative_path = original_url.replace(f'http://{DOMAIN}/', '').replace(f'https://{DOMAIN}/', '')
        output_path = OUTPUT_DIR / relative_path

        filename = output_path.name
        result = download_image(timestamp, original_url, output_path)

        if result == "downloaded":
            print(f"  [{i}/{len(images)}] ✓ {filename}")
            downloaded += 1
        elif result == "exists":
            print(f"  [{i}/{len(images)}] ⊘ {filename} (ya existe)")
            exists += 1
        else:
            print(f"  [{i}/{len(images)}] ✗ {filename} - {result}")
            errors += 1

        time.sleep(0.3)

    print(f"\n  📊 Descargadas: {downloaded} | Ya existían: {exists} | Errores: {errors}")
    return downloaded, exists, errors

def main():
    """
    Función principal
    """
    print("="*60)
    print("🖼️  DESCARGA DE IMÁGENES FALTANTES")
    print("="*60)

    # Directorios prioritarios a descargar
    directories = [
        ("gfx", "Gráficos compartidos (raíz)"),
        ("ll/gfx", "Les Luthiers - Gráficos"),
        ("lbe/gfx", "La Banda Elástica - Gráficos"),
        ("hca/gfx", "Humor con Achís - Gráficos"),
        ("ve/gfx", "Veladas - Gráficos"),
        ("ocho/gfx", "Offside - Gráficos"),
        ("hg/gfx", "Homenaje a Gershwin - Gráficos"),
        ("ladm/gfx", "Los animales de la música - Gráficos"),
        ("dtodo/gfx", "De todo como en botica - Gráficos"),
        ("rr/gfx", "Realizaciones recientes - Gráficos"),
        ("d2", "Diseño v2 (assets)"),
    ]

    total_downloaded = 0
    total_exists = 0
    total_errors = 0

    for dir_path, section_name in directories:
        d, e, err = process_directory(dir_path, section_name)
        total_downloaded += d
        total_exists += e
        total_errors += err

    # Resumen final
    print("\n" + "="*60)
    print("📊 RESUMEN FINAL")
    print("="*60)
    print(f"✓ Descargadas: {total_downloaded}")
    print(f"⊘ Ya existían: {total_exists}")
    print(f"✗ Errores: {total_errors}")
    print(f"📁 Ubicación: {OUTPUT_DIR}")
    print("\n✅ Proceso completado")

if __name__ == "__main__":
    main()
