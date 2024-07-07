from modulo_principal.base_dimension import is_basis_for_r3

def check_basis_r3(vectors_list):
    results = []
    for vectors in vectors_list:
        is_basis = is_basis_for_r3(vectors)
        results.append(f"{vectors}: {'Es base' if is_basis else 'No es base'}")
    return results

# Conjuntos de vectores dados
vector_sets = [
    [(1, 2, 0), (0, 1, -1)],
    [(1, 1, -1), (2, 3, 4), (4, 1, -1), (0, 1, -1)],
    [(3, 2, 2), (-1, 2, 1), (0, 1, 0)],
    [(1, 0, 0), (0, 2, -1), (0, 1, 0)]
]

# Verificar cada conjunto
results = check_basis_r3(vector_sets)

# Imprimir resultados
for result in results:
    print(result)
