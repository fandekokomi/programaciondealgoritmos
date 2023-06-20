#ejercicio while 1:
import os
os.system("cls")
#nombre,edad,altura,teléfono
while True:
    nombre = input("Ingrese su nombre: ")
    if len(nombre.strip()) >= 3:
        break
    else:
        print("ERROR! El nombre debe ser de almenos 3 letras.")
while True:
    edad = int(input("Ingrese su edad: "))
    if edad >= 0:
        print("Usted es mayor de edad")
        break
    else:
        print("ERROR! La edad debe ser mayor o igual a 0")
while True:
    altura = float(input("Ingrese altura: "))
    if altura >= 1.2:
        break
    else:
        print("ERROR! La altura minima es 1.2")
while True:
    telefono = int(input("Ingrese su número de telefono: "))
    if len(str(telefono)) == 9 and str(telefono)[0] == "9":
        break
    else:
        print("ERROR! El teléfono debe tener 9 digitos y comenzar con el número 9")
