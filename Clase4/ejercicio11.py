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

total_compra = 0
lleva_producto = ""
es_preferencial = ""

lleva_producto = input("¿Desea llevar algún producto? (si/no): ")
if lleva_producto.lower() == "si":
  print("Productos disponibles:")
  time.sleep(0.5)
  print("1. Agua ($600)")
  time.sleep(0.5)
  print("2. Azúcar ($1200)")
  time.sleep(0.5)
  print("3. Aceite ($1500)")
  time.sleep(0.5)
  print("4. Arroz ($1250)")
  time.sleep(0.5)
  print("5. Fideos ($790)")
  time.sleep(0.5)
  print("6. Bebida ($1780)")
  time.sleep(0.5)
  print("7. Chocolate ($2500)")
  time.sleep(0.5)
  print("8. Pan molde ($1340)")
  time.sleep(0.5)
  cant_agua = int(input("Ingrese la cantidad de Agua: "))
  cant_azucar = int(input("Ingrese la cantidad de Azúcar: "))
  cant_aceite = int(input("Ingrese la cantidad de Aceite: "))
  cant_arroz = int(input("Ingrese la cantidad de Arroz: "))
  cant_fideos = int(input("Ingrese la cantidad de Fideos: "))
  cant_bebida = int(input("Ingrese la cantidad de Bebida: "))
  cant_chocolate = int(input("Ingrese la cantidad de Chocolate: "))
  cant_pan_molde = int(input("Ingrese la cantidad de Pan molde: "))
  # Calculo del total de compra
  total_compra = (cant_agua * precio_agua) + (cant_azucar * precio_azucar) + (cant_aceite * precio_aceite) + (cant_arroz * precio_arroz) + (cant_fideos * precio_fideos) + (cant_bebida * precio_bebida) + (cant_chocolate * precio_chocolate) + (cant_pan_molde * precio_pan_molde)
  es_preferencial = input("¿Es preferencial? (si/no): ")
  #Descuento del preferencial
  if es_preferencial.lower() == "si":
   total_compra *= 0.75
  efectivo = int(input("Ingrese el efectivo: "))
  if efectivo >= total_compra:
   vuelto = efectivo - total_compra
   print(f"Gracias por su compra. Su vuelto es: ${round(vuelto)}")
  else:
   print("Dinero insuficiente, Guardias!")
else:
  print("Gracias por su visita")