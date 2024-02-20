"""
Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan
son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las
personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente,
imprimiremos en pantalla la lista.

"""

# Atribuir valores a los 3 diccionarios

Diccionario1 = {
    "Nombre": "Yaneisi",
    "Apellido": "Moscoso",
    "Telefono":  56912345678
}
print(Diccionario1)

Diccionario2 = {
    "Nombre": "Pablo",
    "Apellido": "Tiengdan",
    "Telefono": 56956781234
}
print(Diccionario2)

Diccionario3 = {
    "Nombre": "Paloma",
    "Apellido": "Atenas",
    "Telefono": 56943218765
}
print(Diccionario3)

#Crear Lista vacia
Lista = []

#Colocar diccionarios en la lisla vacia
Lista.append(Diccionario1)
Lista.append(Diccionario2)
Lista.append(Diccionario3)

print(Lista)

