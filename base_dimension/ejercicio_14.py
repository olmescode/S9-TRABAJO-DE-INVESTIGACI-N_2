import numpy as np
from modulo_principal.base_dimension import find_matrix_basis, subspace_dimension_matrices

def solve_exercise_14():
    S = [
        np.array([[1, 0], [0, 1]]),
        np.array([[0, 1], [1, 0]]),
        np.array([[1, 1], [1, 1]]),
        np.array([[-1, 1], [1, -1]])
    ]

    basis = find_matrix_basis(S)
    dim_W = subspace_dimension_matrices(S)
    
    print("Base para el subespacio W:")
    for matrix in basis:
        print(matrix)
        print()
    
    print("Dimensión de W =", dim_W)

if __name__ == "__main__":
    solve_exercise_14()
    