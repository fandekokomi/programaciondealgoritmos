#ejercicio Juan Maestro:

#se debe crear una lista por cada valor solicitado de un cliente:
lista_ruts = []
lista_nombres = []
lista_direcciones = []
lista_comunas = []
lista_correos = []
lista_edades = []
lista_generos = []
lista_celulares = []
lista_tipos = []
lista_suscripciones = []

#comienzo del ejercicio con un menú:
while True:
    #mostrar las opciones del menú:
    print("""Juan Maestro App
    1. Registrar Cliente
    2. Suscripción
    3. Consultar Datos Cliente
    4. Eliminar Cliente
    5. Salir""")
    #ingreso de la opción del menú:
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5):
                break
            else:
                print("ERROR! OPCIÓN FUERA DE RANGO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
    #if que valida cada una de las opciones ingresadas por el usuario:
    if opcion==1:
        while True:
            try:
                rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
                if rut >= 4000000 and rut <= 99999999:
                    break
                else:
                    print("ERROR! EL RUT DEBE ESTAR ENTRE 4000000 Y 99999999!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        nombre = input("Ingrese nombre: ")
        direccion = input("Ingrese dirección: ")
        comuna = input("Ingrese comuna: ")
        while True:
            correo = input("Ingrese correo: ")
            if "@" in correo:
                break
            else:
                print("ERROR! CORREO INCORRECTO!")
        while True:
            try:
                edad = int(input("Ingrese edad: "))
                if edad >= 0 and edad <= 110:
                    break
                else:
                    print("ERROR! LA EDAD DEBE ESTAR ENTRE 0 Y 110!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        while True:
            genero = input("Ingrese género(f:femenino, m:masculino, o:otro): ")
            if genero.upper() in("F","M","O"):
                break
            else:
                print("ERROR! EL GÉNERO DEBE SER F, M, O!")
        celular = int(input("Ingrese número celular: "))
        while True:
            tipo = input("Ingrese tipo(premium, silver, gold): ")
            if tipo.upper() in("PREMIUM","SILVER","GOLD"):
                break
            else:
                print("ERROR! EL TIPO DEBE SER PREMIUM, GOLD, SILVER!")
        
        lista_ruts.append(rut)
        lista_nombres.append(nombre)
        lista_direcciones.append(direccion)
        lista_comunas.append(comuna)
        lista_correos.append(correo)
        lista_edades.append(edad)
        lista_generos.append(genero)
        lista_celulares.append(celular)
        lista_tipos.append(tipo)
        lista_suscripciones.append("suscrito")

        print("CLIENTE REGISTRADO!")
    elif opcion==2:
        if rut not in lista_ruts:
            print("USUARIO NO ENCONTRADO EN LA APP!")
        else:
            for x in range(len(lista_ruts)):
                if rut == lista_ruts[x]:
                    posicion_encontrada = x
                    break
            fecha = input("Ingrese fecha: ")
            lista_suscripciones[posicion_encontrada] = lista_suscripciones[posicion_encontrada] + " " + fecha
    elif opcion==3:
        rut = int(input("Ingrese rut: "))
        if rut in lista_ruts:
            for x in range(len(lista_ruts)):
                if rut == lista_ruts[x]:
                    posicion_encontrada = x
                    break
            print(lista_ruts[posicion_encontrada])
            print(lista_nombres[posicion_encontrada])
            print(lista_direcciones[posicion_encontrada])
            print(lista_comunas[posicion_encontrada])
            print(lista_correos[posicion_encontrada])
            print(lista_edades[posicion_encontrada])
            print(lista_generos[posicion_encontrada])
            print(lista_celulares[posicion_encontrada])
            print(lista_tipos[posicion_encontrada])
            print(lista_suscripciones[posicion_encontrada])
        else:
            print("EL RUT NO EXISTE EN LA APP!")
    elif opcion==4:
        rut = int(input("Ingrese rut: "))
        if rut in lista_ruts:
            for x in range(len(lista_ruts)):
                if rut == lista_ruts[x]:
                    posicion_encontrada = x
                    break
            lista_ruts.pop(posicion_encontrada)
            lista_nombres.pop(posicion_encontrada)
            lista_direcciones.pop(posicion_encontrada)
            lista_comunas.pop(posicion_encontrada)
            lista_correos.pop(posicion_encontrada)
            lista_edades.pop(posicion_encontrada)
            lista_generos.pop(posicion_encontrada)
            lista_celulares.pop(posicion_encontrada)
            lista_tipos.pop(posicion_encontrada)
            lista_suscripciones.pop(posicion_encontrada)
            print("Usuario eliminado!")
        else:
            print("RUT INEXISTENTE!")
    else:
        print("Gracias por suscribirse a la App de Juan Maestro...")
        break