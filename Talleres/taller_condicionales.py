#1. Dados dos numeros determine si son iguales o cual es mayor
#Preguntas
preguntaNumero1 = "Ingrese un numero: "
preguntaNumero2 = "Ingrese otro numero: "
#Mensajes
mensajeIgual = "El numero {} es igual al numero {}"
mensajeMayor = "El numero {} es mayor al numero {}"
#Entradas
numero1 = int(input(preguntaNumero1))
numero2 = int(input(preguntaNumero2))
#Condicionales
if (numero2 == numero1):
    print (mensajeIgual.format(numero1,numero2))
elif (numero1 > numero2):
    print (mensajeMayor.format(numero1,numero2))
else:
    print(mensajeMayor.format(numero2,numero1))

#2. Pida la edad del usuario y muestre si es menor de edad, joven, adulto o adulto mayor
#Preguntas
preguntaEdad = "Ingrese su edad: "
#Mensajes
mensajeMenorEdad = "Si tienes {} años eres menor de edad"
mensajeJoven = "Si tienes {} años eres considerado un joven"
mensajeAdulto = "Si tienes {} años eres un adulto"
mensajeAdultoMayot = "Si tienes {} años eres un adulto mayor"
#Entradas
edad = int(input(preguntaEdad))
#Condicionales
if (edad <18):
    print (mensajeMenorEdad.format(edad))
elif (edad >=18 and edad <= 25):
    print (mensajeJoven.format(edad))
elif (edad >=26 and edad <= 60):
    print (mensajeAdulto.format(edad))
else:
    print (mensajeAdultoMayot.format(edad))
