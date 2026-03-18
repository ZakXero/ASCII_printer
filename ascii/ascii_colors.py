#!/usr/bin/env python3

"""
Colores ANSI para ASCII
Se acceden por nombre igual que las fuentes
"""


# Diccionario de los colores asignados a nombre
COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m"
}

# Color por defecto
DEFAULT_COLORS = "green"
# Color de reseteo
RESET_COLOR = "\033[0m"
