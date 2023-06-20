#Ejercicio 7: Se pide identificar el tipo de triángulo, para ello, ingrese el lado A, B y C, luego indique si es Isósceles, Equilátero o Escaleno.
lado_a = int(input("Ingrese Lado A del triangulo "))
lado_b = int(input("Ingrese Lado B del triangulo "))
lado_c = int(input("Ingrese Lado C del triangulo "))
if lado_a == lado_b == lado_c:
    print("Su triangulo es equilátero")
elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
    print("Su triangulo es Isósceles")
else:
    print("Su triangulo es escaleno")