from os import remove, rename
from validaciones import pedir_entero


def realizar_pedido():
    numero_pedido = obtener_numero_pedido()
    total_pedido = 0
    continuar = 1
    while continuar == 1:
        print("\n==============================")
        print("     SISTEMA DE PEDIDOS")
        print("==============================")
        print("Número de pedido:", numero_pedido)

        fileobj = open("productos.txt", "r")
        id_producto = fileobj.readline().strip()

        while id_producto != "":
            nombre_producto = fileobj.readline().strip()
            precio_producto = fileobj.readline().strip()
            stock_producto = fileobj.readline().strip()

            print("ID:", id_producto)
            print("Producto:", nombre_producto)
            print("Precio: $", precio_producto)
            print("Stock:", stock_producto)
            print("---------------------------")

            id_producto = fileobj.readline().strip()

        fileobj.close()

        id_buscado = pedir_entero("\nIngrese el ID del producto: ")

        fileobj = open("productos.txt", "r")

        encontrado = False

        id_producto = fileobj.readline().strip()

        while id_producto != "":

            nombre_producto = fileobj.readline().strip()
            precio_producto = fileobj.readline().strip()
            stock_producto = fileobj.readline().strip()

            if int(id_producto) == id_buscado:

                encontrado = True

                print("\nProducto seleccionado:")
                print("ID:", id_producto)
                print("Producto:", nombre_producto)
                print("Precio: $", precio_producto)
                print("Stock:", stock_producto)

                cantidad = pedir_entero("\nIngrese la cantidad: ")

                while cantidad > int(stock_producto):
                    print("\nStock insuficiente.")
                    cantidad = pedir_entero("Ingrese otra cantidad: ")

                subtotal = cantidad * int(precio_producto)
                total_pedido = total_pedido + subtotal

                print("\nCantidad:", cantidad)
                print("Subtotal: $", subtotal)

                # Guardar pedido
                pedido = open("pedidos.txt", "a")

                pedido.write(str(numero_pedido) + "\n")
                pedido.write(str(id_producto) + "\n")
                pedido.write(str(cantidad) + "\n")
                pedido.write(str(precio_producto) + "\n")
                pedido.write(str(subtotal) + "\n")

                pedido.close()
                fileobj.close()
                print("\nPedido realizado con éxito.")

                # Actualizar stock
                archivo = open("productos.txt", "r")
                auxiliar = open("auxiliar.txt", "w")

                id_actual = archivo.readline().strip()

                while id_actual != "":

                    nombre = archivo.readline().strip()
                    precio = archivo.readline().strip()
                    stock = archivo.readline().strip()

                    if int(id_actual) == id_buscado:

                        nuevo_stock = int(stock) - cantidad

                        auxiliar.write(id_actual + "\n")
                        auxiliar.write(nombre + "\n")
                        auxiliar.write(precio + "\n")
                        auxiliar.write(str(nuevo_stock) + "\n")
                    else:

                        auxiliar.write(id_actual + "\n")
                        auxiliar.write(nombre + "\n")
                        auxiliar.write(precio + "\n")
                        auxiliar.write(stock + "\n")

                    id_actual = archivo.readline().strip()

                archivo.close()
                auxiliar.close()
               
                remove("productos.txt")
                rename("auxiliar.txt", "productos.txt")

                print("\nStock actualizado correctamente.")

                print("desea agregar otro producto? (1 - Sí, 2 - No)")
                continuar = pedir_entero("Ingrese su opción: ")
                while continuar != 1 and continuar != 2:
                  continuar = pedir_entero("Ingrese su opción: ")
                            
                break
            id_producto = fileobj.readline().strip()
        fileobj.close()

        if encontrado == False:
         print("\nNo existe un producto con ese ID.")
         continue

    print("\n==============================")
    print("PEDIDO FINALIZADO")
    print("==============================")
    print("Número de pedido:", numero_pedido)
    print("Total del pedido: $", total_pedido)
    input("\nPresione ENTER para volver al menú...")


def obtener_numero_pedido():
    fileobj = open("pedidos.txt", "r")

    numero_pedido = fileobj.readline().strip()
    ultimo_pedido = 0

    while numero_pedido != "":
        id_producto = fileobj.readline().strip()
        cantidad = fileobj.readline().strip()
        precio = fileobj.readline().strip()
        subtotal = fileobj.readline().strip()

        ultimo_pedido = numero_pedido
        numero_pedido = fileobj.readline().strip()

    fileobj.close()

    ultimo_pedido = int(ultimo_pedido)
    nuevo_pedido = ultimo_pedido + 1

    return nuevo_pedido