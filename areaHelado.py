#Autor: Nataly Lopez
#Calcula el area del helado(vista lateral)

radio=int(input("Teclea el radio: "))
altura=int(input("Teclea la altura: "))

area = (3.141592*radio**2)/2 + radio*altura

print("Area: ",area)