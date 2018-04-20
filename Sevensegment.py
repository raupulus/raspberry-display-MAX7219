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

    def __init__(self, c=1, p=0, d=0):
        self.serial = spi(port=p, device=d, gpio=noop())
        self.device = max7219(self.serial, cascaded=c)
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

    def mostrarMensajeFlotante(self, txt, delay=1):
        """
        Muestra un mensaje como animación recorriendo la pantalla de forma que
        entra por la derecha y sale por la izquierda, útil cuando no cabe al
        completo el texto por ser un mensaje largo conviertiéndolo previamente
        a mayúsculas.
        :param txt: Texto a mostrar por la pantalla
        :param delay: Tiempo entre carácteres para desplazar el mensaje
        """
        width = self.device.width
        padding = " " * width
        txt = padding + txt.upper() + padding
        n = len(txt)

        print("Mostrando mensaje:\n"+txt)

        virtual = viewport(self.device, width=n, height=8)
        sevensegment(virtual).text = txt
        for i in reversed(list(range(n - width))):
            virtual.set_position((i, 0))
            time.sleep(delay)

ss = Sevensegment()

ss.fecha()
sleep(2)

ss.hora()
sleep(2)

ss.mostrarMensajeFlotante('HOLA ESTO ES UN MENSAJE CON UNA LONGITUD SUPERIOR '
                          'AL DE LA PANTALLA')
sleep(2)
