def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_correo():
    while True:
        correo = input("Ingrese su correo: ")
        if "@" in correo:
            return correo
        else:
            print("¡ERROR! ¡INGRESE UN CORREO VÁLIDO!")
def validar_personas(min:int,max:int):
    while True:
        try:
            personas = int(input(f"Ingrese cantidad de personas (entre {min} y {max}): "))
            if personas >= min and personas <= max:
                return personas
            else:
                print(f"¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTRE ({min}) HASTA ({max})!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_fila(min:int,max:int):
    while True:
        try:
            fila = int(input(f"Ingrese número de fila ({min},{max}):"))
            if fila >= min and fila <= max:
                return fila
            else:
                print("ERROR! FILA INCORRECTA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def validar_columna(min:int,max:int):
    while True:
        try:
            columna = int(input(f"Ingrese número de columna ({min},{max}):"))
            if columna >= min and columna <= max:
                return columna
            else:
                print("ERROR! COLUMNA INCORRECTA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def validar_columna_letras(letra1:str,letra2:str):
    while True:
        columna = input(f"Ingrese columna entre ({letra1} a {letra2}):")
        if columna.isalpha() == letra1 or columna.isalpha == letra2:
            return columna
        else:
            print("ERROR! COLUMNA INCORRECTA")
def validar_opcion(min:int,max:int):
        while True:
            try:
                opcion = int(input("Ingrese opción: "))
                if opcion >= min and opcion <= max:
                    return opcion
                else:
                    print("¡ERROR! ¡OPCIÓN INCORRECTA!")
            except:
                print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_telefono():
    while True:
        try:
            telefono = int(input("Ingrese su número de teléfono: "))
            if len(str(telefono)) == 9 and '9' == str(telefono)[0]:
                return telefono
            else:
                print("FORMATO DE TELÉFONO INCORRECTO!")
                
        except:
            print("ERROR! Debe ingresar un número de 9 digitos")
def validar_nota(num:int):
    while True:
        try:
            nota = float(input(f"Ingrese nota {num}: "))
            if nota >= 1.0 and nota <= 7.0:
                return nota
            else:
                print("ERROR! LA NOTA DEBE SER ENTRE 1.0 A 7.0!")
        except:
            print("ERROR! DEBE INGRESAR UNA NOTA VALIDA! (Ejemplo: 6.5)")
def validar_efectivo(total:int):
    while True:
        try:
            efectivo = int(input(f"El total es: ${total} \nIngrese efectivo para pagar: "))
            if efectivo < total:
                print("El dinero ingresado es insuficiente, intente nuevamente!")
            else:
                print("Gracias por pagar!")
                return efectivo
        except:
            print("Ingrese un monto valido!")
def validar_codigo(cod):
    while True:
            codigo = input("Ingrese su codigo: ")
            if codigo == cod:
                return True
            else:
                print("ERROR! El codigo ingresado no existe o ya no es valido!")
                return
def validar_region():
    while True:
        region = input("Ingrese su región: ")
        if region.lower() in ["arica y parinacota", "tarapacá", "antofagasta", "atacama", "coquimbo", "valparaíso", "metropolitana de santiago", "o'higgins", "maule", "ñuble", "biobío", "la araucanía", "los ríos", "los lagos", "aysén", "magallanes"]:
            return region
        else:
            print("La región no existe!")
def validar_comunaderegion():
    region = validar_region()
    while True:
        comuna = input("Ingrese su comuna: ")
        comunas_por_region = {
            "arica y parinacota": ["arica", "putre"],
            "tarapacá": ["iquique", "pozo almonte"],
            "antofagasta": ["antofagasta", "calama"],
            "atacama": ["copiapó", "vallenar"],
            "coquimbo": ["la serena", "coquimbo"],
            "valparaíso": ["valparaíso", "viña del mar"],
            "metropolitana de santiago": ["santiago", "puente alto"],
            "o'higgins": ["rancagua", "san fernando"],
            "maule": ["talca", "curicó"],
            "ñuble": ["chillán", "bulnes"],
            "biobío": ["concepción", "talcahuano"],
            "la araucanía": ["temuco", "padre las casas"],
            "los ríos": ["valdivia", "la unión"],
            "los lagos": ["puerto montt", "osorno"],
            "aysén": ["coyhaique", "puerto aysén"],
            "magallanes": ["punta arenas", "puerto natales"]
        }
        if comuna.lower() in comunas_por_region.get(region.lower(), []):
            return comuna
        else:
            print("La comuna no existe!")
def validar_descuento(subtotal:int,descuento:float):
    total = subtotal * descuento
    return total
def validar_edad(min:int,max:int):
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad >= min and edad <= max:
                return edad
            else:
                print(f"ERROR! La edad debe estar en un rango entre {min} y {max}")
        except:
            print("ERROR! Debe ingresar un número entero!")
def validar_contrasena():
    while True:
        contrasena = input("Ingrese una contraseña: ")
        if len(contrasena) == 8 and not contrasena.isspace():
            return contrasena
        else:
            print("ERROR! La contraseña debe tener minimo 8 caracteres y no debe consistir solo en espacios en blanco!")
def validar_DOScontrasenas():
    while True:
        contrasena = validar_contrasena()
        repetircontrasena = input("Repita la contraseña previamente ingresada: ")
        if repetircontrasena == contrasena:
            return repetircontrasena
        else:
            print("Las contraseñas no coinciden!!")
def validar_nombreusuario():
    while True:
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        if len(nombre_usuario) >= 3 and not nombre_usuario.isspace():
            return nombre_usuario
        else:
            print("ERROR! Nombre de usuario muy corto, este debe tener un minimo de 3 caracteres.")
def validar_direccion(longitud_min):
    while True:
        direccion = input("Ingrese su dirección: ")
        if direccion >= longitud_min:
            return direccion
        else:
            print("La dirección especificada no tiene el minimo de longitud requerida.")

#POR REVISAR:
#def validar_piso(min:int, max:int):
    #while True:
        #try:
            #piso = int(input(f"Ingrese piso({min}-{max}): "))
            #if piso in #lista:
                #return piso
            #else:
                #print("ERROR! PISO INCORRECTO!")
        #except:
            #print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
#def validar_departamento(letra1,letra2,letra3,letra4):
    #while True:
        #departamento = input(f"Ingrese depto({letra1},{letra2},{letra3},{letra4}): ")
        #if departamento.upper() in #lista:
            #return departamento
        #else:
            #print("ERROR! DEPARTAMENTO INCORRECTO!")