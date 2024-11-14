def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def max_product(arr):
    quick_sort(arr, 0, len(arr) - 1)
    n = len(arr)
    return max(arr[n - 1] * arr[n - 2], arr[0] * arr[1])

arr = [5, 20, 2, 6, -10, -7]
result = max_product(arr)
print(result)  # Output: 120
