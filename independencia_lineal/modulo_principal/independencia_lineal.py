import numpy as np
from sympy import symbols, Eq, solve, Matrix

def son_linealmente_independientes(vectores):
    """
    Determina si un conjunto de vectores es linealmente independiente.
    
    Args:
    vectores (list of list): Lista de vectores a evaluar.
    
    Returns:
    bool: True si los vectores son linealmente independientes, False en caso contrario.
    """
    matriz = np.array(vectores).T
    rango = np.linalg.matrix_rank(matriz)
    return rango == len(vectores)
