from menus import *
from titles import *
from functions import *

def start_app():
  option = 0
  while(option != 9):
    if(option < len(menu_initial)):
      print_menu(title_support , menu_initial)
      option = int(input('\nIngresar valor: '))
      if(option ==type(int)):
        option_text = (menu_initial[option-1])
        print(option_text)
        time.sleep(1)
    elif(option>len(menu_initial)):
      option = 0
      error(0)
  
  clean()
  title_exit()
  time.sleep(1)
  clean()