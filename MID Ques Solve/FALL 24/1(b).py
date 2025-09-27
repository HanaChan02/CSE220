import numpy as np

def zig_zag(matrix1):
  n=matrix.shape[0]
  result=""
  for col in range(n):
    i,j=0,col
    temp=""
    while i<n and j>=0:
      temp+=matrix[i][j]
      temp+=" "
      i+=1
      j-=1
    result+=temp[::-1]
  for row in range(n):
    i,j=row,0
    temp=""
    while i>=0 and j<n:
      temp+=matrix[i][j]
      temp+=" "
      i-=1
      j+=1
    result+=temp[::-1]
  return result

matrix = np.array([
    ['D', 'B', 'G', 'S'],
    ['A', 'G', 'T', 'S'],
    ['W', 'U', 'R', 'N'],
    ['O', 'H', 'R', 'O']
])

output = zig_zag(matrix)
print(output)
