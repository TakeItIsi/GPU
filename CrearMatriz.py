import pycuda
import numpy as np

#NuevaMatriz: Dict*Dict*Dict -> Matriz
# Crea una matriz con las relaciones binarias
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