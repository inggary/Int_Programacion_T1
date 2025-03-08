from src.functions.utilidades import mensaje_menu
from src.db.base_datos import personas, horario, reservaciones, restaurates

def make_reservation():

    nombre = input("Digame su nombre: ")
    cantidad_personas = input("Cuantas personas: ")

    restaurante = mensaje_menu("Cual seria su restaurate: ", restaurates)
    restaurante = int(input(restaurante))-1
    restaurante = restaurates[restaurante]


    horario_user = mensaje_menu("Que horario: ", horario)
    horario_user = int(input(horario_user))-1
    horario_user = horario[horario_user]

    contar = 0

    for x in reservaciones[restaurante]:
        if(x["horario"]==horario_user):
            contar+=1

    if(contar>=2):
        print("No se puede hacer reservas")
    else:
        reservaciones[restaurante].append({
            "nombre" : nombre,
            "cantidad_personas" : cantidad_personas,
            "horario": horario_user
        })
        print("Se guardo correctamente")



