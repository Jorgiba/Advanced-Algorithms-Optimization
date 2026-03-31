"""Modulos para la ejecución del archivo"""
import queue
import random
from queue import PriorityQueue
from typing import List
from typing import Tuple
from itertools import permutations
import numpy as np


def init_cd(n: int) -> np.ndarray:
    """inicializa un conjunto disjunto llenando un array con -1"""
    disjoint_set = np.full(n, -1)

    return disjoint_set


def union(rep_1: int, rep_2: int, p_cd: np.ndarray) -> int:
    """une dos subconjuntos disjuntos en base a dos números específicos"""
    num_1 = find(rep_1, p_cd)
    num_2 = find(rep_2, p_cd)

    if (num_1 == num_2 or num_1 == -1 or num_2 == -1):
        return -1

    if p_cd[num_2] < p_cd[num_1]:
        p_cd[num_1] = num_2
        return num_2

    if p_cd[num_2] > p_cd[num_1]:
        p_cd[num_2] = num_1
        return num_1

    p_cd[num_2] = num_1
    p_cd[num_1] -= 1
    return num_1


def find(ind: int, p_cd: np.ndarray) -> int:
    """encuentra cierto numero dentro del conjunto disjunto"""
    search = ind

    while p_cd[search] > -1:
        search = p_cd[search]

    while p_cd[ind] > -1:
        aux = p_cd[ind]
        p_cd[ind] = search
        ind = aux
    return search


def create_pq(n: int, l_g: List) -> queue.PriorityQueue:
    """crea una priority queue con utilidad para el algoritmo de kruskal"""
    p_q = PriorityQueue()
    n += n

    for arista in l_g:

        p_q.put((arista[2], (arista[0], arista[1])))

    return p_q


def kruskal(n: int, l_g: List) -> Tuple[int, List]:
    """define el algoritmo de kruskal usando colas de prioridad y conjuntos disjuntos"""
    l_t = []
    d_s = init_cd(n)
    p_q = create_pq(n, l_g)

    while not p_q.empty() and len(l_t) < n - 1:
        _, (u_node, v_node) = p_q.get()

        x_int = find(u_node, d_s)
        y_int = find(v_node, d_s)

        if x_int != y_int:
            l_t.append((u_node, v_node))
            union(x_int, y_int, d_s)

    if len(l_t) == n - 1:
        return n, l_t
    return None


def complete_graph(n_nodes: int, max_weight=50) -> Tuple[int, List]:
    """crea un grafo aleatorio con el número de nodos indicado y pesos no superiores a 50"""
    l_g = []
    n_n = 1
    flag = 0
    while n_n < n_nodes:
        m_int = 1
        while m_int < n_n:
            if flag == 0:
                rand = random.randint(1, max_weight)
                l_g.append((m_int, n_n, rand))
                m_int += 1
        n_n += 1

    return (n_nodes, l_g)


def dist_matrix(n_nodes: int, w_max=10) -> np.ndarray:
    """crea una matriz de distancias sobre un grafo con pesos máximos de 10"""
    matrix = np.random.randint(1, w_max + 1, (n_nodes, n_nodes))
    matrix = (matrix + matrix.T) // 2
    np.fill_diagonal(matrix, 0)
    return matrix


def greedy_tsp(dist_m: np.ndarray, node_ini=0) -> List:
    """define una versión del problema del viajante"""
    num_nodes = dist_m.shape[0]
    l_circuit = [node_ini]

    while len(l_circuit) < num_nodes:
        current_node = l_circuit[-1]

        choosing = np.argsort(dist_m[current_node])

        for node in choosing:
            if node not in l_circuit:
                l_circuit.append(node)
                break

    return l_circuit + [node_ini]


def len_circuit(circuit: List, dist_m: np.ndarray) -> int:
    """calcula la longitud de un circuito dada una matriz de distancias"""
    suma = 0
    for i in range(len(circuit) - 1):

        suma += dist_m[circuit[i], circuit[i + 1]]

    return suma


def repeated_greedy_tsp(dist_m: np.ndarray) -> List:
    """define el problema del viajante pero aplica el algoritmo a todos los nodos del grafo"""
    num_nodes = dist_m.shape[0]
    sol = []
    i = 0
    f_data = 0
    sol.append(greedy_tsp(dist_m, i))
    minimun = len_circuit(sol[0], dist_m)
    i += 1
    while i < num_nodes:
        sol.append(greedy_tsp(dist_m, i))
        length = len_circuit(sol[i], dist_m)
        if length < minimun:
            minimun = length
            f_data = i
        i += 1
    return sol[f_data]


def exhaustive_tsp(dist_m: np.ndarray) -> List:
    """define el problema del viajante pero examinando todos los posibles circuitos del grafo"""
    size = len(dist_m)
    nodes = list(range(size))
    camino_min = []
    flag = 0

    for perm in permutations(nodes):

        dist = len_circuit(perm, dist_m)
        dist += dist_m[perm[-1]][perm[0]]

        if flag == 0:
            min_dist = dist
            camino_min = list(perm)
            flag = 1
            camino_min.append(perm[0])

        elif dist <= min_dist:
            min_dist = dist
            camino_min = list(perm)
            camino_min.append(perm[0])

    return camino_min
