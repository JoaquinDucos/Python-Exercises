'''
-----------------------------------------------------------

Práctica

-----------------------------------------------------------

from cmath import log
from math import exp, log, pi
import math

x = int(exp(2 * log(3)))
print (x)

y = round(4 * math.sin (3 * pi / 2))

print (y)

z = abs(math.log10(.01) * math.sqrt(25))

print(z)

v = round(3.21123 * math.log10(100), 3)

print(v) 

-----------------------------------------------------------

GUIA 2

-----------------------------------------------------------
## EJ 1

x = int(input("Inserte el valor del lado de un cuadrado: "))

x = 4 * x

print (x)
 -------------------------------------------------------
## EJ 2

ladoMayor = float(input("Ingrese el lador mayor del rectángulo: "))
ladoMenor = float(input("Ingrese el lado menor del rectángulo: "))

perimetro = ladoMayor * 2 + ladoMenor * 2

print("El perimetro es ", + perimetro)

area = ladoMayor * ladoMenor

print("El área del rectángulo es de ", + area)

------------------------------------------------------------------------
## EJ 3

base = float(input("Ingrese el valor de la base del triángulo: "))

altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura)/2

print ("El area del triángulo es ", area) 

----------------------------------------------------------------------
## EJ 4

k = int(input("Introduzca su capital inicial: "))
i = float(input("Introduzca la tasa de interés: "))
n = int(input("Introduzca la cantidad de períodos: "))

IF = k * ((i + 1) ** n)

print("El capital obtenido es de:  ", IF)

----------------------------------------------------------------------
## EJ 6

nombre = str(input("Introduce el nombre de una persona para que se repita 1000 veces: "))

repeticion = (nombre + ' ') * 1000

print(repeticion)

----------------------------------------------------------------------- 
## EJ 7  GUía 3

num1 = float(input("ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Respuesta:")

print("El primer número es impar y el segundo par: ", bool(float(num1%2 != 0 and num2%2 == 0)))
print("La suma de ambos número es par: ", bool(float((num1 + num2) %2 == 0 )))
print("El primer número al cuadrado es menor que el segundo número: ", bool(float(num1 ** 2 < num2)))
print("Los dos números son iguales: ", bool(float(num1 == num2)))
print("El primero es divisible por tres y el segundo divisible por 5: ", bool(float(num1 % 3 == 0 and num2 % 5 == 0)))

-----------------------------------------------------------------------'''
## EJ 8

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

if num1 > num2 and num1 > -1:
   print("num1 es positivo")



