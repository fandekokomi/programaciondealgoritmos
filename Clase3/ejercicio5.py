#fandekokomi :)
import os
os.system("cls")

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

if ((num1 > 0) or (num1 % 2 == 0)) and ((num2 > 0) or (num2 % 2 == 0)) and ((num3 > 0) or (num3 % 2 == 0)):
  sum = num1+num2+num3
elif (num1 > 0 or num1 % 2 == 0) and (num2 > 0 or num2 % 2 == 0):
  sum = num1 + num2
elif (num1 > 0 or num1 % 2 == 0) and (num3 > 0 or num3 % 2 == 0):
  sum = num1 + num3
elif (num2 > 0 or num2 % 2 == 0) and (num3 > 0 or num3 % 2 == 0):
  sum = num2 + num3
elif (num1 > 0 or num1 % 2 == 0):
  sum = num1
elif (num2 > 0 or num2 % 2 == 0):
  sum = num2
elif (num3 > 0 or num3 % 2 == 0):
  sum = num3
else:
  sum = 0

cont = 0
if num1 <= 0 or num1 % 2 != 0:
  cont += 1
if num2 <= 0 or num2 % 2 != 0:
  cont += 1
if num3 <= 0 or num3 % 2 != 0:
  cont += 1

if sum > 0:
  print("La suma de los números que son mayores a cero o pares es:", sum)
elif ((num1 > 0) or (num1 % 2 == 0)) or ((num2 > 0) or (num2 % 2 == 0)) or ((num3 > 0) or (num3 % 2 == 0)):
  print("Solo un número cumple la condición de ser mayor a cero o par.")
else:
  print("No hay números que cumplan la condición de ser mayores a cero o pares.")
if cont > 0:
  print("Hay", cont, "números que son impares o menores a cero.")
else:
  print("No hay números que sean impares o menores a cero.")