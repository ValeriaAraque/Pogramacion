#Ejercicio 1 : Dada una lista muéstrela en pantalla elemento a elemento.
def mostrarLista (lista):
    for elemento in lista:
        print (elemento)

edades = [1,2,3,4,5,6,7]
nombres = ["Ana", "Carolina", "Juan", "Jose", "Salome"]
mostrarLista (edades)
mostrarLista (nombres)

#Ejercicio 2 : Dada una lista de numeros enteros muestre en pantalla el numero mas grande, el numero mas pequeño y el promedio de la lista

def infoLista (lista):
    numeroMax = max(lista)
    numeroMin = min(lista)
    suma = 0
    sizeList = len(lista)
    for numeros in lista:
        suma += numeros
    promedioEnteros = suma/sizeList
    print (promedioEnteros)

enteros = [1,2,5,6,7,8,9,10,11,50,7,100]
infoLista (enteros)
