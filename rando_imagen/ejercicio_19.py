from modulo_principal.rango_imagen import rango_matriz, imagen_matriz, imprimir_matriz

# Ejercicio 19
matriz_19 = [
    [0, 0, 1],
    [0, 0, 2],
    [1, 2, 4]
]

print("Ejercicio 19:")
print("Matriz:")
imprimir_matriz(matriz_19)

rango_19 = rango_matriz(matriz_19)
print(f"Rango: {rango_19}")

print("Imagen (Espacio Columna):")
imagen_19 = imagen_matriz(matriz_19)
imprimir_matriz(imagen_19)