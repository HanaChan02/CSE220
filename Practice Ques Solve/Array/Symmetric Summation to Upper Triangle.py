def toSymUpperTr(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Check if the matrix is square
    if rows != cols:
        return matrix

    # Transform the matrix
    for i in range(rows):
        for j in range(i):
            # Add the element below the diagonal to its symmetric counterpart above the diagonal
            matrix[j][i] += matrix[i][j]
            # Set the element below the diagonal to zero
            matrix[i][j] = 0

    return matrix

# Helper function to print the matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Driver code
def main():
    # Sample Input
    matrix = [
        [8, 2, 1],
        [3, 5, 4],
        [6, 9, 7]
    ]

    print("Original Matrix:")
    print_matrix(matrix)

    # Transform the matrix
    transformed_matrix = toSymUpperTr(matrix)

    print("\nTransformed Matrix:")
    print_matrix(transformed_matrix)

# Run the driver code
if __name__ == "__main__":
    main()
