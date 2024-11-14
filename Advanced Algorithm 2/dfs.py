def radix_sort(arr):
    max_len = max(len(x) for x in arr)
    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(26)]
        for word in arr:
            if i < len(word):
                buckets[ord(word[i]) - ord('A')].append(word)
        arr = [word for bucket in buckets for word in bucket]
    return arr


def exist(board, word):
    if not board or not board[0]:
        return False

    # Sort the characters of the word using Radix Sort
    sorted_word = radix_sort([word])[0]

    rows, cols = len(board), len(board[0])

    def dfs(row, col, idx):
        if idx == len(sorted_word):
            return True

        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != sorted_word[idx]:
            return False

        # Mark the cell as visited
        temp = board[row][col]
        board[row][col] = ''

        # Explore neighbors in all four directions
        found = dfs(row + 1, col, idx + 1) or dfs(row - 1, col, idx + 1) or dfs(row, col + 1, idx + 1) or dfs(row,
                                                                                                              col - 1,
                                                                                                              idx + 1)

        # Restore the cell
        board[row][col] = temp

        return found

    # Iterate over each cell in the board
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


# Example usage
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"
print("Output:", exist(board, word))  # Output: True