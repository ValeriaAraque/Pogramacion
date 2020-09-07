#------Ciclo while------
# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados
preguntaNumero = "Ingrese un numero entero o 0 para terminar: "

numeroUsuario = int(input(preguntaNumero))
suma = 0

while (numeroUsuario != 0):
    suma += numeroUsuario
    numeroUsuario = int(input(preguntaNumero))

print (f"La sumatoria de los numeros que ingresaste antes de ingresar el cero fue de {suma}")

#Ejercicio 2
print ("-----SEGUNDO EJERCICIO-----")
preguntaEntero1 = "Ingrese un numero entero: "
preguntaEntero2 = "Ingrese otro numero entero: "

numeroEntero1 = int(input(preguntaEntero1))
numeroEntero2 = int(input(preguntaEntero2))

while (numeroEntero2 <= numeroEntero1):
    numeroEntero2 = int(input(preguntaEntero2))

print (f"El primer numero que ingresaste fue {numeroEntero1} y el segundo numero que ingresaste fue el {numeroEntero2} ")

#Ejercicio 3
print ("----TERCER EJERCICIO----")

numeroEntero1 = int(input(preguntaEntero1))
numeroEntero2 = int(input(preguntaEntero2))

while (numeroEntero2 >= numeroEntero1):
    numeroEntero1 = numeroEntero2
    numeroEntero2 = int(input(preguntaEntero2))

print ("Has ingresado un numero menor al anterior")
