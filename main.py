from Realizar_pedidos import ver_productos
from Registrar_Nuevo_Producto import agregar_productos

def mostrar_menu():
    print("\n==============================")
    print("     BIENVENIDO A FOODTRUCK ")
    print("==============================")
    print("1 - Realizar pedido")
    print("2 - Registrar nuevo producto")
    print("3 - Ver estadísticas")
    print("4 - Salir")

def main():

    opcion = 0

    while opcion != 4:

        mostrar_menu()

        opcion = int(input("\nSeleccione una opción: "))

        if opcion == 1:
            ver_productos()

        elif opcion == 2:
            agregar_productos()

        elif opcion == 3:
            print("\nOpción 3 seleccionada")

        elif opcion == 4:
            print("\nGracias por utilizar el sistema.")

        else:
            print("\nOpción inválida.")

main()