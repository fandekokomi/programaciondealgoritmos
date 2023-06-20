import os
os.system("cls")
acumulador = 0
#EJERCICIO 4 FOR
while True:
    num = int(input("Ingrese un número entero positivo: "))
    if num > 0:
        break
    else:
        print("ERROR! Debe ingresar un número mayor a 0")
for x in range(num):
    if num%(x+1) == 0 and num != (x+1):
        acumulador = acumulador + (x+1)