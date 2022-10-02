file = open("main.txt", "r")

print(file.read(9))    #con file.read() lee todo lo que contiene el texto plano
file.close()           #con file.read(5) lee las primeras 5 letras y asi con todas las que quieras  y con .close cerramos el archivo llamado

                       #---------------------------------

#print(file.readline())    #Lee unicamente la linea

#for x in file:         #Avanza letra por letra leyendo todo
 #   print(x)

