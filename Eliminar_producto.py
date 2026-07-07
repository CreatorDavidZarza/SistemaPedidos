from os import remove, rename
from validaciones import pedir_entero


def eeliminar_producto():
    print("\n==============================")
    print("     ELIMINAR PRODUCTO")
    print("==============================")

    # Mostrar productos
    archivo = open("productos.txt", "r")

    print(f"\n{'ID':<5}{'PRODUCTO':<25}{'PRECIO':<12}{'STOCK'}")
    print("-" * 50)

    id_producto = archivo.readline().strip()

    while id_producto != "":
        nombre = archivo.readline().strip()
        precio = archivo.readline().strip()
        stock = archivo.readline().strip()

        print(f"{id_producto:<5}{nombre:<25}${precio:<11}{stock}")

        id_producto = archivo.readline().strip()

    archivo.close()

    # Pedir ID a eliminar
    id_eliminar = pedir_entero("\nIngrese el ID del producto a eliminar: ")

    archivo = open("productos.txt", "r")
    auxiliar = open("auxiliar.txt", "w")

    encontrado = False

    id_producto = archivo.readline().strip()

    while id_producto != "":
        nombre = archivo.readline().strip()
        precio = archivo.readline().strip()
        stock = archivo.readline().strip()

        if int(id_producto) != id_eliminar:
            auxiliar.write(id_producto + "\n")
            auxiliar.write(nombre + "\n")
            auxiliar.write(precio + "\n")
            auxiliar.write(stock + "\n")
        else:
            encontrado = True

        id_producto = archivo.readline().strip()

    archivo.close()
    auxiliar.close()

    remove("productos.txt")
    rename("auxiliar.txt", "productos.txt")

    if encontrado:
        print("\nProducto eliminado correctamente.")
    else:
        print("\nNo existe un producto con ese ID.")