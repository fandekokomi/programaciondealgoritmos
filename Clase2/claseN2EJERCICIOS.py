while True:
    nota1 = float(input("Ingrese la nota 1 (entre 1 y 7): "))
    if nota1 >= 1 and nota1 <= 7:
        break
    else:
        print("La nota debe estar entre 1 y 7. Intente nuevamente.")

while True:
    nota2 = float(input("Ingrese la nota 2 (entre 1 y 7): "))
    if nota2 >= 1 and nota2 <= 7:
        break
    else:
        print("La nota debe estar entre 1 y 7. Intente nuevamente.")

while True:
    nota3 = float(input("Ingrese la nota 3 (entre 1 y 7): "))
    if nota3 >= 1 and nota3 <= 7:
        break
    else:
        print("La nota debe estar entre 1 y 7. Intente nuevamente.")

promedio = (nota1 + nota2 + nota3) / 3
print("El promedio de las notas ingresadas es: ", promedio)

if promedio >= 4:
    print("¡Felicidades, está aprobado!")
else:
    print("Lo siento, está reprobado.")