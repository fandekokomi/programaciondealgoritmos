import os
os.system("cls")
import time
precio_agua = 600
precio_azucar = 1200
precio_aceite = 1500
precio_arroz = 1250
precio_fideos = 790
precio_bebida = 1780
precio_chocolate = 2500
precio_pan_molde = 1340
acumulador = 0
cantidad_agua = 0
cantidad_azucar = 0
cantidad_aceite = 0
cantidad_arroz = 0
cantidad_fideos = 0
cantidad_bebida = 0
cantidad_chocolate = 0
cantidad_pan_molde = 0

while True:
    print(f"""Menú del supermercado: 
    1. Agua: ${precio_agua}
    2. Azúcar: ${precio_azucar}
    3. Aceite: ${precio_aceite}
    4. Arroz: ${precio_arroz}
    5. Fideos: ${precio_fideos}
    6. Bebida: ${precio_bebida}
    7. Chocolate: ${precio_chocolate}
    8. Pan de molde: ${precio_pan_molde}
    9. Total o salir""")
    while True:

        try:
            opcion = int(input("Elija una opción: "))
            if opcion in(1,2,3,4,5,6,7,8,9):
                break
            else:
                print("ERROR! La opción debe ser entre 1,2,3,4,5,6,7,8,9. OBLIGATORIO!!!")
        except:
            print("ERROR! Debe ingresar un número entero!")
    if opcion == 9:
        break
    if opcion == 1:
        while True:
            os.system("cls")
            try:
                cantidad_agua = int(input("Ingrese cantidad de Agua a comprar: "))
                if cantidad_agua >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número cero o mayor.")
        total_agua = cantidad_agua*precio_agua
        acumulador = acumulador + total_agua
        print(f"Se agregó {cantidad_agua} de Agua: ${total_agua}")
    elif opcion == 2:        
        while True:
            os.system("cls")
            try:
                cantidad_azucar = int(input("Ingrese cantidad de Azúcar a comprar: "))
                if cantidad_azucar >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número cero o mayor.")
        total_azucar = cantidad_azucar*precio_azucar
        acumulador = acumulador + total_azucar
        print(f"Se agregó {cantidad_azucar} de Azúcar: ${total_azucar}")
    elif opcion == 3:
        while True:
            os.system("cls")
            try:
                cantidad_aceite = int(input("Ingrese cantidad de Aceite a comprar: "))
                if cantidad_aceite >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número cero o mayor.")
        total_aceite = cantidad_aceite*precio_aceite
        acumulador = acumulador + total_aceite
        print(f"Se agregó {cantidad_aceite} de Aceite: ${total_aceite}")
    elif opcion == 4:
        while True:
            os.system("cls")
            try:
                cantidad_arroz = int(input("Ingrese cantidad de Arroz a comprar: "))
                if cantidad_arroz >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número cero o mayor.")
        total_arroz = cantidad_arroz*precio_arroz
        acumulador = acumulador + total_arroz
        print(f"Se agregó {cantidad_arroz} de Arroz: ${total_arroz}")
    elif opcion == 5:
        while True:
            os.system("cls")
            try:
                cantidad_fideos = int(input("Ingrese cantidad de Fideos a comprar: "))
                if cantidad_fideos >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número cero o mayor.")
        total_fideos = cantidad_fideos*precio_fideos
        acumulador = acumulador + total_fideos
        print(f"Se agregó {cantidad_fideos} de Fideos: ${total_fideos}")
    elif opcion == 6:
        while True:
            os.system("cls")
            try:
                cantidad_bebida = int(input("Ingrese cantidad de Bebida a comprar: "))
                if cantidad_bebida >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número cero o mayor.")
        total_bebida = cantidad_bebida*precio_bebida
        acumulador = acumulador + total_bebida
        print(f"Se agregó {cantidad_bebida} de Bebida: ${total_bebida}")
    elif opcion == 7:
        while True:
            os.system("cls")
            try:
                cantidad_chocolate = int(input("Ingrese cantidad de Chocolate a comprar: "))
                if cantidad_chocolate >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número cero o mayor.")
        total_chocolate = cantidad_chocolate*precio_chocolate
        acumulador = acumulador + total_chocolate
        print(f"Se agregó {cantidad_chocolate} de Chocolate: ${total_chocolate}")
    elif opcion == 8:
        while True:
            os.system("cls")
            try:
                cantidad_pan_molde = int(input("Ingrese cantidad de Pan de Molde a comprar: "))
                if cantidad_pan_molde >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número cero o mayor.")
        total_pan_molde = cantidad_pan_molde*precio_pan_molde
        acumulador = acumulador + total_pan_molde
        print(f"Se agregó {cantidad_pan_molde} de Pan de molde: ${total_pan_molde}")
    time.sleep(2)
    os.system("cls")
