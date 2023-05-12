#Lista completa de nombres
lista = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
print(lista)

#Definir y clasificar 3 listas diferentes

#Lista magos
magos = [lista[0], lista[2], lista[5]]

#Lista científicos
cientificos = [lista[1], lista[3], lista[6]]

#Lista otros
otros = [lista[4], lista[7], lista[8]]

#Definir función para lista de los grandes magos
def hacer_grandioso(lista):
    nueva_lista= []
    for x in lista:
       nueva_lista.append("El Gran " + x)
    return nueva_lista

grandes_magos = hacer_grandioso(magos)
print(grandes_magos)

#Definir función de impresión de nombres
def imprimir_nombres(grandes_magos, cientificos, otros):
    lista_nombres = []
    for a in grandes_magos:
        lista_nombres.append(a)
    for b in cientificos:
        lista_nombres.append(b)
    for c in otros:
        lista_nombres.append(c)
    return lista_nombres

lista_definitiva = imprimir_nombres(grandes_magos, cientificos, otros)
print(lista_definitiva)
