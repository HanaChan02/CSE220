! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
def mergeSortedArray(arr1, arr2):
  i,j,k=0,0,0
  new_arr=np.zeros(len(arr1)+len(arr2),dtype=int)
  while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
      new_arr[k]=arr1[i]
      i+=1
    else:
      new_arr[k]=arr2[j]
      j+=1
    k+=1
  while i<len(arr1) or j<len(arr2):
    if i<len(arr1):
      new_arr[k]=arr1[i]
      i+=1
    else:
      new_arr[k]=arr2[j]
      j+=1
    k+=1
  return new_arr


### DRIVER CODE ###
a1 = np.array([4, 8, 10])
print(f'Sorted Array 1: {a1}')
a2 = np.array([3, 6, 9])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [3, 4, 6, 8, 9, 10]
unittest.output_test(returned_value, np.array([3, 4, 6, 8, 9, 10]))

print('\n==================================\n')

a3 = np.array([2, 5, 12, 14])
print(f'Sorted Array 3: {a3}')
a4 = np.array([1, 7, 13])
print(f'Sorted Array 4: {a4}')
returned_value = mergeSortedArray(a3, a4)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 5, 7, 12, 13, 14]
unittest.output_test(returned_value, np.array([1, 2, 5, 7, 12, 13, 14]))
