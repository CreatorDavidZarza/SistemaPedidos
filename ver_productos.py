def ver_productos():
    print("\n==============================")
    print("     SISTEMA DE PEDIDOS")
    print("==============================")
    fileobj = open("productos.txt","r")
    id_producto = fileobj.readline().strip() #.strip() elimina el salto de linea#
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
    input("\nPresione ENTER para volver al menú...")
