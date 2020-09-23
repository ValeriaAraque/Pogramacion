class Persona:
    def __init__(self, estaturaIngresado, pesoIngresado,
    nombreIngresado, idIngresado, edadIngresado):
        self.raza = 'Humana'
        self.estatura = estaturaIngresado
        self.edad = edadIngresado
        self.nombre = nombreIngresado
        self.peso = pesoIngresado
        self.id = idIngresado
        print ('Hola mundo, estoy viv@')
    def caminar (self):
        print ('Hola, voy a caminar')
    def saludo (self,saludoEspecial):
        print (saludoEspecial)
class Arquitecto (Persona):
    
    def dibujarPlanos (self):
        print (f'Hola soy {self.nombre} voy a dibujar el plano')
class Biomedico (Persona):
    
    def cultivarCelulas (self):
        print (f'Hola soy {self.nombre} y voy a cultivar celulas ')

karla = Arquitecto(1.62,48,'Karla',1006958917,18)
karla.caminar()
juan = Biomedico (1.76,82,'Juan Pablo',1214299324,23)
juan.caminar ()
karla.saludo ('HOLI CRAYOLI')
juan.saludo ('HOLA COCACOLA')
karla.dibujarPlanos ()
juan.cultivarCelulas ()

