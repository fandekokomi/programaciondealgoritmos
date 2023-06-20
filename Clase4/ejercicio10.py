"""en el contexto del coronavirus, una persona ha decidico
fabricar mascarillas lavables para la venta online. Las
mascarillas tienen un valor de $500 pero podria variar según
la demanda. Si la compra es superior a $15000 el envio es
gratis, en caso contrario:
-Si es de la misma comuna el envio es de $1000
-Si es de una comuna aledaña $2000
-En otro caso es de $3000
Determine el total a pagar por una persona que requiere X
cantidad de mascarilla"""
mascarilla = 500
import os
os.system("cls")
import time
print("Bienvenido! a la venta de mascarillas online :)")
time.sleep(0.5)
cantidad = int(input("¿Cuantas mascarillas desea? "))
time.sleep(0.5)
comuna = input("¿Cual es su comuna? ")
os.system("cls")
valor = cantidad * mascarilla
envio = 0
if valor > 15000:
    print("Su envio es gratis!")
elif comuna.lower() == 'puente alto' and valor < 15000:
    envio = 1000
    print("Su envio cuesta $1.000")
elif comuna.lower() == 'aledaña'and valor < 15000:
    envio = 2000
    print("Su envio cuesta $2.000")
else:
    envio = 3000
    print("Su envio cuesta $3.000")
time.sleep(2)
os.system("cls")
total = valor + envio
print(f"Su total a pagar es: ${total}, Gracias por comprar!")