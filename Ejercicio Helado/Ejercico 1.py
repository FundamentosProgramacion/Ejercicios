#Autor: Carlos Ochoa
#Calcula el area de un helado


radio = int(input("Teclea el radio"))
altura = int(input("Teclea la altura: "))

area = ((3.141592*radio**2) / 2) + radio*altura

print("Area: ", area)