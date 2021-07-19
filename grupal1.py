'''
ACTIVAR ENTORNO VIRTUAL

Como buen desarrollador, para comenzar a poder trabajar de manera óptima, es necesario que debamos preparar las herramientas necesarias para inicializar nuestro proyecto, 
esto incluye tener ya nuestro editor de texto y la versión de Python disponible en nuestro equipo. Familiarizado ya con estos componentes debemos prepararnos en realizar las 
iguientes acciones, para simular la compra a través de una página web.

Creación de un entorno virtual
# virtualenv -p python3.9 venv3.9

Identificar la dirección de la carpeta donde están los archivos del entorno virtual.
# pwd

Activación del entorno virtual creado
# . "directorioProyecto"/bin/activate


PROYECTO GRUPAL 1

Como grupo, deberán definir un listado de 5 productos con su respectivo valor unitario.
Deberán crear un archivo .py el cual deberá solicitar ingresar una cantidad por cada producto
(definido de la lista).
Se deberá mostrar en pantalla el total de la suma del pedido el que corresponde al valor neto.
Se deberá mostrar en pantalla el total del IVA (19%) del total de pedido ingresado.
Se deberá mostrar en pantalla el total final del pedido (la suma del valor neto + IVA).

'''
# 1.Definir un listado de 5 productos con su respectivo valor unitario
listado_productos = dict(p1=100, p2=200, p3=300, p4=400, p5=500)
compra_cliente = []
iva = 19
# 2.Solicitar ingresar una cantidad por cada producto (definido de la lista)
print(
    '''\n..:: Menú Productos ::..\n
1) Producto1 - 100 c/u
2) Producto2 - 200 c/u
3) Producto3 - 300 c/u
4) Producto4 - 400 c/u
5) Producto5 - 500 c/u

0) Terminar Compra
'''
)
# Control de excepcion en opción del menú
while True:
    try:
        seleccion_producto = int(input("Ingrese opción: "))
        break
    except ValueError:
        print("Opción ingresada no valida, vuelva a ingresarla opción")

seleccion_cantidad_producto = []

while seleccion_producto != 0:
    while True:
        try:
            seleccion_producto = int(input("Ingrese opción: "))
            break
        except ValueError:
            print("Opción ingresada no valida, vuelva a ingresarla opción")
    if seleccion_producto == 1:
        seleccion_cantidad_p1 = int(input("Ingrese la cantidad de p1: "))
        total_p1 = seleccion_cantidad_p1 * listado_productos["p1"]
        compra_cliente.append(total_p1)
        print(compra_cliente)
    elif seleccion_producto == 2:
        seleccion_cantidad_p2 = int(input("Ingrese la cantidad de p2: "))
        total_p2 = seleccion_cantidad_p2 * listado_productos["p2"]
        compra_cliente.append(total_p2)
        print(compra_cliente)
    elif seleccion_producto == 3:
        seleccion_cantidad_p3 = int(input("Ingrese la cantidad de p3: "))
        total_p3 = seleccion_cantidad_p3 * listado_productos["p3"]
        compra_cliente.append(total_p3)
        print(compra_cliente)
    elif seleccion_producto == 4:
        seleccion_cantidad_p4 = int(input("Ingrese la cantidad de p4: "))
        total_p4 = seleccion_cantidad_p4 * listado_productos["p4"]
        compra_cliente.append(total_p4)
        print(compra_cliente)
    elif seleccion_producto == 5:
        seleccion_cantidad_p5 = int(input("Ingrese la cantidad de p5: "))
        total_p5 = seleccion_cantidad_p5 * listado_productos["p5"]
        compra_cliente.append(total_p5)
        print(compra_cliente)
    elif seleccion_producto == 0:
        print("Compra terminada")
        valor_neto = sum(compra_cliente)
    else:
        print('Opción no válida')
# 3.Mostrar en pantalla el valor neto del pedido
print(f'El valor neto de la compra es de: {valor_neto}')
# 4.Mostrar en pantalla el total del IVA (19%) del valor neto
valor_iva = valor_neto * iva / 100
print(f'El valor del iva del producto es de: {valor_iva}')
# 5.Mostrar en pantalla el total final(la suma del valor neto + IVA)
total_pedido = valor_neto + valor_iva
print(f'El total de la compra es de: {total_pedido}')
