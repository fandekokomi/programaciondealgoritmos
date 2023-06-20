#EJERCICIO CLASE 14.
import os
import time
import msvcrt as tecla
os.system("cls")
#LISTAS
run_jugadores = [11111111]
nomusuario_jugadores = ["jugadordeprueba"]
tel_jugadores = [911111111]
edad_jugadores = [19]
correo_jugadores = ["jugadordeprueba@prueba.cl"]
password_jugadores = ["contraseñadeprueba"]
"""VALIDACIONES:
RUN: 7-8 DIGITOS
USUARIO: 3 CARACTERES
TELEFONO: 9 DIGITOS
EDAD: 18 O SUPERIOR
CORREO:  @
CONTRASEÑA: 6 - 18 CARACTERES
VALIDAR CONTRASEÑA 2 VECES."""
while True:
    print("""Menú:
    1. Crear Jugador
    2. Eliminar Jugador
    3. Ver datos de un Jugador
    4. Modificar correo de Jugador
    5. Ver todos los Nombres de los Jugadores
    6. Eliminar todos los Jugadores
    7. Salir""")
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in(1,2,3,4,5,6,7):
                break
            else:
                print("ERROR! Debe ingresar una opción entre 1,2,3,4,5,6 o 7.")
        except:
            print("ERROR! Debe ingresar solo números enteros positivos!")
    if opc == 1:
        os.system("cls")
        while True:
            try:
                run = int(input("Ingrese su RUN (SIN PUNTOS NI DIGITO VERIFICADOR): "))
                if len(str(run))>=7 and len(str(run))<=8:
                    break
                else:
                    print("ERROR! EL RUN DEBE TENER UN MINIMO DE 7 DIGITOS DE LARGO!.")
            except:
                print("ERROR! FORMATO DE RUN INCORRECTO! Debe ingresar digitos enteros!")
        while True:
            nom_usuario = input("Ingrese un nombre de usuario: ")
            if len(nom_usuario) >= 3:
                break
            else:
                print("ERROR! Nombre de usuario muy corto, este debe tener un minimo de 3 caracteres.")
        while True:
            try:
                tel = int(input("Ingrese su número de telefono: "))
                if len(str(tel)) == 9:
                    break
                else:
                    print("ERROR! Formato de Teléfono incorrecto, ingrese un número de teléfono valido!")
            except:
                print("ERROR! Debe ingresar digitos enteros!")
        while True:
            try:
                edad = int(input("Ingrese su edad: "))
                if edad >= 18:
                    break
                else:
                    print("ERROR! Menores de 18 años no pueden crear una cuenta!")
            except:
                print("ERROR! Debe ingresar digitos enteros positivos!")
        while True:
            correo = input("Ingrese un correo electronico: ")
            if "@" in correo:
                break
            else:
                print("ERROR! Debe ingresar un correo valido!")
        while True:
            r_password = input("Ingrese una contraseña: ")
            r2_password = input("Repita la contraseña ingresada anteriormente: ")
            if r2_password == r_password:
                password = r_password
                if len(password) >= 6 and len(password) <= 18:
                    break
                else:
                    print("La contraseña debe ser entre 6 a 18 caracteres.")
            else:
                print("ERROR! Las contraseñas ingresadas no coinciden!")
        run_jugadores.append(run)
        nomusuario_jugadores.append(nom_usuario)
        tel_jugadores.append(tel)
        edad_jugadores.append(edad)
        correo_jugadores.append(correo)
        password_jugadores.append(password)
        print("Jugador registrado correctamente!")
    elif opc == 2:
        os.system("cls")
        rut = int(input("Ingrese rut: "))
        if rut in run_jugadores:
            for x in range(len(run_jugadores)):
                if rut == run_jugadores[x]:
                    posicion_encontrada = x
                    break
        run_jugadores.pop(posicion_encontrada)
        nomusuario_jugadores.pop(posicion_encontrada)
        tel_jugadores.pop(posicion_encontrada)
        edad_jugadores.pop(posicion_encontrada)
        correo_jugadores.pop(posicion_encontrada)
        password_jugadores.pop(posicion_encontrada)
        print("Jugador eliminado correctamente!")
        time.sleep(3)
        os.system("cls")
    elif opc == 3:
        os.system("cls")
        rut = int(input("Ingrese rut: "))
        if rut in run_jugadores:
            for x in range(len(run_jugadores)):
                if rut == run_jugadores[x]:
                    posicion_encontrada = x
                    break
        os.system("cls")
        print("RUN USUARIO:",run_jugadores[posicion_encontrada])
        print("NOMBRE USUARIO:",nomusuario_jugadores[posicion_encontrada])
        print("TELÉFONO USUARIO:",tel_jugadores[posicion_encontrada])
        print("EDAD DE USUARIO:",edad_jugadores[posicion_encontrada])
        print("CORREO USUARIO",correo_jugadores[posicion_encontrada])
        print("CONTRASEÑA USUARIO: ",password_jugadores[posicion_encontrada])
        print("\nIngrese cualquier tecla para continuar...")
        tecla.getch()
        os.system("cls")
    elif opc == 4:
        os.system("cls")
        rut = int(input("Ingrese su rut: "))
        if rut in run_jugadores:
            for x in range(len(run_jugadores)):
                if rut == run_jugadores[x]:
                    posicion_encontrada = x
                    break
            while True:
                print("Su correo actual es:", correo_jugadores[posicion_encontrada])
                nuevocorreo = input("Ingrese su nuevo correo para reemplazar el actual: ")
                if "@" in nuevocorreo:
                    correo_jugadores[posicion_encontrada] = nuevocorreo
                    print("Su correo ha sido modificado con exito!")
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    print("CORREO NO VALIDO!")
                    time.sleep(1)
                    os.system("cls")
    elif opc == 5:
        os.system("cls")
        if nomusuario_jugadores == []:
            print("NO HAY JUGADORES REGISTRADOS!")
            time.sleep(2)
            os.system("cls")
        else:
            print("MOSTRANDO, Nombres de usuario de todos los Jugadores:")
            print(nomusuario_jugadores)
            print("\nPresione una tecla para continuar...")
            tecla.getch()
            os.system("cls")
    elif opc == 6:
        os.system("cls")
        while True:
            seguro = input("¿Estas Seguro de Eliminar a todos los Jugadores? (SI/NO): ")
            if seguro.upper() == "SI" or seguro.upper() == "NO":
                break
            else:
                print("ERROR! DEBE RESPONDER SOLO CON (SI / NO)")
        if seguro.upper() == "SI":
            run_jugadores = []
            nomusuario_jugadores = []
            tel_jugadores = []
            edad_jugadores = []
            correo_jugadores = []
            password_jugadores = []
            print("TODOS LOS JUGADORES HAN SIDO ELIMINADOS CON EXITO!")
            time.sleep(2)
            os.system("cls")
        else:
            print("Volviendo al Menú...")
            time.sleep(2)
            os.system("cls")
    else:
        break
