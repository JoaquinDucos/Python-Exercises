from funciones import cuadratica

print("Ecuación: ax + b = 0")
print("Escribe los valores A y B para la ecuación cuadrática lineal: ")
a = float(input("\nIntroduce el valor A: "))
b = float(input("\nIntroduce el valor B: "))

print("La Expresión quedaría: ", a, "x + ", b, " = 0" )

x = cuadratica(a, b)

if x == None:
    print("La ecuación tiene infinitas soluciones o no tiene solución alguna.")
else:    
    print("La x es: ", x)