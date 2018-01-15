#Autor: Genaro Ortiz Durán
#Descripción: Calcular el área de una car plana de un helado.

from math import pi
Radio=int(input("Teclea el radio:"))
Altura=int(input("Teclea la altura:"))

Area= ((pi*Radio**2)/2) + (2*Radio*Altura/(2))
print(Area)




