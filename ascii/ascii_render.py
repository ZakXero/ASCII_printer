#!/usr/bin/env python3

# Importar utilidades de obtener el tamaño de ancho de la terminal en uso
from ascii_utils import get_terminal_width

# Utilizar en el README.md
"""
Este módulo renderiza texto ASCII usando fuentes FIGlet (.flf), adaptando dinámicamente la salida al ancho de la terminal del usuario. 
El sistema mide el ancho real de cada carácter y realiza un wrap automático sin romper los glyphs, garantizando una salida legible y consistente en cualquier entorno.
"""



# Aquí renderizamos el texto que le pasamos la font con formato .flf
def render_wrapped(text: str, font, spacing: int=1, max_width=None):
    """
    Renderizar texto ASCII usando una fuente `.flf`, respetando un ancho máximo, y haciendo `wrap automático` cuando se supera ese ancho, cuando se supera el máximo por línea hace un salto de línea.\n
    Convirtiendo así `texto` en `letras ASCII`.
    
    :param text: Texto plano cúal convertir en ASCII.
    :param font: Objeto FLFFont que contiene los glyphs.
    :param spacing: Espaciado entre letras ASCII.
    :param max_width: Ancho máximo permitido antes de hacer el wrap.

    :return "\\n".join(output):
    """
    # Si el máximo de anchura es None, obtiene la anchura actual de la terminal en uso.
    if max_width is None:
        max_width = get_terminal_width()

    # Altura de la fuente
    height = font.height
    # Fallback del espacio " " de la fuente
    space_glyph = font.font[" "]
    
    # Sirve para poder calcular los caracteres que caben en una sola línea en la terminal
    # Lista de bloques ya renderizados
    blocks = []
    # Bloque actual de construcción
    current_block = [""] * height
    # Ancho acumulado del bloque actual
    current_width = 0

    # Bucle principal cada carácter por carácter en el texto
    for ch in text:
        # Obtener el glyph, si existe lo usa, si no utiliza " "
        glyph = font.font.get(ch, space_glyph)
        # Calcular el ancho del glyph, busca la línea más larga del glyph y le suma espaciado entre letras
        glyph_width = max(len(line) for line in glyph) + spacing

        # ¿Cabe el siguiente carácter?, si no cabe, hace la parte de los blocks.
        if current_width + glyph_width > max_width:
            # Añadir a bloques el bloque actual 
            blocks.append(current_block)
            # Bloque actual de construcción
            current_block = [""] * height
            # Ancho acumulado del bloque actual
            current_width = 0

        # Concatena esa línea al bloque actual añade el espaciado. Así se construye el ASCII art línea por línea.
        for i in range(height):
            current_block[i] += glyph[i] + (" " * spacing)

        # Actualización del ancho acumulado, se actualiza para la siguiente iteración.
        current_width += glyph_width

    # Añadir último bloque, para evitar añadir bloques vacíos
    if any(line.strip() for line in current_block):
        # Añadir a bloques el bloque actual
        blocks.append(current_block)

    # Unir todos los bloques en línea, listo para imprimir por pantalla
    # Lista vacía de bloques
    output = []
    # Por cada bloque en los bloques
    for block in blocks:
        # Añadir bloque ala lista vacía 
        output.extend(block)

    # Devuelve el ASCII art como string multilínea.
    return "\n".join(output)



