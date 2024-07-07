from modulo_principal.base_dimension import find_basis, subspace_dimension

def solve_exercise_12():
    S = [
        (1, 1, 0, -1),
        (0, 1, 2, 1),
        (1, 0, 1, -1),
        (1, 1, -6, -3),
        (-1, -5, 1, 0)
    ]

    basis = find_basis(S)
    dim_W = subspace_dimension(S)

    print("Conjunto S:", S)
    print("Base para el subespacio W =", basis)
    print("Dimensión de W =", dim_W)

if __name__ == "__main__":
    solve_exercise_12()
    