import numpy as np
from modulo_principal.verificar_subespacios import es_subespacio_R4

# (a) (a, b, c), donde a == b == 0
def conjunto_a(a, b, c, d):
    return a == b == 0

# (b) (a, b, c), donde a == 1 and b == 0 and c + d == 1
def conjunto_b(a, b, c, d):
    return a == 1 and b == 0 and c + d == 1

# (c) (a, b, c), donde a > 0 and b < 0
def conjunto_c(a, b, c, d):
    return a > 0 and b < 0

# Verificaciones
print("Ejercicio 8:")
print("Caso (a):", es_subespacio_R4(conjunto_a))
print("Caso (b):", es_subespacio_R4(conjunto_b))
print("Caso (c):", es_subespacio_R4(conjunto_c))
