from funciones import amigos

print("\nVerificar que dos números son amigos si su suma de divisores es la misma\n\n")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese segundo número: "))

es_amigo = amigos(a, b)

if es_amigo == True:

    print("\nSí! Los números", a, "y ", b, " son amigos!")

else: 
     print("\nNo! Los números", a, "y ", b, " NO son amigos!")