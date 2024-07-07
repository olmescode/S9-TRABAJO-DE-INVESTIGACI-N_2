from modulo_principal.cambio_base import matriz_a_nueva_base
import numpy as np

def ejercicio_18():
    # Matriz dada
    matriz = np.array([[2, -1],
                       [4, 6]])
    
    # Base dada
    base = np.array([
        [[1, 1], [2, 0]],
        [[-1, 0], [3, 1]],
        [[0, 1], [-1, 0]],
        [[0, -2], [0, 4]]
    ])
    
    # Calcular el resultado
    resultado = matriz_a_nueva_base(matriz, base)
    
    return resultado

if __name__ == "__main__":
    resultado = ejercicio_18()
    print("Matriz en la nueva base:")
    print(resultado)
