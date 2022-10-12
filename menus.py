import os
import time
from functions import *


menu_initial = {
  1 : 'Estado del CubiQ',
  2 : 'Validar vpn' ,
  3 : 'Conexión a Internet' ,
  4 : 'Calibrar medidas' ,
  5 : 'Configurar peso' ,
  6 : 'Reinicio de puertos' ,
  7 : 'Revision de camara Externa' ,
  8 : 'Update CubiQ',
  9 : 'Salir'
}

menu_run_cubiq = {
  0 : 'Volver',
  1 : 'Iniciar proceso CubiQ',
  2 : 'Validar estado del CubiQ',
  3 : 'Salir'
}

def print_menu(title, menu):
  clean()
  title()
  for opc, val in menu.items():
    print(f'{opc}. {val}')
