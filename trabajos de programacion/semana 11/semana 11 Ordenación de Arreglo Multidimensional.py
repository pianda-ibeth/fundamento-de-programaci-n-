"""Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.

Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).

Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).

Muestra la matriz original y la matriz con la fila ordenada."""

# Crear una matriz bidimensional (3x3)
matriz = [
    [3, 1, 7],
    [8, 2, 5],
    [4, 9, 6]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)
matriz = [
    [3, 1, 7],
    [8, 2, 5],
    [4, 9, 6]
]
# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort_fila(fila)

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)
[1, 3, 7]
[2, 5, 8]
[4, 6, 9]

