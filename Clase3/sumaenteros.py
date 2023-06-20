#Ejercicio 2
while True:
    print("Ingrese un número entero positivo")
    num1 = int(input())
    if num1 > 0:
        break
    else:
        print("ERROR! Debe ingresar un número entero positivo.")

while True:
    print("Ingrese otro número entero positivo")
    num2 = int(input())
    if num2 > 0:
        break
    else:
        print("ERROR! Debe ingresar un número entero positivo.")

resultado_suma = num1 + num2

print("Resultado de la suma entre los números ingresados es:", resultado_suma)