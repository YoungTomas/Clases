###MENU DESPLEGABLE

Saldo = 100000
Saldo_nuevo = 0

while True: 
    print("Bienvenido a tu banca en línea")
    print("Seleccione una opción:")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero .")
    print("4. Salir")

    try:
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            print(f"Su saldo actual es: {Saldo}")
            
        elif opcion == "2":
            print("Depositar Dinero :")
            print("Ingese el monto del deposito :")
            Saldo_nuevo = int(input("Monto a depositar: "))            
        elif opcion == "3":
            print("Retirar Dinero :")
            print("Ingresa el monto a retirar :")
            Saldo_nuevo = int(input("Monto a retirar: "))
            break
        elif opcion == "4":
            print("Gracias por usar nuestro servicio. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese un número.")
 