#Ejercicio 1
suma = 0

for i in range (101):
    suma += i
print (f"La sumatoria de los numeros del 0 al 100 es {suma} ")

#Ejercicio 2
print("EJERCICIO 2")
preguntaNumero = "Ingrese un numero entero: "
factorial = 1

numero = int(input(preguntaNumero))
for i in range (numero):
    factorial = factorial*(i+1)

print (f"El factorial {numero} es {factorial} ")

#Ejercicio 3
print ("---EJERCICIO 3---")
sumaPositivos = 0
cantidadPositivos = 0
sumaNegativos = 0

for i in range (6):
    numero = int(input("Ingrese un numero entero: "))
    if (numero>0):
        sumaPositivos = sumaPositivos + numero
        cantidadPositivos = cantidadPositivos + 1
    else:
        sumaNegativos = sumaNegativos + numero

print (f"La sumatoria de los numeros negativos es {sumaNegativos}")

if (cantidadPositivos !=0):
    print ("Promedio numeros positivos:", sumaPositivos/cantidadPositivos)
else:
    print ("No se ingresaron numeros positivos")

#Ejercicio 4
print ("----EJERCICIO 4----")

listaCanciones = ["Despeinada","Como estrellas", "Me acuerdo de ti", "Caramelo","La Oficial"]
sizeList = len(listaCanciones)

for i in range(sizeList):
    print (f"Esta es una de mis canciones favoritas: {listaCanciones[i]} ")

import random
cancionAleatoria = random.randint(0,4)
print (f"Se seleccino la siguiente cancion: {listaCanciones[cancionAleatoria]} ")
