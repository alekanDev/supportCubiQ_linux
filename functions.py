import os
import time
from menus import *

error_list = {
  0 : 'Caracter no identificado',
  1 : 'Item no existe en el menu',
  2 : 'Item negativo es incorrecto',
  3 : 'Por definir'
}

def clean():
  os.system('clear')

def state_cubiq():
  state = os.system('systemctl status cubiqagent | grep running')
  print(f'{state} and is type: {type(state)}')
  if('running' in state):
    return ('the service is 0k')
  else:
    return ('the service notFound')

def int_or_noInt(validate):
  if (type(validate) == int):
    return validate
  else:
    return 0

def execut(menu_option):
  if(menu_option == 'Validar servicio'):
    print(state_cubiq())
    time.sleep(1)

def validate_error(value):
  value = int_or_noInt(value)
  if(value == 0):
    print(error_list.get(value))
    # print_error(0)
  elif(value > 0):
    value = 1
    print(error_list.get(value))
    # print_error(1)
  elif (value < 0):
    value = 2
    print(error_list.get(value))
    # print_error(2)