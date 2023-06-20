#ejercicio 4 y 5 y 6:
import random
lista = []

for x in range(20):
    lista.append(random.randint(1,100))
lista.sort()
print(lista)
lista.reverse()
print(lista)