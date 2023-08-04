import csv

#Definir clase Vehiculo.
class Vehiculo():
    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv","a", newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)

        except FileNotFoundError:
            print("El archivo vehiculos.cvs no existe")
        
        except Exception as e:
            print("ERROR: ", e)

    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv","r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de Vehículos {type(self).__name__}")
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item[0]:
                        print (item[1])
                        print("")

        except FileNotFoundError:
            print("El archivo vehiculos.cvs no existe")

        except Exception as e:
            print("ERROR: ", e)

    def __str__(self):
        return "Marca: {}, Modelo: {}, {} ruedas".format(self.marca, self.modelo, self.n_ruedas)

#{type(self).__name__} --> Solo para que se imprima el nombre de la clase
#item[1] ---> diccionario

#Definir clase hija de Vehiculo: Automóvil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + " {} Km/h, {} cc".format(self.velocidad, self.cilindrada)

#Definir clase hija de Vehiculo: Bicicleta.
class Bicicleta (Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, tipo):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + " Tipo: {} ".format(self.tipo)

#Definir características para Motocicleta.
class Caracteristicas():
    def __init__(self, motor, cuadro, n_radio):
        self.motor = motor
        self.cuadro = cuadro
        self.n_radio = n_radio
    def __str__(self):
       return "Motor: {}, Cuadro: {}, Nro Radios:{}".format(self.motor, self.cuadro, self.n_radio)

#Definir clase nieta de Vehiculo, clase hija de Bicicleta: Motocicleta.
class Motocicleta (Bicicleta, Caracteristicas):
    def __init__(self, marca, modelo, n_ruedas, tipo, n_radio, cuadro, motor):
        super().__init__(marca, modelo, n_ruedas, tipo)
        Caracteristicas.__init__(self, motor, cuadro, n_radio)

    def __str__(self):
       return Bicicleta.__str__(self) + Caracteristicas.__str__(self)

#Definir clases hijas de Automovil: Particular y Carga
class Particular (Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, n_puestos):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.n_puestos = n_puestos

    def __str__(self):
        return Automovil.__str__(self) + "Puestos: {}".format(self.n_puestos)

class Carga (Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, peso):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.peso = peso

    def __str__(self):
        return super().__str__() + " Carga: {} Kg".format(self.peso)



