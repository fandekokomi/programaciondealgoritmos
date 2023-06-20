import os
import time
import msvcrt
os.system("cls")
estudiante = False
funcionario = False
total = 0

#PRECIOS:
precio_entradanormal = 2900
precio_entradaestreno = 4800
precio_palomitapeq = 2500
precio_palomitamed = 4500
precio_palomitagra = 7800
precio_bebidapeq = 1000
precio_bebidamed = 1250
precio_bebidagra = 2000

#ACUMULADORES:
acum_entradanormal = 0
acum_entradaestreno = 0
acum_palomitapeq = 0
acum_palomitamed = 0
acum_palomitagra = 0
acum_bebidapeq = 0
acum_bebidamed = 0
acum_bebidagra = 0

acum_totalentradanormal = 0
acum_totalentradaestreno = 0
acum_totalpalomitapeq = 0
acum_totalpalomitamed = 0
acum_totalpalomitagra = 0
acum_totalbebidapeq = 0
acum_totalbebidamed = 0
acum_totalbebidagra = 0

#DESARROLLO
while True:
    print("Hola! Bienvenidx al sistema de mesón del CineDuoc!")
    print("""MENÚ
    1. Comprar Entradas
    2. Comprar palomitas
    3. Comprar bebidas
    4. Pagar
    5. Salir""")
    while True:
        try:
            opc = int(input("Indique opción: "))
            if opc in(1,2,3,4,5):
                break
            else:
                print("ERROR! opción incorrecta!")
        except:
            print("ERROR! Debe ingresar un número entero!")
    if opc == 1:
        print(f"ENTRADAS\nEstreno(E): ${precio_entradaestreno}\nNormal(N): ${precio_entradanormal}")
        while True:
            entrada = input("Indique tipo de entrada (E,N): ")
            if entrada.upper() in("E", "N"):
                break
            else:
                print("ERROR! Elija una opcion correcta!")
        while True:
            try:
                cantidad = int(input("Indique cantidad: "))
                if cantidad >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número mayor o igual a cero.")
            except:
                print("ERROR! Debe ingresar un número entero!")
        if entrada.upper() == "E":
            acum_entradaestreno += cantidad
            acum_totalentradaestreno += precio_entradaestreno*cantidad
        else:
            acum_entradanormal += cantidad
            acum_totalentradanormal += precio_entradanormal*cantidad
    elif opc == 2:
        while True:
            print(f"""PALOMITAS
            1. Pequeñas: ${precio_palomitapeq}
            2. Medianas: ${precio_palomitamed}
            3. Grandes: ${precio_palomitagra}
            4. Volver al menú principal""")
            while True:
                try:
                    opc_pal = int(input("Indique opción: "))
                    if opc_pal in(1,2,3,4):
                        break
                    else:
                        print("ERROR! Debe ingresar una opción valida!")
                except:
                    print("ERROR! Debe ingresar un número entero!")
            if opc_pal == 1:
                while True:
                    try:
                        cantidad = int(input("Indique cantidad: "))
                        if cantidad >= 0:
                            break
                        else:
                            print("ERROR! Debe ingresar un número mayor o igual a cero.")
                    except:
                        print("ERROR! Debe ingresar un número entero!")
                acum_palomitapeq += cantidad
                acum_totalpalomitapeq += precio_palomitapeq*cantidad
            elif opc_pal == 2:
                while True:
                    try:
                        cantidad = int(input("Indique cantidad: "))
                        if cantidad >= 0:
                            break
                        else:
                            print("ERROR! Debe ingresar un número mayor o igual a cero.")
                    except:
                        print("ERROR! Debe ingresar un número entero!")
                acum_palomitamed+= cantidad
                acum_totalpalomitamed += precio_palomitamed*cantidad
            elif opc_pal == 3:
                while True:
                    try:
                        cantidad = int(input("Indique cantidad: "))
                        if cantidad >= 0:
                            break
                        else:
                            print("ERROR! Debe ingresar un número mayor o igual a cero.")
                    except:
                        print("ERROR! Debe ingresar un número entero!")
                acum_palomitagra += cantidad
                acum_totalpalomitagra += precio_palomitagra*cantidad
            else:
                break
    elif opc == 3:
        while True:
            print(f"""BEBIDAS
            1. Pequeñas: ${precio_bebidapeq}
            2. Medianas: ${precio_bebidamed}
            3. Grandes: ${precio_bebidagra}
            4. Volver al menú principal""")
            while True:
                try:
                    opc_beb = int(input("Indique opción: "))
                    if opc_beb in(1,2,3,4):
                        break
                    else:
                        print("ERROR! Debe ingresar una opción valida!")
                except:
                    print("ERROR! Debe ingresar un número entero!")
            if opc_beb == 1:
                while True:
                    try:
                        cantidad = int(input("Indique cantidad: "))
                        if cantidad >= 0:
                            break
                        else:
                            print("ERROR! Debe ingresar un número mayor o igual a cero.")
                    except:
                        print("ERROR! Debe ingresar un número entero!")
                acum_bebidapeq += cantidad
                acum_totalbebidapeq += precio_bebidapeq*cantidad
            elif opc_beb == 2:
                while True:
                    try:
                        cantidad = int(input("Indique cantidad: "))
                        if cantidad >= 0:
                            break
                        else:
                            print("ERROR! Debe ingresar un número mayor o igual a cero.")
                    except:
                        print("ERROR! Debe ingresar un número entero!")
                acum_bebidamed+= cantidad
                acum_totalbebidamed += precio_bebidamed*cantidad
            elif opc_beb == 3:
                while True:
                    try:
                        cantidad = int(input("Indique cantidad: "))
                        if cantidad >= 0:
                            break
                        else:
                            print("ERROR! Debe ingresar un número mayor o igual a cero.")
                    except:
                        print("ERROR! Debe ingresar un número entero!")
                acum_bebidagra += cantidad
                acum_totalbebidagra += precio_bebidagra*cantidad
            else:
                break
    elif opc == 4:
        subtotal = acum_totalentradanormal+acum_totalentradaestreno+acum_totalpalomitapeq+acum_totalpalomitamed+acum_totalpalomitagra+acum_totalbebidapeq+acum_totalbebidamed+acum_totalbebidagra
        if subtotal == 0:
            print("Agregué productos a su compra")
        else:
            duoc = input("Pertenece a Duoc(SI, NO.): ")
            if duoc.upper() == "SI":
                descuento = round((acum_entradaestreno+acum_entradanormal)*0.3)
            else:
                descuento = 0
            total = subtotal - descuento
            print("Su total a pagar es: $", total)
    else:
        break