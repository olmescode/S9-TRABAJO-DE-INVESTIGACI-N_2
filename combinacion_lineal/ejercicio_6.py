import numpy as np
from modulo_principal.linear_algebra_functions import vector_equation_to_system

# Ejercicio 6
x1 = np.array([-2, 3])
x2 = np.array([8, 5])
x3 = np.array([1, -6])
result6 = np.array([0, 0])

A6, b6 = vector_equation_to_system([x1, x2, x3], result6)
print("\nEjercicio 6 - Sistema de ecuaciones equivalente:")
print("A =")
print(A6)
print("b =", b6)
