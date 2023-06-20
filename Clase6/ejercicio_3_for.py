import os
os.system("cls")
contador = 0
#EJERCICIO 3 FOR
while True:
    num = int(input("Ingrese un número entero: "))
    if num > 0:
        break
    else:
        print("ERROR!!! Su número debe ser positivo!")
for x in range(num):
    if num%(x+1) == 0:
        contador += 1
if contador==2:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")