from src.utils.textos import menu_principal
from src.functions.make_reservation import make_reservation
from src.functions.print_reservation import print_reservation
import os #importar libreria para borrar comandos de python

while(True):

    try:
        opcion = int(input(menu_principal))
    except:
        os.system('cls' if os.name == 'nt' else 'clear') #esto es para borrar los comandos anteriores de python
        print("Error: solo insertar numeros")
        continue
    os.system('cls' if os.name == 'nt' else 'clear') #esto es para borrar los comandos anteriores de python

    if(opcion==1):
        print('hacer reservacion')
        make_reservation()

    elif(opcion==2):
        print("ver reservacion")
        print_reservation()

    elif(opcion==3):
        print("Nos vemos!!!")
        break
    else:
        print("Error: numero incorrecto.")



