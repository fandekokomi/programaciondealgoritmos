#EJERCICIO SALA
#ARREGLO, LISTAS, CICLOS, VALIDACIONES:
import os
import time
import msvcrt as tecla
import numpy
lista_ruts = []
lista_nombres = []
lista_correos = []
lista_filas = []
lista_columnas = []
arreglo_sala = numpy.zeros((5,6),int)
while True:
    os.system("cls")
    print("""Menú Sala
    1. Ver Sala
    2. Registrar Alumno
    3. Eliminar Alumno
    4. Terminar Clase
    0. Salir""")
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4,0):
                break
            else:
                print("ERROR! LA OPCIÓN DEBE SER ENTRE 0,1!")
        except:
            print("ERROR! INGRESE NÚMERO ENTERO!")
            os.system("cls")
    if opc == 1:
        os.system("cls")
        print("\tSALA DE CLASES\n")
        print(" "*8+"  COLUMNA")
        print(" "*8+"1 2 3 4 5 6")
        for x in range(5):
            print("Fila", x+1,end=": ")
            for y in range(6):
                print(arreglo_sala[x][y], end=" ")
            print()

        print("\nPresione una tecla para continuar...")
        tecla.getch()
    elif opc == 2:
        if 0 not in arreglo_sala:
            print("SALA LLENA!")
            time.sleep(3)
            continue
        while True:
            try:
                rut = int(input("Ingrese su rut (sin puntos ni digito verificador): "))
                if rut >= 1000000 and rut <= 99999999:
                    break
                else:
                    print("ERROR! RUT INCORRECTO!")
            except:
                print("ERROR! FORMATO DE RUT INCORRECTO!")
        while True:
            nombre = input("Ingrese su nombre: ")
            if len(nombre.strip()) >= 3 and nombre.isalpha():
                break
            else:
                print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
        while True:
            correo = input("Ingrese su correo: ")
            if "@" in correo:
                break
            else:
                print("ERROR! CORREO INCORRECTO!")
        lista_ruts.append(rut)
        lista_nombres.append(nombre)
        lista_correos.append(correo)
        print("ALUMNO REGISTRADO CON ÉXITO!")
        time.sleep(3)
        os.system("cls")
        print("SELECCIÓN DE ASIENTO")
        print("\tSALA DE CLASES\n")
        print(" "*8+"  COLUMNA")
        print(" "*8+"1 2 3 4 5 6")
        for x in range(5):
            print("Fila", x+1,end=": ")
            for y in range(6):
                print(arreglo_sala[x][y], end=" ")
            print()
        while True:
            while True:
                try:
                    fila = int(input("\nIndique número de fila (1-5): "))
                    if fila >= 1 and fila <=5:
                        break
                    else:
                        print("FILA INEXISTENTE!")
                except:
                    print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            while True:
                try:
                    columna = int(input("Indique número de columna: "))
                    if columna >= 1 and columna <=6:
                        break
                    else:
                        print("COLUMNA INEXISTENTE!")
                except:
                    print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            if arreglo_sala[fila-1][columna-1] == 0:
                    arreglo_sala[fila-1][columna-1] = 1
                    lista_filas.append(fila-1)
                    lista_columnas.append(columna-1)
                    print("ASIENTO RESERVADO CON EXITO!")
                    time.sleep(3)
                    break
            else:
                print("ASIENTO OCUPADO!")
    elif opc == 3:
        while True:
            try:
                rut = int(input("Ingrese rut del Alumno que desea eliminar (sin puntos ni digito verificador): "))
                if rut >= 1000000 and rut <= 99999999:
                    break
                else:
                    print("ERROR! RUT INCORRECTO!")
            except:
                print("ERROR! FORMATO DE RUT INCORRECTO!")
        if rut in lista_ruts:
            for x in range(len(lista_ruts)):
                if rut == lista_ruts[x]:
                    posicion_encontrada = x
                    break
            lista_ruts.pop(posicion_encontrada)
            lista_correos.pop(posicion_encontrada)
            lista_nombres.pop(posicion_encontrada)
            arreglo_sala[lista_filas[posicion_encontrada]][lista_columnas[posicion_encontrada]] = 0
            lista_filas.pop(posicion_encontrada)
            lista_columnas.pop(posicion_encontrada)
            print("ALUMNO ELIMINADO CON EXITO!")
            time.sleep(3)
        else:
            print("ALUMNO NO EXISTE EN LA CLASE!")
    elif opc == 4:
        lista_ruts = []
        lista_nombres = []
        lista_correos = []
        lista_filas = []
        lista_columnas = []
        arreglo_sala = numpy.zeros((5,6),int)
        print("Clase finalizada!")
        time.sleep(3)
    else:
        break