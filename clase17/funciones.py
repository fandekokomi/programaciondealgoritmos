#UNIDAD 3: FUNCIONES:
#REUTILZACIÓN DE CÓDIGO
import os
import time
import msvcrt as tecla
import numpy
from funciones2 import *
os.system("cls")
#ejercicio principal:
saludar()
saludar_alumno("Juan", "G")
nombre = validar_nombre()
apellido = validar_apellido()
saludar_alumno(nombre, apellido)
numerito1 = validar_num("primer",0,100)
numerito2 = validar_num("segundo",1,50)
res = sumarnumeros(numerito1,numerito2)
print("El resultado es:", res)