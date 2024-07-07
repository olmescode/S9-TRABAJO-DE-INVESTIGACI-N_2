from modulo_principal.rango_imagen import rango_matriz, imagen_matriz, imprimir_matriz

# Ejercicio 18
matriz_18 = [
    [3, 0, 0],
    [0, 0, 0],
    [0, 0, 6]
]

print("Ejercicio 18:")
print("Matriz:")
imprimir_matriz(matriz_18)

rango_18 = rango_matriz(matriz_18)
print(f"Rango: {rango_18}")

print("Imagen (Espacio Columna):")
imagen_18 = imagen_matriz(matriz_18)
imprimir_matriz(imagen_18)