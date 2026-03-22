#!/usr/bin/env python3

from src.cli.args_utils import ArgsUtils
from src.cli.handler_utils import HandlersUtils
from src.ascii.ascii_printer import ascii_printer


# Importación de librerías internas de Python


##############################################################################################
####       PROCESAMIENTO DE LOS ARGUMENTOS PARA QUE HAGAN SUS FUNCIONES ASIGNADAS         ####
##############################################################################################


class HandlerArgs:

    def __init__(self, logger, parser, args):
        # Llamar a logging de main.py
        self.logger = logger

        # Llamar a create_parser
        self.parser = parser
        # Llamar a args de main.py
        self.args = args

        # Llamar a argsUtils
        self.args_utils = ArgsUtils()

        # Llamar a handlerUtils.py
        self.handlers_utils = HandlersUtils(
            logger=logger,
            parser=parser,
            args=args
        )

    def handler(self):
        # 0 - Verificación de argumentos si se pueden utilizar juntos o no
        # Añadir primero si los hay los args que no pueda utilizarse juntos

        # Verificar si --version y --version-all se utilizan juntos si es así que de error
        if getattr(self.args, "version", False) and getattr(self.args, "version_all", False):
            raise ValueError("You can't use --version and --version-all at the same time.")

        # Verificar si --verbose y --quiet se utilizan juntos si es así que de error
        if getattr(self.args, "verbose", False) and getattr(self.args, "quiet", False):
            raise ValueError("You can't use -v and -q at the same time.")

        # Verificar si el arg --version se ha ejecutado
        if getattr(self.args, "version", False):
            self.run_help_initial()

        # Verificar si el arg --version-all se ha ejecutado
        if getattr(self.args, "version_all", False):
            self.run_help_initial()

        # Verificar si el arg -p / --print se ha ejecutado
        if getattr(self.args, "print", False):
            self.run_ASCII()


    def run_help_initial(self):
        self.logger.debug("Ejecutando el HELP principal")

        try:
            # Version tag actual corta
            if self.args.version:
                # Obtener el arg que se está utilizando en este momento
                command_args_use = self.handlers_utils.get_current_arg_dest()
                # Verificación de los argumentos requeridos
                self.handlers_utils.verify_commands_args_need(
                    required_args=[],
                    commands_use=command_args_use
                )

                # Llamada al --version
                tag_version = f"Tag: {self.args_utils.get_last_tag()}"
                # Imprimir --version en pantalla
                print(tag_version)
                # Devolver la tag_version
                return tag_version

            # Version completa: nombre de archivo, rama de trabajo, tag actual
            if self.args.version_all:
                # Obtener el arg que se está utilizando en este momento
                command_args_use = self.handlers_utils.get_current_arg_dest()
                # Verificación de los argumentos requeridos
                self.handlers_utils.verify_commands_args_need(
                    required_args=[],
                    commands_use=command_args_use
                )

                # Llamada al --version-all
                tag_version_all = (
                    f"Archivo: {self.parser.prog}\n"
                    f"Branch: {self.args_utils.get_current_branch()}\n"
                    f"Tag: {self.args_utils.get_last_tag()}"
                )
                # Imprimir --version-all en pantalla
                print(tag_version_all)
                # Devolver la tag_version_all
                return tag_version_all

        except Exception as e:
            self.logger.error(f"Error en run_help_initial: {e}")
            raise


    def run_ASCII(self):
        """Ejecutar las funciones asociadas a los args de ant"""
        self.logger.debug("Ejecutando módulo ASCII")  # Solo para probar que se ejecuta, borrar antes de terminar el commit
        # Llamar funciones de los args del módulo ant aquí
        try:
            # Argumento -p / --print con las opciones disponibles para el texto ASCII
            if self.args.print:
                # Obtener el arg que se está utilizando en este momento
                command_args_use = self.handlers_utils.get_current_arg_dest()
                # Verificación de los argumentos requeridos
                self.handlers_utils.verify_commands_args_need(
                    required_args=[],
                    commands_use=command_args_use
                )
                # Imprimir ASCII Banner en pantalla
                ascii_printer(text=self.args.print, font_name=self.args.font, color_name=self.args.color)

        except Exception as e:
            self.logger.error(f"Error con run_ASCII: {e}")
            raise