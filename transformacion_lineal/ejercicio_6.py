import numpy as np
from modulo_principal.transformacion_lineal import es_transformacion_lineal

def transformacion_6(v):
    return np.array([v[2], v[0], v[1]])

def resolver_ejercicio_6():
    resultado = es_transformacion_lineal(transformacion_6, 3, 3)
    print(f"Ejercicio 6: La transformación es {'lineal' if resultado else 'no lineal'}")

if __name__ == "__main__":
    resolver_ejercicio_6()
