from modulo_principal.independencia_lineal import son_linealmente_independientes

vectores = [
    [0, 0, -3],
    [0, 5, 4],
    [2, -8, 1]
]

independientes = son_linealmente_independientes(vectores)

if independientes:
    print("Los vectores son linealmente independientes.")
else:
    print("Los vectores son linealmente dependientes.")