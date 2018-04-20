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
# Este script tiene como función mostrar ejemplos básicos de uso.

#######################################
# #       Importar Librerías        # #
#######################################
from Sevensegment import  Sevensegment
from time import sleep

#######################################
# #              SCRIPT             # #
#######################################

# Instancio la clase, sin parámetros
ss = Sevensegment()

# Ejemplo si tuviese dos pantallas en cascada
#ss = Sevensegment(c=2)

# Muestro la fecha
ss.fecha()
sleep(2)

# Muestro la hora
ss.hora()
sleep(2)

# Muestro un mensaje que entra por la derecha y sale por la izquierda
ss.mostrarMensajeFlotante('HOLA ESTO ES UN MENSAJE Largo', 0.4)
sleep(2)

# Muestro otro mensaje similar al anterior
ss.mostrarMensajeFlotante2('PRUEBA')
sleep(2)

# Muestro un mensaje fijo
ss.mostrar('HOLA')
sleep(2)

# Cambio a distintas opciones de brillo
ss.brillo(0)
sleep(1)
ss.brillo(5)
sleep(1)
ss.brillo(10)
sleep(1)
ss.brillo(15)
sleep(1)