#ejercicio 9:
lista_nombres = []

while True:
    nombre = input("Ingrese nombre: ")
    lista_nombres.append(nombre)

    resp = input("Desea agregar otro nombre(SI,NO): ")
    if resp.upper()=="NO":
        break

nombre_ganador = None
posicion_ganador = None

for x in range(len(lista_nombres)):
    if x==0:
        nombre_ganador = lista_nombres[x]
        posicion_ganador = x
    else:
        if len(lista_nombres[x]) < len(nombre_ganador):
            nombre_ganador = lista_nombres[x]
            posicion_ganador = x
lista_nombres.pop(posicion_ganador)
#lista_nombres.remove(nombre_ganador)