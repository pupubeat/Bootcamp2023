#Importar clases desde clases.py
from clases import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print(particular)
#print(carga)
#print(bicicleta)
#print(motocicleta)

#print("")

#Usar isinstance() en instancia de Motocicleta
print("Motocicleta es instancia con respecto a Vehiculo: ", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con respecto a Automovil: ", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con respecto a Vehiculo Particular: ", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con respecto a Vehiculo de Carga: ", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con respecto a Bicicleta: ", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con respecto a Motocicleta: ", isinstance(motocicleta, Motocicleta))