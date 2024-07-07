import numpy as np

def rango_matriz(matriz):
    """
    Calcula el rango de una matriz.
    
    Args:
    matriz (lista de listas): La matriz de entrada
    
    Returns:
    int: El rango de la matriz
    """
    return np.linalg.matrix_rank(np.array(matriz))

def imagen_matriz(matriz):
    """
    Calcula la imagen (espacio columna) de una matriz.
    
    Args:
    matriz (lista de listas): La matriz de entrada
    
    Returns:
    numpy.ndarray: La base ortonormal de la imagen de la matriz
    """
    _, _, Vt = np.linalg.svd(np.array(matriz))
    rango = rango_matriz(matriz)
    return Vt[:rango].T

def imprimir_matriz(matriz):
    """
    Imprime una matriz en un formato legible.
    
    Args:
    matriz (lista de listas): La matriz a imprimir
    """
    for fila in matriz:
        print([round(elemento, 4) for elemento in fila])
