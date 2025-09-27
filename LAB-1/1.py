! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

def mergeSortedArray(arr1, arr2):
  a,b,c=0,0,0
  new_array=np.zeros((len(arr1)+len(arr2)), dtype=int)
  while a < len(arr1) and b < len(arr2):
    if arr1[a]<arr2[b]:
      new_array[c]=arr1[a]
      a+=1
    else:
      new_array[c]=arr2[b]
      b+=1
    c+=1
  while a<len(arr1):
      new_array[c]=arr1[a]
      a+=1
      c+=1
  while b<len(arr2):
      new_array[c]=arr2[b]
      b+=1
      c+=1
  return new_array

a1 = np.array([1, 2, 3])
print(f'Sorted Array 1: {a1}')
a2 = np.array([2, 5, 6])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 2, 3, 5, 6]
unittest.output_test(returned_value, np.array([1, 2, 2, 3, 5, 6]))

print('\n==================================\n')

a3 = np.array([1, 3, 5, 11])
print(f'Sorted Array 3: {a3}')
a4 = np.array([2, 7, 8])
print(f'Sorted Array 4: {a4}')
returned_value = mergeSortedArray(a3, a4)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 3, 5, 7, 8, 11]
unittest.output_test(returned_value, np.array([1, 2, 3, 5, 7, 8, 11]))
