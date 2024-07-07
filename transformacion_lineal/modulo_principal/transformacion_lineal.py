import numpy as np

def es_transformacion_lineal(T, dim_entrada, dim_salida):
    """
    Verifica si una transformación T es lineal.
    
    :param T: Función que representa la transformación
    :param dim_entrada: Dimensión del espacio de entrada
    :param dim_salida: Dimensión del espacio de salida
    :return: True si es lineal, False en caso contrario
    """
    # Generamos vectores aleatorios para la prueba
    v1 = np.random.rand(dim_entrada)
    v2 = np.random.rand(dim_entrada)
    escalar = np.random.rand()
    
    # Propiedad 1: T(v1 + v2) = T(v1) + T(v2)
    propiedad1 = np.allclose(T(v1 + v2), T(v1) + T(v2))
    
    # Propiedad 2: T(c*v) = c*T(v)
    propiedad2 = np.allclose(T(escalar * v1), escalar * T(v1))
    
    return propiedad1 and propiedad2
