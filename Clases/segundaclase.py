nombre = input ("Por favor ingrese su nombre : ")
print ("Hola", nombre, "Eres bienvenido a este codigo")
edad = int (input("Por favor ingrese su edad : "))
estatura = float (input("Por favor ingrese su estatura : "))

print (edad)
print (estatura)

print (type(nombre))
print (type(edad))
print (type(estatura))

if (edad >= 18) :
    print ("Usted es mayor de edad")
    print ("Ya eres un adulto")

if (estatura >= 1.70) :
    print ("Eres muy alto")


print ("Chao que te vaya super bien")

