def rotate_180(matrix):
    # Reverse the order of rows
    matrix.reverse()
    return matrix

# Driver code
def main():
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
