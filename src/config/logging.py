#!/usr/bin/env python3


# Importación de librerías externas
import logging


##############################################################################################
####                                  INICIADOR DEL LOGGING                               ####
##############################################################################################


class LoggingSetup:
    def __init__(self, args=None):
        # Namespace de argparse parseado
        self.args = args

    # Iniciador del logging para mostrar mensajes al user por pantalla
    def setup_logging(self):
        """
        Configura el sistema de logging basado en los argumentos.

        Args:
        \t-v / --verbose
        \t-q / --quiet
        """
        # Determina el nivel de verbose
        if self.args:
            # Verbose
            if getattr(self.args, "verbose", False):
                level = logging.DEBUG
            # Quiet
            elif getattr(self.args, "quiet", False):
                level = logging.ERROR
            # Default
            else:
                level = logging.INFO
        # Default
        else:
            level = logging.INFO

        # Configuración de los mensajes que se imprime al user por pantalla
        logging.basicConfig(
            level=level,
            force=True,
            format="%(levelname)s: %(message)s"
        )

        return logging.getLogger("__name__")