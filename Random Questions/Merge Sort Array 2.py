! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
def mergeSortedArray(arr1,arr2):
  i,j,k,idx=0,0,0,0
  new_arr=np.empty(len(arr1), dtype=int)
  if len(arr1)==len(arr2):
    while i < len(arr1):
      new_arr[i]=int(str(arr1[i])+str(arr2[i]))
      i+=1
  for j in range(len(new_arr)):
    key = new_arr[j]
    k = j
    while k > 0 and new_arr[k - 1] > key:
      new_arr[k] = new_arr[k - 1]  # Shift element
      k -= 1
    new_arr[k] = key  # Insert key at correct position

  return new_arr


### DRIVER CODE ###
print('\n==================================\n')

a1 = np.array([1,2,5,4,3])
print(f'Sorted Array 1: {a1}')
a2 = np.array([9,8,5,6,7])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [3, 4, 6, 8, 9, 10]
unittest.output_test(returned_value, np.array([19,28,37,46,55]))

print('\n==================================\n')
