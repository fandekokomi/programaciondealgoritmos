total = 0
cont = 0

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese un último número: "))

if num1>0 and num1%2==0:
    total=total+num1
else:
    cont=cont+1
if num2>0 and num2%2==0:
    total=total+num2
else:
    cont=cont+1
if num3>0 and num3%2==0:
    total=total+num3
else:
    cont=cont+1
print(f"La suma de los números es {total} y la cuenta es {cont}")