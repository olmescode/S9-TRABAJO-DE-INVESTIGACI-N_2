import numpy as np

def vector_sum(u, v):
    """Calcula la suma de dos vectores."""
    return np.add(u, v)

def scalar_multiply(scalar, vector):
    """Multiplica un vector por un escalar."""
    return np.multiply(scalar, vector)

def is_linear_combination(vectors, b):
    """
    Determina si b es una combinación lineal de los vectores dados.
    
    Args:
    vectors (list): Lista de vectores (cada uno es un np.array)
    b (np.array): Vector a comprobar
    
    Returns:
    bool: True si b es una combinación lineal, False en caso contrario
    """
    A = np.column_stack(vectors)
    try:
        np.linalg.solve(A, b)
        return True
    except np.linalg.LinAlgError:
        return False

def vector_equation_to_system(vectors, result):
    """
    Convierte una ecuación vectorial en un sistema de ecuaciones lineales.
    
    Args:
    vectors (list): Lista de vectores (cada uno es un np.array)
    result (np.array): Vector resultado
    
    Returns:
    tuple: Matriz de coeficientes A y vector de términos independientes b
    """
    A = np.column_stack(vectors)
    b = result
    return A, b

def solve_linear_system(A, b):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b.
    
    Args:
    A (np.array): Matriz de coeficientes
    b (np.array): Vector de términos independientes
    
    Returns:
    np.array: Solución del sistema
    """
    return np.linalg.solve(A, b)
