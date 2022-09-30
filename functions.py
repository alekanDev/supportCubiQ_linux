import os
import time

def clean():
  os.system('clear')

def state_cubiq():
  state = os.system('systemctl status cubiqagent | grep running')
  print(state)
  if(state == 'running'):
    return ('the service is 0k')
  else:
    return ('the service notFound')

def execut(menu_option):
  if(menu_option == 'Validar servicio'):
    print(state_cubiq())
    time.sleep(2)