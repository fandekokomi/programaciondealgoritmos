#Ejemplo while
import os
os.system("cls")
import time
contador = 1
while contador<=10:
    time.sleep(0.5)
    print(contador)
    contador += 1

#ejemplo 2
contador = 0
while True:
    print("Hola mundo")
    contador += 1
    if contador == 5:
        break

#ejemplo 3: validad edad
while True:
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        break
#ejemplo 3 v2: validar edad
edad = 0
while edad<18:
    edad = int(input("Ingrese su edad: "))