#------Ejercicios------
import random

dado = random.randint(1,6)
print (dado)

numeroUsuario = int(input("Ingresa un numero: "))
intentos = 1

while (numeroUsuario != dado):
    print ("No adivinaste el numero")
    intentos += 1
    numeroUsuario = int(input("Ingresa otro numero: "))

print (f"Has realizado {intentos} intentos antes de adivinar el numero")
print ("Felicitaciones")

#-----Lista Alimentos-----
listaAlimentos = []
listaAlimentos = ["Frambuesa",
                    "Chocolate",
                    "Pancakes", 
                    "Pasta", 
                    "Garbanzos"]

sizeList = len(listaAlimentos)

for i in range (sizeList):
    print (f"Me gusta mucho este alimento: {listaAlimentos[i]}")

print (f"El alimento 3 de la lista es: {listaAlimentos[2]} ")



