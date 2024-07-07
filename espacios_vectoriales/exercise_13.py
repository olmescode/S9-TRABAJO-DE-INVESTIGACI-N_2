from modulo_principal.vector_space_axioms import check_vector_space_axioms

def vector_set_13(x, y, z):
    return (0, 0, z)

def add_13(u, v):
    return (0, 0, u[2] + v[2])

def scalar_mult_13(c, v):
    return (0, 0, c * v[2])

zero_vector_13 = (0, 0, 0)

def check_exercise_13():
    failed_axioms = check_vector_space_axioms(vector_set_13, add_13, scalar_mult_13, zero_vector_13)
    
    print("LIBRO DE KOLMAN PAG 278:")
    
    if not failed_axioms:
        print("El conjunto en el ejercicio 13 es un espacio vectorial.")
    else:
        print("El conjunto en el ejercicio 13 no es un espacio vectorial.")
        print("Axiomas que no se cumplen:")
        for axiom_num, axiom_name in failed_axioms:
            print(f"  - Axioma {axiom_num}: {axiom_name}")

    return failed_axioms

if __name__ == "__main__":
    check_exercise_13()