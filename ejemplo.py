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
from Sevensegment import  Sevensegment
from time import sleep

#######################################
# #             Variables           # #
#######################################
ss = Sevensegment()

ss.fecha()
sleep(2)

ss.hora()
sleep(2)

ss.mostrarMensajeFlotante('HOLA ESTO ES UN MENSAJE Largo', 0.4)
sleep(2)

ss.mostrarMensajeFlotante2('PRUEBA')
sleep(2)

ss.mostrar('HOLA')
sleep(2)

ss.brillo(0)
sleep(1)
ss.brillo(5)
sleep(1)
ss.brillo(10)
sleep(1)
ss.brillo(15)
sleep(1)