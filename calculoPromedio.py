#DB Ficticia
import random
nReales = []
cantidad=2
for i in range(cantidad):
    numeroAleatorio=random.randint(-500,500)
    nReales.append(numeroAleatorio)

print(nReales)

suma=0
promedio=0

for x in range (len(nReales)):
    suma+=nReales[x]

promedio=suma/(x+1)

print("El promedio de los n números es: "+str(promedio))
    