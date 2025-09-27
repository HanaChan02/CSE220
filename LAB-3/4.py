! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))
#Task 04: Matrix Compression

def compress_matrix(mat):
  rows, cols = mat.shape
  compressed_matrix = np.zeros((rows // 2, cols // 2), dtype=int)

  for i in range(0, rows, 2):
    for j in range(0, cols, 2):
      block_sum = (mat[i][j] + mat[i][j+1] +mat[i+1][j] + mat[i+1][j+1])
      compressed_matrix[i//2][j//2] = block_sum

  return compressed_matrix


#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
print("...............")
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print

#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------
