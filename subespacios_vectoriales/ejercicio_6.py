from modulo_principal.verificar_subespacios import es_subespacio_R3

# (a) (a, b, c), donde a = c = 0
def condicion_a(a, b, c):
    return a == 0 and c == 0

# (b) (a, b, c), donde a = -c
def condicion_b(a, b, c):
    return a == -c

# (c) (a, b, c), donde b = 2a + 1
def condicion_c(a, b, c):
    return b == 2*a + 1

# Verificaciones
print("Ejercicio 6:")
print("(a) Es subespacio:", es_subespacio_R3(condicion_a))
print("(b) Es subespacio:", es_subespacio_R3(condicion_b))
print("(c) Es subespacio:", es_subespacio_R3(condicion_c))
