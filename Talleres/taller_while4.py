
preguntaMonto = "Ingrese el monto de compra: "
preguntaMonto2= "Ingrese otro monto de compra o 0 para conocer el valor que debe pagar: "
preguntaMontoPositivo = "Ingresa un monto positivo:"

monto1 = float(input(preguntaMonto))
suma =0

while (monto1<0):
    monto1 = float(input(preguntaMontoPositivo))

while (monto1 !=0):
    suma += monto1
    monto2 = float(input(preguntaMonto2))
    monto1 = monto2

if (suma>1000):
    suma = suma-(suma*0.1)

print (f"El valor que debes pagar es {suma} ")


