#Ejercicio 1##

milista = ["Ana", "Luis", "Carlos", "Marta"]
for name in milista:
    print (f"Hola {name} como estas?")

#Ejercicio 2##
total = 0
milista_2 = [25, 25, 25, 25]
for suma in milista_2: 
    total = total + suma
print (f"El total es {total}")

#Ejercicio 3##

valor = int(input("Ingrese un valor: "))
while valor < 0:
    print ("El valor tiene que ser positivo")
    valor = int(input("Ingrese un valor: "))
print (f"Good, {valor}")

#Ejercicio 4##

milista_3 = [1, 2, 3, 4, 5]
for i in milista_3: 
    print (f"Estamos Contando : ", (i))


#Ejercicio 5##
try:
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    resultado = num1 / num2
    print (f"El Resultado es: {resultado}")
except ZeroDivisionError as nodivideporcero:
    nodivideporcero = str("No se puede dividir por cero")
    print (f"Error: {nodivideporcero}")    

















##Gracias profe###

