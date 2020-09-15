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
mensajeAdultoMayor = "Si tienes {} años eres un adulto mayor"
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

#3. Escriba un programa que pida el año actual  y un año cualquiera y que escriba cuantos años han pasado desde ese año o cuantos años faltan para llegar a ese año 
#Preguntas 
preguntaAñoActual = "Ingrese el año actual: "
preguntaAño = "Ingrese un año cualquiera: "
#Mensajes 
añosFaltantes = "Faltan {} años para llegar al año que ingresaste"
añosPasados = "Han pasado {} años desde el año que ingresaste"
#Entradas
añoActual = int(input(preguntaAñoActual))
año = int(input(preguntaAño))
#Condicional
if (añoActual > año):
    resta = añoActual-año
    print (añosPasados.format(resta))
elif (añoActual < año):
    restaPasados = año-añoActual
    print (añosFaltantes.format(restaPasados))
else:
    print ("Los años que ingresaste son iguales")