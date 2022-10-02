from funciones import bisiesto

año = int(input("Ingrese año para verificar si es bisiesto o no: "))

es_bisiesto, div = bisiesto(año)

print(bisiesto(año))

if es_bisiesto == True:

    if (div == 0) :

       print("El año", año, "tiene 366 días; ES bisiesto; porque es divisible por 4 y por 400, pero no por 100") 
    
    elif (div == 1):
        print("El año", año, "tiene 366 días; ES bisiesto; porque es divisible por 4, aunque no por 100 o 400") 


else:
    
    if (div == 2):
        print("El año", año, "tiene 365 días; No es bisiesto; Porque aunque es divisible por 4, tambien lo es por 100") 
    elif(div == 3):
     print("El año", año, "tiene 365 días; No es bisiesto; no es divisible por 4")


