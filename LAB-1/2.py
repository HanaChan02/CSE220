! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
def mostWater(arr):
  l,r,maxA=0,len(arr)-1,0
  while l<r:
    if arr[l]<arr[r]:
      height=arr[l]
    else:
      height=arr[r]
    width=abs(r-l)
    area=height*width
    if maxA<area:
      maxA=area
    if arr[l]<arr[r]:
      height=arr[l]
      l+=1
    else:
      height=arr[r]
      r-=1

  return maxA

height = np.array([1,8,6,2,5,4,8,3,7])
print(f'Given Array: {height}')

print(f'\nExpected Output: 49')
print(f'Your Output: ',end='')
mostWater(height)
