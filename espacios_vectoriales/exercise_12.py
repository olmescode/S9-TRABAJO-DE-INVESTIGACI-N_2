from modulo_principal.vector_space_axioms import check_vector_space_axioms

def vector_set_12(x, y, z):
    return (x, y, z)

def add_12(u, v):
    return (u[0] + v[0], u[1] + v[1], u[2] + v[2])

def scalar_mult_12(c, v):
    return (v[0], 1, v[2])

zero_vector_12 = (0, 0, 0)

def check_exercise_12():
    failed_axioms = check_vector_space_axioms(vector_set_12, add_12, scalar_mult_12, zero_vector_12)
    
    print("LIBRO DE KOLMAN PAG 278:")

    if not failed_axioms:
        print("El conjunto en el ejercicio 12 es un espacio vectorial.")
    else:
        print("El conjunto en el ejercicio 12 no es un espacio vectorial.")
        print("Axiomas que no se cumplen:")
        for axiom_num, axiom_name in failed_axioms:
            print(f"  - Axioma {axiom_num}: {axiom_name}")

    return failed_axioms

if __name__ == "__main__":
    check_exercise_12()
    