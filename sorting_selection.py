"""Funciones que resuelven todos los problemas establecidos durante la práctica"""
from typing import Tuple, Union, List, Dict
from collections import OrderedDict
import numpy as np

def split(t: np.ndarray)-> Tuple[np.ndarray, int, np.ndarray]:
    """Función que divide una tabla en función de su primer elemento"""
    piv = t[0]
    t_l = [u for u in t if u < piv]
    t_r = [u for u in t if u > piv]
    return np.array(t_l), piv, np.array(t_r)

def qsel(t: np.ndarray, k: int)-> Union[int, None]:
    """Función recursiva que devuelve el elemento que ocuparía un índice dado en una lista"""

    if k > len(t) - 1 or k < 0 or len(t) < 1:
        return None

    if len(t) == 1 and k == 0:
        return t[0]

    if len(t) <= 5:
        t = np.sort(t)
        return t[k]

    t_l, piv, t_r = split(t)
    left_longitude = len(t_l)

    if k == left_longitude:
        return piv

    if k < left_longitude:
        return qsel(t_l, k)

    return qsel(t_r, k-left_longitude-1)

def qsel_nr(t: np.ndarray, k: int)-> Union[int, None]:
    """Función no recursiva que devuelve el elemento que ocuparía un índice dado en una lista"""

    while True:

        if k > len(t) - 1 or k < 0 or len(t) < 1:
            return None

        if len(t) == 1 and k == 0:
            return t[0]

        if len(t) <= 5:
            t = np.sort(t)
            return t[k]

        t_l, piv, t_r = split(t)
        left_longitude = len(t_l)

        if k == left_longitude:
            return piv

        if k < left_longitude:
            t = t_l

        elif k > left_longitude:
            t = t_r
            k = k - left_longitude - 1

        else:
            return None

def split_pivot(t: np.ndarray, mid: int)-> Tuple[np.ndarray, int, np.ndarray]:
    """Función que divide una tabla en función de un elemento introducido"""

    t_l = [u for u in t if u < mid]
    t_r = [u for u in t if u > mid]
    return t_l, mid, t_r

def pivot5(t: np.ndarray)-> int:
    """Función que escoge el pivote según el procedimiento mediana de medianas"""
    size = len(t)
    t_pivotes = []
    i = 0

    while (i + 4) < size:

        pivote = qsel5_nr(t[i:i+4], 2)
        t_pivotes.append(pivote)
        i += 4

    if i < (size - 1):
        selec = qsel5_nr(t[i:], int((len(t[i:])/2 - 1)))
        t_pivotes.append(selec)

    np_pivotes = np.array(t_pivotes)

    return qsel5_nr(np_pivotes, int((len(np_pivotes)/2 - 1)))

def qsel5_nr(t: np.ndarray, k: int)-> Union[int, None]:
    """Función que implementa el QuickSelect con procedimiento de mediana de medianas"""

    while True:

        if k > len(t) - 1 or k < 0:
            return None

        if len(t) == 1 and k == 0:
            return t[0]

        if len(t) <= 5:
            t = np.sort(t)
            return t[k]

        t_l, mid, t_r = split_pivot(t, pivot5(t))
        left_longitude = len(t_l)

        if k == left_longitude:
            return mid

        if k < left_longitude:
            t = t_l

        elif k > left_longitude:
            t = t_r
            k = k - left_longitude - 1

        else:
            return None

def qsort_5(t: np.ndarray)-> np.ndarray:
    """Función que implementa el QuickSort con procedimiento de mediana de medianas"""
    size = len(t)
    pivot = 0
    t_l = np.empty(0)
    t_r = np.empty(0)

    if size - 1 >= 1:

        t_l, pivot, t_r = split_pivot(t, pivot5(t))

        izquierda = qsort_5(t_l)
        derecha = qsort_5(t_r)

        t = np.append(izquierda, pivot)
        t = np.append(t, derecha)

    return t

def change_pd(c: int, l_coins: List[int]) -> np.ndarray:
    """Función que devuelve la matriz que resuelve el problema del cambio"""
    matrix = np.full((len(l_coins) + 1, c + 1), float('inf'))
    matrix[:, 0] = 0
    for i in range(1, len(l_coins) + 1):
        for amount in range(1, c + 1):
            if l_coins[i - 1] <= amount:
                aux = min(matrix[i - 1, amount], 1 + matrix[i, amount - l_coins[i - 1]])
                matrix[i, amount] = aux
            else:
                matrix[i, amount] = matrix[i - 1, amount]
    return matrix

def optimal_change_pd(c: int, l_coins: List[int]) -> Dict:
    """Función que devuelve una combinación de monedas equivalentes a un valor de manera óptima"""
    matrix = [[float('inf')] * (c + 1) for _ in range(len(l_coins) + 1)]
    coins_used = {}

    for i in range(len(l_coins) + 1):
        matrix[i][0] = 0

    for i in range(1, len(l_coins) + 1):
        for amount in range(1, c + 1):
            if l_coins[i - 1] <= amount:
                aux = min(matrix[i - 1][amount], 1 + matrix[i][amount - l_coins[i - 1]])
                matrix[i][amount] = aux
            else:
                matrix[i][amount] = matrix[i - 1][amount]
    i = len(l_coins)
    j = c
    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i - 1][j]:
            coin = l_coins[i - 1]
            coins_used[coin] = coins_used.get(coin, 0) + 1
            j -= coin
        else:
            i -= 1

    coins_used = dict(OrderedDict(sorted(coins_used.items())))

    return coins_used

def knapsack_fract_greedy(l_weights: List[int], l_values: List[int], bound: int) -> Dict:
    """Función que devuelve la solución voraz requerida para el problema de la mochila fracc"""
    size = len(l_weights)

    items = [{'index': i, 'weight': l_weights[i], 'value': l_values[i]} for i in range(size)]

    sorted_items = sorted(items, key=lambda items: items['value'] / items['weight'], reverse=True)

    result = {}
    for i in range(size):
        result[i] = 0

    remaining_space = bound

    for item in sorted_items:
        index = item['index']
        weight = item['weight']

        if weight <= remaining_space:
            result[index] = weight
            remaining_space -= weight
        else:
            result[index] = remaining_space
            break

    return result

def knapsack_01_pd(l_weights: List[int], l_values: List[int], bound: int)-> int:
    """Función que devuelve la solución PD requerida para el problema de la mochila 0/1"""
    size = len(l_weights)

    matrix = [[0] * (bound + 1) for i in range(size)]

    for j in range(size):
        for k in range(bound + 1):
            if l_weights[j - 1] <= k:
                aux = max(matrix[j - 1][k], matrix[j - 1][k - l_weights[j - 1]] + l_values[j - 1])
                matrix[j][k] = aux
            else:
                matrix[j][k] = matrix[j - 1][k]

    return matrix[size - 1][bound]
