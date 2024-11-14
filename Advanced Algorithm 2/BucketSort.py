def bucket_sort(arr):
    n = len(arr)
    # Determine the number of buckets (here, we choose 10)
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        index = int(num * num_buckets)
        buckets[index].append(num)

    # Sort each bucket individually (using insertion sort in this case)
    for bucket in buckets:
        bucket.sort()

    # Concatenate sorted buckets to get the sorted array
    sorted_arr = [num for bucket in buckets for num in bucket]

    # Update the original array with the sorted elements
    for i in range(n):
        arr[i] = sorted_arr[i]

# Main code
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucket_sort(arr)
print(arr)  # Output: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
