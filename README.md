# Arquitectura del Proyecto

El proyecto fue desarrollado utilizando una estructura modular, donde cada archivo tiene una única responsabilidad. Esta organización permite que el código sea más ordenado, reutilizable y fácil de mantener.

Actualmente la estructura del proyecto es la siguiente:

```text
SistemaPedidos/
│
├── main.py
├── Registrar_Nuevo_Producto.py
├── ver_productos.py
├── validaciones.py
├── productos.txt
├── README.md
└── .gitignore
```

## Responsabilidad de cada módulo

| Archivo | Función |
|----------|---------|
| **main.py** | Controla el flujo general del programa y administra el menú principal. |
| **Registrar_Nuevo_Producto.py** | Registra nuevos productos dentro del menú del local. |
| **ver_productos.py** | Lee el archivo de productos y muestra la información almacenada. Este módulo será reutilizado posteriormente dentro de la funcionalidad **Realizar Pedido**. |
| **validaciones.py** | Centraliza todas las validaciones utilizadas por el sistema para evitar repetir código. |
| **productos.txt** | Almacena permanentemente la información de todos los productos registrados. |

---

# Explicación del código

## Ciclo principal del sistema

Todo el funcionamiento del sistema comienza en **main.py**.

```python
opcion = 0

while opcion != 0:

    mostrar_menu()

    opcion = pedir_opcion_menu()

    if opcion == 1:
        realizar_pedido()

    elif opcion == 2:
        Registrar_Nuevo_Producto()
```

Este ciclo mantiene el programa en ejecución hasta que el usuario decide salir.

Después de ejecutar cualquier funcionalidad, el programa vuelve nuevamente al menú principal sin necesidad de reiniciarse.

---

## Función mostrar_menu()

```python
def mostrar_menu():

    print("==============================")
    print(" SISTEMA DE PEDIDOS")
    print("==============================")
    print("1 - Realizar pedido")
    print("2 - Registrar nuevo producto")
    print("3 - Modificar producto")
    print("4 - Eliminar producto")
    print("5 - Estadísticas")
    print("0 - Salir")
```

Esta función tiene únicamente la responsabilidad de mostrar el menú principal.

Separar el menú en una función permite reutilizar el mismo código cada vez que el programa vuelve al menú.

---

## Lectura de productos

Para recorrer todos los productos almacenados se utiliza una lectura anticipada.

```python
id_producto = fileobj.readline().strip()

while id_producto != "":

    nombre_producto = fileobj.readline().strip()
    precio_producto = fileobj.readline().strip()
    stock_producto = fileobj.readline().strip()

    print("ID:", id_producto)
    print("Producto:", nombre_producto)
    print("Precio:", precio_producto)
    print("Stock:", stock_producto)

    id_producto = fileobj.readline().strip()
```

La primera lectura obtiene el ID del primer producto.

Mientras exista un ID, el programa continúa leyendo el resto de los datos del producto.

Al finalizar cada iteración vuelve a leer el siguiente ID, permitiendo recorrer completamente el archivo hasta llegar al final.

---

## Generación automática del ID

Al registrar un nuevo producto, el sistema necesita generar un identificador único.

Para ello primero recorre completamente el archivo y conserva el último ID encontrado.

```python
ultimoid = int(ultimoid)
nuevoid = ultimoid + 1
```

De esta manera el nuevo producto siempre tendrá un identificador diferente sin que el usuario deba ingresarlo manualmente.

---

## Registro de un nuevo producto

Una vez obtenido el nuevo ID y solicitados los datos al usuario, el sistema escribe el nuevo registro al final del archivo.

```python
fileobj = open("productos.txt","a")

fileobj.write(str(nuevoid)+"\n")
fileobj.write(nuevoProd+"\n")
fileobj.write(str(precioProd)+"\n")
fileobj.write(str(stockProd)+"\n")

fileobj.close()
```

Se utiliza el modo `"a"` (append) para agregar información al final del archivo sin modificar los productos ya existentes.

---

## Validación del nombre

Todas las validaciones fueron agrupadas dentro del módulo **validaciones.py**.

Por ejemplo, para validar el nombre del producto:

```python
def pedir_nombre():

    nombre = input("Ingrese el nombre del producto: ")

    while len(nombre) < 3:
        print("ERROR: El nombre debe tener al menos 3 caracteres.")
        nombre = input("Ingrese el nombre del producto: ")

    return nombre
```

La función solicita el nombre del producto y verifica que tenga al menos tres caracteres.

Si el dato no cumple la condición, vuelve a solicitarlo hasta que sea válido.

---

## Validación de números enteros

Muchas partes del sistema necesitan solicitar números.

Para evitar repetir la misma lógica se creó una función reutilizable.

```python
def pedir_entero(mensaje):

    numero = input(mensaje)

    while numero.isdigit() == False:
        print("ERROR: Debe ingresar un número.")
        numero = input(mensaje)

    return int(numero)
```

Esta función garantiza que el dato ingresado sea numérico antes de devolverlo al programa.

Posteriormente es reutilizada por otras validaciones como precio, stock y opciones del menú.

---

## Validación del precio

```python
def pedir_precio():

    precio = pedir_entero("Ingrese el precio del producto: ")

    while precio <= 0:
        print("ERROR: El precio debe ser mayor que cero.")
        precio = pedir_entero("Ingrese el precio del producto: ")

    return precio
```

En este caso se reutiliza `pedir_entero()` para asegurar que el dato sea numérico y luego se verifica que el precio sea mayor que cero.

---

## Validación del stock

```python
def pedir_stock():

    stock = pedir_entero("Ingrese el stock del producto: ")

    while stock <= 0:
        print("ERROR: El stock debe ser mayor que cero.")
        stock = pedir_entero("Ingrese el stock del producto: ")

    return stock
```

La lógica es similar a la utilizada para el precio.

Se garantiza que el usuario ingrese un número entero positivo antes de registrar el producto.

---

## Organización de las validaciones

Todas las funciones de validación fueron agrupadas en un único módulo.

Actualmente el sistema utiliza:

- `pedir_nombre()`
- `pedir_entero()`
- `pedir_precio()`
- `pedir_stock()`
- `pedir_opcion_menu()`

Centralizar las validaciones evita repetir código y permite reutilizar las mismas funciones desde cualquier módulo del proyecto.

---

## Formato del archivo productos.txt

Cada producto ocupa cuatro líneas consecutivas dentro del archivo.

```text
1
Hamburguesa
8000
10
```

Cada línea representa un dato diferente:

| Línea | Información |
|--------|-------------|
| 1 | ID |
| 2 | Nombre |
| 3 | Precio |
| 4 | Stock |

Este formato facilita la lectura secuencial del archivo utilizando únicamente `readline()`, sin necesidad de estructuras de datos más avanzadas.
