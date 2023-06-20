#Ejercicio 1

while True:
    print("Ingrese un número")
    num1 = int(input())
    if num1 > 0:
        break
    else:
        print("ERROR! Debe ingresar un número entero positivo.")

while True:
    print("Ingrese otro número")
    num2 = int(input())
    if num2 > 0:
        break
    else:
        print("ERROR! Debe ingresar un número entero positivo.")
    
if num1 > num2:
    print(f"El número {num1} es mayor a el número {num2}")
elif num1 == num2:
    print(f"El número {num1} es igual a el número {num2}")
else:
    print(f"El número {num1} es menor a el número {num2}")