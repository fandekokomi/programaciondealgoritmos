# Solicitar al usuario los valores de los tres lados del triángulo
a = float(input("Ingrese la longitud del lado A: "))
b = float(input("Ingrese la longitud del lado B: "))
c = float(input("Ingrese la longitud del lado C: "))

# Verificar si se trata de un triángulo válido
if a + b > c and a + c > b and b + c > a:
    # Identificar el tipo de triángulo
    if a == b or a == c or b == c:
        print("El triángulo es Isósceles")
    elif (a == b == c):
        print("El triángulo es Equilátero")
    else:
        print("El triángulo es Escaleno")
else:
    print("Los valores ingresados no corresponden a los lados de un triángulo válido")