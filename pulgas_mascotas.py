while True:
    try:
        total_mascotas = int(input("Ingrese la cantidad de mascotas a registrar:"))
        break
    except:
        print("Error, debe ingresar un numero entero")

mascotas_medicamento = 0
mascotas_banio = 0
lista=[]
for i in range(total_mascotas): 
    
    nombre = input(f"Ingrese el nombre de la mascota {i+1} :")

    while True:
        try:
            pulgas = int(input(f"Ingrese la cantidad de pulgas que tiene {nombre} :"))  
            break
        except:
            print("Error, debe ingresar un numero entero para indicar la cantidad de pulgas")

    if(pulgas > 5):
        print("A",nombre," hay que darle un medicamento para las pulgas.")
        mascotas_medicamento = mascotas_medicamento + 1
    else:
        print("A",nombre," hay que bañarlo solamente.")  
        mascotas_banio = mascotas_banio + 1   




print("\n---- Resumen Final ----")
print("Mascotas que necesitan medicamente : ",mascotas_medicamento)
print("Mascotas que necesitan solo un baño :",mascotas_banio)