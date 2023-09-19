producto_1 = ["Producto 1", 300, 5]
producto_2 = ["Producto 2", 400, 4]
producto_3 = ["Producto 3", 500, 7]

def mostrar_productos():
    print(f'NOMBRE \t\t PRECIO \t STOCK')
    print(f'{producto_1[0]} \t {producto_1[1]} \t\t {producto_1[2]}')
    print(f'{producto_2[0]} \t {producto_2[1]} \t\t {producto_2[2]}')
    print(f'{producto_3[0]} \t {producto_3[1]} \t\t {producto_3[2]}')

def elegir_medio_pago(producto):
    while True:
        opcion_1 = input('''
Eliga el medio de pago
- Efectivo (E)
- Tarjeta debito (TD))
- Tarjeta credito (TC))
Opcion: ''')
        if opcion_1.lower() == 'e':
            recargo = 1.1
            print(f"En efectivo costara 10% mas, le saldra ${round(producto[1] * recargo)}")
            producto[2] -=1
        elif opcion_1.lower() == 'td':
            print(f"El pago con tarjeta debito le saldra ${round(producto[1])}")
            producto[2] -=1
        elif opcion_1.lower() == 'tc':
            descuento = 0.9
            print(f"El pago con tarjeta credito costara 10% menos, le saldra ${round(producto[1] * descuento)}")
            producto[2] -=1
        else:
            print('opcion incorrecta')
        return 
    
def agregar_stock():
    producto = input("\n -producto1 \n -producto2 \n -producto3 \n A cual producto quiere agregar stock?: ")
    if producto == "producto1":
        print ("Agregaste un articulo mas al producto 1")
        producto_1[2] +=1
    elif producto == "producto2":
        print ("Agregaste un articulo mas al producto 2")
        producto_2[2] +=1
    elif producto == "producto3":
        print ("Agregaste un articulo mas al producto 3")
        producto_3[2] +=1
    else:
        print ("No elegiste nada")

def cambiar_precio():
    producto = input("\n -producto1 \n -producto2 \n -producto3 \n A cual producto quiere cambiar el precio?: ")
    if producto == "producto1":
        precio_nuevo = float(input(f"Que precio nuevo quieres ponerle al {producto} ?: " ))
        producto_1[1] = precio_nuevo
    elif producto == "producto2":
        precio_nuevo = float(input(f"Que precio nuevo quieres ponerle al {producto} ?: " ))
        producto_2[1] = precio_nuevo
    elif producto == "producto3":
        precio_nuevo = float(input(f"Que precio nuevo quieres ponerle al {producto} ?: " ))
        producto_3[1] = precio_nuevo
    else:
        print ("No elegiste nada")


def consulta_stock():
    print(f'NOMBRE \t\t STOCK')
    print(f'{producto_1[0]} \t {producto_1[2]}')
    print(f'{producto_2[0]} \t {producto_2[2]}')
    print(f'{producto_3[0]} \t {producto_3[2]}')

def elegir_producto():
    while True:
        producto_comprar = input('\n -producto1 \n -producto2 \n -producto3 \n Elija el producto a comprar: ')
        if (producto_comprar) == "producto1":
            print ("Usted eligio el Producto 1")
            elegir_medio_pago(producto_1)
        elif producto_comprar == "producto2":
            print ("Usted eligio el Producto 2")
            elegir_medio_pago(producto_2)
        elif producto_comprar == "producto3":
            print ("Usted eligio el Producto 3")
            elegir_medio_pago(producto_3)
        else:
            print ("Opcion incorrecta")
        break
    

def menu_general():
    while True:
        opcion = input('''
Eliga una opcion
  1. Ver menu de productos
  2. Comprar un producto
    -  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock)
    -  Pagar con tarjeta debito (se debe descontar el stock)
    -  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock)
  3.  consultar productos y stock
  4.  agregar stock a los productos
  5.  cambiar el precio a los productos
  6.  Salir
Opcion: ''')
        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            elegir_producto()
        elif opcion == '3':
            consulta_stock()
        elif opcion == '4':
            agregar_stock()
        elif opcion == '5':
            cambiar_precio()
        elif opcion == '6':
            print("Hasta luego")
            break
        else:
            print('opcion incorrecta')