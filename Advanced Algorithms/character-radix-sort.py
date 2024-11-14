def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 26  # Assuming only lowercase letters

    for i in range(0, n):
        index = ord(arr[i][exp]) - ord('a') if len(arr[i]) > exp else 0
        count[index] += 1

    for i in range(1, 26):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = ord(arr[i][exp]) - ord('a') if len(arr[i]) > exp else 0
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max_length = max(len(s) for s in arr)
    for exp in range(max_length - 1, -1, -1):
        countingSort(arr, exp)


strings = ['d', 'a', 'c', 'b', 'f', 'e']
radixSort(strings)
print("Sorted strings:", strings)