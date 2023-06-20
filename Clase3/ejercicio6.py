menor_a_cero = 0
num1 = int(input("Ingrese un número entero "))
num2 = int(input("Ingrese segundo número entero "))
num3 = int(input("Ingrese tercer número entero "))
if num1 < 0:
    menor_a_cero = menor_a_cero + 1
if num2 < 0:
    menor_a_cero = menor_a_cero + 1
if num3 < 0:
    menor_a_cero = menor_a_cero + 1
print(f"Hay {menor_a_cero} números menores a 0")