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

def split(S, c):

    lista=[]
    sub=""

    for i in S:
        if i != c:
            sub += i  
        else:
            lista.append(sub)
            sub = ""    

    if sub != "":
        lista.append(sub) 
            
    return lista

def transformar_archivo_DB(archivo):
    try:    
        archivo = open (archivo, "r")
        matriz = split (archivo.read(), "\n") 
        matriz_aux= []

        for fila in matriz:
            fila = split (fila, " ")
            matriz_aux.append(fila) 
        archivo.close ()  

        return matriz_aux

    except FileNotFoundError:
        print("No existe el archivo 'ventas.txt', crearemos uno nuevo\n")  
        matrizDB = []

        return matrizDB           

def transform_to_str(matriz):
    matriz_nuev= []

    for fila in matriz:
        cadena = ''
        for elemento in fila:
            cadena += str(elemento)+' '
        matriz_nuev.append(cadena)    
    return matriz_nuev                  
