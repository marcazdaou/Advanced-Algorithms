def find_min_in_matrix(matrix):

    # Divide and conquer approach
    def divide_conquer(matrix):
        n = len(matrix)
        m = len(matrix[0])

        if n == 1 and m == 1:
            return matrix[0][0] if matrix[0][0] is not None else float('inf')

        mid_row = n // 2
        mid_col = m // 2

        # Divide the matrix into four submatrices
        submatrices = [
            [row[:mid_col] for row in matrix[:mid_row]],  # Top left
            [row[mid_col:] for row in matrix[:mid_row]],  # Top right
            [row[:mid_col] for row in matrix[mid_row:]],  # Bottom left
            [row[mid_col:] for row in matrix[mid_row:]]  # Bottom right
        ]

        # Recursively find minimum in each submatrix
        min_values = [divide_conquer(submatrix) for submatrix in submatrices if any(submatrix)]

        # Handle case where all values in a submatrix are None
        min_values = [value for value in min_values if value is not None]

        # Combine the minimum values
        return min(min_values)

    min_value = divide_conquer(matrix)
    if min_value == float('inf'):
        return "Empty"
    return min_value

def main():
    # Input
    dimensions_input = input("A1:").strip('()').split(',')
    if dimensions_input == ['', '']:
        print("Matrix is empty")
        return
    n, m = map(int, dimensions_input)  # Read dimensions of the matrix
    if n < 0 or m < 0:
        print("Must Be Between 1 and 100")
        return
    if n == 0 or m == 0:
        print("Matrix is empty")
        return
    if n > 100 or m > 100:
        print("Must Be Between 1 and 100")
        return
    matrix = []
    for i in range(n):  # iterate n times only
        row_input = input(f"A{i+2}:").strip('()').split(',')  # Read each row
        if len(row_input) != m:  # Check if the number of elements in the row matches the number of columns
            print("Invalid input: Doesn't Match The Dimensions Provided.")
            return
        row = []
        for elem in row_input:
            if elem:  # If the element is not empty
                elem_value = int(elem)
                if -1000 <= elem_value <= 1000:  # Check if the element falls within the specified range
                    row.append(elem_value)
                else:
                    print("Invalid input: Element value out of range (-1000 to 1000).")
                    return
            else:  # If the element is empty, treat it as if the value is missing
                row.append(None)
        matrix.append(row)

    # Output
    print(find_min_in_matrix(matrix))


if __name__ == "__main__":
    main()