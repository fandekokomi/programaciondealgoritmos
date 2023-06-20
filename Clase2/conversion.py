moneda_origen = input("Ingrese la moneda que quiere convertir (AUD, ARS, JPY): ").upper()
cantidad_origen = float(input("Ingrese la cantidad que desea convertir: "))

tasa_aud_clp = 538.49
tasa_ars_clp = 3.70
tasa_jpy_clp = 5.96

if moneda_origen == "AUD":
    cantidad_destino = cantidad_origen * tasa_aud_clp
    moneda_destino = "CLP"
elif moneda_origen == "ARS":
    cantidad_destino = cantidad_origen * tasa_ars_clp
    moneda_destino = "CLP"
elif moneda_origen == "JPY":
    cantidad_destino = cantidad_origen * tasa_jpy_clp
    moneda_destino = "CLP"
else:
    print("Moneda ingresada no válida.")

print(f"{cantidad_origen} {moneda_origen} son equivalentes a {cantidad_destino} {moneda_destino}.")