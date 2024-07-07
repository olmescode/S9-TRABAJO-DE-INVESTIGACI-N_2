from modulo_principal.vector_space_axioms import check_vector_space_axioms

def vector_set_11(x, y, z):
    return (x, y, z)

def add_11(u, v):
    return (u[0] + v[0], u[1] + v[1], v[2])

def scalar_mult_11(c, v):
    return (c * v[0], c * v[1], c * v[2])

zero_vector_11 = (0, 0, 0)

def check_exercise_11():
    failed_axioms = check_vector_space_axioms(vector_set_11, add_11, scalar_mult_11, zero_vector_11)
    
    print("LIBRO DE KOLMAN PAG 278:")

    if not failed_axioms:
        print("El conjunto en el ejercicio 11 es un espacio vectorial.")
    else:
        print("El conjunto en el ejercicio 11 no es un espacio vectorial.")
        print("Axiomas que no se cumplen:")
        for axiom_num, axiom_name in failed_axioms:
            print(f"  - Axioma {axiom_num}: {axiom_name}")

    return failed_axioms

if __name__ == "__main__":
    check_exercise_11()
