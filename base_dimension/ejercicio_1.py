from modulo_principal.base_dimension import is_basis_for_r2

def check_basis_r2(vectors_list):
    results = []
    for vectors in vectors_list:
        is_basis = is_basis_for_r2(vectors)
        results.append(f"{vectors}: {'Es base' if is_basis else 'No es base'}")
    return results

# Conjuntos de vectores dados
vector_sets = [
    [(1, 3), (1, -1)],
    [(0, 0), (1, 2), (2, 4)],
    [(1, 2), (2, -3), (3, 2)],
    [(1, 3), (-2, 6)]
]

# Verificar cada conjunto
results = check_basis_r2(vector_sets)

# Imprimir resultados
for result in results:
    print(result)
