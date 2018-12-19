import pycuda
from CrearMatriz import NuevaMatriz
import json



f= open("probando.txt","w+")
ciudades = json.load("cities.json")
paises = json.load("countries.json")
continentes = json.load("continents.json")
for a in ciudades:

#CrearMatriz(continentes, paises, )
