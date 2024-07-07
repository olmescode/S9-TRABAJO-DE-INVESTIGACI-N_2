import numpy as np
from modulo_principal.transformacion_lineal import es_transformacion_lineal

def transformacion_8(v):
    return np.array([v[0]**2, v[1]**2])

def resolver_ejercicio_8():
    resultado = es_transformacion_lineal(transformacion_8, 2, 2)
    print(f"Ejercicio 8: La transformación es {'lineal' if resultado else 'no lineal'}")

if __name__ == "__main__":
    resolver_ejercicio_8()
