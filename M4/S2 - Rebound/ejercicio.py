class Animal():
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

Caballo = Animal("Zeus", "5 años", "Pura Sangre", "450Kg")
León = Animal("Boulder", "10 años", "Atlas", "130Kg")

print(León.__dict__)