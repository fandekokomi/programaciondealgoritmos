#Ejercicio 9
import os
os.system("cls")
import time
precio_churrascos = 1500
precio_completos = 1000
precio_vegetariano = 2000
precio_barrosluco = 3000
print(f"Hola, bienvenidx! al nuevo delivery, por favor escriba que tipo de sandwishes quiere!: ")
#tambien pueden ser con triple comillas dentro de un print.
time.sleep(1)
print(f"Carta del delivery: \n1. Churrascos: ${precio_churrascos} \n2. Completos: ${precio_completos} \n3. Vegetariano: ${precio_vegetariano} \n4. Barros Luco: ${precio_barrosluco}")
cant_churrascos = int(input("Ingrese cantidad de churrascos a comprar: "))
cant_completos = int(input("Ingrese cantidad de completos a comprar: "))
cant_vegetariano = int(input("Ingrese cantidad de vegetarianos a comprar: "))
cant_barrosluco = int(input("Ingrese cantidad de barros luco a comprar: "))

total = precio_churrascos*cant_churrascos + precio_completos*cant_completos + precio_vegetariano*cant_vegetariano + precio_barrosluco*cant_barrosluco
os.system("cls")
codigo = input("Ingrese su código de descuento: ")
if codigo.upper() == "PGY1121":
    total = round(total * 0.9)
print("Su total a pagar es:",total)