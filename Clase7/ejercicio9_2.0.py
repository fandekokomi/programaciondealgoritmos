#EJERCICIO 9
import os
import time
import msvcrt
precio_churrasco = 1500
precio_completo = 1000
precio_vegetariano = 2000
precio_barrosluco = 3000
acumulador = 0
while True:
    os.system("cls")
    print(f"""Menú
    1. Churrasco ${precio_churrasco}
    2. Completo ${precio_completo}
    3. Vegetariano ${precio_vegetariano}
    4. Barros Luco ${precio_barrosluco}
    5. Total y salir""")
    while True:
        try:
            opcion = int(input("Indique opción del menú: "))
            if opcion in(1,2,3,4,5):
                break
            else:
                print("ERROR! La opción debe ser 1,2,3,4,5!")
        except:
            print("ERROR! Debe ingresar un número entero!")
    if opcion == 1:
        while True:
            os.system("cls")
            try:
                cantidad = int(input("Ingrese cantidad churrascos a comprar: "))
                if cantidad >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número entero")
        total_churrascos = cantidad*precio_churrasco
        acumulador = acumulador + total_churrascos
        print(f"Se agregó {cantidad} churrascos:", total_churrascos)
    elif opcion == 2:
        while True:
            os.system("cls")
            try:
                cantidad = int(input("Ingrese cantidad completos a comprar: "))
                if cantidad >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número entero")
        total_completos = cantidad*precio_completo
        acumulador = acumulador + total_completos
        print(f"Se agregó {cantidad} completos:", total_completos)
    elif opcion == 3:
        while True:
            os.system("cls")
            try:
                cantidad = int(input("Ingrese cantidad de vegetariano a comprar: "))
                if cantidad >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número entero")
        total_vegetariano = cantidad*precio_vegetariano
        acumulador = acumulador + total_vegetariano
        print(f"Se agregó {cantidad} vegetariano:", total_vegetariano)
    elif opcion == 4:
        while True:
            os.system("cls")
            try:
                cantidad = int(input("Ingrese cantidad barros luco a comprar: "))
                if cantidad >= 0:
                    break
                else:
                    print("ERROR! Debe ingresar un número entero positivo y si no va a comprar digite 0!")
            except:
                print("ERROR! Debe ingresar un número entero")
        total_barrosluco = cantidad*precio_barrosluco
        acumulador = acumulador + total_barrosluco
        print(f"Se agregó {cantidad} barrosluco:", total_barrosluco)
    else:
        cupon = input("Ingrese cupón 5(si no tiene cupón, presione enter): ")
        if cupon.upper()  == "PGY1121":
            acumulador = round(acumulador*0.9)
        print("El total a pagar es:", acumulador)
        break
    time.sleep(2)