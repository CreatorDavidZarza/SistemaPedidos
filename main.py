from Realizar_pedidos import realizar_pedido
from Registrar_Nuevo_Producto import agregar_productos
from Eliminar_producto import eeliminar_producto
from Estadisticas import stats

def mostrar_menu():
    print("\n==============================")
    print("     BIENVENIDO A FOODTRUCK ")
    print("==============================")
    print("1 - Realizar pedido")
    print("2 - Registrar nuevo producto")
    print("3 - Eliminar producto")
    print("4 - Estadisticas")
    print("5 - SALIR DEL PROGRAMA")

def main():

    opcion = 0

    while opcion != 5:

        mostrar_menu()

        while True:
            try:
                opcion = int(input("\nSeleccione una opción: "))
                break
            except ValueError:
                print("\nOpción inválida.")

        if opcion == 1:
            realizar_pedido()

        elif opcion == 2:
            agregar_productos()

        elif opcion == 3:
            eeliminar_producto()

        elif opcion == 4:
            stats()

        else:
            print("\nOpción inválida.")

main()
