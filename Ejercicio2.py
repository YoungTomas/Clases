from random import randint

num2 = int(input("Ingrese el rango inferior: "))
num1 = int(input("Ingrese el rango superior: "))

secret = randint(num2, num1)
intentos = 0

while intentos < 2:
    i1 = int(input("Vamos Adivinar el Numero :"))
    intentos += 1
    if i1 == secret:
        print ("Felicitaciones, Adivinaste el numero")
        break
    elif i1 < secret:
        print ("El numero es mayor")
    elif i1 > secret:
        print ("El numero es menor")
    if intentos == 1:
        intentos += 1
        print ("No adivinaste")
        i2 = int(input("Vamos Adivinar el Numero :"))
        if i2 == secret:
            print ("Felicitaciones, Adivinaste el numero")
            break
        elif i2 < secret:
            print ("El numero es mayor")
        elif i2 > secret:
            print ("El numero es menor")
    if intentos == 2:
        intentos += 1
        print (f"El numero es {secret + 1} o {secret - 2} o {secret}")
        i3 = int(input("Vamos Adivinar el Numero :"))
        if i3 == secret:
            print ("Felicitaciones, Adivinaste el numero")
            break
        elif i3 != secret:
            print (f"No adivinaste el numero este era {secret}")

            