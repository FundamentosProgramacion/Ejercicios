#Autor: Andrés Reyes Rangel
#Calcular el área de un helado (vista lateral)

radio = int(input("Ingrese el radio: "))
altura = int(input("Ingrese la altura: "))

area= (3.141592*radio**2)/ 2 + radio*altura

print ("Área= ", area)