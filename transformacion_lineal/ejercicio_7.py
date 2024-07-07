import numpy as np
from modulo_principal.transformacion_lineal import es_transformacion_lineal

def transformacion_7(v):
    return np.array([1, v[2]])

def resolver_ejercicio_7():
    resultado = es_transformacion_lineal(transformacion_7, 3, 2)
    print(f"Ejercicio 7: La transformación es {'lineal' if resultado else 'no lineal'}")

if __name__ == "__main__":
    resolver_ejercicio_7()
