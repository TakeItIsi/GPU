import pycuda
import numpy as np

#NuevaMatriz: Crea una matriz con las relaciones binarias
#entre pais y continente
def NuevaMatriz(conti, pais, cp):
    mat=np.zeros((len(conti), len(pais)))
    p=0
    while(p<len(pais)):
        i=0
        while(i<len(conti)):
            if cp[pais[str(p)]]==conti[str(i)]:
                    mat[i][p]= 1
            i=i+1
        p=p+1
    return mat

#Test

#ccc = {"0":"a","1":"b","2":"c"}
#ppp = {"0":"alfa","1":"beta","2":"alfalfa","3":"comino","4":"cuchifli","5":"bumblebee"}
#cyp =[["alfa","a"],["alfalfa","a"],["beta","b"],["bumblebee","b"],["comino","c"],["cuchifli","c"]]
#print(NuevaMatriz(ccc,ppp,cyp))