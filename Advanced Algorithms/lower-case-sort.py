def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)

    # Initialize a count array with zeros
    count = [0] * (ord(max_val) - ord('a') + 1)

    # Count occurrences of each character
    for char in arr:
        count[ord(char) - ord('a')] += 1

    # Modify count array to contain actual position of characters in sorted array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Reconstruct the sorted array
    sorted_arr = [''] * len(arr)
    for char in reversed(arr):
        sorted_arr[count[ord(char) - ord('a')] - 1] = char
        count[ord(char) - ord('a')] -= 1

    return sorted_arr

# Test the function
arr = ['b', 'd', 'a', 'c', 'f', 'e']
sorted_arr = counting_sort(arr)
print("Output:", sorted_arr)  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
