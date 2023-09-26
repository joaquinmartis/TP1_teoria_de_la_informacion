import numpy
import binascii

def probabilidades_condicionales(matcond,nombre_archivo):
    bloque=0

    with open(nombre_archivo,"rb") as archivo:
        contenido_binario=archivo.read()
    
    cadena_bits = ''.join(format(byte, '08b') for byte in contenido_binario)

    print(cadena_bits)

    matcond = [
    [0, 0],
    [0, 0],
    ]

    matcond=numpy.array(matcond)
    i=1
    for i in range(len(cadena_bits)):
        matcond[int(cadena_bits[i-1]),int(cadena_bits[i])]+= 1

    print(matcond)



filename="tp1_sample0.bin"
matcond=0
probabilidades_condicionales(matcond,filename)