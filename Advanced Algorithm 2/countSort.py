def counting_sort(arr):
    # Count the frequency of each character
    count = [0] * 26  # Initialize count array for lowercase English letters

    for char in arr:
        count[ord(char) - ord('a')] += 1

    # Construct the sorted array
    sorted_arr = []
    for i in range(26):
        sorted_arr.extend([chr(ord('a') + i)] * count[i])

    return sorted_arr

# Test the function
arr = ['b', 'd', 'a', 'c', 'f', 'e']
sorted_arr = counting_sort(arr)
print("Output:", sorted_arr)  # Output: ['a', 'b', 'c', 'd', 'e', 'f']