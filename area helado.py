#Autor:Luis Arturo Leon Mendez
#Calcula el area de un helado (vista lateral)

radio=int(input("Teclea el radio: "))
altura=int(input("Teclea la altura: "))

area=(3.14159265*radio**2)/2+radio*altura

print("Area= ",area)