#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @copyright  Copyright © 2018 Raúl Caro Pastorino
# @license    https://wwww.gnu.org/licenses/gpl.txt
# @email      tecnico@fryntiz.es
# @web        www.fryntiz.es
# @github     https://github.com/fryntiz
# @gitlab     https://gitlab.com/fryntiz
# @twitter    https://twitter.com/fryntiz

# Guía de estilos aplicada: PEP8

#######################################
# #           Descripción           # #
#######################################

#######################################
# #       Importar Librerías        # #
#######################################

## Librerías del sistema
import time  # Importamos la libreria time --> time.sleep
from datetime import datetime
import os  # Importamos la libreria para comandos de la consola/shell
import random  # Genera números aleatorios --> random.randrange(1,100)

## Librerías específicas
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment


#######################################
# #             Variables           # #
#######################################
sleep = time.sleep

#######################################
# #             Funciones           # #
#######################################


class Sevensegment:

    def __init__(self):
        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=1)
        self.seg = sevensegment(self.device)

    def fecha(self):
        """
        Muestra la fecha actual en el dispositivo
        """
        fecha_ahora = datetime.now().strftime('%d-%m-%y')
        self.seg.text = fecha_ahora

    def hora(self):
        """
        Muestra la hora actual
        """
        hora_actual = datetime.now().strftime('%H-%M-%S')
        self.seg.text = hora_actual


ss = Sevensegment()

ss.fecha()
sleep(2)

ss.hora()
sleep(2)

