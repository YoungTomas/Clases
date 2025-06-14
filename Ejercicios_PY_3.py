from random import randint

#numero = randint (1, 10)

#print ("EL NUMERO ES: ", numero)    


#from random import randint


#numero = randint (1, 10)
#numero_2 = randint (1, 10)

#result = numero + numero_2

#print (f"El resultado de {numero} mas {numero_2} es: {result}")

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
    print ("Felicitaciones, adivinaste el numero!!!!")
    flag = False
elif num_1 < numero:
    print ("El numero es mayor...")
elif num_1 > numero:
    print ("El numero es menor..")


if flag == True:
    if num_2 == numero:
        print ("Felicitaciones, adivinaste el numero!!!!")
        flag = False
elif num_2 < numero:
        print ("El numero es mayor...")
elif num_2 > numero:
        print ("El numero es menor..")
        flag = False
        print ("Felicidades, adivinaste el numero")

if flag == True:
    num_3 = int(input("La tercera es la vencida :\n"))
    if  num_3 == numero:
       print ("Felicitaciones, adivinaste el numero")
    elif num_3 < numero:
     print ("El numero es mayor...")
    elif num_3 > numero:
     print ("El numero es menor...")