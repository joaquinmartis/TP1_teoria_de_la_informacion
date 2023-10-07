import numpy as np
import sys
import binascii

def probabilidades_condicionales(nombre_archivo):
    bloque=0

    with open(nombre_archivo,"rb") as archivo:
        contenido_binario=archivo.read()
    
    cadena_bits = ''.join(format(byte, '08b') for byte in contenido_binario)

    #print(cadena_bits)

    matcond = np.zeros((2, 2), dtype=int)

    matcond=np.array(matcond)
    i=1
    for i in range(len(cadena_bits)):
        matcond[int(cadena_bits[i-1]),int(cadena_bits[i])]+= 1
    return matcond

def matriz_probabilidades_condicionales(matcond):
    auxmat = np.zeros((2, 2), dtype=float)  # Create a copy to avoid modifying the original matrix
    
    aux = matcond[0, 0] + matcond[0, 1]
    auxmat[0, 0] = matcond[0, 0] / aux
    auxmat[1, 0] = matcond[1, 0] / aux

    aux = matcond[0, 1] + matcond[1, 1]
    auxmat[0, 1] = matcond[0, 1] / aux
    auxmat[1, 1] = matcond[1, 1] / aux
    return auxmat


def fuente_memoria_nula(matprob):
    return abs(matprob[0,0]-matprob[1,0])<0.05 and abs(matprob[0,1]-matprob[1,1])<0.05

def entropia(matprob):
    entropia=0
    for i in range(len(matprob)):
        for j in range(len(matprob)):
            if matprob[i,j]!=0:
                entropia+=matprob[i,j]*np.log2(1/matprob[i,j])
    return entropia

def probabilidades_extension_orden_n(matcond,orden):
    mat_prob_orden=np.zeros((2**orden,2**orden),dtype=float)
    


if len(sys.argv) >1:
    filename2 = sys.argv[1]
    print(filename2)
    if len(sys.argv)==3:
        N=sys.argv[2]
else:
    print("No se proporcionaron parámetros.")
filename="tp1_sample0.bin"

matcond=probabilidades_condicionales(filename)
print(matcond)
mat_prob_condicionales=matriz_probabilidades_condicionales(matcond)
if fuente_memoria_nula(mat_prob_condicionales)==True:
    print("La fuente es de memoria nula")
print("La entropia es: ",entropia(mat_prob_condicionales))
