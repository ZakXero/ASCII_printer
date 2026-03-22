#!/usr/bin/env python3



# Renderizado del archivo en formato .flf
class FLFFont:
    """
    La clase FLFFont:

    1. Carga un archivo .flf desde disco.

    2. Valída el formato del archivo.

    3. Lee el header para obtener:

        - Altura de los caracteres (height)

        - Carácter hardblank interno (hardblank)

        - Líneas de comentario a ignorar

    4. Itera sobre los caracteres ASCII imprimibles (32-126) y:

        - Limpia los terminadores

        - Reemplaza hardblank por espacio

        - Guarda cada carácter como una lista de strings (glyph)

    5. Permite acceder a los caracteres para renderizar texto ASCII.
    """
    
    def __init__(self, path):
        """
        Inicializa una fuente FIGlet (.flf).

        :param path: Ruta al archivo de fuente .flf
        """
        # Guardar la ruta del archivo .flf
        self.path = path
        # Diccionario que contendrá las fuentes de texto
        self.font = {}
        # Altura de cada glyph(número de líneas verticales)
        self.height = 0
        # Carácter especial definido por FIGlet para representar espacios internos
        self.hardblank = " "
        # Cargar y proces el archivo de fuente
        self.load()


    def load(self):
        """
        Carga el archivo .flf, parsea su cabecera y construye los glyphs
        para cada carácter ASCII imprimible
        """
        # Abre el archivo .flf en modo lectura, y lee todas las líneas
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"File font not found: {self.path}")
        except UnicodeDecodeError:
            raise ValueError(f"Archivo {self.path} no es UTF-8 válido")

        # Validación del archivo que comprueba si es tiene el formato FIGlet correcto, si no lanza un error ValueError()
        if not lines or not lines[0].startswith("flf2a"):
            raise ValueError("Archivo FLF inválido: header incorrecto")

        # ---- PARSE HEADER ----
        # Primera línea del .flf -> contiene metadata del archivo FIGlet
        header = lines[0].rstrip("\n")
        # Divide en partes por espacios
        parts = header.split()

        # Leer parámetros importantes del header
        # Último carácter del identificador 'flf2aX' -> hardblank
        self.hardblank = parts[0][-1]
        # Altura de cada carácter ASCII
        self.height = int(parts[1])
        # Número de líneas de comentario después del header
        comment_lines = int(parts[5]) if len(parts) > 5 else 0

        # ---- COMENZAR DESPUÉS DE COMENTARIOS ----
        # Índice desde el cual comienzan los glyphs reales
        idx = 1 + comment_lines
        # Código inicial ASCII (espacio)
        ascii_code = 32  # espacio

        # ---- LEER GLYPHS ----
        # Leer los glyphs carácter por carácter
        # Itera por los carácteres imprimibles ASCII (32-126) 
        while ascii_code <= 126 and idx < len(lines):
            # Lista temporal que almacena las líneas del carácter actual
            glyph = []

            # Leer cada línea  del glyph, cada carácter tiene height líneas
            for _ in range(self.height):
                # Elimina salto de línea
                line = lines[idx].rstrip("\n")

                # Eliminar caracteres terminadores de FIGlet (@, $, #, etc.)
                while line and line[-1] in "@$#":
                    line = line[:-1]

                # Reemplazar hardblank por espacio real " "
                line = line.replace(self.hardblank, " ")
                # Añade la línea al glyph
                glyph.append(line)
                # Incrementa el idx(índice) para la siguiente línea
                idx += 1

            # Guardar el glyph en el diccionario:
            # clave = carácter ASCII
            # valor = lista de strings
            self.font[chr(ascii_code)] = glyph
            # Incrementa el ASCII code para pasar al siguiente carácter
            ascii_code += 1
