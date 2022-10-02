class Persona:    
                                #Se usa para crear pobjetos
    """Create a new person"""

    def __init__(self, pnombre, apellido):           # Self = Prámetro de referencia.    

        self.pnombre = pnombre

        self.apellido = apellido

    def nuevo(self):
         print("Hola, mi nombre es: " + self.pnombre)
         print("Y mi apellido es: " + self.apellido)

nuevaPersona = Persona("Juan", "Lopez")   

nuevaPersona.nuevo()
#Displaying the output

print(nuevaPersona)
print(nuevaPersona.pnombre)
print(nuevaPersona.apellido)

