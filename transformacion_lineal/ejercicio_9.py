import numpy as np
from modulo_principal.transformacion_lineal import es_transformacion_lineal

def transformacion_9(v):
    return np.array([v[0]**2, v[1]])

def resolver_ejercicio_9():
    resultado = es_transformacion_lineal(transformacion_9, 2, 2)
    print(f"Ejercicio 9: La transformación es {'lineal' if resultado else 'no lineal'}")

if __name__ == "__main__":
    resolver_ejercicio_9()
