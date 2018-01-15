#Autor: Eduardo R. Müller Romero, A01745219
#encoing: UTF-8
#Encontrar el area de una silueta en forma de helado recibiendo como parámetros radio(R) y altura(h)
#    _____
#  /       \
# |         |
#  \       /
#   \     /
#    \   /
#     \ /
#      V
radio = int(input("¿Cuál es el radio(R) de la figura? "))
altura = int(input("¿Cuál es la altura(h)? "))
area = ((3.1416 * (radio ** 2)) / 2) + (((radio * 2) * altura) / 2)
print("El area total es de", area, "unidades cuadradas")