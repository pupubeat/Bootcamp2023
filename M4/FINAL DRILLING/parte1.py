from main import Vehiculo, Automovil

instancias = []

n = int(input("Cuántos vehículos desea ingresar?: "))

for a in range(n):
    print(f"Datos del Automóvil {a+1}")
    marca = input("Inserte la marca del Automóvil:")
    modelo = input("Inserte el modelo: ")
    n_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en Km/h: "))
    cilindrada = int(input("Inserte el cilindraje: "))

    conjunto = Automovil(marca,modelo, n_ruedas, velocidad, cilindrada)
    instancias.append(conjunto)

print("Imprimiendo por pantalla los Vehiculos...")

for x,y in enumerate(instancias):
    print(f"Datos del Automovil {x+1}: Marca: {y.marca}, Modelo: {y.modelo}, {y.n_ruedas} ruedas, {y.velocidad} Km/h.")
