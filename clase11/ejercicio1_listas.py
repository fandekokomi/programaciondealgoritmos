import os
import time
os.system("cls")
while True:
    try:
        n1 = int(input("Ingrese un número entre 1 a 10 para calcular su tabla de multiplicar: "))
        if n1 > 0 and n1 < 11:
            break
        else:
            print("ERROR! Debe ingresar un número entero positivo entre 1 a 10.")
    except:
        print("ERROR! Ingrese un número entero.")

if n1 == 1:
    tabla = [1,2,3,4,5,6,7,8,9,10]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
elif n1 == 2:
    tabla = [2,4,6,8,10,12,14,16,18,20]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
elif n1 == 3:
    tabla = [3,6,9,12,15,18,21,24,27,30]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
elif n1 == 4:
    tabla = [4,8,12,16,20,24,28,32,36,40]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
elif n1 == 5:
    tabla = [5,10,15,20,25,30,35,40,45,50]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
elif n1 == 6:
    tabla = [6,12,18,24,30,36,42,48,54,60]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
elif n1 == 7:
    tabla = [7,14,21,28,35,42,49,56,63,70]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
elif n1 == 8:
    tabla = [8,16,24,32,40,48,56,64,72,80]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
elif n1 == 9:
    tabla = [9,18,27,36,45,54,63,72,81,90]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)
else:
    tabla = [10,20,30,40,50,60,70,80,90,100]
    for x in range(len(tabla)):
        print(tabla[x])
        time.sleep(0.5)