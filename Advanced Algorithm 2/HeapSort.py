def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)

    # Build a min-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap in sorted order
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def find_kth_smallest(arr, k):
    heap_sort(arr)  # Sort the array using Heap Sort
    return arr[k - 1]  # Return the kth smallest element

arr = [5, 3, 8, 2, 1, 4]
k = 3
result = find_kth_smallest(arr, k)
print(result)  # Output: 4