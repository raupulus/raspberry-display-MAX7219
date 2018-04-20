# raspberry-MAX7219

Instalación y librerías personalizadas para display de 7 segmentos (8 dígitos) con el chip MAX7219 en Raspberry y Raspbian Estable

Esta herramienta facilita el acceso, instalación y manipulación de pantallas
con el chip max7219

## Instalar librerías en Raspbian desde PyPy
Para instalar la librería debemos tener instalado pip y python.

### Para python =2.7

```bash
sudo -H pip install --upgrade luma.led_matrix
```

### Para python >=3.4

```bash
sudo -H pip3 install --upgrade luma.led_matrix
```

Para otros modos de instalación o/y contemplar otros sistemas operativos
tendrás que consultar la fuente oficial del autor para la librería usada, esta
información la puedes encontrar un poco más abajo.


## Librería usada

https://github.com/rm-hull/luma.led_matrix


## Documentación de la librería oficial

https://luma-led-matrix.readthedocs.io/en/latest/api-documentation.html#module-luma.led_matrix.device
