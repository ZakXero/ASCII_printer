#!/usr/bin/env python3

# Fuentes de tipo de letras ASCII disponible
from . import ascii_fonts      # Importar todas las fuentes disponibles en el archivo ascii_fonts.py

# Importación de librerías internas de Python
import os
import shutil



# Listar las fuentes disponibles en el directorio de las fuentes
def list_available_fonts(fonts_dir: str):
    """
    Devuelve una lista de nombres de fuentes disponibles (sin extensión).
    
    :param fonts_dir: Carpeta donde se encuentra las fuentes.

    :return fonts:
    """
    # Lista de fuentes vacía
    fonts = []
    # Por cada fuente que se encuentre dentro de la carpeta de fonts_dir
    for f in os.listdir(fonts_dir):
        # Buscar los archivos terminados en .flf
        if f.lower().endswith(".flf"):
            fonts.append(os.path.splitext(f)[0])
    # Devuelve las fuentes encontradas en la carpeta de fuentes
    return fonts



# Obtener el tamaño exacto de la pantalla para poder redimensionar el print de las letras según el tamaño actual de la pantalla
def get_terminal_width(default=80):
    """
    Obtener el tamaño exacto de la terminal en uso.
    
    :param default: Número de columnas por defecto.
    
    :return columns:
    """
    try:
        # Obtener el tamaño exacto actual de la terminal en uso
        return shutil.get_terminal_size().columns
    
    except Exception:
        # Devuelve default=80 sí falla
        return default