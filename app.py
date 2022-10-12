from menus import *
from titles import *
from functions import *

def validate_int(value):
  if(type(value) == int):
    return value
  else:
    return 0

def start_app():
  option = 0
  while(option != 9):
    try:
      print_menu(title_support , menu_initial)
      option = int(input('\nIngresar opcion: '))
      validate_int(option)
      state_cubiq = execut(menu_initial[option])
      # print(state_cubiq)
      if(state_cubiq == 0):
        while(option != 0):
          try:
            print_menu(title_support, menu_run_cubiq)
            option = int(input('\nIngresar opcion: '))

            option_run_cubiq = validate_int(option)

            if(option_run_cubiq == 0):
              option=0
            elif(option_run_cubiq == 1):
              execut(menu_run_cubiq[option])
            elif(option_run_cubiq == 2):
              execut(menu_run_cubiq[option])
            elif(option_run_cubiq == 3):             
              clean()
              title_exit()
              return
          except:
            option = validate_error(option)
            time.sleep(1)
      # elif(state_cubiq == 3):
      #   print(error_list.get(3))
      elif(state_cubiq == 9):
        return
    except:
      option = validate_error(option)
      print(option)
      time.sleep(1)
      
  clean()
  title_exit()