import numpy as np
def print_arr(arr):
  arr1=np.zeros(len(arr) ,dtype=int)

  for i in range(len(arr)):
    arr1[i]=arr[len(arr)-1-i]
  return arr1


arr=np.array([1,2,3,4,5])
print_arr(arr)
