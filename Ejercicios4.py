from random import randint

inferior = int(input("Ingrese Desde que numero desea empezar :"))
superior = int(input("Ingrese Hasta que numero desea terminar :"))

numero = randint(inferior, superior)
flag = True
num_1 = 0
num_2 = 0
num_3 = 0   

print ("Tienes 3 intentos para adivinar el numero.")
num_1 = int(input("El numero es... :"))

if num_1 == numero:
    print ("Felicitaciones, adivinaste el numero!!!! y a la primera maquina.")
    flag = False

elif numero != num_1:
    print(f"el numero puede estar cerca de {inferior}")
elif num_1 < numero:
    print ("El numero es mayor...")
elif num_1 > numero:
    print ("El numero es menor..")


if  flag == True:
    num_2 = int(input("El segundo intento es... :"))
    if num_2 == numero:
        print ("Felicitaciones, adivinaste el numero ... al segundo intento.")
        flag = False
    elif num_2 < numero:
        print(f"El numero es mayor... puede estar entre {inferior} y {superior}")
    elif num_2 > numero:
        print ("El numero es menor..")
       
if flag == True:
    num_3 = int(input("La tercera es la vencida : "))
    if  num_3 == numero:
        print ("Felicitaciones, adivinaste el numero... a la tercera.")
    elif num_3 < numero:
        print ("El numero es mayor...\n y te quedaste sin intentos.")
    elif num_3 > numero:
        print ("El numero es menor...\n y te quedaste sin intentos.")