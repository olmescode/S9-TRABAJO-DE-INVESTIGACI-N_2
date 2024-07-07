import numpy as np
from modulo_principal.verificar_subespacios import es_subespacio_M23

# (a) [a b c; d e f], donde a = 2c + 1
def condicion_a(matriz):
    return matriz[0, 0] == 2 * matriz[0, 2] + 1

# (b) [a 1 a; b c 0]
def condicion_b(matriz):
    return matriz[0, 1] == 1 and matriz[0, 2] == matriz[0, 0] and matriz[1, 2] == 0

# (c) [a b c; d e f], donde a + e = 0 y b + d + f = 0
def condicion_c(matriz):
    return matriz[0, 0] + matriz[1, 1] == 0 and matriz[0, 1] + matriz[1, 0] + matriz[1, 2] == 0

# Verificaciones
print("Ejercicio 17:")
print("(a) Es subespacio:", es_subespacio_M23(condicion_a))
print("(b) Es subespacio:", es_subespacio_M23(condicion_b))
print("(c) Es subespacio:", es_subespacio_M23(condicion_c))