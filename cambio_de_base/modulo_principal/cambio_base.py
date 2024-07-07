import numpy as np

def vector_a_nueva_base(vector, base_antigua, base_nueva):
    """
    Convierte un vector de una base a otra.
    
    :param vector: El vector a convertir
    :param base_antigua: La base actual del vector
    :param base_nueva: La nueva base a la que se convertirá el vector
    :return: El vector en la nueva base
    """
    # Convertir bases a arrays de numpy
    base_antigua = np.array(base_antigua).T
    base_nueva = np.array(base_nueva).T
    
    # Calcular la matriz de transición
    matriz_transicion = np.linalg.inv(base_nueva) @ base_antigua
    
    # Convertir vector a array de numpy
    vector = np.array(vector)
    
    # Calcular vector en la nueva base
    nuevo_vector = np.linalg.inv(matriz_transicion) @ vector
    
    return nuevo_vector.round(10)  # Redondear para evitar errores de punto flotante

def matriz_a_nueva_base(matriz, base):
    """
    Expresa una matriz en términos de una base dada de matrices.
    
    :param matriz: La matriz a convertir (2x2)
    :param base: La base de matrices (lista de cuatro matrices 2x2)
    :return: Coeficientes de la matriz en la nueva base
    """
    # Convertir la matriz y la base a arrays de numpy
    matriz = np.array(matriz)
    base = np.array(base)
    
    # Crear una matriz de 4x4 a partir de la base
    A = np.vstack([base[i].flatten() for i in range(4)])
    
    # Aplanar la matriz dada
    b = matriz.flatten()
    
    # Resolver el sistema de ecuaciones Ax = b
    coeficientes = np.linalg.solve(A, b)
    
    return coeficientes.round(10)  # Redondear para evitar errores de punto flotante
