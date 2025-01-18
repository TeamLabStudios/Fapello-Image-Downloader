# Fapello Image Downloader

Un script en Python para descargar imágenes en alta resolución desde Fapello.com.

## Características

- Descarga automática de todas las imágenes de un perfil
- Descarga en alta resolución 
- Nombrado automático de archivos
- Gestión de errores
- Muestra progreso en tiempo real
- Permite especificar carpeta de destino
- Soporte para URLs con o sin https://

## Requisitos

pip install requests beautifulsoup4

## Uso

### Forma básica
python script.py fapello.com/usuario

### Con URL completa
python script.py https://fapello.com/usuario

### Especificando carpeta de destino 
python script.py fapello.com/usuario -o carpeta_destino

### Ver ayuda
python script.py --help

## Ejemplos

# Descargar imágenes del usuario "ejemplo"
python script.py fapello.com/ejemplo

# Descargar a una carpeta específica
python script.py fapello.com/ejemplo -o mis_descargas

## Estructura del directorio
📁 carpeta_destino/
  └── usuario_0001.jpg
  └── usuario_0002.jpg
  └── usuario_0003.jpg
  ...

## Opciones

| Opción | Descripción |
|--------|-------------|
| url | URL del perfil (requerido) |
| -o, --output | Carpeta de destino (opcional) |

## Errores comunes

- URL inválida: Asegúrate de que la URL sea de fapello.com
- Sin acceso: Verifica tu conexión a internet
- Descarga interrumpida: Usa Ctrl+C para detener la descarga de forma segura

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu característica
3. Commit tus cambios 
4. Push a la rama
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## Notas

- Respeta los términos de servicio del sitio web
- Usa el script de manera responsable
- Las descargas tienen pausas integradas para evitar sobrecarga del servidor

## Contacto

Para reportar bugs o sugerir mejoras, por favor abre un issue en el repositorio.

---
Nota: Este script es solo para fines educativos.
