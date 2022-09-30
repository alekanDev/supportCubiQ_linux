from menus import *
from titles import *
from functions import *

def start_app():
  option = 0
  while(option != 9):
    try:
      if(option < 0):
        option = 0
        error(0)
      elif(option < len(menu_initial)):
        print_menu(title_support , menu_initial)
        option = int(input('\nIngresar valor: '))
        if(type(option) == int):
          execut(menu_initial[option])
      elif(option>len(menu_initial)):
        option = 0
        error(0)
    except:
      option = 0
      error(0)
  clean()
  title_exit()
  time.sleep(1)
  clean()