if acumulador > 0:
    while True:
        es_preferencial = input("¿Es usted preferencial? (Responda con un si o no.): ")
        if es_preferencial.upper() == "SI":
            preferencial = True
            break
        elif es_preferencial.upper() == "NO":
            preferencial = False
            break
        else:
            print("ERROR! Debe responder si usted es preferencial o no, SOLO CON UN (SI) o (NO).")
    if preferencial == True:
        print("Se le dará un descuento del 25%")
        total_con_descuento = acumulador * 0.75
    while True:
        print(f"El total a pagar es ${acumulador}")
        try:
            efectivo = int(input("Ingrese el efectivo: "))
            if efectivo >= acumulador and preferencial == True:
                vuelto = efectivo - acumulador
                print(f"""
                ------------------------------------------
                BOLETA
                ------------------------------------------
                PRODUCTO | UNIDADES | PRECIO
                ------------------------------------------
                AGUA | {cantidad_agua} X ${precio_agua}
                AZÚCAR | {cantidad_azucar} X ${precio_azucar}
                ACEITE | {cantidad_aceite} X ${precio_aceite}
                ARROZ | {cantidad_arroz} X ${precio_arroz}
                FIDEOS | {cantidad_fideos} X ${precio_fideos}
                BEBIDA | {cantidad_bebida} X ${precio_bebida}
                CHOCOLATE | {cantidad_chocolate} X ${precio_chocolate}
                PAN DE MOLDE | {cantidad_pan_molde} X ${precio_pan_molde}
                --------------------------------------------
                SUBTOTAL: ${acumulador}
                --------------------------------------------
                TOTAL: ${total_con_descuento}
                """)
                print(f"Gracias por su compra. Su vuelto es: ${round(vuelto)}")
                break
            elif efectivo >= acumulador and preferencial == False:
                vuelto = efectivo - acumulador
                print(f"""
                ------------------------------------------
                BOLETA
                ------------------------------------------
                PRODUCTO | UNIDADES | PRECIO
                ------------------------------------------
                AGUA | {cantidad_agua} X ${precio_agua}
                AZÚCAR | {cantidad_azucar} X ${precio_azucar}
                ACEITE | {cantidad_aceite} X ${precio_aceite}
                ARROZ | {cantidad_arroz} X ${precio_arroz}
                FIDEOS | {cantidad_fideos} X ${precio_fideos}
                BEBIDA | {cantidad_bebida} X ${precio_bebida}
                CHOCOLATE | {cantidad_chocolate} X ${precio_chocolate}
                PAN DE MOLDE | {cantidad_pan_molde} X ${precio_pan_molde}
                --------------------------------------------
                SUBTOTAL: ${acumulador}
                --------------------------------------------
                TOTAL: ${acumulador}
                """)
                print(f"Gracias por su compra. Su vuelto es: ${round(vuelto)}")
                break
            else:
                print("Dinero insuficiente, Guardias!")
                break
        except:
            print("ERROR! Debe ingresar un monto valido!")
else:
        print("Gracias por su visita")