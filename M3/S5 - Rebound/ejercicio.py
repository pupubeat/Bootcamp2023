"""
Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla.
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay
entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1

"""

n = int(input(f"Introduzca un número aquí"))
i = 1

while n >= i:
    factorial = n*i
    i = i+1

print(factorial)