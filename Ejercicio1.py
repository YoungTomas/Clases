# Ejercicio 1
promedio_estudiante = float(input("Ingrese el promedio del estudiante : "))
quintil_economico = int((input("Ingrese el quintil economico del estudiante : ")))
arancel = 1800000
matricula = 90000
dscto_arancel = 0.0
dscto_matricula = 0.0 

if promedio_estudiante > 5.0 and promedio_estudiante <= 6.0:
    if quintil_economico == 1 or quintil_economico == 2:
        dscto_arancel = (0.10 * arancel) 
        print (f"El valor de su Arancel es  : {arancel - dscto_arancel}")
    elif quintil_economico == 3 or quintil_economico == 4:
        arancel = (0.13 * arancel)
        print (f"El valor de su Arancel es  : {arancel - dscto_arancel}")
elif promedio_estudiante > 6.0 and promedio_estudiante <= 7.0:
    if quintil_economico == 1 or quintil_economico == 2:
        dscto_arancel = (0.20 * arancel) 
        print (f"El valor de su Arancel es  : {arancel - dscto_arancel}")
    elif quintil_economico == 3 or quintil_economico == 4:
        dscto_arancel = (0.15 * arancel) 
        print (f"El valor de su Arancel es  : {arancel - dscto_arancel}")
elif promedio_estudiante <= 4.9:
    print ("No tiene derecho a descuento en el arancel")
    print (f"El valor de su Arancel es  : {arancel}")
    print (f"El valor de su Matricula es  : {matricula}")
    exit()
    
#
if quintil_economico == 1 or quintil_economico == 2  or quintil_economico == 3:
    dscto_matricula = 0.10
    if promedio_estudiante >= 5.5: 
        dscto_matricula = dscto_matricula + 0.05
        print (f"El valor de su Matricula es  : {matricula - (matricula * dscto_matricula)}")
elif quintil_economico == 4 or 5 and promedio_estudiante < 5.0:
    print (f"El valor de su Matricula es  : {matricula}")
    print (f"El valor de su Arancel es  : {arancel}")