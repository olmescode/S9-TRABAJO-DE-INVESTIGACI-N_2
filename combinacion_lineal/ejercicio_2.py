import numpy as np
from modulo_principal.linear_algebra_functions import vector_sum, scalar_multiply

# Ejercicio 2
u2 = np.array([3, 2])
v2 = np.array([2, -1])
result2 = vector_sum(u2, v2)
result2 = scalar_multiply(-1, result2)  # Restar 2v
print("Ejercicio 2 resultado:", result2)
