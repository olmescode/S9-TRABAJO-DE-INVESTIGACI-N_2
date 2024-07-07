import numpy as np

def es_subespacio_R3(condicion):
    """
    Verifica si un subconjunto de R^3 es un subespacio.
    
    :param condicion: Función que toma (a, b, c) y devuelve True si el vector cumple la condición
    :return: True si es subespacio, False si no lo es
    """
    # Verificar si el vector cero (0,0,0) está en el subconjunto
    if not condicion(0, 0, 0):
        return False
    
    # Verificar cerradura bajo la suma y multiplicación escalar
    for _ in range(100):  # Prueba con 100 pares de vectores aleatorios
        v1 = np.random.rand(3)
        v2 = np.random.rand(3)
        escalar = np.random.rand()
        
        if condicion(*v1) and condicion(*v2):
            # Suma
            suma = v1 + v2
            if not condicion(*suma):
                return False
            
            # Multiplicación escalar
            producto = escalar * v1
            if not condicion(*producto):
                return False
    
    return True

def es_subespacio_R4(condicion):
    """
    Verifica si un subconjunto de R^4 es un subespacio.
    
    :param condicion: Función que toma (a, b, c, d) y devuelve True si el vector cumple la condición
    :return: True si es subespacio, False si no lo es
    """
    # Verificar si el vector cero (0,0,0,0) está en el subconjunto
    if not condicion(0, 0, 0, 0):
        return False
    
    # Verificar cerradura bajo la suma y multiplicación escalar
    for _ in range(100):  # Prueba con 100 pares de vectores aleatorios
        v1 = np.random.rand(4)
        v2 = np.random.rand(4)
        escalar = np.random.rand()
        
        if condicion(*v1) and condicion(*v2):
            # Suma
            suma = v1 + v2
            if not condicion(*suma):
                return False
            
            # Multiplicación escalar
            producto = escalar * v1
            if not condicion(*producto):
                return False
    
    return True

def es_subespacio_M23(condicion):
    """
    Verifica si un subconjunto de M2x3 es un subespacio.
    
    :param condicion: Función que toma una matriz 2x3 y devuelve True si cumple la condición
    :return: True si es subespacio, False si no lo es
    """
    # Verificar si la matriz cero está en el subconjunto
    if not condicion(np.zeros((2, 3))):
        return False
    
    # Verificar cerradura bajo la suma y multiplicación escalar
    for _ in range(100):  # Prueba con 100 pares de matrices aleatorias
        m1 = np.random.rand(2, 3)
        m2 = np.random.rand(2, 3)
        escalar = np.random.rand()
        
        if condicion(m1) and condicion(m2):
            # Suma
            suma = m1 + m2
            if not condicion(suma):
                return False
            
            # Multiplicación escalar
            producto = escalar * m1
            if not condicion(producto):
                return False
    
    return True
