import numpy as np
import sys
import binascii
import math

def Genera_Matriz_Acumulada(nombre_archivo):

    with open(nombre_archivo,"rb") as archivo: #se abre el archivo en modo de lectura binaria
        contenido_binario=archivo.read() #se lee el contenido del archivo y se guarda  en contenido_binario
    
    cadena_bits = ''.join(format(byte, '08b') for byte in contenido_binario) #se convierte el contenido binario en una cadena de bits (cadena unica)

    mat = np.zeros((2, 2), dtype=int) 
    mat=np.array(mat) #se crea una matriz NumPy int de 2x2 llena de ceros
    
    for i in range(1,len(cadena_bits)): # se recorre secuencialmente la cadena de bits y se acumula en la matriz segun corresponda
        mat[int(cadena_bits[i]),int(cadena_bits[i+1])]+= 1 #se acumuna en fila de lectura actual y en la columna lectura anterior
    return mat

def matriz_probabilidades_condicionales(matcond):
    auxmat = np.zeros((2, 2), dtype=float)  # se crea una matriz auxiliar de 2x2 para almacenar las probabilidades condicionales
    
    aux = matcond[0, 0] + matcond[0, 1] #se suma la columna 0
    auxmat[0, 0] = matcond[0, 0] / aux
    auxmat[1, 0] = matcond[1, 0] / aux

    aux = matcond[0, 1] + matcond[1, 1]  #se suma la columna 1
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
    
def Genera_VecEstacionario(mat_prob_condionales):
    auxmat=copy.deepcopy(mat_prob_condicionales)
    auxmat[1,0]=1
    auxmat[1,1]=1
    b=np.array([0,1])
    x=np.linalg.solve(auxmat,b)
    return x

def entropiaNoNula(vecestacionario,mat_prob_condicionales):
    log_mat= np.log2(1/mat_prob_condicionales) #calcula el  base 2 de los elementos de la matriz
    producto = mat_prob_condicionales*log_mat #calcula el producto elemento a elemento entre las dos matrices
    return np.dot(vecestacionario, producto.sum(axis=0)) #suma las columnas armando un nuevo vector y multiplicando este por el vector estacionario


if len(sys.argv) >1:
    filename2 = sys.argv[1]
    print(filename2)
    if len(sys.argv)==3:
        N=sys.argv[2]
else:
    print("No se proporcionaron parámetros.")
filename="tp1_sample0.bin"

mat_acum=Genera_Matriz_Acumulada(filename) 
print(mat_acum)
mat_prob_condicionales=matriz_probabilidades_condicionales(mat_acum)
if fuente_memoria_nula(mat_prob_condicionales)==True:
    print("La fuente es de memoria nula")
    print("La entropia es: ",entropia(mat_prob_condicionales))
else:
    print("La fuente es de memoria no nula")
    vecestacionario= Genera_VecEstacionario(mat_prob_condicionales)
    print("La entropia de la fuente es: ", entropiaNoNula(vecestacionario,mat_prob_condicionales))
    print("El vector estacionario resulta:", vecestacionario)

