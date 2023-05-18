lista = [0,1,2,3,4,5,6,7,8,9]

for x in lista:
    if x % 2 == 0 and x!= 0:
        print(f"{x} es par.")
    elif x % 2 == 1:
        print(f"{x} es impar.")
    else:
        print(f"{x} es cero.")