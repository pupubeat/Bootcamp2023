"""
Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar.
En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar
subcondiciones; en su lugar, usar condiciones anidadas.

"""

n = int(input("Ingrese un número"))

if n > 0:
    if n % 2 == 0:
        print(f"{n} es positivo y par.")
    else:
        print(f"{n} es positivo e inpar.")

elif n < 0:
    if n % 2 == 0:
        print(f"{n} es negativo y par.")
    else:
        print(f"{n} es negativo e inpar.")

else:
    print("el número es 0.")