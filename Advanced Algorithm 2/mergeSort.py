def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def kth_smallest_after_merge(arr1, arr2, k):
    merged = merge_sort(arr1 + arr2)
    return merged[k - 1]


# Test the function
arr1 = [6, 7, 2, 4]
arr2 = [3, 1, 5]
k = 4
result = kth_smallest_after_merge(arr1, arr2, k)
print(result)