
def mensaje_menu(titulo, lista):

  menu = titulo

  for indice in range(0, len(lista)):
    menu = menu + f'\n{indice+1}-{lista[indice]}'

  menu = menu + '\nColocar el numero: '
  return menu



