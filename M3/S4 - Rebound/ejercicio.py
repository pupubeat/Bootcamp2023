"""
Requerimos crear una variable con el número 8, una con el número 10.5, y una con la palabra
“ejercicio”. Luego, crear un set que contendrá cada una de las variables que creamos, y será
asignado a una variable.
A continuación, crearemos una lista que contendrá el set creado anteriormente, y una variable con
el valor lógico False. Esta lista la asignaremos a una variable que luego imprimiremos en pantalla

"""


#Declarar variables
a = 8
b = 10.5
c = "ejercicio"

#Conjunto de variables a, b y c
conjunto = {a,b,c}
print(conjunto)

#Conversión del conjunto a una lista
lista = list(conjunto)
print(lista)

#Agregar variable False a la lista
lista.append(False)
print(lista)