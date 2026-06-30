#FUNCIONES DE SEGURIDAD Y REUTILIZABLES#

def pedir_nombre():

    nombre = input("Ingrese el nombre del producto: ")

    while len(nombre) < 3:
        print("\nERROR: El nombre debe tener al menos 3 caracteres.")
        nombre = input("Ingrese el nombre del producto: ")

    return nombre

def pedir_entero(mensaje):

    numero = input(mensaje)

    while numero.isdigit() == False:
        print("\nERROR: Debe ingresar un número.")
        numero = input(mensaje)

    return int(numero)

def pedir_stock():

    stock = pedir_entero("Ingrese el stock del producto: ")

    while stock <= 0:
        print("\nERROR: El stock debe ser mayor que cero.")
        stock = pedir_entero("Ingrese el stock del producto: ")

    return stock