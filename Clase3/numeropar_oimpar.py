#Ejercicio 4
while True:
    num = int(input("Ingrese un número: "))
    if num > 1 and num <101:
        if num%2==0:
            print("El número es par")
            break
        else:
            print("El número es impar")
            break
    else:
        print("ERROR! Debe ingresar un número entre 2 y 100!")