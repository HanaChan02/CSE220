def findQueenAge(matrix):
    if not matrix or not matrix[0]:
        return None

    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Find the row with the smallest sum
    min_row_sum = sum(matrix[0])  # Initialize with the sum of the first row
    min_row_index = 0
    for i in range(1, rows):
        row_sum = 0
        for j in range(cols):
            row_sum += matrix[i][j]
        if row_sum < min_row_sum:
            min_row_sum = row_sum
            min_row_index = i

    # Step 2: Find the column with the smallest sum
    # Initialize min_col_sum with the sum of the first column
    min_col_sum = 0
    for i in range(rows):
        min_col_sum += matrix[i][0]
    min_col_index = 0

    # Iterate through the remaining columns
    for j in range(1, cols):
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        if col_sum < min_col_sum:
            min_col_sum = col_sum
            min_col_index = j

    # Step 3: Find the Queen's age at the intersection of min_row_index and min_col_index
    queen_age = matrix[min_row_index][min_col_index]
    return queen_age

# Driver code
def main():
    # Sample Input
    matrix = [
        [50, 45, 90],
        [70, 80, 60],
        [40, 30, 25]
    ]

    print("Queen's Age:", findQueenAge(matrix))

# Run the driver code
if __name__ == "__main__":
    main()
