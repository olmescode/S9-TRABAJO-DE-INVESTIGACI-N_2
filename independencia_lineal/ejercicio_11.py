from modulo_principal.independencia_lineal import son_linealmente_independientes

vectores = [
    [1, -1, 4],
    [2, 1, -1],
    [3, -1, 1]
]

independientes = son_linealmente_independientes(vectores)

if independientes:
    print("Los vectores son linealmente independientes.")
else:
    print("Los vectores son linealmente dependientes.")
