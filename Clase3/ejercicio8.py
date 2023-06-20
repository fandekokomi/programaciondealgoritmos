zapatos_a_comprar = int(input("Ingrese cantidad de zapatos que quiere comprar: "))
subtotal = 20000*zapatos_a_comprar
if subtotal >= 40000:
    total = subtotal
else:
    total = subtotal + 3000
print(f"El total de su compra es ${total}")