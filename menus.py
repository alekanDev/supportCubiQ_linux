# coding=utf-8

import os
import time
from functions import *


menu_initial = {
  1 : 'Validar servicio',
  2 : 'Estado de la vpn' ,
  3 : 'Conexión a Internet' ,
  4 : 'Calibrar medidas' ,
  5 : 'Configurar peso' ,
  6 : 'Reinicio de puertos' ,
  7 : 'Revision de camara Externa' ,
  8 : 'Update CubiQ',
  9 : 'Salir'
}

error_list = [
  'Item no existe en el menu'
]

def salir():
  print('gracias')

def print_menu(title, menu):
  clean()
  title()
  for opc, val in menu.items():
    print(f'{opc}. {val}')

def error(item):
  print(f'{error_list[item]}')
  time.sleep(0.8)
  return