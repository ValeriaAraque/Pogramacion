#Crear una clase persona con los atributos id, nombre, peso, altura y sexo
#   Creo un objeto a partir de la clase y muestre sus atributos
class Persona:
    def __init__ (self, idIngresado,nombreIngresado,pesoIngresado,alturaIngresada,sexoIngresado):
        self.id = idIngresado
        self.nombre = nombreIngresado
        self.peso = pesoIngresado
        self.altura = alturaIngresada
        self.sexo = sexoIngresado
    def mostrarAtributos(self):
        print (f'Se ha creado una persona identidicada con el numero {self.id}, de nombre {self.nombre}, estatura {self.altura}, peso {self.peso} kg y sexo {self.sexo} ')

persona1 = Persona (1006959918,'Valeria',50,1.64,'femenino')
persona1.mostrarAtributos()

#Crear una clase estudiante que hereda de persona, dado esta info se agrega un nuevo atributo, semestre,universidad y carrera
#   Cree una funcion que dado el nombre de una materia el estudiante diga voy a ir a esa materia
class Estudiante (Persona):
    def __init__(self, idIngresado,nombreIngresado, pesoIngresado,alturaIngresada, sexoIngresado, semestreIngresado,universidadIngresado,carreraIngresado):
        Persona.__init__(self,idIngresado,nombreIngresado, pesoIngresado,alturaIngresada, sexoIngresado)
        self.universidad = universidadIngresado
        self.carrera = carreraIngresado
        self.semestre = semestreIngresado
    def mostrarAtributos(self):
        print (f'Se ha creado una persona identidicada con el numero {self.id}, de nombre {self.nombre}, estatura {self.altura}, peso {self.peso} kg, sexo {self.sexo}, carrera {self.carrera}, universidad {self.universidad} y semestre {self.semestre} ')
    def asistirMateria (self,materia):
        print (f'Hola soy {self.nombre} y voy a asistir a {materia}')

estudiante1 = Estudiante(1006959918,'Valeria',50,1.55,'femenino',5,'CES','MVZ')
estudiante1.mostrarAtributos()
estudiante1.asistirMateria('Farmacologia')
