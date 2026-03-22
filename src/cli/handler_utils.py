#!/usr/bin/env python3


# Importación de librerías externas
import sys


##############################################################################################
####                                 UTILIDADES PARA handlers.py                          ####
##############################################################################################


class HandlersUtils:

    def __init__(self, logger, parser, args):
        # Obtener logger real de main.py
        self.logger = logger

        # Obtener argumentos de main.py
        self.args = args
        # Obtener el parser de main.py
        self.parser = parser

    ##############################################################################################
    ####                                     FUNCIONES EXTRA                                  ####
    ##############################################################################################

    # Verificación de los comandos de los args requeridos para su uso
    def verify_commands_args_need(self, required_args: list[str] | dict, commands_use):
        """
        Verificación de la ejecución de los comandos con sus argumentos requeridos y comando que se utiliza en el momento de ejecución.

        :param required_args: Lista de argumentos necesarios.
        :type required_args: list[str]
        :param commands_use: Comando en el cual se está utilizando esta función, para mostrar en pantalla en caso de error.
        :type commands_use: func get_current_arg_dest()
        """
        # Lista de args faltantes
        missing = []
        # Por cada dest en los args requeridos
        for dest in required_args:
            # 1. Verificar si el dest existe en el parser
            if not self.dest_exists(dest):
                # Si te da este error revisa que no estes añadiendo un arg inexistente en la parte de self.args, cuando defines lo que hace un arg.
                self.logger.error(f"El argumento requerido '{dest}' no existe en wifi_parser.")
                sys.exit(1)  # Cambiar por un raise sí funciona igual

            # 2. Obtener el valor real del argumento
            value = getattr(self.args, dest, None)

            # 3. Si el usuario NO lo pasó
            if value in (None, False):
                missing.append(dest)

        # Si faltan argumentos requeridos
        if missing:
            formatted = self.format_requerid_args(missing)
            self.logger.error(f"Para {commands_use} faltan: {', '.join(formatted)}")
            sys.exit(1)

    # Verificar si un dest existen en el parser de wifi_parser
    def dest_exists(self, dest):
        """
        Verificación si existe un dest, si no devuelve `False`

        :param dest: El nombre que se le pone cuando define el arg en el helper dest=

        :return True: Sí existe.
        :return False: Sí no existe.
        """
        # Por cada acción  dentro de wifi_parser
        for action in self.parser._actions:
            # Sí la acción tiene un dest, devuelve True
            if action.dest == dest:
                return True
        # Sí no, devuelve False
        return False

    # Formateo de los argumentos restantes para su uso
    def format_requerid_args(self, requerid_args):
        """
        Formateo de los argumentos requeridos para su uso por los comandos requeridos.

        :param requerid_args: Argumentos que se requieren para su uso.

        :return formatted:
        """
        formatted = []
        # Por cada dest dentro de los args requeridos
        for dest in requerid_args:
            # Obtener Flags del dest del args, uqe se utiliza en el momento de la llamada a la función
            flags = self.get_flags_for_args_dest(dest)
            # Sí hay flags
            if flags:
                # Versión corta del arg
                short = next((f for f in flags if f.startswith('-') and not f.startswith('--')), None)
                # Versión larga del arg
                long = next((f for f in flags if f.startswith('--')), None)
                # Añadir ala lista vacía de args la versión corta o larga
                formatted.append(short or long)
            else:
                # Añadir ala lista vacía de args el dest puesto en la definición del arg en el helper
                formatted.append(dest)
        # Devuelve la lista de args
        return formatted

    # Obtener el dest del argumento actual en uso en este momento
    def get_current_arg_dest(self):
        """
        Devuelve un `string` de `get_flags_for_dest` y formatea, añadiendo "short arg / long arg "

        :return short arg / long arg:
        """
        # Obtener los args en uso, cuando se ejecuta el programa
        argv = sys.argv
        # Por cada acción dentro del parser de wifi
        for action in self.parser._actions:
            # Saltar argumentos sin flags (posicionales)
            if not action.option_strings:
                continue

            # Si alguna de sus variantes aparece en sys.argv -> el usuario la pasó
            for flag in action.option_strings:
                # Si hay algúna flag en el arg en uso
                if flag in argv:
                    # Convertir lista de flags en string separado por " / "
                    return " / ".join(action.option_strings)

        return None

    # Obtener las flags del dest que se le pase
    def get_flags_for_args_dest(self, dest):
        """
        Obtener flags crudas del dest(arg) que se le pasan, para su posterior uso en `get_current_arg_dest`

        :return dest del arg en su ejecución:
        """
        # Por cada acción dentro de las acciones de wifi_parser
        for action in self.parser._actions:
            # Si la acción del dest es igual al dest que se le pasa
            if action.dest == dest:
                # Devuelve las opciones de la acción
                return action.option_strings
        # Devuelve una lista vacía
        return []

    # Obtener todas las flags válidas del wifi_parser
    def get_all_valid_flags_from_wifi_parser(self):
        """
        Obtener todas las flags válidas de wifi_parser

        :return flags:
        """
        # Lista de flags vacía
        flags = []
        # Por cada acción en las acciones de wifi_parser
        for action in self.parser._actions:  # Posible fallo
            # Añadir las opciones de cada acción ala lista de flags
            flags.extend(action.option_strings)
        # Devuelve la lista de flags
        return flags

    # Obtener todas las flags válidas del parser
    @property
    def get_all_valid_flags(self):
        """
        Obtener todas las flags válidas de parser

        :return flags:
        """
        # Lista de flags vacía
        flags = []
        # Por cada acción en las acciones de parser
        for action in self.parser._actions:
            # Añadir las opciones de cada acción ala lista de flags
            flags.extend(action.option_strings)
        # Devuelve la lista de flags
        return flags

    # Detectar si un arg es inválido por su flag cuando no existen, que se compara con todas las flags obtenidas en get_all_valid_flags
    def detect_invalid_flags(self):
        """
        Detecta las flags inválidas dentro de los requerid_args, para saber si se ponen mal los args o no existen los args.

        :return invalid:
        """
        # Ver los argumentos que se utilizan en el momento
        argv = sys.argv
        # Validar si las flags que hay son válidas
        valid_flags = self.get_all_valid_flags
        # Lista de args inválido
        invalid = []

        for arg in argv:
            # Solo mirar flags (empiezan por -)
            if arg.startswith('-') and arg not in valid_flags:
                # Añadir el arg inválido a la lista
                invalid.append(arg)
            # Solo mirar flags (empiezan por --)
            if arg.startswith('--') and arg not in valid_flags:
                # Añadir el arg inválido a la lista
                invalid.append(arg)
        # Devuelve los args inválidos
        return invalid

