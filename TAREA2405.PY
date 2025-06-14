##EJERCICIOTIPOPRUEBA
while True:
    try:
        numeropersona = int(input("Ingrese la Cantidad de Participantes :"))
        break
    except ValueError:
        print ("Ingrese un numero entero.")


mayor65 = 0
menor65 = 0


for i in range(numeropersona):
    
    nombre= input("Ingrese el nombre de la Persona :")
    while True:
        try:
            edad = int(input(f"Ingrese la Edad de {nombre} :"))
            if edad >= 65:
                print ("Mayor de 65 años")
                mayor65 = +1
            elif edad < 65:
                print ("65 años o menos.")
                menor65 = +1            
            break
        except ValueError:
            print("Ingrese una edad entera.")
        
print(f"La cantidad de participantes mayores de 65 años es {mayor65}, \n y la cantidad de personas menores de 65 años es {menor65}.")
