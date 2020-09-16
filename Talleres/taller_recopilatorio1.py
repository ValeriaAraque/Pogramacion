#Entradas
listaDolares = [20000,30000,4000,2500,1000,7600]
#Preguntas
preguntaMenu= '''
Ingrese alguna de las siguientes opciones 
1-Convertir Dolares
2-Mostrar categoria de ingresos 
3-Ver maximo,minimo y promedio de ingresos
4-Salir del programa
: '''
preguntaMoneda = '''
                Ingrese la moneda a la que desea convertir:
                C - Pesos Colombianos
                D - Dolares
                E - Euros
: '''
#Mensajes Error
mensajeErrorMoneda = "Por favor ingrese una opcion valida, C,D,E"
mensajeErrorMenu = "Por favor ingrese una opcion valida, 1,2,3,4"
#Mensajes informativos
mensajeDolares = "No es necesaria una conversion"
mensajeSalida = "Gracias por usar el codigo"
mensajeOpcion = "Usted escogio la opcion {}"
mensajeMaximo = "El salario maximo es de {}"
mensajeMinimo = "El salario minimo es de {}"
mensajePromedio = "El salario promedio es de {}"

#Inicio Codigo
opcionMenu = int(input(preguntaMenu))
#Calculos
listaCOP = []
listaDolar = listaDolares
listaEuro = []
listaClasificacion = []
#----Pasar de dolar a COP
for elemento in listaDolar:
    COP = elemento * 3700
    listaCOP.append(COP)
#----Pasar de dolar a euro
for elemento in listaDolar:
    euro = elemento *0.84
    listaEuro.append(euro)

#Categoria de ingresos
for elemento in listaDolar:
    clasificacion = ''
    if (elemento<1000):
        clasificacion = 'Ingresos bajos'
    elif (elemento>= 1000 and elemento<7000 ):
        clasificacion = 'Ingresos medios'
    elif (elemento>= 7000 and elemento <20000):
        clasificacion = 'Ingresos altos'
    else:
        clasificacion = 'Ingresos elevados'
    listaClasificacion.append (clasificacion)

#Calculo ingreso max e ingreso min
ingresoMax = max(listaDolares)
ingresoMin = min(listaDolares)
suma = 0 
for elementos in listaDolares:
    suma += elemento
promedio= suma/len(listaDolares)
#Para redondear
promedioIngresos = round(promedio,2)

#Menu
while (opcionMenu !=4):
    if (opcionMenu ==1):
        print(mensajeOpcion.format(1))
        #Pregunta Conversion
        moneda = input(preguntaMoneda)
        if (moneda == 'C'):
            print (listaCOP)
        elif (moneda == 'E'):
            print (listaEuro)
        elif (moneda == "D"):
            print (mensajeDolares)
        else:
            print (mensajeErrorMoneda)
    elif (opcionMenu ==2):
        print (mensajeOpcion.format(2))
        print (listaClasificacion)
    elif (opcionMenu ==3):
        print (mensajeOpcion.format(3))
        print (mensajeMaximo, ingresoMax)
        print (mensajeMinimo, ingresoMin)
        print (mensajePromedio, promedioIngresos)
    else:
        print (mensajeErrorMenu)
    #Entrada variable opcion
    opcionMenu = int(input(preguntaMenu))

#Salida del programa
print (mensajeSalida)

