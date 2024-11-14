def tropical_sort(arr):
    n = len(arr)

    # Perform tropical sorting
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


# Example usage
arr = [4, 7, 2, 5]
sorted_arr = tropical_sort(arr)
print("Output:", sorted_arr)  # Output: [2, 4, 5, 7]