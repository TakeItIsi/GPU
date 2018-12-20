import time
start = time.time()
#"the code you want to test stays here"

import pycuda
from CrearMatriz import NuevaMatriz
import json
#from Tablas import continentes, paises, ciudades
import pandas
import numpy as np



with open("countries.json") as f:
    paises = json.load(f)

with open("cities.json") as f:
    ciudades = json.load(f)

with open("continents.json") as f:
    continentes = json.load(f)

paiscont = pandas.read_csv("countries-continent.csv", sep=';')
paiscontdic = dict(zip(paiscont.Country, paiscont.Continent))
print(paiscontdic)

ciupai = pandas.read_csv("cities-country.csv", sep=";")
ciupaidic = dict(zip(ciupai.name, ciupai.country))

paiscontinente = NuevaMatriz(continentes, paises, paiscontdic)
ciudadpais = NuevaMatriz(paises, ciudades, ciupaidic)

np.savetxt('PaisEnContinente.txt', paiscontinente, fmt='%.1i')
np.savetxt('CiudadEnPais.txt', ciudadpais, fmt='%.1i')

ciudadcontinente=np.zeros((len(continentes), len(ciudades)))
np.matmul(paiscontinente, ciudadpais, ciudadcontinente)

np.savetxt('CiudadEnContinente.txt', ciudadcontinente, fmt='%.1i')

end = time.time()
print(end - start)