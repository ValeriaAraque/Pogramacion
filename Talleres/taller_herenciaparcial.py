#Cree las siguientes funciones
#Funcion 1
def infoLista (lista):
    numeroMax = max(lista)
    numeroMin = min(lista)
    suma = 0
    for numeros in lista:
        suma += numeros
    promedio = suma/len(lista)
    print(f'El promedio de los numeros es {promedio}, el numero mas grande es el {numeroMax} y el numero mas pequeño es el {numeroMin}')

numeros =[4,5,1,25,-3,5]
infoLista (numeros)

#Funcion 2 
def numerosPares (lista):
    pares =[]
    for elemento in lista:
        if (elemento % 2 == 0):
            pares.append (elemento)
    return pares

numerosX = [1,2,3,5,8,56,34,55,7,2,3,5,0]
paresLista = numerosPares(numerosX)
print(paresLista)

#Funcion 3
def mostrarMensaje (mensaje):
    print (f'El mensaje  introducido fue : {mensaje}')

mostrarMensaje('Hola, me llamo Valeria')

#Funcion 4 : Dado un numero le reste 12 y devuleva el resultado
def restar12 (numero):
    return numero-12
numeroNuevo = restar12(80)
print (f'El numero introducido menos 12 es: {numeroNuevo}')

#Funcion 5: Dado un numero lo multiplique por 12 y devuelva el resultado
def multiplicar12(numero):
    return numero*12
numeroMultiplicado = multiplicar12(10)
print (f'El numero introducido multiplicado por 12 es: {numeroMultiplicado}')

#Funcion 6: Dado un numero se divida por 12 y muestre el mresultado
def dividir12(numero):
    return numero/12
numeroDividido = dividir12(120)
print (f'El numero introducido dividido por 12 es: {numeroDividido}')

#Funcion 7: Dado un numero se le sume 12
def sumar12(numero):
    return numero+12
numeroSumado = sumar12(10)
print (f'El numero introducido mas 12 es: {numeroSumado}')

#Funcion 8: Dada una de las 4 funciones anteriores y su entrada mostrar el resultado
def operaciones12 (operacion,numero):
    print (operacion(numero))
operaciones12(restar12,20)
operaciones12(sumar12,20)
operaciones12(multiplicar12,20)
operaciones12(dividir12,20)

#Clase Paciente
class Paciente:
    def __init__(self,idIn,nombreIn,sexoIn,afiliadoIn):
        self.id = idIn
        self.nombre = nombreIn
        self.sexo = sexoIn
        self.afiliado = afiliadoIn
    def mostrarAtributos(self):
        print (f'El paciente de nombre {self.nombre} se identifica con el id {self.id}, es de sexo {self.sexo} y afiliado a {self.afiliado}')
    def mostrarSintomas(self,lista):
        for elementos in lista:
            print (elementos)

paciente1 = Paciente(1006959817,'Susana', 'Femenino', 'Sura')
paciente1.mostrarAtributos()
listaSintomas = ['Fiebre', 'Tos','Dolor de pecho']
paciente1.mostrarSintomas(listaSintomas)

#Clase Estable
class Estable(Paciente):
    def __init__(self,idIn,nombreIn,sexoIn,afiliadoIn,tiempoIn,temperaturaIn,animoIn):
        Paciente.__init__(self,idIn,nombreIn,sexoIn,afiliadoIn)
        self.tiempo = tiempoIn
        self.animo = animoIn
        self.temperatura = temperaturaIn
    def mostrarAtributos (self):
        print(f'El paciente de nombre {self.nombre}, identificado {self.id}, de sexo {self.sexo}, afiliado a {self.afiliado}, con un tiempo de espera de {self.tiempo} minutos, con una temperatura {self.temperatura} y con un animo de {self.animo} ')
    def recomendacionesPaciente(self,lista):
        for elemento in lista:
            print(f'El paciente debe: {elemento}')

estable1 = Estable(1006958718,'Laura','Femenino','Coomeva',50, 38,'bueno')
listaRecomendaciones = ['Descansar', 'Tomar agua', 'No estresarse']

estable1.mostrarAtributos()
estable1.recomendacionesPaciente(listaRecomendaciones)

#Clase Critico
class Critico(Paciente):
    def __init__(self,idIn,nombreIn,sexoIn,afiliadoIn,habitacionIn,patologiaIn):
        Paciente.__init__(self,idIn,nombreIn,sexoIn,afiliadoIn)
        self.habitacion = habitacionIn
        self.patologia = patologiaIn
    def mostrarAtributos(self):
        print (f'El paciente de nombre {self.nombre}, de sexo {self.sexo}, afiliado a {self.afiliado}, identificado con el numero {self.id}, esta ubicado en la habitacion {self.habitacion} y la patologia {self.patologia}')
    def mostrarSintomasCriticos(self,lista):
        for elemento in lista:
            print(elemento)

listaSintomasCriticos = ['Taquicardia','Presion alta','Ojos hinchados']
critico1 = Critico(10059195,'Geronimo','Masculino','Sura',302,'Infarto')
critico1.mostrarAtributos()
critico1.mostrarSintomasCriticos(listaSintomasCriticos)