entradas = 20          #Stock inicial
eleccion = 0
devolucion = 0
comproentradas = 0

while True:
    print("---Bienvenido a Fantasilandia---")
    print("1- Stock de Entradas.")
    print("2- Comprar Entradas.")
    print("3- Devolver Entradas.")
    print("4- Salir de la tienda online.")

    try:     
        eleccion = int(input("Hola, Que desea hacer; comprar, hacer devolucion o salir del sistema? :"))
    except TypeError:
        print("Ingrese un numero valido.\n")
    except ValueError:
        print("Ingrese un numero valido.\n")
    if eleccion == 1:
            print(f"En este Momento me quedan, {entradas} \n")
    elif eleccion == 2:
        while True:
                try:
                    if entradas == 0:
                        print("Lo siento, NO QUEDA STOCK.")
                        break
                    comproentradas = int(input("Cuantas entradas desea llevar?:"))
                    if comproentradas > entradas or comproentradas < 0:
                        print(f"No tengo tantas entradas, me quedan: {entradas} entradas al ¨Parque")
                    elif comproentradas == 0:
                         print("Tiene que llevar Minimo 1 .")
                    else:
                        print(f"Gracias por su compra de  {comproentradas} entradas.")
                        entradas = entradas - comproentradas
                        print(f"Me quedan {entradas} entradas al Parque .")
                        break
                except ValueError:
                    print("Ingrese un numero valido.\n")  
    elif eleccion == 3:
        while True:
            try: 
                devolucion = int(input("Esta bien, Cuantas Entradas desea Devolver? :"))
                if devolucion <= 0:
                    print("Lo siento, no existen entradas al negativo.")
                else:
                    entradas = entradas + devolucion
                    print (f"Gracias por la Devolucion de {devolucion} entradas al Parque.")
                    break
            except ValueError:
                print("Lo siento, intente nuevamente.")  
    elif eleccion == 4:
        print("Gracias vuelva pronto.")
        break
    else:
        print("Debe elegir una opcion del menu.")