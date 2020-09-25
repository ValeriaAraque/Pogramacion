import persona as p 
import estudiante as es
import egresado as eg
laura = p.Persona ('Laura', 18, 1002939918)
mario = p.Persona ('Mario', 20, 10216956920)
valeria = es.Estudiante ('Valeria',18,1006959920,'Biomedica',3)
laura.hablar ('Todo anda muy bien, me gusta aprender')
mario.comer ('Taco')
valeria.estudiar ('Calculo')
melany = eg.Egresado ('Melany', 20, 1113450, 'Biomedica','2023/12/12')
print (melany.semestre)
melany.trabajar ('MIT')