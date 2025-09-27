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
#Task 02: Decryption Process

def decrypt_matrix(matrix):
  row,col=matrix.shape
  sum_array=np.zeros(col,dtype=int)
  decrypted_matrix=np.zeros(col-1,dtype=int)

  for j in range(col):
    sum=0

    for i in range(row):
      sum+=matrix[i][j]
    sum_array[j]=sum

  for x in range(col-1):
    decrypted_matrix[x]=sum_array[x+1]-sum_array[x]

  return decrypted_matrix

#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
#This should print [-13, 1]
