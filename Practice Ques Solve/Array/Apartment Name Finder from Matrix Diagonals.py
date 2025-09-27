import numpy as np
## SET A
def find_apartment_names(matrix):
    n = matrix.shape[0]  # Get the size of the square matrix
    mismatched = np.array([], dtype=str)  # Initialize an empty numpy array to store mismatched elements

    for i in range(n // 2):
        j = n - 1 - i
        if matrix[i, i] != matrix[j, j]:
            # Add matrix[i, i] if not already in the mismatched array
            if matrix[i, i] not in mismatched:
                mismatched = np.append(mismatched, matrix[i, i])
            # Add matrix[j, j] if not already in the mismatched array
            if matrix[j, j] not in mismatched:
                mismatched = np.append(mismatched, matrix[j, j])

    # If the matrix has an odd size, check the middle element
    if n % 2 == 1:
        mid = n // 2
        if matrix[mid, mid] not in mismatched:
            mismatched = np.append(mismatched, matrix[mid, mid])

    return mismatched

# Driver code
def main():
    # Sample Input 1
    matrix1 = np.array([
        ['A', 'D', 'M', 'Q'],
        ['E', 'S', 'Y', 'K'],
        ['J', 'F', 'O', 'L'],
        ['P', 'X', 'J', 'A']
    ])

    print("Sample Input 1:")
    print(matrix1)

    apartment_names1 = find_apartment_names(matrix1)
    print("\nPossible Apartment Names:", ' '.join(apartment_names1))

    print("\n-----------------------------\n")

    # Sample Input 2
    matrix2 = np.array([
        ['A', 'D', 'M', 'Q', 'F'],
        ['E', 'S', 'Y', 'K', 'W'],
        ['J', 'F', 'O', 'L', 'T'],
        ['P', 'X', 'J', 'S', 'Y'],
        ['V', 'R', 'K', 'G', 'P']
    ])

    print("Sample Input 2:")
    print(matrix2)

    apartment_names2 = find_apartment_names(matrix2)
    print("\nPossible Apartment Names:", ' '.join(apartment_names2))

# Run the driver code
if __name__ == "__main__":
    main()
