#-------Preguntas-------#
preguntaNumero = "ingrese un numero del 1 al 10 : "
#-------Mensajes-------#
mensajeFallido = "Fallaste, no es el numero secreto"
mensajeExitoso = "Felicitaciones, encontraste el numero secreto"
mensajeDespedida = "Gracias por jugar"
mensajeVida= "Ten cuidado has perdido {} vida te quedan {}"

#Ciclos while

numeroSecreto = 6
numeroIngresado = int(input(preguntaNumero))
vidasPerdidas = 0
while(numeroSecreto != numeroIngresado and vidasPerdidas<=2):
    vidasPerdidas = vidasPerdidas +1
    print (mensajeVida.format(vidasPerdidas,3-vidasPerdidas))
    print (mensajeFallido)
    if vidasPerdidas <3:
        numeroIngresado = int(input(preguntaNumero))

if vidasPerdidas<3:
    print(mensajeExitoso)
else:
    print(mensajeFallido)
print (mensajeDespedida)

#------Preguntas2-------#
preguntaVocal = "Ingrese una vocal en minuscula: "
#------Mensajes2-------#
mensajeFallido2 = "Fallaste, no es la vocal secreta"
mensajeExitoso2 = "Felicitaciones, encontraste la vocal secreta"

vocalSecreta = "e"
vocalIngresada = input(preguntaVocal)
while(vocalSecreta != vocalIngresada) :
    print (mensajeFallido2)
    vocalIngresada = input (preguntaVocal)
print (mensajeExitoso2)
print (mensajeDespedida)
