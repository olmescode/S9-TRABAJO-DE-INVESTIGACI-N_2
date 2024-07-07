from modulo_principal.independencia_lineal import son_linealmente_independientes

vectores = [
    [5, 7, 9],
    [0, 2, 4],
    [0, -6, -8]
]

independientes = son_linealmente_independientes(vectores)

if independientes:
    print("Los vectores son linealmente independientes.")
else:
    print("Los vectores son linealmente dependientes.")
