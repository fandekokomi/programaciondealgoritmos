#Ejercicio 1 IF:
print("Ingrese su edad")
edad = int(input())

if edad < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")

#Ejercicio 2 IF:
user_1 = "pedro"
pass_1 = "1234"
user_2 = "angel"
pass_2 = "a4s1"

print("Inicio de sesión")
print("Ingrese su usuario:")
usuario = input()
print("Ingrese su contraseña:")
contrasenia = input()

if usuario == user_1 and contrasenia == pass_1:
    print("Bienvenido! Usuario 1")
elif usuario == user_2 and contrasenia == pass_2:
    print("Bienvenido! Usuario 2")
else:
    print("Cuenta incorrecta! el acceso no esta disponible.")