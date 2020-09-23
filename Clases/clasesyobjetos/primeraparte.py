class TortaRedondas:
    def __init__(self,saborIngresado):
        #Definiendo atributos
        self.forma = 'Redonda'
        self.sabor = saborIngresado
        #Accion al crear objeto
        print ('Soy una torta nueva')
    def mostrarAtributos (self):
        print (f'Soy de forma {self.forma} y de sabor {self.sabor}')

#Creo torta
tortaChocolate = TortaRedondas('Chocolate')
tortaVainilla = TortaRedondas('Vainilla')
#Se muestran los atributos
print (tortaChocolate.sabor)
print (tortaVainilla.sabor)
print (tortaChocolate.forma)
print (tortaVainilla.forma)

#
tortaChocolate.mostrarAtributos()
tortaVainilla.mostrarAtributos()