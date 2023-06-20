import os
os.system("cls")
import time
contador = 0
for c in range(101):
    print(f"Cargando programa, por favor espere: {c}% Completado")
    contador += 1
    time.sleep(0.2)
    os.system("cls")
#ejercicio 5 for
#el for de x será para las 10 tablas.
for x in range(10):
    for y in range(10):
        print(f"{x+1} X {y+1} = {(x+1)*(y+1)}")
        time.sleep(0.3)
    time.sleep(1)
    os.system("cls")
