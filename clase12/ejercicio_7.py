#ejercicio 7:
lista_nombres = []

for x in range(3):
    nombre = input("Ingrese un nombre: ")
    lista_nombres.append(nombre)

nombre_ganador = None
posicion_ganador = None
for x in range(3):
    if x == 0:
        nombre_ganador = lista_nombres[x]
        posicion_ganador = x
    else:
        if len(lista_nombres[x]) > len(nombre_ganador):
            nombre_ganador = lista_nombres[x]
            posicion_ganador = x

print(nombre_ganador)
print(posicion_ganador)