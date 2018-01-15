# Autor: Carlos Martinez Rodriguez
# Descripción: Calcula el area de un helado de la vista lateral

radio = int(input("Ingresa el radio: "))
altura = int(input("Ingresa la altura: "))

area = (3.1416 * radio ** 2) / 2 + radio * altura

print("Area =", area)