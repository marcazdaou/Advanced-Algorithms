import time


def hamming_weight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


binary_representation = input("Enter the binary representation of an unsigned integer: ")

start_time = time.time()  # Start time measurement
decimal_value = int(binary_representation, 2)
print("Hamming weight:", hamming_weight(decimal_value))
end_time = time.time()  # End time measurement

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
