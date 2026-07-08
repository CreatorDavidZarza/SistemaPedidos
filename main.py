from Realizar_pedidos import ver_productos
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
    print("4 - ESTADISTICAS")
    print("5 - SALIR DEL PROGRAMA")

def main():

    opcion = 0

    while opcion != 5:

        mostrar_menu()

        opcion = int(input("\nSeleccione una opción: "))

        if opcion == 1:
            ver_productos()

        elif opcion == 2:
            agregar_productos()

        elif opcion == 3:
            eeliminar_producto()

        elif opcion == 4:
            stats()

        elif opcion == 5:
            print("\n prueba")

        else:
            print("\nOpción inválida.")

main()
