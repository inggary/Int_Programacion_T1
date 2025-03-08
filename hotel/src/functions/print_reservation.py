from src.functions.utilidades import mensaje_menu
from src.db.base_datos import personas, horario, reservaciones, restaurates

def print_reservation():

    restaurante = mensaje_menu("Cual seria su restaurate: ", restaurates)
    restaurante = int(input(restaurante))-1
    restaurante = restaurates[restaurante]

    if(len(reservaciones[restaurante])!=0):

        horario1 = [x for x in reservaciones[restaurante] if(x['horario']=='6-8pm')]
        horario2 = [x for x in reservaciones[restaurante] if(x['horario']=='8-10pm')]

        print(f'Estas son las reservaciones para este restaurante {restaurante}')

        print('horario 6-8pm:')
        if(len(horario1)>0):
            for x in horario1:
                print(f'{x['nombre']} - {x['cantidad_personas']} personas')
        else:
            print("Esta vacio, el horario")

        print('horario 8-10pm:')
        if(len(horario2)>0):
            for x in horario2:
                print(f'{x['nombre']} - {x['cantidad_personas']} personas')
        else:
            print("Esta vacio, el horario")
    else:
        print("Esta vacio")
