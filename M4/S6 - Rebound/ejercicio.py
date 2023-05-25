suma = 3000
contador = 0

try:
    cociente = (suma / contador)
    print(f"El resultado es {cociente}")

except ZeroDivisionError:
    print("División por cero")