import numpy as np
from modulo_principal.verificar_subespacios import es_subespacio_M23

# (a) [a b c; d 0 0], donde b = a + c
def condicion_a(matriz):
    return matriz[0, 1] == matriz[0, 0] + matriz[0, 2]

# (b) [a b c; d 0 0], donde c > 0
def condicion_b(matriz):
    return matriz[0, 2] > 0

# (c) [a b c; d e f], donde a = -2c y f = 2e + d
def condicion_c(matriz):
    return matriz[0, 0] == -2 * matriz[0, 2] and matriz[1, 2] == 2 * matriz[1, 1] + matriz[1, 0]

# Verificaciones
print("Ejercicio 16:")
print("(a) Es subespacio:", es_subespacio_M23(condicion_a))
print("(b) Es subespacio:", es_subespacio_M23(condicion_b))
print("(c) Es subespacio:", es_subespacio_M23(condicion_c))
