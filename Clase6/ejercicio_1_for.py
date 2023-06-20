#ejercicio 1 for
positivos = 0
negativos = 0
ceros = 0
for x in range(5):
    num = int(input(f"Ingrese número {x+1}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1
print(f"Hay una cantidad de {positivos} números positivos, {negativos} números negativos y {ceros} ceros")