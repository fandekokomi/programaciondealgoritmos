#ejercicio 1:
numero = int(input("Ingrese un número: "))

lista = []
#x:0,1,2,3,4,5,6,7,8,9
for x in range(10):
    lista.append(numero*(x+1))
print(lista)