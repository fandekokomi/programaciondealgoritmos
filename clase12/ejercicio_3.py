#ejercicio 3:
lista = []

cantidad = int(input("Ingrese cantidad de números: "))

for x in range(cantidad):
    numero = float(input("Ingrese un número: "))
    lista.append(numero)

acumulador = 0
#x: 0,1,2,3,4,5,6,7,8,9
for x in range( len(lista) ):
    acumulador = acumulador + lista[x]

for x in lista:
    acumulador = acumulador + x

print(acumulador)
print(acumulador/len(lista))