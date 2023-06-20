#ejercicio 8:
lista_nombres = []
lista_apellidos = []

for x in range(3):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

for x in range( len(lista_nombres) ):
    print(f"Nombre: {lista_nombres[x]} {lista_apellidos[x]}")
