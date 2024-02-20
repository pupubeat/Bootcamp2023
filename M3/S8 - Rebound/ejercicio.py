"""
En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, se
solicita realizar las siguientes acciones en el orden indicado:
    1. Eliminar los elementos duplicados.
    2. Ordenar la lista resultante en orden ascendente.

La lista es:
1 mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

"""


mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

#Eliminar elementos repetidos
mi_lista2= list(set(mi_lista))
print(mi_lista2)

#Ordenar elementos menor a mayor
mi_lista2.sort()
print(mi_lista2)