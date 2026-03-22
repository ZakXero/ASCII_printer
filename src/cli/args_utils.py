#!/usr/bin/env python3


# Importación de librerías externas
import subprocess
import re
import argparse


##############################################################################################
####                                 UTILIDADES PARA args.py                              ####
##############################################################################################


class ArgsUtils:

    def __init__(self):
        pass

    # Obtener la última tag del commit
    def get_last_tag(self):
        """
        Obtener la tag del commit actual de trabajo, que se va actualizando con los commit que van pasando.

        :return tag:
        """
        try:
            tag = subprocess.check_output(
                ["git", "describe", "--tags", "--abbrev=0"],
                stderr=subprocess.STDOUT
            ).decode().strip()
            return tag
        except Exception:
            return "0.0.0"  # fallback si no hay tags

    # Obtener la branch actual de trabajo
    def get_current_branch(self):
        """
        Obtener la rama actual de trabajo del repositorio Git.

        :return branch:
        """
        try:
            branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                stderr=subprocess.STDOUT
            ).decode().strip()
            return branch
        except Exception:
            return "unknown-branch"

    # Verificación del MAC si es válida
    def mac_type(self, value):
        """
        Verificación de la MAC ,si es válida.

        :param value: MAC cual válida.
        :return value:
        """
        # REGEX MAC
        MAC_RE = re.compile(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$')

        if not MAC_RE.match(value):
            raise argparse.ArgumentTypeError(f"Invalid MAC address: {value}")
            # raise self.logger.error("Invalid MAC address")
        return value

    # Verificación de la IP si es válida
    def ip_type(self, value):
        """
        Verificación de la IP, si es válida.

        :param value: IP cual válidar.
        :return value:
        """
        # REGEX IP
        # IP_RE = re.compile(r'^((0?\d?\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(0?\d?\d|1\d\d|2[0-4]\d|25[0-5])$')        # Esta REGEX permite tener 001.001.001.001 ,tener ceros ala izquierda.
        IP_RE = re.compile(
            r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$')  # Esta REGEX es la común utilzada por lo programas, la que no tiene ceros ala izquierda, por motivos de ambiguedad. Si se pone esta var no hace falta importar ningun modulo.

        if not IP_RE.match(value):
            raise argparse.ArgumentTypeError(f"Invalid IP address: {value}")

        return value