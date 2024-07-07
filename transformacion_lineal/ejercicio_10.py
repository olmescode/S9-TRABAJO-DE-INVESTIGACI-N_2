import numpy as np
from modulo_principal.transformacion_lineal import es_transformacion_lineal

def transformacion_10(v):
    return np.array([v[1], v[0]])

def resolver_ejercicio_10():
    resultado = es_transformacion_lineal(transformacion_10, 2, 2)
    print(f"Ejercicio 10: La transformación es {'lineal' if resultado else 'no lineal'}")

if __name__ == "__main__":
    resolver_ejercicio_10()
