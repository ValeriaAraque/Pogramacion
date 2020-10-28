archivo = open('parrafo.txt', encoding= 'UTF-8')
print (archivo)
parrafo = archivo.readlines()
archivo.close()

print (parrafo)
listaRenglones = []
with open('parrafo.txt', encoding= 'UTF-8') as parrafo:
    for line in parrafo :
        print(line)
        listaRenglones.append(line)
