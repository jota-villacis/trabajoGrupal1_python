# 1.Definir un listado de 5 productos con su respectivo valor unitario 
listado_productos = dict(producto1=100, producto2=200, producto3=300, producto4=400, producto5=500)
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

9) Eliminar un producto
0) Terminar Compra
    
'''
)
# Control de excepcion en opción del menú
while True:   
    try:
        seleccion_producto = int(input("Seleccione el número de la opción del producto a comprar: "))
        break
    except ValueError:
        print("Opción ingresada no valida, vuelva a ingresarla opción")

seleccion_cantidad_producto = []

while seleccion_producto != 0:
    
    seleccion_producto = int(input("Seleccione el número de la opción del producto a comprar: "))

    if seleccion_producto == 1:
        seleccion_cantidad_producto = int(input("Ingrese la cantidad de productos1 que llevara: "))
        total_producto1 = seleccion_cantidad_producto * listado_productos["producto1"]
        compra_cliente.append(total_producto1)
        print(compra_cliente)
        
    elif seleccion_producto == 2:
        seleccion_cantidad_producto = int(input("Ingrese la cantidad de productos2 que llevara: "))
        total_producto2 = seleccion_cantidad_producto * listado_productos["producto2"]
        compra_cliente.append(total_producto2)
        print(compra_cliente)
    
    elif seleccion_producto == 3:
        seleccion_cantidad_producto3 = int(input("Ingrese la cantidad de productos3 que llevara: "))
        total_producto3 = seleccion_cantidad_producto3 * listado_productos["producto3"]
        compra_cliente.append(total_producto3)
        print(compra_cliente)

    elif seleccion_producto == 4:
        seleccion_cantidad_producto4 = int(input("Ingrese la cantidad de productos4 que llevara: "))
        total_producto4 = seleccion_cantidad_producto4 * listado_productos["producto4"]
        compra_cliente.append(total_producto4)
        print(compra_cliente)   

    elif seleccion_producto == 5:
        seleccion_cantidad_producto5 = int(input("Ingrese la cantidad de productos5 que llevara: "))
        total_producto5 = seleccion_cantidad_producto5 * listado_productos["producto5"]
        compra_cliente.append(total_producto5)
        print(compra_cliente)

    elif seleccion_producto == 0:
        print("Compra terminada")
        valor_neto = sum(compra_cliente)

    else:
        print('Opción no válida')

# 3.Se deberá mostrar en pantalla el total de la suma del pedido el que corresponde al valor neto
print(f'El valor neto de la compra es de: {valor_neto}')

# 4.Se deberá mostrar en pantalla el total del IVA (19%) del total de pedido ingresado
valor_iva = valor_neto * iva / 100
print(f'El valor del iva del producto es de: {valor_iva}')

# 5.Se deberá mostrar en pantalla el total final del pedido (la suma del valor neto + IVA)
total_pedido = valor_neto + valor_iva
print(f'El total de la compra es de: {total_pedido}')



''' 

Extras:

1. Eliminar un producto ya seleccionado
2. Crear un login para ingresar al menu 

'''