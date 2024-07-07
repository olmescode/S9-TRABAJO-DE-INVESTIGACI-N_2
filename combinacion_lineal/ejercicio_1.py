import numpy as np
from modulo_principal.linear_algebra_functions import vector_sum, scalar_multiply

# Ejercicio 1
u1 = np.array([-1, -2])
v1 = np.array([-3, -1])
result1 = vector_sum(u1, v1)
result1 = scalar_multiply(-1, result1)  # Restar 2v
print("Ejercicio 1 resultado:", result1)
