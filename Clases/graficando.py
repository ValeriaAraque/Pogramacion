import matplotlib.pyplot as plt
ciudades = ['Medellin', 'Cali', 'Ibague', 'Cartagena']
personas = [21345,345678,234567,124589]
plt.bar (ciudades,personas)
plt.title ('Ciudades vs poblacion')
plt.xlabel('Ciudades colombianas')
plt.ylabel('Poblacion')
plt.savefig('GraficoCiudades.png')
plt.show()