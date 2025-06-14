
AguasMinerales = 20          #Stock inicial de aguas minerales
eleccion = 0


while True:
    print("---Bienvenido a la tiendita del tio tomi---")
    print("1- Stock de Aguas Minerales.")
    print("2- Comprar Agua Mineral.")
    print("3- Salir de la tienda.")

    try:
        
        eleccion = int(input("Quiere Agüita?, o mejor le digo cuantas me quedan?, tambien puede salir con el 3: "))
    except TypeError:
        print("Vecino ingrese un numero valido.\n")
    except ValueError:
        print("Vecino ingrese un numero valido.\n")
    if(eleccion == 1):
            print("Mire caserito, me van quedando ", AguasMinerales, " botellas de agua mineral\n")
    elif(eleccion == 2):
        while True:
                try:
                    if AguasMinerales == 0:
                        print("Lo siento caserito, no me quedan botellas de agua mineral, vuelva mas tarde.")
                        break
                    comproagua = int(input("Cuantas botellas le doy vecino?:"))
                    if comproagua > AguasMinerales or comproagua < 0:
                        print("No tengo tantas botellas, me quedan ", AguasMinerales, " botellas de agua mineral")
                    elif comproagua == 0:
                         print("Como no vay a llevar niuna, yapo no le de color.")
                    else:
                        print("Tome caserito, aqui tiene ", comproagua, " botellas de agua mineral.")
                        print("Gracias caserito.")
                        AguasMinerales = AguasMinerales - comproagua
                        print("Me quedan ", AguasMinerales, " botellas de agua mineral.")
                        break
                except ValueError:
                    print("Vecino ingrese un numero valido.\n")  
    elif(eleccion == 3):
        print("Vuelva pronto caserito, que tenga un buen dia.")
        break
    else:
        print("Debe elegir una opcion del menu, no sea malo vecino.")