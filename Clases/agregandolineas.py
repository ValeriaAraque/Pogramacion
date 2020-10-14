import funciones_archivos as helper
nameFile = 'libro.txt'
helper.agregarLinea ('opinion.txt', 'Nueva linea')
renglonesLibro = helper.leerArchivos(nameFile)
print (len(renglonesLibro))

if (len(renglonesLibro)==0):
    print ('Es la primera linea que se escribira en el libro')
    helper.agregarLinea(nameFile,'El dia que programar fue facil')
else:
    linea = input ('Ingrese la linea que desea agregar: \n')
    helper.agregarLinea(nameFile,linea)
