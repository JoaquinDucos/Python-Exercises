from funciones import amigos, todos_amigos

n = int(input(" \nIngrese un número para determinar todos los números amigos por debajo del mismo: "))
print("\nParejas de números amigos: ")
cont = todos_amigos(n)

print("\nCon un total de ", cont, " parejas de números amigos.\n")

