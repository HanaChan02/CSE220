## QUESTION 1
def sum_diff(matrix):
  row,col=matrix.shape
  total_sum=0
  col_sums = np.zeros(col, dtype=int)
  arr1=np.zeros(col-1,dtype=int)
  for i in range(col):
    col_sum=0
    for j in range(row):
      col_sum+=matrix[j][i]
    col_sums[i]=col_sum

  for i in range(col-1):
    arr1[i]=col_sums[i+1]-col_sums[i]
  return arr1

# Driver code
def main():
    # Sample Input
    matrix = np.array([
        [1, 6, 5],
        [9, 8, 7],
        [4, 3, 2],
        [5, 6, 1]
    ])

    print("Input Matrix:")
    print(matrix)

    # Compute the decrypted linear array
    decrypted_array = sum_diff(matrix)

    print("\nDecrypted Linear Array:")
    print(decrypted_array)

# Run the driver code
if __name__ == "__main__":
    main()
