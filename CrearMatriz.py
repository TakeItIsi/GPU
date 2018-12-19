import pycuda
import numpy as np

#NuevaMatriz: Crea una matriz con las relaciones binarias
#entre pais y continente
def NuevaMatriz(conti, pais, cp):
    mat=np.zeros((len(conti), len(pais)))
    for p in pais:
        #print(p)
        i=0
        while(i<len(conti)):
            #print(conti[i])
            #print([p[1], conti[i][1]])
            if [p[1], conti[i][1]] in cp:
                mat[i][p[0]]= 1
                #print("ye")
            #else:
                #print("nah")
            i=i+1
    return mat

#Test

ccc = [[0,"a"],[1,"b"],[2,"c"]]
ppp = [[0,"alfa"],[1,"beta"],[2,"alfalfa"],[3,"comino"],[4,"cuchifli"],[5,"bumblebee"]]
cyp =[["alfa","a"],["alfalfa","a"],["beta","b"],["bumblebee","b"],["comino","c"],["cuchifli","c"]]
print(NuevaMatriz(ccc,ppp,cyp))