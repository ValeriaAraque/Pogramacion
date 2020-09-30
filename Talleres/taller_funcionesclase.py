#Una funcion que dados dos numeros determine cual es el mayor o si son iguales
a = int(input('Por favor ingrese un numero entero: '))
b = int(input('Por favor ingrese otro numero entero: '))
#Las variables pueden tener diferente nombre pero las definidas en la funciones deben ser iguales a los condicionales que la contengan
def infoNumero (numero1,numero2):
    if (numero1>numero2):
        print (f'El numero {numero1} es mayor que el numero {numero2}')
    elif (numero2>numero1):
        print (f'El numero {numero2} es mayor que el numero {numero1}')
    else:
        print (f'Los numeros ingresados son iguales')

infoNumero(a,b)
infoNumero(7,8)

#Dada una lista de nombres cree una funcion que muestre en pantalla nombre por nombre
def mostrarNombres (lista):
    for elemento in lista:
        print (elemento)

nombres = ['Daniel', 'Carolina', 'Laura', 'Valeria']
mostrarNombres(nombres)

#Calculo IMC dado peso y estatura
def calculoIMC (estatura,peso):
    return round(peso/(estatura**2),2)
imc = calculoIMC (1.64, 50)
print(f'El IMC calculado es de {imc}')

#Dada la funcion de IMC y los valores de peso y altura mostrar en pantalla el IMC calculado
def mostrarIMC (funcionIMC,estatura,peso):
    imc = funcionIMC (estatura,peso)
    print (f'El IMC calculado es de {imc}')

mostrarIMC(calculoIMC,1.63,60)