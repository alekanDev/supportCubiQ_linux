from menus import *
from titles import *
from functions import *

def start_app():
  option = 0
  while(option != 9):
    try:
      print_menu(title_support , menu_initial)
      option = int(input('\nIngresar valor: '))
      if(type(option) == int):
        execut(menu_initial[option])
    except:
      option = validate_error(option)
      time.sleep(1)
      
  clean()
  title_exit()