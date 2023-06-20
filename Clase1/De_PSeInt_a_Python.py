#sigueme en instagram como @fandekokomi.
"""También unete a mi servidor de discord:
https://www.discord.gg/b8aqvmuSj6"""

#Use el Hashtag (gato) para comentar.

"""
Use tres comillas para comentar más parrafos seguidos,
sin complicaciones,
para evitar usar el # en estos casos.
"""

#Variables con tipos de datos:
"""
PSeInt: Caracter --> Python: Str() / String se utiliza para representar texto, más conocido en el mundo de la programación como string o cadena de caracteres.
PSeInt: Entero --> Python: int() / Integer son un tipo de datos que permite representar números enteros, es decir, positivos y negativos no decimales.
PSeInt: Real --> Python: float() / Float permite representar un número positivo o negativo con decimales, es decir, números reales.
PSeInt: Lógico --> Python: bool() / Boolean convierte un valor x en su equivalente booleano según el procedimiento de prueba de veracidad (Verdadero/True o Falso/False).
PSeInt: ??? --> Python: chr() / Chr devuelve el carácter que representa el Unicode especificado.
PSeInt: Escribir --> print("") / Print imprime el mensaje especificado en la pantalla.
"""

nombre = "" #Python entiende automáticamente que esto es un String.
edad = 20 #Python entenderá automáticamente que esto es Integer.
#Si está escrito así: 
edadd = "20"
#Python determinará que es un String (Se deben quitar las comillas para definirlo como Integer).
altura = 1.7 #Python determinará que esta variable es un Float.

"""
Si le pasan una variable que está entre comillas puede usar el () para definirlo.
Ejemplo:
edad = int(19).
"""

"""
Ejemplo de Verdadero o Falso:
Use True o False para definirlo como Booleano.
True = Verdadero y False = Falso
"""
tiene_mascotas = True

"""
El termino None es para definir la variable
Si le paso algún valor, ya sea Número para definirlo como interger, 
letras para definirlo como String y así.
"""
rut = None

#Puede usar tanto comilla simple como comillas dobles para definir una variable como String.
nombre = 'Jorge'
nombre = "Raul"

#Constante:
#Se usa para saber que el valor no se debe modificar.
IVA = 0.19
#tambien puede escribir la variable así:
c_iva = 0.19
#Esto solo son prácticas.

#Diferencias:
#Puede usar comillas dobles para evitar esto:
"""region = 'O'higgins'"""
#Aquí la segunda comilla cierra la primera.
#Solución:
region = "O'higgins"

#Comandos:
print("Hola!")
print("Bienvenido",nombre,"que tengas un buen día")
#Puedes poner f entre el ( y la " para buscar una palabra y que Python la use como variable.
#Debes encerrar entre llaves "{}" lo que quieres que se traduzca a variable.
#Ejemplo:
print(f"Bienvenido {nombre} cuya edad es {edad}")

#Operaciones Matemáticas:
resultado = 5 + 4 #Suma
print(resultado)
resultado = 1-7 #Resta
print(resultado)
resultado = 5*5 #Multiplicación
print(resultado)
resultado = 8/2 #División
print(resultado)
resultado = 2**4 #Potencia con 2 signos *
print(resultado)
resultado = 8//2 #División que considera solo parte entera.
print(resultado)
resultado = 7%2 #Sacar módulo con signo de %.
print(resultado)

#Python puede sumar palabras y además puede multiplicarlos.
resultado = "hola" + "mundo"
print(resultado)
resultado = "hola" * 3
print(resultado)

#Se pueden sumar variables siempre que sean del mismo tipo.
resultado = nombre + region #Ambos son del tipo String.

"""
Puedes Sumar, Restar, Multiplicar, Dividir, Potenciar, Sacar modulo de los números.
Además solamente sumar y multiplicar palabras.
"""

#Transformar variable Interger a String.
print("Bienvenido " + str(edad))