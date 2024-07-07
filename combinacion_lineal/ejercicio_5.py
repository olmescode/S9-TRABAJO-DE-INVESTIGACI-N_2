import numpy as np
from modulo_principal.linear_algebra_functions import vector_equation_to_system

# Ejercicio 5
x1 = np.array([6, -1, 5])
x2 = np.array([-3, 4, 0])
result5 = np.array([1, -7, -5])

A5, b5 = vector_equation_to_system([x1, x2], result5)
print("Ejercicio 5 - Sistema de ecuaciones equivalente:")
print("A =")
print(A5)
print("b =", b5)
