#Cree la clase persona con id,nombre,edad y cree la funcion hablar, la cual dado mensaje se muestra en pantalla,cree la clase caminar que dado una cantidad de pasos muestre en pantalla cuanto ha caminado
class Persona:
    def __init__(self,idIn,nombreIn,edadIn):
        self.id = idIn
        self.nombre = nombreIn
        self.edad = edadIn
    def hablar(self,mensaje):
        print (f'La persona {self.nombre} esta diciendo que {mensaje}')
    def caminar(self,pasos):
        print (f'La persona {self.nombre} ha caminado {pasos} pasos')

persona1 = Persona(1006959918,'Melany', 20)
persona1.hablar('Hola,como estas')
persona1.caminar(100)

#Herede la clase persona y cree la clase doctor el cual tendra el nuevo atributo especialidad y podra ejecutar una nueva funcion, la cual dada una enfermedad muestra,procedo a tratar enfermedad
class Doctor(Persona):
    def __init__(self,idIn,nombreIn,edadIn,especialidadIn):
        Persona.__init__(self,idIn,nombreIn,edadIn)
        self.especialidad = especialidadIn
    def mostrarAtributos(self):
        print (f'El/La doctor/a {self.nombre}, tiene {self.edad}, se especializo en {self.especialidad} y se identifica con el id {self.id}')
    def tratarEnfermedad (self,enfermedad):
        print(f'El/La doctor/a {self.nombre} va a tratar la enfermedad: {enfermedad}')

doctor1 = Doctor(1011945710,'Susana',24,'Cardiologia')
doctor1.mostrarAtributos()
doctor1.tratarEnfermedad('Taquicardia')

#Herede la clase persona y creee la clase nutricionista y cree un atributo que se refiera a la universidad enla que fue egresado.Tambien una fucnion que devuelva el IMC
class Nutricionista(Persona):
    def __init__(self,idIn,nombreIn,edadIn,universidadIn):
        Persona.__init__(self,idIn,nombreIn,edadIn)
        self.universidad = universidadIn
    def mostrarAtributos(self):
        print (f'El/La nutricionista {self.nombre}, tiene {self.edad}, se identifica con el id {self.id} y se graduo de la universidad {self.universidad}')
    def funcionIMC(self,peso,altura):
        return round(peso/(altura**2),2)

nutricionista1 = Nutricionista(1246576,'Simon', 21, 'CES')
nutricionista1.mostrarAtributos()
imc = nutricionista1.funcionIMC(60,1.70)
print (f'El IMC calculado por el/la nutricionista es de : {imc}')

#Herede de la clase Persona y cree la clase abogado adidcione dos atributos, uno asociado a su especialidad y otro a la universidad de la que egreso.Finalmente cree la funcion que dado un nombre y el caso del cliente, el abogado diga procedo a representar en el caso
class Abogado(Persona):
    def __init__(self,idIn,nombreIn,edadIn,especialidadIn,universidadIn):
        Persona.__init__(self, idIn,nombreIn,edadIn)
        self.especialidad = especialidadIn
        self.universidad = universidadIn
    def mostrarAtributos(self):
        print(f'El/La abogad@ {self.nombre}, de edad {self.edad}, id {self.id}, especializado en {self.especialidad} y egresado de {self.universidad}')
    def casoRepresentado(self,nombre,caso):
        print(f'El/La abogad@ procede a representar al cliente {nombre} en el caso {caso} ')

abogado1 = Abogado(10161718,'Salome',22,'derecho penal','UDM')
abogado1.mostrarAtributos()
abogado1.casoRepresentado('Valeria','Crimen pasional ')

