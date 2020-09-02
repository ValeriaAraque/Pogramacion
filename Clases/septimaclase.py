#----- se crea la listaNombres----
listaNombres = []
listaNombres = ["Melany",
            "Karla",
            "Laura Paredes",
            "Laura Montoya",
            "Juan Pablo",
            "Mario",
            "Valeria",
            "Santi"]

listaEdades = [20,18,18,18,21,20,18,18]
print (listaNombres)
print (listaNombres [2])
print (listaNombres [-1])
listaNombres.append("Daniel")
print (listaNombres [-1])
print (listaNombres)

listaNombres.pop(-1)
print (listaNombres)
listaNombres.append ("Daniel")
listaEdades.append(27)
sizeList = len(listaNombres)
print (sizeList)

for i in range (sizeList):
    print (f"Hola soy {listaNombres [i]} y estoy feliz programando")
print ("Segundo metodo")
for nombre in listaNombres:
    print (f"Hola soy {nombre} y estoy feliz programando")

for i in range (sizeList):
    print (f"Nombre: {listaNombres [i]} Edad: {listaEdades [i]}")

listaHobbies = []
desicion = 0
while (desicion == 0):
    hobbie = input("Cual es tu hobbie favorito? : ")
    listaHobbies.append (hobbie)
    desicion = int (input ("""Ingrese :
                0 - Para seguir agregando hobbies
                !0 - Para finalizar
    : """))
print (listaHobbies)

desicion = "si"
while (desicion == "si"):
    hobbie = input("Cual es tu hobbie favorito? : ")
    listaHobbies.append (hobbie)
    desicion = input ("""Ingrese :
                si - Para seguir agregando hobbies
                no - Para finalizar
    : """)
print (listaHobbies)
