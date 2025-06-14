precio = 1000
dscto = 0.0
kilos_manzana = float(input("Ingrese cuantos kg de Manzanas desea comprar: "))

if kilos_manzana >= 1.0  and kilos_manzana <= 5.0:
    precio= 1000 * 0.8 * kilos_manzana   #aplica 20% dscto
elif kilos_manzana >5 and kilos_manzana <= 10.0:
    precio = 1000 * 0.65 * kilos_manzana   #aplica 35% dscto
elif kilos_manzana > 10.1:
    precio = 1000 * 0.5 * kilos_manzana   #aplica 50% dscto

precio_oringinal = precio * kilos_manzana
monto_dscto = precio * dscto
precio_total = precio 

print("Resumen Compra ; \n kilos_manzana : ", kilos_manzana, "\n Precio Unitario : ", precio * kilos_manzana, "\n Precio Total : ", precio_total)

#usar el dscto al calculo del precio total


#
#
#
#
#