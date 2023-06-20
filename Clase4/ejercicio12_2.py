import os
os.system("cls")
import time
estudiante = False
funcionario = False
total = 0
print("Hola! Bienvenidx al sistema de mesón del CineDuoc!")
while True:
 pertenece_a_duoc = input("Usted pertenece a Duoc? (si/no): ")
 if pertenece_a_duoc.lower() == "si":
     while True:
      persona = float(input("¿Es usted Estudiante o Funcionario? (1. para Estudiante, 2. para Funcionario): "))
      if persona == 1:
         estudiante = True
         break
      elif persona == 2:
         funcionario = True
         break
      else:
        print("ERROR! Ingrese opción valida!")
        time.sleep(1)
        os.system("cls")
     break
 elif pertenece_a_duoc.lower() == "no":
    pass
    break
 else:
    print("ERROR! Escriba una opción valida")
    time.sleep(1)
os.system("cls")
while True:
   entrada = float(input("¿Qué tipo de entrada desea? (1. Estreno, 2. Normal): "))
   if entrada == 1:
      precio_entrada = 4800
      break
   elif entrada == 2:
      precio_entrada = 2900
      break
   else:
      print("ERROR! Debe ingresar un tipo de entrada correcta!")
      time.sleep(1)
os.system("cls")
while True:
   cantidad_entrada = float(input("¿Cuantas entradas va a comprar?: "))
   if cantidad_entrada > 0:
      break
   else:
      print("ERROR! Debe ingresar la cantidad de entradas que desea comprar!")
      time.sleep(1)
if estudiante == True or funcionario == True:
   precio_entrada = precio_entrada * 0.7
os.system("cls")
while True:
   palomitas = input("¿Desea llevar palomitas? (si/no): ")
   if palomitas.lower() == "si":
      while True:
         print("Tamaños de palomitas disponibles: \n 1. Pequeña \n 2. Mediana \n 3. Grande")
         tipo_de_palomita = float(input("¿Que tamaño de palomita va a llevar?: "))
         if tipo_de_palomita == 1:
            precio_palomita = 2500
            break
         elif tipo_de_palomita == 2:
            precio_palomita = 4500
            break
         elif tipo_de_palomita == 3:
            precio_palomita = 7800
            break
         else:
            print("ERROR! Debe ingresar un tamaño de palomitas valido!")
            time.sleep(1)
      break
   elif palomitas.lower() == "no":
      precio_palomita = 0
      break
   else:
      print("ERROR! Ingrese una opción valida")
      time.sleep(1)
os.system("cls")
while True:
   bebida = input("¿Desea llevar alguna bebida? (si/no): ")
   if bebida.lower() == "si":
      while True:
         print("Tipos de bebida disponibles: \n 1. Pequeña \n 2. Mediana \n 3. Grande")
         tipo_de_bebida = float(input("¿Que tipo de bebida desea llevar?: "))
         if tipo_de_bebida == 1:
            precio_bebida = 1000
            break
         elif tipo_de_bebida == 2:
            precio_bebida = 1250
            break
         elif tipo_de_bebida == 3:
            precio_bebida = 2000
            break
         else:
            print("ERROR! Debe ingresar un tipo de bebida")
            time.sleep(1)
      break
   elif bebida.lower() == "no":
      precio_bebida = 0
      break
   else:
      print("ERROR! Ingrese una opción valida.")
      time.sleep(1)
os.system("cls")
total = (precio_entrada*cantidad_entrada) + (tipo_de_palomita*precio_palomita) + (tipo_de_bebida*precio_bebida)
while True:
   print(f"El total a pagar es de ${round(total)}.")
   efectivo = float(input("¿Con cuánto dinero va a pagar?: "))
   if efectivo < total:
      print("El dinero ingresado es insuficiente, intente nuevamente!")
      time.sleep(1)
   else:
      vuelto = efectivo - total
      print(f"Su vuelto es de ${round(vuelto)}. Gracias por comprar en CineDuoc")
      break