import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time
import argparse
import sys

def descargar_imagen_alta_resolucion(url, carpeta_destino, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"No se pudo acceder a {url}")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        div_container = soup.find('div', class_='flex justify-between items-center')
        if div_container:
            img = div_container.find('img')
            if img and img.get('src'):
                img_url = img['src']
                num = url.strip('/').split('/')[-1]
                nombre_archivo = f"{carpeta_destino.split('/')[-1]}_{num.zfill(4)}.jpg"
                ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
                
                print(f"Descargando {nombre_archivo} desde {img_url}")
                img_response = requests.get(img_url, headers=headers)
                
                if img_response.status_code == 200:
                    with open(ruta_archivo, 'wb') as f:
                        f.write(img_response.content)
                    print(f"✓ Imagen guardada: {nombre_archivo}")
                    time.sleep(0.5)
                else:
                    print(f"✗ No se pudo descargar {nombre_archivo}")
            else:
                print(f"No se encontró la imagen en {url}")
        else:
            print(f"No se encontró el contenedor de la imagen en {url}")
                
    except Exception as e:
        print(f"Error descargando imagen: {str(e)}")

def obtener_total_imagenes(url, headers):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', class_='divide-gray-300')
        if div:
            texto = div.get_text()
            for palabra in texto.split():
                if palabra.isdigit():
                    return int(palabra)
    except Exception as e:
        print(f"Error obteniendo total de imágenes: {str(e)}")
    return 170

def validar_url(url):
    """Valida el formato de la URL y extrae el nombre de usuario"""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    if 'fapello.com' not in url:
        raise ValueError("La URL debe ser de fapello.com")
    
    # Eliminar trailing slash si existe
    url = url.rstrip('/')
    
    # Extraer el nombre de usuario
    username = url.split('/')[-1]
    
    return url, username

def descargar_imagenes(url_base, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    total_imagenes = obtener_total_imagenes(url_base, headers)
    print(f"Total de imágenes a descargar: {total_imagenes}")
    
    for num in range(1, total_imagenes + 1):
        try:
            url = f"{url_base}/{num}/"
            print(f"\nProcesando imagen {num} de {total_imagenes}")
            descargar_imagen_alta_resolucion(url, carpeta_destino, headers)
            
        except Exception as e:
            print(f"Error procesando imagen {num}: {str(e)}")
            continue

def main():
    parser = argparse.ArgumentParser(description='Descarga imágenes de fapello.com')
    parser.add_argument('url', help='URL del perfil (ejemplo: fapello.com/usuario o https://fapello.com/usuario)')
    parser.add_argument('-o', '--output', help='Carpeta de destino (opcional)')
    
    args = parser.parse_args()
    
    try:
        # Validar y formatear URL
        url_base, username = validar_url(args.url)
        
        # Determinar carpeta de destino
        carpeta_destino = args.output if args.output else f"{username}_images_hd"
        
        print("\n=== Iniciando descarga de imágenes ===")
        print(f"URL: {url_base}")
        print(f"Usuario: {username}")
        print(f"Carpeta destino: {carpeta_destino}\n")
        
        descargar_imagenes(url_base, carpeta_destino)
        
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDescarga interrumpida por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()