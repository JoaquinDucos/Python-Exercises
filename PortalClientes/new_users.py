from functions import*
from prints import*

dataBase = transformar_archivo_DB('database.txt')

##Print de bienvenida.
bienvenida()
resp = input()
resp = str(resp.lower())

cont = 0

print("\n---------------------------------------------------------------------------")

# Comprobación por si el usuario escribe un caracter no pedido.
while ( resp != chr(115) and resp != chr(110)):
    respuesta_inexistente()
    resp = input()
    resp = str(resp.lower())

## Usuario ingresa N/n ==> No quiere continuar.
while (resp == chr(110)):
    
    fin_programa()

## Usuario ingresa S/s ==> Quiere continuar con el programa.
while ( resp == chr(115)):

    recordatorio_usuario()
    usuario = input() 

    if is_user_valid(usuario) == False:                    ##   Si el argumento es falso continúo el pedido al usuario a que ingrese nuevamente su usuario.

        while ( is_user_valid(usuario) == False ):
            usuario_invalido()
            usuario = input()

    if is_user_valid(usuario) == True:                     ##   Valido con la función si cumplió los valores pedidos.
       usuario_valido()
       contraseña = input()

    if is_password_valid(contraseña) == False:             ##   Si el argumento es falso continúo el pedido al usuario a que ingrese nuevamente la contraseña.

        while ( is_password_valid(contraseña) == False ):

            contraseña_invalida()
            contraseña = input()

    if is_password_valid(contraseña) == True:              ##  Mensaje de éxito cuando el Usuario cree su cuenta.
        
        exito_usuario(usuario, contraseña)
    
    lista_usr = [usuario, contraseña]
    dataBase.append(lista_usr)
    
    resp = 'q'

print("\n        BIENVENID@ A DUCOS AUTOMATION COMPANY      \n")    
print("\n\n-----------------------------------------------------\n\n")
print("-Ingrese a la plataforma con su usuario y contraseña-\n\n")

while (cont < 2):

    login_user = input("Usuario: ")

    for i in range(len(dataBase[0])-1):
    
        while ( login_user != str(dataBase[i][0])):
            login_user = input("Usuario inexistente en la base de datos, inténtelo nuevamente: ")
    
        if ( login_user == str(dataBase[i][0])):
            cont +=1
    
    login_password = input("Contraseña: ")
    
    for i in range(len(dataBase[0])-1):
        
        while ( login_password != dataBase[i][1]):
            login_password = input("Contraseña inexistente en la base de datos, inténtelo nuevamente: ")
    
        if ( login_password == dataBase[i][1]):
            cont += 1

if ( cont == 2):

    print("\nSuccesfull login.\nPlease wait to be redirected to the main page.\n")
    cont = 0

DB_str = transform_to_str(dataBase)


try:  
    fd = open('database.txt', 'w')
    for fila in DB_str:
        fd.write(fila + '\n') 
    fd.close()    

except FileNotFoundError:  

    fd = open('database.txt', 'w')
    for fila in DB_str:
        fd.write(fila + '\n')       
    fd.close()    

fin_programa()   
