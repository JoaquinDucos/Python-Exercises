''' GUIA 3 
-----------------------------------------------------------------------------------
EJERCICIO 1 

num = float(input("Ingrese un número para verificar si es positivo o negativo: "))

if (num < 0):
    print("El número es negativo")
elif (num > 0):
    print("El número es positivo")
else:
    print("El 0 es neutro!")   

----------------------------------------------------------------------------------
EJERCICIO 2

edad1 = int(input("Ingrese la edad de la primer persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))

if (edad1 == edad2):
    print("Tienen la misma edad!")
    
elif (edad1 >edad2):
    print("La persona 1 es mayor que la persona 2")

else:
    print("La persona 2 es mayor que la persona 1")

------------------------------------------------------------------------------------
EJERCICIO 3

num = int(input("Ingrese un número entero: "))

if (num % 2 == 0):
    print("El numero es par!")
else:
    print("El numero es impar!")
------------------------------------------------------------------------------------
EJERCICIO 4

num_ent = int(input("Ingrese un número entero para determinar si es el doble de un número impar: "))

num_doble = int

if (num_ent % 2 >= 1 ):
     print("El número es impar, nunca va a ser doble de un número impar")

elif (num_ent % 2 == 0):
    num_doble = num_ent // 2
    
    if(num_doble % 2 >=1):
        print("El número", + num_ent, "es el doble de", + num_doble, "que es impar.") 
    else:
        print("El número", + num_ent, "es el doble de", + num_doble, "que no es impar.")        

------------------------------------------------------------------------------------
EJERCICIO 5  

num = int(input("Introduce la cantidad que quiera desglosar: €"))
cont = 0
if (num > 0) :

  if (num >= 500):
      cont = num // 500
      print(+ cont, "billetes de €500")        

      num = num % 500
      cont = 0

  if (num >= 200 and num < 500):
      cont = num // 200
      print(+ cont, "billetes de €200")        

      num = num % 200
      cont = 0

  if (num >= 100 and num < 200):
      cont = num // 100
      print(+ cont, "billetes de €100")        

      num = num % 100
      cont = 0    

  if (num >= 50 and num < 100):
      cont = num // 50
      print(+ cont, "billetes de €50")        

      num = num % 50
      cont = 0   
  
  if (num >= 20 and num < 50):
      cont = num // 20
      print(+ cont, "billetes de €20")        

      num = num % 20
      cont = 0  

  if (num >= 10 and num < 20):
      cont = num // 10
      print(+ cont, "billetes de €10")        

      num = num % 10
      cont = 0  

  if (num >= 5 and num < 10):
      cont = num // 5
      print(+ cont, "billetes de €5")        

      num = num % 5
      cont = 0      

  if (num >= 2 and num < 5):
      cont = num // 2
      print(+ cont, "monedas de €2")        

      num = num % 2
      cont = 0      

  if (num == 1):
      cont = num // 1
      print(+ cont, "moneda de €1")        

      num = num % 1
      cont = 0      
else :
    print("El número no puede ser negativo")      

--------------------------------------------------------------------------------
EJERCICIO 6

char = str(input("Introduce un caracter para saber si está en mayúscula o minúscula: "))

if (char >= chr(65) and char <= chr(90)):
    print("El caracter seleccionado está en mayúscula")

elif (char >= chr(97) and char <= chr(122)):
    print("El caracter seleccionado está en minúscula")    

else:
    print("El caracter seleccionado no es una letra y no puede ser mostrado en mayúscula")

---------------------------------------------------------------------------------

EJERCICIO 7

num = input("Ingresa un rango de 5 números para determinar cuál es el mayor: ")
numMayor = int(input("Ingresá otro número: "))
cont = 0
if (num >= chr(48) and num <= chr(57)):

 while(cont < 3) :
   num = int(input("Ingresa otro número: "))
   if(num > numMayor):
     numMayor = num
   else:
        num = numMayor
   cont +=1

 print("El mayor de los número es el", numMayor)

else: 
      print("El caracter introducido  no es un número, inténtelo nuevamente")
      print("")
      num = int(input("Ingresa un rango de 5 números para determinar cuál es el mayor: "))
      while(cont < 4) :
        num = int(input("Ingresa otro número: "))
        if(num > numMayor):
          numMayor = num
     
        cont +=1
     
      print("El mayor de los número es el", + numMayor)

otra manera de hacerlo: 

numMayor = int(input("Ingresa un rango de 5 números para determinar cuál es el mayor: "))
cont = 0


while ( cont <= 3):
    num =int(input("Ingresá otro número: "))
    if(num > numMayor):
        numMayor = num
    else:
        num = numMayor
    cont += 1
   
print("El mayor es el número:",numMayor)
---------------------------------------------------------------------------------

EJERCICIO 8  BIS



cont = 0
longMayor = 0
##print("La longitud desta palabra es de: ", len(s))
memoria = []

while(cont < 4) :
  ##s = str(input("Ingresa un rango de 5 palabras para determinar cuál es la de mayor longitud: "))
  s = str(input("Ingresa otra palabra: "))
  long = len(s)

  print("La longitud de esta palabra es de:", len(s))

  if(long > longMayor):
     sMayor = s
     longMayor = long
     memoria = [s]
  elif long == longMayor:
    memoria.append(s)
  print(memoria)
  cont +=1

print("La palabra de mayor longitud es: ", len(sMayor), "y la palabra es: ", memoria)

---------------------------------------------------------------------------------
EJERCICIO 8 Original

numMayor = input("Ingresa 5 palabras para ordenarlas alfabéticamente : ")
cont = 0

while ( cont <= 3):
    if(( (numMayor >= chr(65) and numMayor <= chr(90) ) or (numMayor >= chr(97) and numMayor <= chr(122)) )):
       num =input("Ingresá otra palabra: ")
       if(( (num >= chr(65) and num <= chr(90) ) or (num >= chr(97) and num <= chr(122)) )):
          
           if(ord(num)  < ord(numMayor)):
              numMayor = num
           else:
             num = numMayor
           cont += 1
       else:    
             print("No has ingresado una letra")
    else:
        print("No has ingresado una letra")

print("La primer palabra alfabéticamente ordenada es:",numMayor)

---------------------------------------------------------------------------------
EJERCICIO 9


num1 = int(input("Ingrese el primer número (entero) de los 5: "))
cont = 0

while(cont < 4):

    num2 = int(input("Ingrese otro número:"))

    if (num1 > num2):
        resto = num1 - num2
        
        if(resto <= numCercano ):
            numCercano = num2

    if (num1 < num2):
        resto = num2 - num1

        if(resto <= numCercano):
            numCercano = num2        

    cont += 1

print("El número más cercano al", num1, "es el", numCercano)           

---------------------------------------------------------------------------------

EJERCICIO 10

recup_a = 0
recup_b = 0
p_a = float(input("Ingrese la nota del primer parcial: "))

if (( p_a >= 0) and (p_a <= 10)):

    if(p_a < 5):
        recup_a += 1  

else:
    while( float(p_a) < 0 or float(p_a) > 10) :

       print("La nota cargada debe ser un entero en el rango de 1 a 10, pruebe nuevamente: ")
       p_a = int(input())  

       if(p_a < 5):
          recup_a += 1  

p_b = float(input("Ingrese la nota del segundo parcial: "))

if (( p_b >= 0) and (p_b <= 10)):

       if(p_b < 5):
         recup_b += 1       

else:
    while( float(p_b) < 0 or float(p_b) > 10) :

       print("La nota cargada debe ser un numero en el rango de 1 a 10, pruebe nuevamente: ")
       p_b = float(input())

    if(( p_b >= 0) and (p_b <= 10)):

       num_b = p_b

       if(p_b < 5):
         recup_b += 1  

if (recup_a != 0):
    print("Debe recuperatorio del primer parcial")
    recup_a = float(input("Introduzca nota de recuperatorio: "))

if (recup_b != 0):
    print("Debe recuperatorio del segundo parcial")     
    recup_b = float(input("Introduzca nota de recuperatorio: "))

if(recup_a == 0 and recup_b == 0):
    prom = (p_a + p_b) / 2

if(recup_a > 0 and recup_b == 0):
    prom = ( (0.25 * p_a) +(0.75 * recup_a) + p_b) / 2

if(recup_b > 0) and (recup_a == 0):
    prom = ( (0.25 * p_b) +(0.75 * recup_b) + p_a) / 2

print("Nota de cursada del alumno en números: ", prom)

if(prom == 9 or prom == 10):
 
    letra = 'A'

elif(prom >= 7 and prom < 9):

    letra = 'B'

elif(prom >= 5 and prom < 7):
   
    letra = 'C'

elif(prom >= 3 and prom < 5):

    letra = 'D'

elif(prom <= 3):
    
    letra = 'E' 

print("Nota de cursada del alumno en letra: ", letra)    

---------------------------------------------------------------------------------

EJERCICIO 11

num = int(input("Introduzca un número entero positivo: "))
cont = 0
suma = num
num_mayor = 0
num_menor = num

while(num > 1):

   if (num >= num_mayor):
    num_mayor = num

   if(num <= num_menor):
    num_menor = num

   num = int(input("Introduzca otro número: "))

   if(num > 1):
     suma += num

   cont += 1

print ("El mayor de los numeros ingresados es el", num_mayor, ", el menor es el", num_menor, "y el promedio total es de:", (suma / cont))   
---------------------------------------------------------------------------------

EJERCICIO 12
 
cont = 6

while (cont >= 6  and cont <= 150):
    if (cont % 6 == 0):
        num = cont
        print(num)
    cont += 1

---------------------------------------------------------------------------------

EJERCICIO 13

n = int(input("N: "))
m = int(input("M: "))
cont = n

while(cont>=n and cont <= (n*m)):
    if (cont % n == 0):
       num = cont
       print("Múltiplos de N entre N * M:", num)
    cont += 1

---------------------------------------------------------------------------------

EJERCICIO 14

cont = 20
potencia = 1
num = 2 ** potencia

while(num <= 230):
    num = 2 ** potencia
    if (num < 20): 
        num += 1

    elif ( num >= 20 and num <= 230):
        num_2 = num
        print("Número potencia de 2:", num_2)
    potencia += 1

---------------------------------------------------------------------------------

EJERCICIO 15

print("\n\n            INTRODUCE NÚMEROS PARA MOSTRARLOS EN PANTALLA\n")
print("Si desea salir del programa, introduzca un número negativo.\n")
print("-------------------------------------------------------------\n")
print("\nCOMIENZO DE PROGRAMA\n\n")
print("-------------------------------------------------------------\n\n")

num = float(input("Introduce un número: "))

while num > 0:
    num = float(input("\nIntroduce otro número: "))
    
---------------------------------------------------------------------------------

EJERCICIO 16


print("\n\n           CALCULAR SUMATORIA DE I = N HASTA M\n")
print("\n-------------------------------------------------------------\n")
print("\nCOMIENZO DE PROGRAMA\n\n")
print("-------------------------------------------------------------\n\n")

i = int(input("Introduce i: "))
m = int(input("Introduce M: "))
n = 1

while (n < m):
    i += i 
    n += 1

print("\nSumatoria de i =>", i, "\n\n")

---------------------------------------------------------------------------------

EJERCICIO 17

print("\n\n           CALCULAR FACTORIAL DE UN NÚMERO POSITIVO\n")
print("\n-------------------------------------------------------------\n")
print("\nCOMIENZO DE PROGRAMA\n\n")
print("-------------------------------------------------------------\n\n")

num = int(input("Introduce un número entero positivo: "))
cont = num
factorial = num
num1= num
while(cont > 0):
    num -= 1
    if(num > 0):
       factorial *= (num)
    cont -= 1

print("EL factorial de", num1, "es:", factorial)    

---------------------------------------------------------------------------------

EJERCICIO 18

print("\n\n           VISUALIZAR NÚMEROS PRIMOS ENTRE N Y M\n")
print("\n-------------------------------------------------------------\n")
print("\n             COMIENZO DE PROGRAMA\n")
print("\n-------------------------------------------------------------\n\n")

print("\nÚnicamente introducir números positivos!\n")

n = int(input("Introduce N: "))
m = int(input("Introduce M: "))

resto = 0
i = 0

if ( n > m or n < 0 or m < 0):
    while (n < 0 or m < 0):
        print("\nEl número introducido es negativo, introduce nuevamente los mismos.")
        n = int(input("Introduce N: "))
        m = int(input("Introduce M: "))

    while (n > m):
        print("\nEl número N es mayor a M, por favor introduce nuevamente los mismos.")
        n = int(input("Introduce N: "))
        m = int(input("Introduce M: "))

print("\nLista de números primos entre", n, "y", m, ":\n")

while ( i >= 0 and i <= n and n <= m):

    while (i <= n):
        
        if(i == 0):
            i = 1

        if(n % i == 0):
            resto += 1
        i += 1

    if (resto == 2):
        print(n)

    resto = 0    
    n += 1
    i = 1
print("\n \n            FIN DE PROGRAMA\n\n") 

---------------------------------------------------------------------------------

EJERCICIO 1 1er PARCIAL

num = int(input("Introduce un número positivo: "))
suma = 0
suma1 = 0
cont = 0

while ( num > 0):
    if (num / 10 > 1):

       while( num > 0):   

          suma = suma + (num % 10)
          num = num // 10   

       print("La suma de sus dígitos es: ",suma) 
       suma = 0
       num = int(input("Introduce otro número positivo: "))

    else:
        suma1 += num
        cont += 1
        num = int(input("Introduce otro número positivo: "))
    
print("promedio de números de un sólo dígito: ", suma1 / cont )      


EJERCICIO 4 GUÍA 5



n = int(input("Ingrese un número múltiplo de 5: "))
cont = 0

while (n >= 0):

   if (str(n) >= chr(48) and str(n) <= chr(57)): 

       while ( (n % 5) != 0 and n != -1):
           preg = input("El número ingresado no es múltiplo de 5, desea introducir otro? (S/N):")
           if (preg == chr(83)):
               n = int(input("Ingrese un número múltiplo de 5: "))
           elif (preg == chr(78)):
               print("Has escrito", cont, "números múltiplos de 5.\nFin del programa")
               n= -1
           else:
               print("El caracter ingresado no es una opción. Fin del programa")
               n = -1
       
       while ( (n % 5) == 0 ):
           print("Muy bien, el número", n, "es múltiplo de 5!")
           cont += 1
           preg = input("¿Quieres escribir otro número múltiplo de 5? (S/N): ")
           if (preg == chr(83)):
               n = int(input("Ingrese un número múltiplo de 5: "))
           elif (preg == chr(78)):
               print("Has escrito", cont, "números múltiplos de 5.\nFin del programa")
               n=-1
           else:
              print("El caracter ingresado no es una opción. FIN DEL PROGRAMA")
              n = -1   
   else:
        preg = input("El caracter ingresado no es un número desea introducir otro? (S/N):")
        
        if (preg == chr(83)):
               n = int(input("Ingrese un número múltiplo de 5: "))
        elif (preg == chr(78)):
               n= -1

---------------------------------------------------------------------------------

EJERCICIO 19

n = int(input("Ingrese N: "))
m = int(input("Ingrese M: "))

i = 1
cont = 0

p = 0
dist = 0
distMin = m

print("Los números primos entre N y M son: ", end="")
while ( n <= m):

    while (i <= n):

        if( n % i == 0):

            cont += 1

        i += 1

    if (cont == 2):
    
        dist = n - p

        if (dist <= distMin):
            distMin = dist  
            
        p = n 

        print(p, end=",")
    
    n += 1
    i = 1
    cont = 0

print("\nLa distancia mínima entre dos números primos adyacentes es de: ", distMin, "números")

---------------------------------------------------------------------------------

EJERCICIO 20


n = int(input("Ingrese el primer rango de valores: "))
m = int(input("Ingrese el segundo rango de valores: "))

num = int(input("Ingrese el tercer valor a determinar: "))   
if n > m or m < n:
    while ( (n > m) ):
        num = int(input("El valor de N es mayor a M"))
    while ( (m < n) ):
        num = int(input("El valor de M es menor a N"))     


elif n < m:  
   if num < n or num > m:

       while (num < n or num > m):
            num = int(input("El valor ingresado no se encuentra dentro del rango establecido, vuelva a introducir otro número"))
   
   if (num >= n and num <= m):
         print("El valor se encuentra dentro del rango de números!")


---------------------------------------------------------------------------------


num1 = int (input ('ingrese primer numero'))
num2= int (input ('ingrese segundo numero'))
divisor1 = 1
divisor2 = 1
suma1_divisores = 0
suma2_divisores = 0
    
while num1 > divisor1:

    while num1 % divisor1 == 0:

        suma1_divisores = suma1_divisores + divisor1
    
    divisor1 += 1
       
while num2 > divisor2:

    while num2 % divisor2 == 0:

        suma2_divisores = suma2_divisores + divisor2
    
    divisor2 += 1
        
      
if suma1_divisores == num2:
    print( num1, 'y', num2, 'son amigos.')
elif (suma2_divisores == num1):
    print( num1, 'y', num2, 'son amigos.')
    
else:
    print (num1, 'y', num2, 'no son amigos.')

---------------------------------------------------------------------------------

 EJERCICIO 7

cant_num = int(input("Cuántos números desea introducir?:" ))

while cant_num <= 0:
    cant_num = int(input("Cuántos números desea introducir?; no 0:"))

num = int(input("Inserte un número:"))
mayor = num 
menor = num
promedio = 0
contador = 1 
suma_num = 0  

while cant_num > contador:
    num = int(input("Inserte un número:"))
    
    if num > mayor:
        mayor = num

    if num < menor:
        menor = num

    contador += 1
    suma_num += num
    promedio = suma_num / contador

print ("mayor: ", mayor) 
print ("menor: ", menor)   
print ("promedio: ", promedio)

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

GUIA 5

---------------------------------------------------------------------------------

EJERCICIO 1 


cant_num = int(input("Cuántos números desea introducir?:" ))

while cant_num <= 0:
    cant_num = int(input("Cuántos números desea introducir?; no 0:"))

negativo= 0
suma_num = 0  
contador = 0

while cant_num > contador:
    num = int(input("Inserte un número:"))
    
    if num < 0:
        negativo += 1
    contador += 1

print ("Hay:", negativo, "números negativos" )

---------------------------------------------------------------------------------

EJERCICIO 3 

num = (int(input("Introduce un número entero mayor que 0: ")))

fact = 1
print("El factorial de", num, end=" es: ")

if num > 0:
    while(num > 1):
       fact *= num
       num -= 1
print(fact)


---------------------------------------------------------------------------------

EJERCICIO 2 PARCIAL

cont = 0
suma = 0

while cont >= 0:

   producto = input("Ingrese el nombre del producto, si desea salir escriba 'FIN': ")
   
   if (producto  != 'FIN'):

      cat = int(input("Ingrese una de las categorías => 1. Lana ; 2. Hilo de Algodón ; 3. Acrílico\n"))
      
      print("Ingresaste la categoría", cat)

      if cat == 1:
          precioKg = int(input("Introduce el precio por Kilogramo en $ ($1000 a $5000): "))
          peso = int(input("Introduce el peso que desea entre 100 Gramos a 10.000 Gramos: "))
          if peso > 5000:
            suma +=( ( (peso * precioKg) / 1000) - ( (peso * precioKg) / 1000)* 0.05)
          else:  
            suma += (peso * precioKg) / 1000
          suma += (peso * precioKg) / 1000
          lanaTot = suma

      elif cat == 2:
          precioKg = int(input("Introduce el precio por Kilogramo en $ ($1000 a $5000): "))
          peso = int(input("Introduce el peso que desea entre 100 Gramos a 10.000 Gramos: "))
          if peso > 5000:
            suma +=( ( (peso * precioKg) / 1000) - ( (peso * precioKg) / 1000)* 0.05)

          else:  
            suma += (peso * precioKg) / 1000
          suma += (peso * precioKg) / 1000
          hiloTot = suma

      elif cat == 3:
          precioKg = int(input("Introduce el precio por Kilogramo en $ ($1000 a $5000): "))
          peso = int(input("Introduce el peso que desea entre 100 Gramos a 10.000 Gramos: "))
          if peso > 5000:
            suma +=( ( (peso * precioKg) / 1000) - ( (peso * precioKg) / 1000)* 0.05)
          else:  
            suma += (peso * precioKg) / 1000
          suma += (peso * precioKg) / 1000  
          acriTot = suma

      else:
        print("No has introducido una categoría disponible, introduce nuevamente el programa.")    

   else:
        cont = -1   

print("Total vendido de Lana: ", lanaTot, "gramos")
print("Total vendido de Hilo: ", hiloTot, "gramos")
print("Total vendido de Acrílico: ", acriTot, "gramos")
print("--------------------------------------------")
print("Porcentajes de ventas de Lana en relación al total de ventas: ", (lanaTot * 100)*suma ) 

---------------------------------------------------------------------------------

EJERCICIO 10

from random import randint

i = 0
aux = 0
cont = 1

while i < 3:
    num = randint(1, 5)
    print(num,",", end="")
    if aux == num:
        cont += 1
    aux = num  
    i += 1

if  cont == 3:
    print("Todos los números son iguales")

elif cont == 2:            
    print("Hay dos números son iguales")

else:
    print("No hay números son iguales")  

cont = 0
cont = 0

---------------------------------------------------------------------------------

EJERCICIO 5


num = int(input("Introduce un número para saber si es primo o no: "))
i = 1
cont = 0

while i <= num:
    if(num % i == 0 and num > 0):
        cont += 1 
    i += 1

if cont == 2:
    print("El número", num,"es primo!")

else:
    print("El número", num,"no es primo!")
 
---------------------------------------------------------------------------------

EJERCICIO 6

from random import randint 

print("\n--------------------------------------------------------------------------------\n\n")

print("Programa que generará un número al azar del 2 al 1000\n\n Número random es: ", end="")
cont = 0
i = 1
num = randint(2, 1000)
print(num)

while i <= num:
    if(num % i == 0 and num > 0):
       cont += 1 
    i += 1

if cont == 2:
       print("\nEl número", num,"es primo!")

else:
       print("\nEl número", num,"no es primo!")

---------------------------------------------------------------------------------
EJERCICIO 7      

n = int(input("¿Cuántos valores vas a introducir?: "))
i = 0
suma = 0
nMenor = 0
nMayor = 0

if ( n < 1 ):
    print("¡Imposible!\ FIN DEL PROGRAMA")

elif (n > 0):

    while(i < n):

       i += 1
       print("Ingresa el número", i,":") 
       n2 = int(input())
       
       suma += n2

       if (n2 >= nMayor):
        nMayor = n2

       elif(n2 <= nMayor and nMayor == 0):
        nMayor = n2

       if (n2 <= nMenor):
        nMenor = n2  

       elif(n2 >= nMenor and nMenor == 0):
        nMenor = n2  

    print("El mínimo de los valores introducidos es:", nMenor)
    print("El máximo de los valores introducidos es:", nMayor)
    print("La media de los valores introducidos es:", float(suma / n) )

---------------------------------------------------------------------------------

EJERCICIO 8

num = int(input("Ingrese un número entero para sumar sus dígitos: "))
resto = 0

while num / 10 > 1:
    resto += (num % 10)

    num = num // 10
if num / 10 < 1 and num / 10 > 0:
    resto += num  

print("Suma de sus dígitos: ",resto)    

---------------------------------------------------------------------------------

Ejercicio 9

num = int(input("Ingrese un número para descomponerlo en factores primos: "))
i = 2
num1 = num
factMayor = 0
print("\nLa descomposición es: ")
while num > 1:

    while num1 % i == 0:
        num1 = num1 / i
        print((i), end="*" )
    i += 1

    if num1 <= 1:
        num = 0 

print("\n\n\nFin del programa\n\n")    

---------------------------------------------------------------------------------

EJERCICIO INTEGRADOR 4


num = int(input("Ingrese un número para descomponerlo en factores primos: "))
i = 2
num1 = num
factMayor = 0
print("\nLa descomposición es: ")
while num > 1:

    while num1 % i == 0:
        num1 = num1 / i

        if num1 > factMayor:
            factMayor = num1

    i += 1

    if num1 <= 1:
        num = 0 
        
print(int(factMayor), end="*" )
print("\n\n\nFin del programa\n\n")    

---------------------------------------------------------------------------------

EJERCICIO 13

from random import*

cont = 1
i = 0
aux = 0
aux1 = 0
suma = 0
fin = 's'

while fin == 's':

    dinero = int(input("Ingrese el dinero que desea apostar: "))
    while i < 3:
        num = randint(1, 5)
        print(num,",", end="")

        if i == 0:
                aux1 = num   
        if aux == num:
            cont += 1
        aux = num  
    
        i += 1
    
    if cont == 3:
    
        dinero *= 5
        print("Felicitaciones salieron los 3 números igual, ganaste X5!")    
        print("Dinero actual en cuenta: $", dinero)
    
    elif cont == 2:
         
         dinero *= 2
         print("Felicitaciones salieron 2 números igual, ganaste X2!") 
         print("Dinero actual en cuenta: $", dinero)
    
    elif aux1 == num:            
    
         dinero *= 2
         print("Felicitaciones salieron 2 números igual, ganaste X2!") 
         print("Dinero actual en cuenta: $", dinero)     
    
    else:
         
         dinero = 0
         print("Felicitaciones! Ponele! Perdiste toda la guita, sos un papelón.!")      
         print("Dinero actual en cuenta: $", dinero)
    
    cont = 0
    i = 0
    aux= 0
    fin = input("\n\nQuiere seguir apostando? Presione 's' si desea continuar, o cualquier caracter si desea finalizar el programa: ")     
    suma += dinero

print("\n\nDinero en cuenta del jugador: $", suma)

print("\nFIN DEL PROGRAMA\n\n")

---------------------------------------------------------------------------------

MODELO 1 PARCIAL EJ 1
promedio = 0
suma = 0
cont = 0
num = int(input("Introduce un número, o uno negativo para salir del programa: "))

while (num > 0):
    
    print("Número elegido: ", num)
    if (num < 10):
        promedio += num
        cont += 1
    else:
        while (num / 10 > 1):
            suma += num % 10
            num = num //10

        if (num < 10):   
            suma += num 

        print("Suma de dígitos es: ", suma)     
        suma = 0   
    num = int(input("Ingrese otro número o uno negativo para terminar: "))

if cont > 0:
    print("El promedio de los números de un sólo dígito es: ", promedio / cont)
else:
    print("No hay números de un sólo dígito")    

---------------------------------------------------------------------------------


EJERCICIO 14

from random import randint

print("\n       LANZANDO DOS DADOS    \n")

print("----------------------------------------\n")

primero =randint(1,6)
sumaA = primero
print("Primer jugador tira: ", primero)
print("\nPuntos del primer jugador hasta el momento: ", sumaA)
segundo = randint(1, 6)
sumaB= segundo
print("Segundo jugador tira: ", segundo)
print("\nPuntos del Segundo jugador hasta el momento: ", sumaB)

fin= input("Desea continuar? Presione 'S' o 's' para continuar: ")

while(fin == 's' or fin == 'S'):
    print("\nPrimer jugador tira: ", end="")

    primero = randint(1,6)
    print(primero)
    sumaA += primero
    print("\nPuntos del primer jugador hasta el momento: ", sumaA)

    print("\nSegundo jugador tira: ", end="")

    segundo = randint(1,6)
    print(segundo)
    sumaB += segundo
    print("\nPuntos del segundo jugador hasta el momento: ", sumaB)

    fin = input("Desea continuar? Presione 'S' o 's' para continuar: ")

print("\n+++++++++++++++++++++++++++++++++++++++++++++++\n")

if (sumaA == sumaB):
    print("Jugador 1 y jugador 2 han empatado con", sumaA, "puntos!")

elif(sumaA > sumaB):
    print("Jugador 1 ha ganado con", sumaA, "puntos!")
    print("Jugador 2 ha perdido con", sumaB, "puntos!")

elif (sumaB > sumaA):
    print("Jugador 2 ha ganado con", sumaB, "puntos!")
    print("Jugador 1 ha perdido con", sumaA, "puntos!")

---------------------------------------------------------------------------------
EJERCICIO 15

i = 1
mayorEdad = 0
menorAltura = 0
sumaAltura = 0
sumaEdad = 0

while(i <= 10):
    print("\nIngrese nombre del jugador n°", i, ": ", end="")
    nombre = input()
    print("\nIngrese edad de ", nombre, ": ", end="")
    edad = float(input())
    print("\nIngrese altura de ", nombre, "en centímetros : ", end="")
    altura = float(input())

    if (edad >= mayorEdad):
        mayorEdad = edad 
        nombreMaxE = nombre 

    if (i == 1):
        menorAltura = altura 

    if ( altura <= menorAltura):   
        menorAltura = altura 
        nombreMinA = nombre 

    sumaEdad += edad 
    sumaAltura += altura 

    i += 1

print("\nNombre del jugador de mayor edad: ", nombreMaxE)
print("\nNombre del jugador de menor altura: ", nombreMinA)
print("\nPromedio de edades: ", sumaEdad / 10)
print("\nPromedio de altura: ", sumaAltura/ 10)


INTEGRADOR 4


num = int(input("Ingrese un número: "))
num1 = num
pal= 0
i = 0

while (num >= 1):

    if (i > 0):
       pal += (num % 10) * 10 **i

    elif(i == 0): 
        pal += num % 10

    num = num // 10
    i += 1

print("\nNumero: ",num1)
print("\nPalíndromo: ", pal)

if (num1 == pal):
    print("\nSon palíndromos wachiinnn\n\n")
else:
    print("\nNo son nada que ver amigo, suerte\n\n")    

a = 'abcde'

b = 'd'

b += 'e'

print("Longitud A: ", a)
print("Longitud B: ", b)

a -= b

print("La cadena A queda: ", a)

'''
def is_user_valid(user):   

        upper, lower, count = 0, 0, 0

        if (len(user) >= 6):

          for i in user:

              if (i.islower()):
                  lower+=1            
    
              if (i.isupper()):
                  upper+=1            
    
              if (i.isnumeric()):
                  count+=1                
          
        if (upper>=1 and lower >=1 and count>=1 and lower+upper+count == len(user)):
           return True
        else:
           return False   

