def initializeMatrix(n):
    return [[0] * n for _ in range(n)]

def setToZero(matrix, n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 0

def multiply(A, B, n):
    C = initializeMatrix(n)
    setToZero(C, n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add(M1, M2, n):
    temp = initializeMatrix(n)
    for i in range(n):
        for j in range(n):
            if M1[i][j] is None:
                M1[i][j] = 0
            if M2[i][j] is None:
                M2[i][j] = 0
            temp[i][j] = M1[i][j] + M2[i][j]
    return temp

def subtract(M1, M2, n):
    temp = initializeMatrix(n)
    for i in range(n):
        for j in range(n):
            if M1[i][j] is None:
                M1[i][j] = 0
            if M2[i][j] is None:
                M2[i][j] = 0
            temp[i][j] = M1[i][j] - M2[i][j]
    return temp

def pad_matrix(matrix):
    n = len(matrix)
    next_power_of_two = 2 ** (n - 1).bit_length()
    padded_matrix = [[0] * next_power_of_two for _ in range(next_power_of_two)]
    for i in range(n):
        for j in range(n):
            padded_matrix[i][j] = matrix[i][j]
    return padded_matrix

def remove_padding(matrix, original_size):
    return [row[:original_size] for row in matrix[:original_size]]

def strassenMultiply(A, B, n):
    original_size = n
    # Pad matrices to the nearest power of 2
    A = pad_matrix(A)
    B = pad_matrix(B)
    n = len(A)

    if n == 1:
        C = initializeMatrix(1)
        C[0][0] = A[0][0] * B[0][0]
        return C

    C = initializeMatrix(n)

    k = n // 2

    A11 = [row[:k] for row in A[:k]]
    A12 = [row[k:] for row in A[:k]]
    A21 = [row[:k] for row in A[k:]]
    A22 = [row[k:] for row in A[k:]]

    B11 = [row[:k] for row in B[:k]]
    B12 = [row[k:] for row in B[:k]]
    B21 = [row[:k] for row in B[k:]]
    B22 = [row[k:] for row in B[k:]]

    P1 = strassenMultiply(A11, subtract(B12, B22, k), k)
    P2 = strassenMultiply(add(A11, A12, k), B22, k)
    P3 = strassenMultiply(add(A21, A22, k), B11, k)
    P4 = strassenMultiply(A22, subtract(B21, B11, k), k)
    P5 = strassenMultiply(add(A11, A22, k), add(B11, B22, k), k)
    P6 = strassenMultiply(subtract(A12, A22, k), add(B21, B22, k), k)
    P7 = strassenMultiply(subtract(A11, A21, k), add(B11, B12, k), k)

    C11 = subtract(add(add(P5, P4, k), P6, k), P2, k)
    C12 = add(P1, P2, k)
    C21 = add(P3, P4, k)
    C22 = subtract(subtract(add(P5, P1, k), P3, k), P7, k)

    for i in range(k):
        for j in range(k):
            C[i][j] = C11[i][j]
            C[i][j + k] = C12[i][j]
            C[k + i][j] = C21[i][j]
            C[k + i][k + j] = C22[i][j]

    # Remove padding before returning the result
    return remove_padding(C, original_size)

# Interactive Input
print("Input:")
n = int(input())
if n <= 0 or n > 100:
    print("Size of matrices must be between 1 and 100.")
    exit()


A = []
for i in range(n):
    row_input = input().split(',')
    if len(row_input) != n:
        print("invalid number of elements.")
        exit()
    A.append([int(x) if x != '' else None for x in row_input])

n = int(input())
if n <= 0 or n > 100:
    print("Size of matrices must be between 1 and 100.")
    exit()

B = []
for i in range(n):
    row_input = input().split(',')
    if len(row_input) != n:
        print("invalid number of elements.")
        exit()
    B.append([int(x) if x != '' else None for x in row_input])

# Perform Strassen multiplication
result = strassenMultiply(A, B, n)

# Output the result
print('Output:')
for row in result:
    print(','.join(map(lambda x: str(x) if x is not None else '', row)))