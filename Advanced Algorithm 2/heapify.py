def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l][1] > arr[largest][1]:
        largest = l

    if r < n and arr[r][1] > arr[largest][1]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap in sorted order
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def topKFrequent(nums, k):
    # Count the frequency of each element
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Convert frequency map to a list of tuples (num, frequency)
    frequency_list = list(frequency_map.items())

    # Sort the list based on frequency using Heap Sort
    heap_sort(frequency_list)

    # Extract the top k elements from the sorted list
    top_k = [frequency_list[i][0] for i in range(len(frequency_list) - 1, len(frequency_list) - k - 1, -1)]

    return top_k


# Test the function
arr = [1, 1, 1, 2, 2, 3]
k = 2
output = topKFrequent(arr, k)
print("Output:", output)  # Output: [1, 2]