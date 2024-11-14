def counting_sort_with_duplicates(arr):
    # Find the range of the input elements
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Count the frequency of each element
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Create an auxiliary array to store the positions
    positions = [0] * len(arr)
    for i in range(1, range_size):
        count[i] += count[i - 1]

    # Construct the sorted array while preserving the order of duplicates
    sorted_arr = [0] * len(arr)
    for num in arr[::-1]:
        sorted_arr[count[num - min_val] - 1] = num
        positions[count[num - min_val] - 1] = count[num - min_val] - 1
        count[num - min_val] -= 1

    # Adjust the sorted array to preserve the order of duplicates
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] == sorted_arr[i + 1]:
            sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
            positions[i], positions[i + 1] = positions[i + 1], positions[i]
        else:
            break

    # Rearrange sorted array to preserve the original order of duplicates
    for i in range(len(sorted_arr)):
        if positions[i] != i:
            sorted_arr[positions[i]], sorted_arr[i] = sorted_arr[i], sorted_arr[positions[i]]
            positions[positions[i]], positions[i] = positions[i], positions[positions[i]]

    return sorted_arr

# Test the function
arr = [3, 5, 1, 9, 3, 8, 1, 2]
sorted_arr = counting_sort_with_duplicates(arr)
print("Output:", sorted_arr)  # Output: [1, 1, 2, 3, 3, 5, 8, 9]