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
    print (f"El promedio de los numeros de la lista es {promedioEnteros} ")
    print (f"El numero mayor de la lista es {numeroMax} y el numero menor de la lista es {numeroMin} ")

enteros = [1,2,5,6,7,8,9,10,11,50,7,100]
infoLista (enteros)

#Ejercicio 3: Salude n veces
def repeticiones (n=0):
    print ('Hola ' *n)
repeticiones (8)

#Ejercicio 4: Que devuelva todos los numeros pares de una lista de numeros enteros
def numerosPares (lista):
    pares = []
    for elemento in lista:
        if (elemento % 2 == 0):
            pares.append (elemento)
    return pares
listaEdad = [1,2,3,4,6,7,9,12,80,24]
paresLista = numerosPares (listaEdad)
print (paresLista)

#Ejercicio 5: Que devuelva unicamente los elementos mayores a 24
def mayores (lista):
    mayores = []
    for elemento in lista:
        if (elemento >24):
            mayores.append (elemento)
    return mayores
listaNumeros = [50,67,71,13,18,29,33]
numerosMayores = mayores (listaNumeros)
print (numerosMayores)

#Ejercicio 6: Se sabe que el IMC se calcula diviendo el peso por la altura al cuadrado, realice una funcion que lo calcule
def calcularIMC (peso,altura):
    return round(peso/(altura**2),2)
imc = calcularIMC (57,1.57)
print (imc)

#Ejercicio 7: Crea una funcion que sirva para despedirte del que esta ejeutando el codigo
def adios ():
    print ("Hasta luego, que estes bien")
adios ()