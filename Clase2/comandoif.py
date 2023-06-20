#Comando IF de python:

ranking = input("Ingrese su rango(bronce, plata, oro, diamante, retador)")

if ranking == "bronce":
    print("Debes esforzarte más")
elif ranking == "plata":
    print("Siga subiendo, puede mejorar!")
elif ranking == "oro":
    print("Felicidades")
else:
    print("Eres muy bueno!")