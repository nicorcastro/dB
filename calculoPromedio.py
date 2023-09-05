#DB Ficticia
import random
nReales = []
cantidad=500
for i in range(cantidad):
    numeroAleatorio=random.randint(-500,500)
    nReales.append(numeroAleatorio)

suma=0
promedio=0
elementos=len(nReales)

for x in nReales:
    suma+=x

promedio=suma/elementos

print("El promedio de los n números es: "+str(promedio))
    
    