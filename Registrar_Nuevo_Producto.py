from validaciones import pedir_nombre, pedir_entero, pedir_stock


def agregar_productos():
    print("\n==============================")
    print("     REGISTRAR NUEVO PRODUCTO")
    print("==============================")
    fileobj = open("productos.txt","r")
    id_producto = fileobj.readline().strip()
    ultimoid = 0
    while id_producto != '': 
        nombre_producto = fileobj.readline().strip()
        precio_producto = fileobj.readline().strip()
        stock_producto = fileobj.readline().strip()

        ultimoid = id_producto
        id_producto = fileobj.readline().strip()
    fileobj.close()
    ultimoid = int(ultimoid)
    nuevoid = ultimoid + 1
    print(f"\nID asignado automáticamente: {nuevoid}")
    nuevoProd = pedir_nombre()
    precioProd = pedir_entero("Ingrese el precio del producto: ")
    stockProd = pedir_stock()
    fileobj = open("productos.txt","a")
    fileobj.write(str(nuevoid)+"\n")
    fileobj.write(nuevoProd+("\n"))
    fileobj.write(str(precioProd)+"\n")
    fileobj.write(str(stockProd)+"\n")
    fileobj.close()
    print("\n====================================")
    print("Producto agregado correctamente.")
    print("====================================")
    print("ID:", nuevoid)
    print("Producto:", nuevoProd)
    print("Precio: $", precioProd)
    print("Stock:", stockProd) 
    input("\nPresione ENTER para volver al menú...")