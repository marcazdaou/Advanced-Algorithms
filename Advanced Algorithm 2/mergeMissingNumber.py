def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls to sort left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half and right_half if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def find_missing_number(arr):
    merge_sort(arr)
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] > 1:
            return arr[i] + 1
    return None

# Test the function
arr = [1, 5, 3, 6, 8, 7, 2]
output = find_missing_number(arr)
print("Output:", output)  # Output: 4