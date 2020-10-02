#Funciones
print ('-------Primera parte: Funciones-------')
def elevarCuadrado (numero):
    return numero**2
numeroCuadrado = elevarCuadrado(2)
print (f'El numero elevado al cuadrado es: {numeroCuadrado}')

def elevarCubico (numero):
    return numero**3
numeroCubico = elevarCubico(2)
print (f'El numero elevado a la tres es: {numeroCubico}')

def elevarCuatro (numero):
    return numero**4
numeroCuatro = elevarCuatro(2)
print (f'El numero elevado a la cuatro es: {numeroCuatro}')

def elevarCinco(numero):
    return numero**5
numeroCinco = elevarCinco(2)
print (f'El numero elevado a la cinco es: {numeroCinco}')

def operacionElevado (operacion,numero):
    print (f'La operacion realizada fue {operacion.__name__} y el numero resultante es {operacion(numero)}')
operacionElevado (elevarCuadrado,3)
operacionElevado (elevarCubico,2)
operacionElevado (elevarCuatro,4)
operacionElevado (elevarCinco,10)

#Clases
print ('-------Segunda parte: Clases-------')
class Doctor:
    def __init__(self,idIn,nombreIn,sexoIn,universidadIn):
        self.id = idIn
        self.nombre = nombreIn
        self.sexo = sexoIn
        self.universidad = universidadIn
    def mostrarAtributos (self):
        print (f'El/la doctor/a de nombre {self.nombre}, sexo {self.sexo}, egresad@ de la universidad {self.universidad} se identifica con el número {self.id}')
    def mostrarSintomas (self,lista):
        for elemento in lista:
            print (elemento)

doctor1 = Doctor(112567890,'Susana','Femenino','CES')
sintomas = ['Fiebre', 'Dolor de garganta','Dolor de oidos']
doctor1.mostrarAtributos()
doctor1.mostrarSintomas(sintomas)

class Neurologo(Doctor):
    def __init__(self,idIn, nombreIn,sexoIn,universidadIn,experienciaIn,consultorioIn,salarioIn):
        Doctor.__init__(self,idIn,nombreIn,sexoIn,universidadIn)
        self.experiencia = experienciaIn
        self.consultorio = consultorioIn
        self.salario = salarioIn
    def mostrarAtributos(self):
        print (f'El/La neurolog@ de nombre {self.nombre}, sexo {self.sexo}, egresad@ de la universidad {self.universidad}, con {self.experiencia} años de experiencia atiende en el consultorio {self.consultorio} y tiene un salario de {self.salario} millones')
    def mostrarPacientes (self,lista):
        for elemento in lista:
            print(f'Atendera al paciente de nombre: {elemento}')

neurologo1 = Neurologo(428815567,'Daniel','Masculino','CES',20,'2022',20)
listaPacientes = ['Laura','Marcela','Juan Jose','Patricia']
neurologo1.mostrarAtributos()
neurologo1.mostrarPacientes(listaPacientes)

class Cardiologo(Doctor):
    def __init__(self,idIn, nombreIn,sexoIn,universidadIn,experienciaIn,consultorioIn,salarioIn):
        Doctor.__init__(self,idIn,nombreIn,sexoIn,universidadIn)
        self.experiencia = experienciaIn
        self.consultorio = consultorioIn
        self.salario = salarioIn
    def mostrarAtributos(self):
        print (f'El/La neurolog@ de nombre {self.nombre}, sexo {self.sexo}, egresad@ de la universidad {self.universidad}, con {self.experiencia} años de experiencia atiende en el consultorio {self.consultorio} y tiene un salario de {self.salario} millones')
    def mostrarSintomas (self,lista):
        for elemento in lista:
            print (elemento)
        print ('Despues de analizar los sintomas el/la doctora ya tiene un diagnostico para el paciente')

cardiologo1 = Cardiologo(13829487,'Juan Miguel','Masculino','UPB',4,3203,10)
listaSintomas = ['Dolor en el pecho','Tos','Fatiga','Inflamación de los pies']
cardiologo1.mostrarAtributos()
cardiologo1.mostrarSintomas(listaSintomas)