import os
import time
from functions import *

menu_initial = [
'Validar servicio' ,
'Estado de la vpn' ,
'Conexión a Internet' ,
'Calibrar medidas' ,
'Configurar peso' ,
'Reinicio de puertos' ,
'Revision de camara Externa' ,
'Update CubiQ',
'Salir'
]

error_list = [
  'Item no existe en el menu'
]

def salir():
  print('gracias')

def print_menu(title, menu):
  i=1
  clean()
  title()
  for x in menu:
    print(f'{i}. {x}')
    i = i+1

def error(item):
  return(error_list[item])