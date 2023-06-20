#ARREGLOS
import numpy

#VAMOS A CREAR VARIOS ARREGLOS DIFERENTES:
#1. A PARTIR DE UNA LISTA:
lista_uni = [7,2,9,10]
arreglo_uni = numpy.array(lista_uni)

lista_bi = [[5.2,3.0,4.5],[9.1,0.1,0.3]]
arreglo_bi = numpy.array(lista_bi)

#2. ARREGLO DE ZEROS:
arreglo_zeros_1 = numpy.zeros(10)
print(arreglo_zeros_1)

arreglo_zeros_2 = numpy.zeros((3,5),int)
print(arreglo_zeros_2)
#3. ARREGLO DE UNO:
arreglo_unos_1 = numpy.ones(10, int)
arreglo_unos_2 = numpy.ones((10,2))
print(arreglo_unos_1)
print(arreglo_unos_2)

#arreglo con range():
arreglo_range = numpy.arange(5)

#arreglo de 2 dimensiones con una diagonal igual:
arreglo_diagonal = numpy.diag((1,2,3))
print(arreglo_diagonal)

#6. Crear un arreglo con número aleatorio
arreglo_random_uni = numpy.random.randint(0,10,100)
arreglo_random_bi = numpy.random.randint(0,10,(5,10))

#comandos de utilidad:
print( numpy.sum(arreglo_uni) )
print( numpy.average(arreglo_uni) )
print( numpy.mean(arreglo_uni) )
print( numpy.max(arreglo_uni) )
print( numpy.min(arreglo_uni) )
print( len(arreglo_uni) )
print( len(arreglo_bi) )