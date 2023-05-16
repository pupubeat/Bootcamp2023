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