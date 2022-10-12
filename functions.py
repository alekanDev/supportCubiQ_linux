import os
import time
from menus import *

error_list = {
  0 : 'Caracter no identificado',
  1 : 'Item no existe en el menu',
  2 : 'Item negativo es incorrecto',
  3 : 'No existe el servicio',
  4 : 'Por definir'
}

def print_menu(title, menu):
  clean()
  title()
  for opc, val in menu.items():
    print(f'{opc}. {val}')

def clean():
  os.system('clear')

def state_cubiq():
  state = os.system('systemctl status cubiqagent | grep running')
  # state = 'Active: active (inactive) since Tue 2022-10-04 13:09:19 -05; 47min ago'
  # print(f'{state} y es de tip {type(state)} ')
  if(state == 256):
    print(error_list.get(3))
    time.sleep(1)
    return 0
  elif('running' in state):
    print('The service is running')
    return 1
  elif('inactive' in state):
    print("The service isn't running")
    return 0
  

def int_or_noInt(validate):
  if (type(validate) == int):
    return validate
  else:
    return 0


def execut(menu_option):
  if(menu_option == 'Validar estado del CubiQ'):
    state = state_cubiq()
    time.sleep(1)
    return state
  elif(menu_option == 'Iniciar proceso CubiQ'):
    os.system('sudo systemctl start cubiqagent')
  elif(menu_option == 'Validar estado del CubiQ'):
    state = os.system('systemctl status cubiqagent')
    time.sleep(1)
  elif(menu_option == 'Salir'):
    return

def validate_error(value):
  value = int_or_noInt(value)
  print(value)
  if(value == 0):
    print(error_list.get(value))
  if(value == 3):
    print(error_list.get(value))
  elif(value > 0):
    value = 1
    print(error_list.get(value))
  elif (value < 0):
    value = 2
    print(error_list.get(value))