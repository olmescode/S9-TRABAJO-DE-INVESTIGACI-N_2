import numpy as np
from modulo_principal.linear_algebra_functions import is_linear_combination, solve_linear_system

# Ejercicio 12
a1 = np.array([1, -2, 2])
a2 = np.array([0, 5, 5])
a3 = np.array([2, 0, 8])
b = np.array([-5, 11, -7])

is_combination = is_linear_combination([a1, a2, a3], b)
print("\nEjercicio 12 resultado:", "b es una combinación lineal" if is_combination else "b no es una combinación lineal")

if is_combination:
    A = np.column_stack([a1, a2, a3])
    x = solve_linear_system(A, b)
    print("Coeficientes de la combinación lineal:", x)
