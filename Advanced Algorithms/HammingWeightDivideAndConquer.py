
import time

def hamming_weight_divide_conquer(binary):
    # Base case: if the binary number has only one bit
    if len(binary) == 1:
        return int(binary)

    # Recursive case: divide the binary number into halves
    mid = len(binary) // 2
    left_half = binary[:mid]
    right_half = binary[mid:]

    # Count '1' bits in left and right halves recursively
    left_count = hamming_weight_divide_conquer(left_half)
    right_count = hamming_weight_divide_conquer(right_half)

    # Combine counts from left and right halves
    return left_count + right_count

# Interactive input
binary_number = input("Enter a binary number: ")

start_time = time.time()
hamming_weight = hamming_weight_divide_conquer(binary_number)
end_time = time.time()

print("Hamming weight:", hamming_weight)
print("Execution time:", end_time - start_time, "seconds")

"""
import time
def hamming_weight(n):  # for the sequential algorithm
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
"""