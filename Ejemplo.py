#Karla Fabiola Ramirez
#Calcular el area de un helado en 2d


radio=int(input("Dame el radio: "))
altura=int(input("Dame la altura: "))

areac=(3.1416*radio**2)/2
areat=((radio*2)*altura)/2
Total=areac+areat
print ("El area total seria de: ",Total)