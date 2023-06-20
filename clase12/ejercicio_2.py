#ejercicio 2:
lista = []

while True:
    try:
        numero = int(input("Ingrese un número: "))
        if numero == 0:
            break
        else:
            lista.append(numero)
    except:
        print("ERROR! debe ingresar un número entero!")
lista.sort()
print(lista)