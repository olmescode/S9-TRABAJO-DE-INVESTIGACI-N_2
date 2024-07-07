from modulo_principal.rango_imagen import rango_matriz, imagen_matriz, imprimir_matriz

# Ejercicio 16
matriz_16 = [
    [1, -1, 2, 3],
    [-2, 2, -4, -6],
    [2, -2, 4, 6],
    [3, -3, 6, 9]
]

print("Ejercicio 16:")
print("Matriz:")
imprimir_matriz(matriz_16)

rango_16 = rango_matriz(matriz_16)
print(f"Rango: {rango_16}")

print("Imagen (Espacio Columna):")
imagen_16 = imagen_matriz(matriz_16)
imprimir_matriz(imagen_16)
