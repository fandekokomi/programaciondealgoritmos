#Variables, Constantes, Print.
#print(texto,variable), print(f"texto {variable}")
#OPERACIONES MATEMÁTICAS: +, -, *, /, **, //, %

#Clase 2 Python:
"""Comandos:
input(): nos permite ingresar información por teclado:"""
#encerrar input dentro de print hara que no se guarde la variable.
print("Ingrese su nombre:")
print("Su nombre es:", input())

print("Ingrese su nombre:")
#usar (variable = input()) siempre la variable sera string
nombre = input()
print("Su nombre es:", nombre)

#ejemplo
print("Ingrese un número:")
num1 = input()
print("Ingrese otro número:")
num2 = input()
print(num1+num2)

#use int() o float() para transformarlo a número.
print("Ingrese un número:")
num1 = int(input())
print("Ingrese otro número:")
num2 = float(input())
print(num1+num2)