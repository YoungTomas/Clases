#Ejercicio 1

print("Ingrese 5 numeros para realizar el calculo :\n")
num = int
suma = 0
for i in range(5):
    try:
        milista = [] 
        num = int(input("Ingrese los 5 numeros : "))
        milista.append(num)
        suma += num
    except ValueError:
            print("Debes ingresar solo valores numericos")
print(f"La suma de los numeros es : {suma}")

# #Ejercicio 2

# contador = 0
# milista1 = []
# while contador < 5:
#     for num1 in range(6):
#         if num1 > 0:
#             milista1.append(num1)
#             contador += 1
#             try: 
#                 num1 = int(input("Ingrese los 5 numeros POSITIVOS : "))
#                 contador += 1
#             except ValueError:
#                 print ("Debes ingresar solo valores numericos")
#         else:
#             num1 <= 0
#             print("Debe ingresar solo numeros positivos")
#             contador += 1
        
# print("El programa ha terminado, se acabaron los intentos")