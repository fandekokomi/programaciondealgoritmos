#EJERCICIO FINAL:
import os
import time
from numpy import *
import random
from ejerciciofinalfunciones import *
#CINE: A-F, 1 - 12, DEL 5 - 9 $7200, los demás $4000.
#RUT, CORREO, TELÉFONO
#0 = LIBRE, 1 = OCUPADO
"""LISTAS Y ARREGLOS"""
cine = zeros((12,6), int)
ruts = []
correos = []
telefonos = []
filas = []
columnas = []
while True:
    os.system("cls")
    opcion = menu()
    os.system("cls")
    if opcion==1:
        os.system("cls")
        versala(cine)
        os.system("cls")
    elif opcion==2:
        rut = vrut()
        correo = vcorreo()
        telefono = vtelefono()
        ruts.append(rut)
        correos.append(correo)
        telefonos.append(telefono)
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    else:
        print("Gracias, Nos vemos!")
        break
