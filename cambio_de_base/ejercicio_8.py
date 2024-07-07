from modulo_principal.cambio_base import vector_a_nueva_base
import numpy as np

def ejercicio_8():
    # Vectores dados en R³
    v1 = np.array([1, 0, 0])
    v2 = np.array([0, 0, 1])
    v3 = np.array([1, 1, 1])
    
    # Base dada
    # Transponemos para que cada columna sea un vector de la base
    base = np.array([v1, v2, v3]).T
    
    # Vectores a expresar en la nueva base
    vectores = [
        np.array([1, 0, 0]),
        np.array([0, 1, 1]),
        np.array([1, 1, 1])
    ]
    
    resultados = []
    for v in vectores:
        resultado = vector_a_nueva_base(v, np.eye(3), base)
        resultados.append(resultado)
    
    return resultados

if __name__ == "__main__":
    resultados = ejercicio_8()
    for i, resultado in enumerate(resultados, 1):
        print(f"Vector {i} en la nueva base: {resultado}")
