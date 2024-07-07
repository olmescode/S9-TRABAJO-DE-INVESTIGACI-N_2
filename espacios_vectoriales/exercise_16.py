from modulo_principal.vector_space_axioms import check_vector_space_axioms

def vector_set_16(x, y, z):
    return (x, y)  # Aqui solo usamos x e y

def add_16(u, v):
    return (u[0] + v[0], u[1] + v[1])

def scalar_mult_16(c, v):
    return (0, 0)  # Siempre retorna el vector cero

zero_vector_16 = (0, 0)

def check_exercise_16():
    failed_axioms = check_vector_space_axioms(vector_set_16, add_16, scalar_mult_16, zero_vector_16)
    
    print("LIBRO DE KOLMAN PAG 278:")

    if not failed_axioms:
        print("El conjunto en el ejercicio 16 es un espacio vectorial.")
    else:
        print("El conjunto en el ejercicio 16 no es un espacio vectorial.")
        print("Axiomas que no se cumplen:")
        for axiom_num, axiom_name in failed_axioms:
            print(f"  - Axioma {axiom_num}: {axiom_name}")

    return failed_axioms

if __name__ == "__main__":
    check_exercise_16()
