#control de errores: 
try:
    num = int(input("Ingrese un número: "))
    total = 10/num
except ValueError:
    print("ERROR! Debe ingresar un número entero!")
except ZeroDivisionError:
    print("ERROR! División por cero!")
    