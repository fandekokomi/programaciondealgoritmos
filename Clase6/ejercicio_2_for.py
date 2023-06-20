import os
os.system("cls")
#EJERCICIO 2 FOR
vocales = 0
consonantes = 0
for x in range(10):
    while True:
        letra = input(f"Ingrese letra N°{x+1}: ")
        if len(letra.strip()) == 1 and letra.isalpha()==True:
            break
        else:
            print("ERROR! Debe escribir una letra!")
    if letra.lower() in("a", "e", "i", "o","u"):
        vocales += 1
    else:
        consonantes += 1
print(f"Hay {vocales} letras vocales y {consonantes} letras consonantes")