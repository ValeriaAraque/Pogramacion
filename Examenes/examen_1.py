procedencia = input ("Ingrese la procedencia del pasajero: ")
if (procedencia == "China" or procedencia== "china" or procedencia == "italia" or procedencia == "Italia" or procedencia== "Iran" or procedencia == "iran") :
    print (f"El pasajero de {procedencia} debe entrar en estado de observacion")
else:
    temperatura = float(input("Ingrese la temperatura del pasajero en grados celsius: "))
    if (temperatura < 36):
        print (f"El pasajero de {procedencia} se encuentra en estado de hipotermia")
    elif (temperatura >= 36 and temperatura < 38.5): 
        print (f"El pasajero de {procedencia} se encuentra en estado saludable")
    elif (temperatura >=38.5 and temperatura <= 40 ):
        print (f"El pasajero de {procedencia} se encuentra en estado de alerta")
    else:
        print (f"El pasajero de {procedencia} se encuentra en estado de peligro")
