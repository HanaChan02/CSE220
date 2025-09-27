import numpy as np
def compress_matrix(mat):
  total_sum=0
  row,col=mat.shape
  arr1=np.zeros((row//2,col//2),dtype=int)
  for i in range(0,row,2):
    for j in range(0,col,2):
        arr1[i//2][j//2]=mat[i][j]+mat[i+1][j]+mat[i][j+1]+mat[i+1][j+1]
  return arr1


# Example usage:
input_matrix = np.array([
    [1, 2, 3, 4, 1, 9],
    [5, 6, 7, 8, 5, 6],
    [1, 3, 5, 2, 7, 8],
    [-2, 0, 6, -3, -8, 1],
    [-5, 2, 10, -5, 9, 12],
    [6, 8, 2, -2, 1, 8]
])

compressed_matrix = compress_matrix(input_matrix)
print(compressed_matrix)
