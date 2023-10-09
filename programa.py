import numpy as np
import sys
import copy
import binascii
import math
from itertools import product

def Genera_Matriz_Acumulada(nombre_archivo):
    
    with open(nombre_archivo,"rb") as archivo: #se abre el archivo en modo de lectura binaria
        contenido_binario=archivo.read() #se lee el contenido del archivo y se guarda  en contenido_binario
    
    cadena_bits = ''.join(format(byte, '08b') for byte in contenido_binario) #se convierte el contenido binario en una cadena de bits (cadena unica)

    mat = np.zeros((2, 2), dtype=int) 
    mat=np.array(mat) #se crea una matriz NumPy int de 2x2 llena de ceros
    
    for i in range(1,len(cadena_bits)): # se recorre secuencialmente la cadena de bits y se acumula en la matriz segun corresponda
        mat[int(cadena_bits[i]),int(cadena_bits[i-1])]+= 1 #se acumuna en fila de lectura actual y en la columna lectura anterior
    return mat

def matriz_probabilidades_condicionales(matcond):
    auxmat = np.zeros((2, 2), dtype=float)  # Create a copy to avoid modifying the original matrix
    
    aux = matcond[0, 0] + matcond[0, 1]
    aux = np.sum(matcond, axis=0)
    auxmat[:, 0] = matcond[:, 0] / aux[0]
    auxmat[:, 1] = matcond[:, 1] / aux[1]
    
    return auxmat

def is_fuente_memoria_nula(matprob):
    return abs(matprob[0,0]-matprob[1,0])<0.05 and abs(matprob[0,1]-matprob[1,1])<0.05

def calcular_probabilidades_fuente_nula(mat_acum):
    aux = np.sum(mat_acum)
    P0 = mat_acum[0] / aux
    P1 = mat_acum[1] / aux
    return {'0': P0, '1': P1}

def calcular_probabilidades_extension(probabilidades,orden):
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

def entropiaNula(probabilidades):
    return probabilidades['0']*math.log2(1/probabilidades['0']) + probabilidades['1']*math.log2(1/probabilidades['1'])

def entropiaExtensionNula(probabilidades,orden):
    aux=entropiaNula(probabilidades)
    return orden*aux
    
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
    mat_acum=Genera_Matriz_Acumulada(filename)
    mat_prob_condicionales=matriz_probabilidades_condicionales(mat_acum)

    if is_fuente_memoria_nula(mat_prob_condicionales)==True:
        print("La fuente es de memoria nula")
        prob_simbolos=calcular_probabilidades_fuente_nula(mat_acum)
        print("La entropia es: ",entropiaNula(prob_simbolos))   
        if len(sys.argv)==3:
            orden=sys.argv[2]
            probabilidades_extension= calcular_probabilidades_extension(prob_simbolos,orden)
            print("La entropia de la extension de orden N resulta: ", entropiaExtensionNula(prob_simbolos,orden))
        else:
            print("No se ha recibido el orden para el calculos de extension")
    else:
        print("La fuente es de memoria no nula")
        vecestacionario= Genera_VecEstacionario(mat_prob_condicionales)
        print("La entropia de la fuente es: ", entropiaNoNula(vecestacionario,mat_prob_condicionales))
        print("El vector estacionario resulta:", vecestacionario)
else:
    print("No se proporcionaron parámetros.")
