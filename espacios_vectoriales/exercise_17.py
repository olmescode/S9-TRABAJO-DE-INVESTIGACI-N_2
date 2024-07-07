from modulo_principal.vector_space_axioms import check_vector_space_axioms

def vector_set_17(x, y, z):
    return max(0.1, x)  # El valor sea siempre positivo

def add_17(u, v):
    return (u * v)  # La operación ⊕ se define como multiplicacion

def scalar_mult_17(c, v):
    return (v ** c)  # La operación ⊙ se define como potenciacion

zero_vector_17 = 1  # El elemento neutro es 1 para la multiplicacion

def check_exercise_17():
    failed_axioms = check_vector_space_axioms(vector_set_17, add_17, scalar_mult_17, zero_vector_17)
    
    print("LIBRO DE KOLMAN PAG 278:")

    if not failed_axioms:
        print("El conjunto en el ejercicio 17 es un espacio vectorial.")
    else:
        print("El conjunto en el ejercicio 17 no es un espacio vectorial.")
        print("Axiomas que no se cumplen:")
        for axiom_num, axiom_name in failed_axioms:
            print(f"  - Axioma {axiom_num}: {axiom_name}")

    return failed_axioms

if __name__ == "__main__":
    check_exercise_17()