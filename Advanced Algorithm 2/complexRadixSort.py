def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Counting occurrences of digits
    for i in range(n):
        index = (arr[i][0] ** 2 + arr[i][1] ** 2) // exp
        count[index % 10] += 1

    # Update count array to store actual position
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i][0] ** 2 + arr[i][1] ** 2) // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort_complex(arr):
    # Find the maximum magnitude
    max_magnitude = max([(x[0] ** 2 + x[1] ** 2) ** 0.5 for x in arr])

    # Perform radix sort
    exp = 1
    while max_magnitude // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr

# Test the function
arr = [(3, 4), (0, 1), (3, 3), (4, 0)]
sorted_arr = radix_sort_complex(arr)
print("Output:", sorted_arr)  # Output: [(0, 1), (3, 4), (4, 0), (3, 3)]