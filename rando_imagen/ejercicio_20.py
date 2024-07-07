from modulo_principal.rango_imagen import rango_matriz, imagen_matriz, imprimir_matriz

# Ejercicio 20
matriz_20 = [
    [1, 2, 3],
    [0, 0, 4],
    [0, 0, 6]
]

print("Ejercicio 20:")
print("Matriz:")
imprimir_matriz(matriz_20)

rango_20 = rango_matriz(matriz_20)
print(f"Rango: {rango_20}")

print("Imagen (Espacio Columna):")
imagen_20 = imagen_matriz(matriz_20)
imprimir_matriz(imagen_20)