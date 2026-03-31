# Advanced Algorithms & Optimization 

## Overview
This repository contains a collection of advanced algorithms and data structures implemented in **Python**, focusing on computational efficiency, complexity analysis, and optimization. It covers core areas such as Graph Theory, Robust Sorting, and Dynamic Programming.

## Key Implementations

### 1. Robust Sorting & Selection
* **Median of Medians Algorithm:** Implemented a robust version of QuickSort and QuickSelect (`qsort_5`) that avoids the $O(n^2)$ worst-case scenario by using the Median of Medians selection pivot, guaranteeing $O(n \log n)$ complexity.
* **Dynamic Programming:** Solvers for the Knapsack Problem (0/1 and Fractional) and Optimal Coin Change, focusing on space-time complexity trade-offs.

### 2. Graph Theory & Optimization
* **Kruskal’s Algorithm (MST):** Implementation of Minimum Spanning Trees using an optimized **Disjoint-Set (Union-Find)** with path compression for near-constant time operations.
* **TSP (Traveling Salesperson Problem):** Comparative analysis between Greedy heuristics and Brute-force exhaustive search for path optimization.

### 3. Priority Queues & Data Structures
* **Manual Min-Heap Implementation:** Core logic for heapification (`O(n)` build-heap) and heap-sort. Essential for priority-based task scheduling in high-performance engines.

## Complexity Analysis
Each implementation includes a study of its Big O complexity, verified through empirical testing and performance benchmarking (see implementation comments for details).

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** NumPy (Vectorized operations), Itertools.
