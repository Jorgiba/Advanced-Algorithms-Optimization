import numpy as np
from typing import Tuple

# Multiplicacion de matrices


def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray) -> np.ndarray:
    i = 0
    j = 0
    k = 0

    m1_rows = np.size(m_1[0])
    m2_lines = np.size(m_2)

    C = np.zeros((m1_rows, m2_lines))

    if m1_rows == m2_lines:
        for i in range(m1_rows):
            for j in range(m2_lines):
                for k in range(m2_lines):
                    C[i, j] += m_1[i, k] * m_2[k, j]
        return C

    else:
        return "No se pueden multiplicar las matrices"

# Busqueda binaria recursiva


def rec_bb(t: list, f: int, l: int, key: int) -> int:

    if f > l or key > t[l] or key < t[f] or len(t) == 0:
        return None

    mid = (f + l) // 2

    if t[mid] == key:
        return mid

    elif t[mid] > key:
        return rec_bb(t, f, mid - 1, key)

    else:
        return rec_bb(t, mid + 1, l, key)

# Busqueda binaria iterativa


def bb(t: list, f: int, l: int, key: int) -> int:

    while f <= l:
        mid = (f + l) // 2
        if t[mid] == key:
            return mid
        elif t[mid] < key:
            f = mid + 1
        else:
            l = mid - 1
    return None

# Declaracion de padre e hijos


def _left(i: int) -> int:
    return 2 * i + 1


def _right(i: int) -> int:
    return 2 * i + 2


def _parent(i: int) -> int:
    return (i - 1) // 2

# heapify


def min_heapify(h: np.ndarray, i: int):

    root = i

    while 2 * i + 1 < len(h):

        if h[i] > h[_left(i)]:
            root = _left(i)

        if _right(i) < len(h) and h[i] > h[_right(
                i)] and h[_right(i)] < h[root]:
            root = _right(i)

        if root > i:
            h[i], h[root] = h[root], h[i]
            i = root

        else:
            return

# Insercion en min_heap


def insert_min_heap(h: np.ndarray, k: int) -> np.ndarray:

    h = np.append(h, k)
    j = np.size(h) - 1

    while j > 0 and h[_parent(j)] > h[j]:
        h[_parent(j)], h[j] = h[j], h[_parent(j)]
        j = _parent(j)

    return h

# creacion de min_heap


def create_min_heap(h: np.ndarray):

    x = (np.size(h) - 2) // 2

    while x > -1:
        min_heapify(h, x)
        x -= 1

# creacion cola de prioridad


def pq_ini():
    return np.zeros(0)

# inserción cola de prioridad


def pq_insert(h: np.ndarray, k: int) -> np.ndarray:

    return insert_min_heap(h, k)

# Extraccion cola de prioridad


def pq_remove(h: np.ndarray) -> tuple[int, np.ndarray]:

    if np.size(h) < 1:
        return h

    root = h[0]

    h[0] = h[np.size(h) - 1]
    np.delete(h, -1)
    min_heapify(h, 0)

    return (root, h)

# Ordenacion de min_heap


def min_heap_sort(h) -> np.ndarray:

    n = np.size(h)
    sorted_arr = np.empty(0)
    create_min_heap(h)

    for i in range(n):

        root = h[0]
        h[0] = h[np.size(h) - 1]
        np.delete(h, -1)
        min_heapify(h, 0)
        sorted_arr = np.append(sorted_arr, root)

    return sorted_arr
