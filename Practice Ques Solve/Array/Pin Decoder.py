def decodeMessage(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return []

    M = len(matrix)
    decoded_pin = []

    # Iterate through the matrix to compute absolute differences
    for i in range(M):
        diagonal_element = matrix[i][i]
        counter_diagonal_element = matrix[i][M - 1 - i]
        absolute_difference = abs(diagonal_element - counter_diagonal_element)
        decoded_pin.append(absolute_difference)

    return decoded_pin

# Driver code
def main():
    # Sample Input
    matrix = [
        [1, 2, 3, -4],
        [5, -6, 7, 8],
        [9, -10, 11, 12],
        [13, 14, 15, -16]
    ]

    print("Decoded Pin:", decodeMessage(matrix))

# Run the driver code
if __name__ == "__main__":
    main()
