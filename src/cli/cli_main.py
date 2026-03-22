#!/usr/bin/env python3

from src.config.logging import LoggingSetup
from src.cli.args import ParserBuilder
from src.cli.handler import HandlerArgs

# Importación de librerías externas
import sys


##############################################################################################
####                               INICIADOR DEL PROGRAMA                                 ####
##############################################################################################


def main():
    """Función donde se inicia todos los procesos para ejecutar el programa correctamente."""
    # Iniciar el logging sin args (OPCIONAL)
    setup_logging = LoggingSetup()
    logger = setup_logging.setup_logging()

    # Llamar al constructor de parsers
    parser_builder = ParserBuilder()
    # Construir parser del archivo args.py
    parser = parser_builder.create_parser()

    # Si no hay argumentos, mostrar help general
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    # Parsear args SOLO UNA VEZ
    args = parser.parse_args()

    # Iniciar el logging con args
    setup_logging = LoggingSetup(args=args)
    logger = setup_logging.setup_logging()

    # Llamar a handlers.py
    handler = HandlerArgs(
        logger=logger,
        parser=parser,
        args=args
    )

    # Procesamos los argumentos con las funciones correspondientes
    handler.handler()


# Iniciado de la clase main_central
if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    except KeyboardInterrupt:
        print(f"\nInterrumpiendo el programa...\n")
        sys.exit(1)