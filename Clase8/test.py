carga = 0
for x in range(101):
    print(f"Cargando programa, por favor espere: {x}% Completado")
    carga += 1
    time.sleep(0.1)
    os.system("cls")