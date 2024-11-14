def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n  # Initialize LIS array to 1
    max_length = 1  # Initialize maximum length to 1

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                if lis[i] > max_length:
                    max_length = lis[i]

    return max_length

# Test the function
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
length = longest_increasing_subsequence(arr)
print("Length of the longest increasing subsequence:", length)