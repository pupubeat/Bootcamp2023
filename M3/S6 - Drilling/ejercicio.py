"""
Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
orden de mayor a menor.

"""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

#Agrupar números7
numeros = [a,b,c]

#Ordenar números de mayor a menor
num_ordenados = sorted(numeros, reverse=True)

print(f"Números ordenados de mayor a menor: {num_ordenados}")