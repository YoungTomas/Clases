
stock = 0
catalogo = {}
opcion = 0

def agregar():
    item = str(input("Ingrese el Productor que desea agregar :"))
    valor = int(input(f"Ingrese el Valor de {item} : "))
    catalogo[item] = valor
    print(f"Agregaste, {item}.")

def consultar():
    print("Aqui Tienes el Catalogo:")
    for item,valor in catalogo.items():
        print(f"{item} : ${valor}")

def quitar():
    item=input("Ingrese el producto a eliminar :")
    if item in catalogo:
        catalogo.pop(item)
        print("Eliminado.")
    else:
        print("El Producto no Existe.")

while True:
        
    print ("Bienvenido a la tiendita.")
    print ("1- Quieres Agregar productos?.")
    print ("2- Quieres ver el Catalogo.")
    print ("3- Quieres Sacar un producto?.")
    print ("4- Salir.")

    opcion = int(input("Ingrese la opcion :"))
    if opcion == 1:
        agregar()
    elif opcion == 2:
        consultar()
    elif opcion == 3:
        quitar()
    elif opcion == 4:
        break
    else:
        print("Seleccione una opcion Valida.")