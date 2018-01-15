# Autor: José Francisco Murillo Lozano A01374561
# Calcula el área de la figura
import math

radio = int(input("Radio: "))
altura = int(input("Altura: "))
pi = math.pi

areaSemicirculo = ((pi*radio**2)/2)
areaTriangulo = radio*altura

areaTotal = areaSemicirculo+areaTriangulo

print("Area = ", areaTotal)