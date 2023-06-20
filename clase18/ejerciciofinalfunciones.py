import msvcrt as tecla
import re
def menu():
    print("""MENÚ CINE:
    1. Ver Sala
    2. Comprar
    3. Ver asiento
    4. Cancelar compra
    5. Salir""")
    opcion = v_opcion(1,5)
    return opcion
def v_opcion(min:int, max:int):
    while True:
        try:
            opc = int(input("Ingrese opción (Unicamente entre 1 a 5.): "))
            if opc >= min and opc <= max:
                return opc
            else:
                print("ERROR! Opción incorrecta!")
        except:
            print("ERROR! Debe ingresar unicamente digitos enteros!")
def versala(cine):
    print("   SALA DE CINE")
    for x in range(12):
        for y in range(6):
            print("",cine[x][y], end=" ")
        print()
    print("Presione una tecla para continuar...")
    tecla.getch()
def vrut():
    while True:
        try:
            rut = int(input("Ingrese su rut (sin puntos pero con digito verificador): "))
            if len(str(rut)) >= 8 and len(str(rut)) <= 9:
                return rut
        except:
            print("ERROR! Formato de RUT incorrecto! DEBE TENER 8 O 9 DIGITOS.")
def vcorreo():
    while True:
        correo = input("Ingrese su correo: ")
        if es_correo_valido(correo) == True:
            return correo
        else:
            print("Correo Invalido!")

def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

def vtelefono():
    while True:
        try:
            tel = int(input("Ingrese su número de teléfono: "))
            if len(str(tel)) == 9 and '9' == str(tel)[0]:
                return tel
            else:
                print("FORMATO DE TELÉFONO INCORRECTO!")
                
        except:
            print("ERROR! Debe ingresar un número de 9 digitos")