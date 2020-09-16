#Entradas
listaPesos = [20000,30000,4000,2500,1000,7600]
#Preguntas
preguntaMenu = '''
            Ingrese alguna de las siguientes opciones:
                1 - Conversion de moneda
                2 - Agregar valor
                3 - Mostrar ingreso mas alto, mas bajo y el promedio de ingresos
                4 - Eliminar un valor
                5 - Salir del programa
                : '''
preguntaMoneda = '''
            Ingrese la moneda a la que desea convertir :
                C - Pesos colombianos
                D - Dolares
                E - Euros
                :'''
preguntaAgregar = "Agregue un valor a la lista: "
preguntaRemover = "Ingrese la posicion del elemento que desea eliminar: "

#Mensajes Error
mensajeErrorMenu = "Por favor ingrese una opcion valida, 1,2,3,4,5"
mensajeErrorMoneda = "Por favor ingrese una opcion valida, C,D,E"

#Mensajes informativos
mensajeSalida = "Gracias por usar este codigo"
mensajeIngresoMax = "El ingreso mas alto es {} pesos"
mensajeIngresoMin = "El ingreso mas bajo es {} pesos"
mensajeIngresoPromedio = "El ingreso promedio es de {} pesos"
mensajeOpcion = "Has elegido la opcion {} :"
mensajePesos = "No hay necesidad de hacer una conversion"

#Inicio codigo
opcionMenu = int(input(preguntaMenu))

#CALCULOS
#Calculos Conversion opcion 1
listaCOP = listaPesos
listaDolar = []
listaEuro = []
#Conversion pesos a dolares *0.00027
for elemento in listaPesos:
    dolar = round(elemento *0.00027,2)
    listaDolar.append (dolar)
#Conversion a euros *0.00023
for elemento in listaPesos:
    euro = round(elemento* 0.00023,2)
    listaEuro.append (euro)

#Calculos clasificacion opcion 3
ingresoMax = max(listaPesos)
ingresoMin = min(listaPesos)
suma = 0
for elementos in listaPesos:
    suma += elementos
promedio = suma/len(listaPesos)
promedioIngresos = round(promedio,2)

#Menu
while (opcionMenu != 5):
    if (opcionMenu == 1):
        print (mensajeOpcion.format(1))
        #Pregunta conversion
        opcionMoneda = input(preguntaMoneda)
        if (opcionMoneda == 'D'):
            print (listaDolar)
        elif (opcionMoneda == 'E'):
            print (listaEuro)
        elif (opcionMoneda == 'C'):
            print (mensajePesos)
            print (listaPesos)
        else:
            print (mensajeErrorMoneda)
    elif (opcionMenu == 2):
        print (mensajeOpcion.format(2))
        valorAgregado = int(input(preguntaAgregar))
        listaPesos.append(valorAgregado)
        print (listaPesos)
    elif (opcionMenu == 3):
        print (mensajeOpcion.format(3))
        print (mensajeIngresoMax.format (ingresoMax))
        print (mensajeIngresoMin.format (ingresoMin))
        print (mensajeIngresoPromedio.format (promedioIngresos))
    elif (opcionMenu == 4):
        print (mensajeOpcion.format (4))
        print (listaPesos)
        valorRemovido = int(input(preguntaRemover))
        listaPesos.pop(valorRemovido)
        print (listaPesos)
    else:
        print (mensajeErrorMenu)
    opcionMenu = int(input(preguntaMenu))

#Salida del programa
print (mensajeSalida)