def is_password_valid(password):  
     upper, lower, count = 0, 0, 0  
     if (len(password) >= 8):  
       for i in password:  
           if (i.islower()):
               lower+=1            
 
           if (i.isupper()):
               upper+=1            
 
           if (i.isnumeric()):
               count+=1                
       
     if (upper>=1 and lower >=1 and count>=3 and lower+upper+count==len(password)):
        return True
     else:
        return False

print("\n\nBIENVENIDO AL PORTAL DE NUEVOS USUARIOS!\n")

print("Desea registrarse con un nuevo usuario y contraseña? (S/N) :", end="")
resp = input()
resp = str(resp.lower())
print("Respuesta elegida: ", resp)

while ( resp != chr(115) and resp != chr(110)):

    print("\nNo has ingresado un valor existente, pruebe nuevamente: ", end="")
    resp = input()
    resp = str(resp.lower())

while (resp == chr(110)):
    print("\nFue un placer poder ayudarte!\n")
    print("\n       FIN DEL PROGRAMA     \n\n")
    quit()

while ( resp == chr(115)):
    
    print("\n** Recuerde que el usuario debe contener al menos 6 caracteres y un número **\n")
    usuario = input("\nIngrese nombre de usuario: ") 

    if is_user_valid(usuario) == False:

        while ( is_user_valid(usuario) == False ):

            print("\nUsuario inválido, pruebe nuevamente.\n")
            print("\n** Recuerde que el usuario debe contener al menos 6 caracteres, una mayúscula y un número **\n")
            usuario = input("\nIngrese nombre de usuario: ")

    if is_user_valid(usuario) == True:

       print("\nUsuario creado con éxito!\n Ahora cree una contraseña  ** Recuerde que debe contener al menos 8 caracteres, y al menos 3 números) ")
       contraseña = input("Contraseña: ")

    if is_password_valid(contraseña) == False:

        while ( is_password_valid(contraseña) == False ):

            print("\nContraseña inválida, pruebe nuevamente.\n")
            print("\n** Recuerde que la contraseña debe contener al menos 8 caracteres y 3 números **\n")
            contraseña = input("\nIngrese contraseña: ")

    if is_password_valid(contraseña) == True:
        print("\nEl usuario y contraseña se han creado con éxito!\nBienvenido", usuario, " al portal!\n")


    quit()    

