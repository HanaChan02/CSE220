## QUESTION 1
def rotate_anticlockwise(matrix):
    n = len(matrix)
    for x in range(n // 2):
        first = x
        last = n - 1 - x
        for i in range(first, last):
            offset = i - first
            # Save top
            top = matrix[first][i]
            # Move right to top
            matrix[first][i] = matrix[i][last]
            # Move bottom to right
            matrix[i][last] = matrix[last][last - offset]
            # Move left to bottom
            matrix[last][last - offset] = matrix[last - offset][first]
            # Move top to left
            matrix[last - offset][first] = top
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

    # Rotate the matrix anticlockwise
    rotated_matrix1 = rotate_anticlockwise(matrix1)

    print("\nRotated Matrix 1 (Anticlockwise):")
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

    # Rotate the matrix anticlockwise
    rotated_matrix2 = rotate_anticlockwise(matrix2)

    print("\nRotated Matrix 2 (Anticlockwise):")
    for row in rotated_matrix2:
        print(row)

# Run the driver code
if __name__ == "__main__":
    main()
