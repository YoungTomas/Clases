manzanas=20

while True:
    print("--- Venta de manzanas ---")
    print("1) Comprar manzanas")
    print("2) Stock de manzanas")
    print("3) Salir de venta")

    opcion = int(input("Cual opcion desea elegir (1 a 3)??"))


    if(opcion == 1):
        cantidad_comprada = int(input("¿Cuantas manzanas quiere?"))
        manzanas = manzanas - cantidad_comprada
    elif(opcion == 2):
        print("La cantidad de manzanas que queda son ",manzanas)          
    elif(opcion == 3):
        print("Ha decidido salir, nos vemos!!")
        break  
    else:
        print("Debe elegir una opcion del menu") 



        AguasMinerales = 20          #Stock inicial de aguas minerales

while True:
    print("---Bienvenido a la tiendita del tio tomi---")
    print("1- Comprar Agua Mineral.")
    print("2- Stock de Aguas Minerales.")
    print("3- Salir de la tienda.")

    eleccion = int(input("Quiere Agüita?, o mejor le digo cuantas me quedan?, tambien puede salir con el 3."))

    if(eleccion == 1):
        comproagua = int(input("Cuantas botellas le doy vecino?."))
        AguasMinerales = AguasMinerales - comproagua
    elif(eleccion == 2):
        print("Mire caserito, me van quedando ", AguasMinerales, " botellas de agua mineral")
    elif(eleccion == 3):
        print("Vuelva pronto caserito, que tenga un buen dia.")
        break
    else:
        print("Debe elegir una opcion del menu, no sea malo vecino.")