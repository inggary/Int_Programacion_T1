
from src.db.db import pizza
from src.functions.functions import mensaje_menu

menu = mensaje_menu('''Bienvenido a la pizzeria Bella Napoli
Por favor, seleccionar el tipo de pizza que desea:\n''',
                    [tipo_pizza['tipo'] for tipo_pizza in pizza] )
menu = int(input(menu))

if((menu<=len(pizza)) & (menu>=1)):

  menu_2 = mensaje_menu('Elegir el sabor: \n', pizza[menu-1]['sabores'])
  menu_2 = int(input(menu_2))

  if((menu_2<=len(pizza[menu-1]['sabores'])) & (menu_2>=1)):

    print(f'Su pizza sera "{pizza[menu-1]["tipo"]}" tendra el ingrediente: {pizza[menu-1]["sabores"][menu_2-1]}')

  else:
    print("Error")

else:
  print("Error")
