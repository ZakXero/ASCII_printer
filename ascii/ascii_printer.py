#!/usr/bin/env python3

# Fuentes de tipo de letras ASCII disponible
from ascii_fonts import *     # Importar todas las fuentes disponibles en el archivo ascii_fonts.py
# Colores disponibles para las letras ASCII disponible
from ascii_colors import DEFAULT_COLORS, COLORS, RESET_COLOR     # Importar todas las fuentes disponibles en el archivo ascii_colors.py
# Importar el cargador de fuentes de letras con formato .flf
from flf_loader import FLFFont
# Importar el renderer, para procesar el texto que queremos imprimir en pantalla
from ascii_render import render_wrapped
# Importar la func de lista de fuentes disponibles
from ascii_utils import list_available_fonts

# Importar librerías internas de Python
import os


# Mostrar el Banner Principal del programa
def show_banner_initial():
    """
    Banner para el help principal del programa.

    :return banner: ascii_printer(text="TEXT", font_name="doom", color_name="green")
    """
    # Mensaje del programa al inicio
    banner = ascii_printer(text="TEXT", font_name="doom", color_name="green")
    # Devuelve el banner por default
    return banner


# Inyectar banner donde sea, se utiliza en el parser y subparser
def inject_banner(parser, banner_func):
    """
    Sobrescribe format_help() del parser para añadir un banner
    SOLO la primera vez que se llama (evita duplicados).

    :param parser: Instancia de argparse. ArgumentParser.
    :param banner_func: Función que devuelve el banner como string (si se utiliza ascii_printer(), hay que poner una `lambda delante` de la func.)
    """
    # Flag interno para evitar duplicados
    banner_printed = False
    # Guarda el formato original format_help() del parser, para no perder la funcionalidad original del help de argparse
    original_format_help = parser.format_help

    # Función que remplazará parser.format_help()
    def format_help_with_banner():
        # Permite modificar la variable del scope externo para controlar si ya se ha imprimido
        nonlocal banner_printed
        # Si no se ha imprimido
        if not banner_printed:
            # Lo marca como True
            banner_printed = True
            # Genera el banner en este momento, retrasando la ejecución hasta que realmente lo necesite, así se evita llamar más de una vez
            banner = banner_func()

        # Devolver el help original
        return f"\n{original_format_help()}" # \n es para separalo de la zona del usage:
    
    # Sobrescribe el método format_help() del parser con nuestra versión que inyecta el banner
    parser.format_help = format_help_with_banner



# Imprimir en pantalla letras ASCII
def ascii_printer(text: str, font_name=None, color_name=None):
    """
    Imprime texto ASCII usando la fuente seleccionada internamente.

    :param text: Texto a imprimir en ASCII por pantalla al user.
    :param font_name: Opcional, nombre de la fuente a usar.
    :param color_name: Opcional, nombre del color a usar.

    :return rendered:
    """ 
    # Carpeta donde están tus fuentes ASCII
    fonts_dir = "ascii_fonts/"

    # Búsqueda de fuentes disponibles
    available_fonts = list_available_fonts(fonts_dir=fonts_dir)
    

    # Si la fuente es None, por default elige una fuente
    if font_name is None:
        # Fuente de las letras ASCII
        font_file = os.path.join(fonts_dir, "epic.flf")  # default
    # Si se elige una fuente, buscar la fuente en concreto y verificar si existe
    else:
        # Construir ruta del archivo de fuente
        font_file = os.path.join(fonts_dir, f"{font_name}.flf")
        # Validar que exista
        if not os.path.isfile(font_file):
            # Elegir fuente por defecto
            print(f"[WARNING]: Fuente '{font_name}' no encontrada.")
            print(f"[WARNING]: Se usará la fuente por defecto 'epic'.\n")
            print("Fuentes disponibles:", ", ".join(available_fonts))
            # Fuente por defecto
            font_file = os.path.join(fonts_dir, "epic.flf")

    # Definir la fuente seleccionada o sí no la por defecto
    font = FLFFont(font_file)

    # Render sin color
    rendered = render_wrapped(text, font)

    # Colores internos
    color_key = (color_name or DEFAULT_COLORS).lower()
    # Obtener color en concreto
    color = COLORS.get(color_key, "")
    # Color reseteo
    reset = RESET_COLOR if color else ""
    

    # Aplicar color línea a línea
    for line in rendered.splitlines():
        print(f"{color}{line}{reset}")

    return rendered