def rotate_clockwise(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save top
            top = matrix[first][i]
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Move top to right
            matrix[i][last] = top
    return matrix

# Driver code
def main():
    # Input matrix 1: 4x4
    matrix1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print("Original Matrix 1:")
    for row in matrix1:
        print(row)

    # Rotate the matrix clockwise
    rotated_matrix1 = rotate_clockwise(matrix1)

    print("\nRotated Matrix 1 (Clockwise):")
    for row in rotated_matrix1:
        print(row)

    print("------------------------------------------------------")

    # Input matrix 2: 3x3
    matrix2 = [
        [1, 2, 3],
        [5, 6, 7],
        [9, 10, 11]
    ]

    print("Original Matrix 2:")
    for row in matrix2:
        print(row)

    # Rotate the matrix clockwise
    rotated_matrix2 = rotate_clockwise(matrix2)

    print("\nRotated Matrix 2 (Clockwise):")
    for row in rotated_matrix2:
        print(row)

# Run the driver code
if __name__ == "__main__":
    main()
