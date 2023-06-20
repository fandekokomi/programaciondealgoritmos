import os
import time
import msvcrt as tecla
import numpy
os.system("cls")
#FUNCIÓN SIN PARÁMETROS Y SIN RETORNO.
def saludar():
    print("Hola!")
#FUNCIÓN PARAMETROS Y SIN RETORNO.
def saludar_alumno(nombre, apellido):
    print("Hola", nombre, apellido)
#FUNCIÓN SIN PARAMETROS - CON RETORNO:
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! El Nombre debe tener al menos 3 letras!")
def validar_apellido():
    while True:
        apellido = input("Ingrese apellido: ")
        if len(apellido.strip()) >= 2 and apellido.isalpha():
            return apellido
        else:
            print("ERROR! El Apellido debe tener al menos 2 letras!")
def validar_num(p_pal,p_minimo,p_maximo):
    while True:
        try:
            num = int(input(f"Ingrese {p_pal} número: "))
            if num >= p_minimo and num <= p_maximo:
                return num
            else:
                print(f"ERROR! El número debe estar entre {p_minimo} y {p_maximo}")
        except:
            print("ERROR! DEBE INGRESAR NÚMEROS ENTEROS!")
#FUNCIÓN CON PARAMETROS CON RETORNO:
def sumarnumeros(p_num1:int, p_num2:int):
    total = p_num1 + p_num2
    return total