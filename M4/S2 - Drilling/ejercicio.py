class Persona():
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_edad(self, edad):
        self.edad = edad

persona_01 = Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg")
persona_02 = Persona("Juan", "Camargo", "Masculino", "18", "1.8 mts", "75 Kg")

#Cambiar edad a persona_01
persona_01.set_edad("21 años")
print(persona_01.edad)

#Cambiar apellido a persona_02
persona_02.set_apellido("Santiago")
print(persona_02.apellido)

