from modulo_principal.base_dimension import find_basis, subspace_dimension

def solve_exercise_11():
    S = [
        (1, 2, 2),
        (3, 2, 1),
        (11, 10, 7),
        (7, 6, 4)
    ]

    basis = find_basis(S)
    dim_W = subspace_dimension(S)

    print("Conjunto S:", S)
    print("Base para el subespacio W =", basis)
    print("Dimensión de W =", dim_W)

if __name__ == "__main__":
    solve_exercise_11()
    