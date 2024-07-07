import random
from typing import Callable, Any

def check_vector_space_axioms(
    vector_set: Callable[[float, float, float], Any],
    add: Callable[[Any, Any], Any],
    scalar_mult: Callable[[float, Any], Any],
    zero_vector: Any,
    num_tests: int = 100
) -> list:
    failed_axioms = []
    axiom_names = {
        1: "Cierre bajo la adición",
        2: "Conmutatividad de la adición",
        3: "Asociatividad de la adición",
        4: "Existencia del elemento neutro",
        5: "Existencia del inverso aditivo",
        6: "Cierre bajo multiplicación escalar",
        7: "Distributividad de escalares sobre vectores",
        8: "Distributividad de escalares",
        9: "Asociatividad de multiplicación escalar",
        10: "Identidad de multiplicación escalar"
    }

    def almost_equal(a, b, tolerance=1e-9):
        if isinstance(a, (tuple, list)) and isinstance(b, (tuple, list)):
            return all(abs(x - y) < tolerance for x, y in zip(a, b))
        return abs(a - b) < tolerance

    def random_vector():
        return vector_set(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10))

    # Axioma 1: Cerradura bajo la adicion
    for _ in range(num_tests):
        u, v = random_vector(), random_vector()
        if not isinstance(add(u, v), type(u)):
            failed_axioms.append((1, axiom_names[1]))
            break

    # Axioma 2: Conmutatividad de la adicion
    for _ in range(num_tests):
        u, v = random_vector(), random_vector()
        if not almost_equal(add(u, v), add(v, u)):
            failed_axioms.append((2, axiom_names[2]))
            break

    # Axioma 3: Asociatividad de la adicion
    for _ in range(num_tests):
        u, v, w = random_vector(), random_vector(), random_vector()
        if not almost_equal(add(u, add(v, w)), add(add(u, v), w)):
            failed_axioms.append((3, axiom_names[3]))
            break

    # Axioma 4: Existencia del elemento neutro
    for _ in range(num_tests):
        v = random_vector()
        if not almost_equal(add(v, zero_vector), v):
            failed_axioms.append((4, axiom_names[4]))
            break

    # Axioma 5: Existencia del inverso aditivo
    for _ in range(num_tests):
        v = random_vector()
        v_inv = scalar_mult(-1, v)
        if not almost_equal(add(v, v_inv), zero_vector):
            failed_axioms.append((5, axiom_names[5]))
            break

    # Axioma 6: Cerradura bajo multiplicación escalar
    for _ in range(num_tests):
        c = random.uniform(-10, 10)
        v = random_vector()
        if not isinstance(scalar_mult(c, v), type(v)):
            failed_axioms.append((6, axiom_names[6]))
            break

    # Axioma 7: Distributividad de escalares sobre vectores
    for _ in range(num_tests):
        c = random.uniform(-10, 10)
        u, v = random_vector(), random_vector()
        if not almost_equal(scalar_mult(c, add(u, v)), add(scalar_mult(c, u), scalar_mult(c, v))):
            failed_axioms.append((7, axiom_names[7]))
            break

    # Axioma 8: Distributividad de escalares
    for _ in range(num_tests):
        c, d = random.uniform(-10, 10), random.uniform(-10, 10)
        v = random_vector()
        if not almost_equal(scalar_mult(c + d, v), add(scalar_mult(c, v), scalar_mult(d, v))):
            failed_axioms.append((8, axiom_names[8]))
            break

    # Axioma 9: Asociatividad de multiplicación escalar
    for _ in range(num_tests):
        c, d = random.uniform(-10, 10), random.uniform(-10, 10)
        v = random_vector()
        if not almost_equal(scalar_mult(c, scalar_mult(d, v)), scalar_mult(c * d, v)):
            failed_axioms.append((9, axiom_names[9]))
            break

    # Axioma 10: Identidad de multiplicacion escalar
    for _ in range(num_tests):
        v = random_vector()
        if not almost_equal(scalar_mult(1, v), v):
            failed_axioms.append((10, axiom_names[10]))
            break

    return failed_axioms
