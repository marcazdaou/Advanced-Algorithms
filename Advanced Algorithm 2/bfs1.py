def num_squares(n):
    if n <= 0:
        return 0

    squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
    queue = [(n, 0)]
    visited = set()

    while queue:
        num, step = queue.pop(0)
        for square in squares:
            if num - square == 0:
                return step + 1
            elif num - square > 0 and (num - square) not in visited:
                visited.add(num - square)
                queue.append((num - square, step + 1))

    return -1


# Test the function
n = 12
print("Least number of perfect square numbers that sum to", n, "is:", num_squares(n))