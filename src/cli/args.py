#!/usr/bin/env python3


# Importación de librerías externas
import argparse


class ParserBuilder:

    def __init__(self):
        # Iniciamos el parser
        self.parser = argparse.ArgumentParser(
            description="ASCII Banner",
            parents=[self.add_common_args(), self.add_help_args(), self.add_ascii_banner_args()],
            add_help=False,
            formatter_class=argparse.RawTextHelpFormatter  # Añadir formateo de texto al helper
        )

    # Crear el parser principal
    def create_parser(self):
        """
        Creación del parser

        :return self.parser:
        """
        # Devolvemos self.parser
        return self.parser

    # Añadir argumentos al help principal
    def add_help_args(self):
        """
        Añadir argumentos al panel de help principal.

        :return self.parser:
        """
        # Parser para el help
        help_parser = argparse.ArgumentParser(add_help=False)

        # ARGUMENTOS HELP PRINCIPAL

        # Añadir argumento -h / --help con mensaje personalizado.
        help_parser.add_argument(
            "-h", "--help",
            action="help",
            help="Show ASCII Banner help and exit.\n\n"
        )

        # Añadir arg --version al solo parser principal
        help_parser.add_argument(
            "--version",
            help="Show program's tag version number and exit.\n\n",
            action="store_true",
            dest="version"
        )

        # Añadir arg --version-all al solo parser principal
        help_parser.add_argument(
            "--version-all",
            help="Show file run program's, branch actual work, tag number and exit.\n\n",
            action="store_true",
            dest="version_all"
        )

        # Devolver el parse de los args de help principal
        return help_parser

    # Añadir argumentos comunes
    def add_common_args(self):
        """
        Añadir argumentos comunes al todos los panels de help.

        :return common_parser:
        """
        # Parser de Common para su posterior integración en parents de wifi_subparsers
        common_parser = argparse.ArgumentParser(add_help=False)

        # Grupo de comunes
        common_group = common_parser.add_argument_group("Common options")

        # ARGUMENTOS COMUNES

        # Verbose
        common_group.add_argument(
            "-v", "--verbose",
            help="Increment output verbosity.\n\n",
            action="store_true",
            dest="verbose"
        )

        # Quiet
        common_group.add_argument(
            "-q", "--quiet",
            help="Quiet output verbosity.\n\n",
            action="store_true",
            dest="quiet"
        )

        # Devolver el parse de los args comunes
        return common_parser

    # Parser principal de ant
    def add_ascii_banner_args(self):
        ##############################################################################################
        ####                                 GRUPO ANT                                            ####
        ##############################################################################################

        # Parser de Utils para su posterior integración en parents de wifi_subparsers
        ascii_parser = argparse.ArgumentParser(add_help=False)

        # Añadir grupo de argumentos Utils args
        ascii_group = ascii_parser.add_argument_group("ASCII Banner options")

        # ARGUMENTOS ASCII BANNER

        # Imprimir texto ASCII en pantalla
        ascii_group.add_argument(
            "-p", "--print",
            help="Print ASCII text in terminal.\n\n",
            type=str,
            metavar="TEXT",
            dest="print"
        )

        # Elegir la fuente de texto ASCII
        ascii_group.add_argument(
            "-f", "--font",
            help="Choose font ASCII text.\n\n",
            type=str,
            metavar="FONT",
            dest="font"
        )

        # Elegir el color texto ASCII
        ascii_group.add_argument(
            "-c", "--color",
            help="Choose color ASCII text.\n\n",
            type=str,
            metavar="COLOR",
            dest="color"
        )

        # Devolvemos el subparser de ant_parser
        return ascii_parser
