import os
import time

error_list = [
  'Item no existe en el menu'
]

def clean():
  os.system('clear')

def state_cubiq():
  state = os.system('pidof cubiq')
  if(state):
    return state
  else:
    return ('the service notFound')
  
def error(item):
  print(f'{error_list[item]}')
  time.sleep(0.8)
  return
