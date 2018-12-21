import time
import pycuda
from CrearMatriz import NuevaMatriz
import json
#from Tablas import continentes, paises, ciudades
import pandas
import numpy as np


start = time.time()
with open("countries.json") as f:
    paises = json.load(f)

with open("cities.json") as f:
    ciudades = json.load(f)

with open("continents.json") as f:
    continentes = json.load(f)
end = time.time()
print("Tiempo de conversion json a dict:", end - start)

start = time.time()
paiscont = pandas.read_csv("countries-continent.csv", sep=';')
paiscontdic = dict(zip(paiscont.Country, paiscont.Continent))

ciupai = pandas.read_csv("cities-country.csv", sep=";")
ciupaidic = dict(zip(ciupai.name, ciupai.country))

end = time.time()
print("Tiempo de Conversion csv a dict:", end - start)

start = time.time()
paiscontinente = NuevaMatriz(continentes, paises, paiscontdic)
end = time.time()
print("Tiempo de Conversion a matriz", len(continentes), "x", len(paises), ":", end - start)

start = time.time()
ciudadpais = NuevaMatriz(paises, ciudades, ciupaidic)
end = time.time()
print("Tiempo de Conversion a matriz", len(paises), "x", len(ciudades), ":", end - start)


np.savetxt('PaisEnContinente.txt', paiscontinente, fmt='%.1i')
np.savetxt('CiudadEnPais.txt', ciudadpais, fmt='%.1i')

start = time.time()
ciudadcontinente=np.zeros((len(continentes), len(ciudades)))
start = time.time()
np.matmul(paiscontinente, ciudadpais, ciudadcontinente)

np.savetxt('CiudadEnContinente.txt', ciudadcontinente, fmt='%.1i')
end = time.time()
print("Tiempo de multiplicación de matrices:", end - start)

a =""
while True:
    b = 0
    a = input("Que ciudad desea buscar?")
    if a=="exit":
        exit()
    start = time.time()
    while (b<len(ciudades)):
        if ciudades[str(b)]==a:
            print("Buscando ciudad ", b)
            break
        b=b+1
    t = 0
    if b==len(ciudades):
        print("Ciudad no se encuentra en la base de datos")
        t=len(continentes)

    while (t<len(continentes)):
        if ciudadcontinente[t][b]==1:
            print(ciudades[str(b)], "se encuentra en", continentes[str(t)])
            break
        t=t+1
    end = time.time()
    print("Tiempo de consulta", end - start)