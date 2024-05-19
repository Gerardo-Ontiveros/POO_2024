"""
 Crear un programa que permita calcular e imprimir el precio a pagar por un articulo.
 en el precio a pagar se incluye el IVA el programa debera de funcionar n veces como el usuario desee.
"""

new_product = "s"
while new_product == "s":
    price = float(input("Ingresa el precio del producto: "))
    IVA = price * .16
    price_total = price + IVA
    print(f"Subtotal: ${price}")
    print(f"IVA: ${IVA}")
    print(f"El precio total del producto es de: ${price_total}")
    print(f"deseas agregar otro producto? (S/N)")
    new_product = input("")