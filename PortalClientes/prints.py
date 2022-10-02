
## Print por pantalla de Bienvenida
def bienvenida():
    print("\n\n                   ¡BIENVENIDO AL PORTAL DE NUEVOS USUARIOS!\n\n")
    print("---------------------------------------------------------------------------\n\n")
    print("Desea registrarse con un nuevo usuario y contraseña? (S/N) :", end="")

## Print valor inexistente por el Usuario
def respuesta_inexistente():
    print("\nNo has ingresado un valor existente, intente nuevamente: ", end="")


## Print recordatorio de especificaciones para creación de Usuario.
def recordatorio_usuario():
    print("\n\n** Recuerde que el usuario debe contener al menos 6 caracteres y un número **\n")
    print("\nIngrese nombre de usuario: ", end="") 


## Print Usuario inválido.
def usuario_invalido():

    print("\n---------------------------------------------------------------------------")
    print("\nUsuario inválido, inténtelo nuevamente:\n")
    print("\n** Recuerde que el usuario debe contener al menos 6 caracteres, una mayúscula y un número **\n")
    print("Ingrese el Usuario: ", end="")


## Print Usuario válido.
def usuario_valido():
    print("\n---------------------------------------------------------------------------")
    print("\nUsuario creado con éxito!\n\nAhora cree una contraseña.\n\n** Recuerde que debe contener al menos 8 caracteres, y al menos 3 números) **\n\n")
    print("Ingrese contraseña: ", end="")


## Print Contraseña inválida.
def contraseña_invalida():
    print("\n---------------------------------------------------------------------------")
    print("\nContraseña inválida, intente nuevamente.\n")
    print("\n** Recuerde que la contraseña debe contener al menos 8 caracteres y 3 números **\n")
    print("Ingrese contraseña: ", end="")


## Print éxito de creación de Usuario y Contraseña.
def exito_usuario(usuario, contraseña):
    print("\n---------------------------------------------------------------------------")
    print("\nEl usuario y contraseña se han creado con éxito!\n\nBienvenido", usuario, "al portal! Nos alegra que formes parte de nuestra plataforma!\n")
    print("No te olvides tu usuario y contraseña! Te recuerdo:\n\nUsuario:", usuario, "\nContraseña:", contraseña, "\n\nAprovecha al máximo tu cuenta con los beneficios que tenemos para ofrecerte!\n")


## Print de finalización de programa.
def fin_programa():
    print("\nFue un placer poder ayudarte!\n")
    print("\n       FIN DEL PROGRAMA     \n\n")
    quit()    