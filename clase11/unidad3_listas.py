"""UNIDAD 3:
LISTAS:
LISTA = COLECCIÓN (Tipo de dato que permite almacenar muchos valores).
Una lista puede crecer o disminuir."""

#Puedo crear una lista vacia.
lista = []

#puedo crear una lista con valores precargados.
lista_regiones = ["Metropolitana","Arica y Parinacota","O'Higgins"]

#Puedo tener una lista heterogenia:
lista_mixta = ["hola", 15, 5.2, True, [7,8,10]]

#Una lista es dinamica o heterogenia.

#Vamos a usar una lista vacia:
lista_ejemplo = []

#Agregar elementos al final de la lista.
lista_ejemplo.append("Elvis")
lista_ejemplo.append("Elsa")
lista_ejemplo.append("Lalo")

print(lista_ejemplo)
print(lista_ejemplo[0])
print(lista_ejemplo[1])
print(lista_ejemplo[2])

#agregar elemento a donde uno elija
lista_ejemplo.insert(0, "Juanito")
print(lista_ejemplo)
#ELIMINAR A ALGUIEN DE LA LISTA
lista_ejemplo.remove("Elsa")
print(lista_ejemplo)
#ELIMINAR POR POSICION
lista_ejemplo.pop(0) #ingresar valor elimina por posicion
print(lista_ejemplo)
#ELIMINAR ULTIMA POSICION
lista_ejemplo.pop() #no ingresar valor elimina ultima posicion

print(lista_ejemplo)
print(lista_ejemplo[0])

#COMPLEMENTOS:
#ORDENAR LA LISTA DE MAYOR A MENOR O POR ABC.
lista_regiones.sort()
print(lista_regiones)

#INVIERTE EL ORDEN
lista_regiones.reverse()
print(lista_regiones)

#LIMPIA LA LISTA
lista_ejemplo.clear()
print(lista_ejemplo)

lista_ejemplo = ["Goku", "Luffy", "Saitama", "Naruto"]

for x in range(len(lista_ejemplo)):
    print(lista_ejemplo[x])