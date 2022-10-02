libro = {
    'nombre': 'Culo',
    'autor': 'John.B',
    'año': '2013'
}

print(libro['nombre'])

libro['nombre'] = 'cola'

print( libro['nombre'])

#Keys son las "palabras clave" en cada diccionario tal como nombre, autor, año, etc

keys = libro.keys()
print(keys)

personalidades = [{
    'nombre': 'Johnathan',
    'edad': 18,
    'fuma faso?': "Probablemente"
}, {
    'nombre': 'Joaquin',
    'edad': 19,
    'fuma faso?': 'No creo, es un capo'
}
]
print(personalidades)

bolsa = {
    "libros" : [{
    'nombre': 'Culo',
    'autor': 'John.B',
    'año': '2013'
    }, {
        'nombre': 'Calor',
    'autor': 'nadie',
    'año': '2013'
    }]
}

print(bolsa)


#convertir int en str

edad = 23
print("Su edad es: " + str(edad))