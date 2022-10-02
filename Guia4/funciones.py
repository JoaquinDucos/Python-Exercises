def bisiesto (año):

    if año % 400 == 0:
        return True, 0

    elif ( (año % 4 == 0)  and (año % 100 != 0)):
        return True, 1

    elif (año % 100 == 0):
        return False, 2

    else:
        return False, 3

# ------------------------------------------------------------------


def cuadratica (a, b):
    if a != 0:

       x = b / (-a)

    else: 
        return None    

    return x

# ------------------------------------------------------------------

def amigos(a,b):
    i = 2
    sumaA = 1
    sumaB = 1
    a1 = a
    b1 = b

    while i < a : 
        if a1 % i == 0:
           while a1 % i == 0:
              a1 /= i
           sumaA += i
        a1 = a 
        i += 1  

    i = 2

    while i < b : 
       if b % i == 0:
          while b1 % i == 0:
             b1 /= i
          sumaB += i

       b1 = b 
       i += 1
       ##print("SumaA:", sumaA)
       ##print("SumaB:", sumaB)

    if sumaA == b and sumaB == a :
        return True   
        
    else:
        return False       

# ------------------------------------------------------------------

def todos_amigos (n):
    b = n
    a = 1
    a1 = 0
    b1 = 0
    cont = 0
    while a <= n:

        while b > 0:

            if amigos(a, b) == False and b > 0:
                b -= 1
                ##print("a: ",a, "b: ", b)

            else:
                if a != b:

                    if b1 != a and a1 != b:

                       print("Los números ", a, " y ", b, " son amigos")
                       cont += 1
                       a1 = a
                       b1 = b 
                b = 0  
        b = n
        a += 1

    return cont      