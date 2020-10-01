#Cree la clase torta con atributos forma,sabor,altura, tambien tendra una funcion donde muestre todos sus atributos
class Torta:
    def __init__(self,formaIn,saborIn,alturaIn):
        self.forma = formaIn
        self.sabor = saborIn
        self.altura = alturaIn
    def mostrarAtributos (self):
        print (f'Se creo una torta de forma {self.forma}, sabor {self.sabor} y altura {self.altura}')

torta1 = Torta('redonda','chocolate',20)
torta1.mostrarAtributos()

# Cree una clase estudiante con atributos edad,nombre,id,carrera,semestre, que tenga una funcion donde dada una materia y una cantidad de tiempo muestre en pantalla que estudiara esa materia en dicho tiempo
class Estudiante:
    def __init__(self,edadIn,nombreIn,idIn,carreraIn,semestreIn):
        self.edad = edadIn
        self.nombre = nombreIn
        self.id = idIn
        self.carrera = carreraIn
        self.semestre = semestreIn
    def mostrarAtributos(self):
        print (f'El estudiante se identifica con el numero {self.id}, edad {self.edad},de nombre {self.nombre}, carrera {self.carrera} y semestre {self.semestre}')
    def estudiarMateria (self,materia,tiempo):
        print (f'El estudiante de nombre {self.nombre} va a estudiar {materia} por {tiempo} minutos')

estudiante1 = Estudiante(18,'Valeria',1006959918,'IBM', 6)
estudiante1.mostrarAtributos()
estudiante1.estudiarMateria('programacion',120)

# Creee una clase nutricionista donde tendra los atributos edad,nombre,universidad de la que egreso.Tendra la funcion que dado el peso y altura del paciente calcule su imc
class Nutricionista:
    def __init__(self, edadIn, nombreIn, universidadIn):
        self.edad = edadIn
        self.nombre = nombreIn
        self.universidad = universidadIn
    def mostrarAtributos(self):
        print(f'Soy un@ nutricinista, tengo {self.edad}, me llamo {self.nombre} y soy egresad@ de {self.universidad}')
    def funcionIMC(self,peso,altura):
        return round(peso/(altura**2),2)

nutricionista1 = Nutricionista (24,'Sofia','CES')
nutricionista1.mostrarAtributos()
imc = nutricionista1.funcionIMC(50,1.63)
print (f'El IMC calculado por el/la nutricionista es de: {imc}')

#Cree una clase canguro que tenga atributos edad,id,nombre.Cree una funcion que dada una cantidad de saltos muestre en pantalla uno a uno
class Canguro:
    def __init__(self,edadIn,nombreIn,idIn):
        self.id = idIn
        self.edad = edadIn
        self.nombre = nombreIn
    def mostrarAtributos (self):
        print (f'Hola soy el canguro {self.nombre}, tengo {self.edad} años y me identifico con el numero {self.id}')
    def mostrarSaltos (self,saltos):
        for saltos in range (saltos):
            print (f'El canguro {self.nombre} ha dado {saltos +1} saltos')

canguro1 = Canguro(4,'Saltarin',1675)
canguro1.mostrarAtributos()
canguro1.mostrarSaltos(6)

#Piense en su instrumento musical favorito y cree una clase asociada al mismo, defina los atributos y cree una funcion que permita dada una cancion interpretarla en el mismo
class Arpa:
    def __init__(self,cuerdasIn, colorIn, tipoIn):
        self.cuerdas = cuerdasIn
        self.color = colorIn
        self.tipo = tipoIn
    def interpretarCancion (self,cancion):
        print (f'La cancion {cancion} es interpretada con el arpa {self.tipo}, de color {self.color} y con {self.cuerdas} cuerdas')

arpa1 = Arpa(26,'marfil','Celta')
arpa1.interpretarCancion('Cant help falling in love')
