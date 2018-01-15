#Autor: Diana Aguilar
#Descripcion: calcula el area de un helado

radio= int(input("teclea el radio:"))
altura=int(input("tecle la altura:"))

areaCirculo= (3.1416*radio**2)/2
areaTriangulo= radio*altura

areaTotal= areaCirculo + areaTriangulo

print ("el area total es: ", areaTotal)