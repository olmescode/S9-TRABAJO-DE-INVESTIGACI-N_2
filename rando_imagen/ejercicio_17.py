from modulo_principal.rango_imagen import rango_matriz, imagen_matriz, imprimir_matriz

# Ejercicio 17
matriz_17 = [
    [-1, -1, 0, 0],
    [0, 0, 2, 3],
    [4, 0, -2, 1],
    [3, -1, 0, 4]
]

print("Ejercicio 17:")
print("Matriz:")
imprimir_matriz(matriz_17)

rango_17 = rango_matriz(matriz_17)
print(f"Rango: {rango_17}")

print("Imagen (Espacio Columna):")
imagen_17 = imagen_matriz(matriz_17)
imprimir_matriz(imagen_17)