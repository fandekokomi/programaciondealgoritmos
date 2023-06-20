#ejercicio factorial:
import os
os.system("cls")
#validación para número positivo
while True:
    num = int(input("Ingrese un número positivo: "))
    if num > 0:
        break
    else:
        print("ERROR! DEBES INGRESAR UN NÚMERO POSITIVO!")

#fatorial
contador = 1
acumulador = 1
while contador <= num:
   acumulador = acumulador * contador
   contador += 1
print(f"El factorial de {num} es {acumulador}")