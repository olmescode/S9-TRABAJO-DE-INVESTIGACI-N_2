from modulo_principal.verificar_subespacios import es_subespacio_R4

# (a) (a, b, c), donde a - b == 2
def conjunto_a(a, b, c, d):
    return a - b == 2

# (b) (a, b, c), donde c == a + 2*b and d == a - 3*b
def conjunto_b(a, b, c, d):
    return c == a + 2*b and d == a - 3*b

# (c) (a, b, c), donde a == 0 and b == -d
def conjunto_c(a, b, c, d):
    return a == 0 and b == -d

# Verificaciones
print("Ejercicio 7:")
print("Caso (a):", es_subespacio_R4(conjunto_a))
print("Caso (b):", es_subespacio_R4(conjunto_b))
print("Caso (c):", es_subespacio_R4(conjunto_c))
