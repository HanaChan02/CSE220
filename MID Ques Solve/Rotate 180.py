def rotate_180(matrix):
    n = len(matrix)
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    # Reverse the order of rows
    matrix.reverse()
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

    # Rotate the matrix 180 degrees
    rotated_matrix1 = rotate_180(matrix1)

    print("\nRotated Matrix 1 (180 Degrees):")
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

    # Rotate the matrix 180 degrees
    rotated_matrix2 = rotate_180(matrix2)

    print("\nRotated Matrix 2 (180 Degrees):")
    for row in rotated_matrix2:
        print(row)

# Run the driver code
if __name__ == "__main__":
    main()
