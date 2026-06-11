# Advanced Algorithms

Python implementations of advanced algorithm design techniques — covering sorting, graph traversal, dynamic programming, greedy algorithms, and divide-and-conquer strategies.

## Algorithms Implemented

### Sorting
| Algorithm | File | Time (avg) | Time (worst) |
|---|---|---|---|
| Merge Sort | `mergeSort.py` | O(n log n) | O(n log n) |
| Quick Sort | `quicksort.py` | O(n log n) | O(n²) |
| Heap Sort | `HeapSort.py` | O(n log n) | O(n log n) |
| Radix Sort | `radixSort.py` | O(nk) | O(nk) |
| Count Sort | `countSort.py` | O(n + k) | O(n + k) |
| Bucket Sort | `BucketSort.py` | O(n + k) | O(n²) |
| Complex Radix Sort | `complexRadixSort.py` | O(nk) | O(nk) |
| Character Radix Sort | `character-radix-sort.py` | O(nk) | O(nk) |

### Graph Algorithms
| Algorithm | File | Complexity |
|---|---|---|
| BFS (Breadth-First Search) | `bfs1.py`, `bfs2.py` | O(V + E) |
| DFS (Depth-First Search) | `dfs.py` | O(V + E) |
| Dijkstra's (adjacency list) | `dijkstras.py` | O(E log V) |
| Dijkstra's (min-heap) | `heap_dijkstra.py` | O(E log V) |

### Dynamic Programming
| Problem | File |
|---|---|
| 0/1 Knapsack | `knapsack.py` |
| Minimum coin change | `min_coins.py` |
| Longest subsequence | `longest_subsequence.py` |
| Maximum profit | `profit.py` |
| Activity selection | `max_activity.py`, `max_activity2.py` |

### Divide & Conquer
| Problem | File |
|---|---|
| Hamming Weight (brute force) | `HammingWeight.py` |
| Hamming Weight (D&C) | `HammingWeightDivideAndConquer.py` |
| Matrix multiplication | `Matrix Multiplication.py` |
| Maximum 2D submatrix | `Max 2D Matrix.py` |
| Towers of Hanoi | `Towers of Hanoi.py` |

### Utility Algorithms
| Problem | File |
|---|---|
| Top-k frequency elements | `top_k_frequency.py` |
| Missing number detection | `mergeMissingNumber.py`, `missing number.py` |
| Duplicate detection via sort | `duplicatesCountSort.py` |
| Min platforms (interval scheduling) | `min_platform.py` |

## Technologies

- **Python 3**
- Standard library only (no external dependencies)

## Usage

```bash
# Each file is standalone
python mergeSort.py
python dijkstras.py
python knapsack.py
```