def find_max_index(arr):
    if not arr:
        return -1  # If the list is empty, return -1 as there is no maximum element

    max_element = arr[0]
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i

    return max_index
arr = [1, 3, 5, 4, 2,]
max_index = find_max_index(arr)
print("Output:", max_index)