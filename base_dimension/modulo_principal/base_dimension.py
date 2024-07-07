import numpy as np

def is_linearly_independent(vectors):
    matrix = np.array(vectors)
    rank = np.linalg.matrix_rank(matrix)
    return rank == len(vectors)

## Ejercicio 1, 2
def is_basis_for_r2(vectors):
    if len(vectors) != 2:
        return False
    return is_linearly_independent(vectors)

def is_basis_for_r3(vectors):
    if len(vectors) != 3:
        return False
    return is_linearly_independent(vectors)

## Ejercicio 11, 12
def find_basis(vectors):
    matrix = np.array(vectors)
    rank = np.linalg.matrix_rank(matrix)
    basis = []
    for i in range(len(vectors)):
        temp = basis + [vectors[i]]
        if np.linalg.matrix_rank(np.array(temp)) > len(basis):
            basis.append(vectors[i])
        if len(basis) == rank:
            break
    return basis

def subspace_dimension(vectors):
    return np.linalg.matrix_rank(np.array(vectors))

## Ejercicio 14
def find_matrix_basis(matrices):
    vectors = [matrix.flatten() for matrix in matrices]
    basis_vectors = find_basis(vectors)
    return [vector.reshape(matrices[0].shape) for vector in basis_vectors]

def subspace_dimension_matrices(matrices):
    vectors = [matrix.flatten() for matrix in matrices]
    return subspace_dimension(vectors)
