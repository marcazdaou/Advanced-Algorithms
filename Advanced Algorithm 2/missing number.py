def find_missing_number(arr):
    n = len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    for i in range(1,n):
        if arr[i]-arr[i-1] != 1:
            return arr[i-1]+1

arr = [ 1,2,3,5,6,7,8]
missing_number = find_missing_number(arr)
print("Missing number:",missing_number) # output 4