name = input("Por favor ingrese el nombre de la persona : ")

print(f"Hola, para calcular el IMC de {name} necesitamos los siguientes datos : ")

peso = float(input("Ingrese el peso de la persona en kilogramos : "))
estatura = float(input("Ingrese la estatura de la persona en metros : "))

imc = round(peso/estatura**2,2)
if (imc < 18.5) :
    print (f"{name} tiene estado de infrapeso con un IMC de {imc} ")
elif (imc >= 18.5 and imc<25) :
    print (f"{name} tiene un peso normal con un IMC de {imc}")
elif (imc >= 25 and imc<30) :
    print (f"{name} tiene sobrepeso con un IMC de {imc}")
elif (imc >= 30 and imc<35) :
    print (f"{name} tiene obesidad con un IMC de {imc}")
else:
    print (f"{name} tiene obesidad morbida con un IMC de {imc}")

