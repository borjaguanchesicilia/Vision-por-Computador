import math
from matriz import *

def brillo(matriz, filas, columnas):
    n = filas*columnas
    sum = 0
    media = 0
    for i in range(filas):
        for j in range(columnas):
            sum += matriz.getVal(i, j)
    
    media = sum / n

    return round(media)