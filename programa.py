import numpy as np
import sys
import copy
import binascii
import math

<<<<<<< Updated upstream
def Genera_Matriz_Acumulada(nombre_archivo):
=======
from itertools import product

def calcular_probabilidades_fuente_nula(probabilidades, orden):
    # Inicializar un diccionario para almacenar las probabilidades de la fuente nula
    probabilidades_fuente_nula = {}

    # Generar todas las posibles secuencias de longitud 'orden'
    simbolos = list(probabilidades.keys())
    secuencias = product(simbolos, repeat=orden)

    # Calcular las probabilidades de la fuente nula
    for secuencia in secuencias:
        prob_secuencia = 1.0  # Probabilidad de la secuencia inicializada a 1.0
        for simbolo in secuencia:
            prob_secuencia *= probabilidades[simbolo]
        probabilidades_fuente_nula[''.join(secuencia)] = prob_secuencia

    return probabilidades_fuente_nula

# Símbolos y sus probabilidades
probabilidades = {'A': 0.3, 'B': 0.4, 'C': 0.3}

# Orden de la fuente nula (puede cambiar)
orden = 3

# Calcular las probabilidades de la fuente nula con el orden especificado
resultados = calcular_probabilidades_fuente_nula(probabilidades, orden)

# Mostrar las probabilidades de la fuente nula
for secuencia, probabilidad in resultados.items():
    print(f"P({secuencia}) = {probabilidad}")

def probabilidades_condicionales(nombre_archivo):
    bloque=0
>>>>>>> Stashed changes

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
    auxmat[0,0]-=1
    auxmat[1,]=1 # se pone unos en la fila 1
    b=np.array([0,1]) #vector de terminos independientes o constantes
    x=np.linalg.solve(auxmat,b) #resuelve sistema de ecuaciones a partir de que (M-I)V*=0 y sumatoria_de_Vi*=1
    return x

def entropiaNoNula(vecestacionario,mat_prob_condicionales):
    log_mat= np.log2(1/mat_prob_condicionales) #calcula el  base 2 de los elementos de la matriz
    producto = mat_prob_condicionales*log_mat #calcula el producto elemento a elemento entre las dos matrices
    return np.dot(vecestacionario, producto.sum(axis=0)) #suma las columnas armando un nuevo vector y multiplicando este por el vector estacionario


if len(sys.argv) >1:
    filename = sys.argv[1]
    print(filename)
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
<<<<<<< Updated upstream
    print("La entropia es: ",entropia(mat_prob_condicionales))
else:
    print("La fuente es de memoria no nula")
    vecestacionario= Genera_VecEstacionario(mat_prob_condicionales)
    print("La entropia de la fuente es: ", entropiaNoNula(vecestacionario,mat_prob_condicionales))
    print("El vector estacionario resulta:", vecestacionario)

=======
print("La entropia es: ",entropia(mat_prob_condicionales))
vec_probabilidades_simbolos=['0':0.5,'1':0.5]
calcular_probabilidades_fuente_nula(mat_prob_condicionales,2)
>>>>>>> Stashed changes
