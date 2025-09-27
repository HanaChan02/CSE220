! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
#TASK-2
def task2A( arr ):
  i=0
  while i<len(arr):
    print(arr[i], end=" ")
    i+=1
  print()

def task2B_recursive( arr ):
  if len(arr)==0:
    return
  print(arr[0], end=" ")
  if len(arr)>0:
    task2B_recursive(arr[1:])


def task2C( arr ):
  i=0
  summation=0
  while i<len(arr):
    summation+=arr[i]
    i+=1
  return summation

def task2D_recursive( arr ):
    if len(arr)==0:
      return 0
    return arr[0]+task2D_recursive(arr[1:])


def task2E( arr ):
    i=0
    minus=0
    sum=0
    mult=1
    while i<len(arr):
      if arr[i]%2==0:
        sum+=arr[i]
      else:
        mult*=arr[i]
      i+=1
    minus=mult-sum
    return minus

def task2F_recursive( arr, i=0, oddProduct=1, sumEven=0 ):
  if i==len(arr):
    return oddProduct-sumEven
  if arr[i]%2==0:
    return task2F_recursive(arr,i+1,oddProduct,sumEven+arr[i])
  else:
    return task2F_recursive(arr,i+1,oddProduct*arr[i],sumEven)


# Driver Code for Task-2
# task2A
print("Task2A: ")
arr = np.random.randint(1, 20, size=6, dtype=int)
print( "Expected Output: "+str(arr)[1:-1] )
print( "Your Output    : ",end="" )
task2A( arr )
print()

# task2B_recursive
print("\nTask2B_recursive: ")
print( "Expected Output: ",str(arr)[1:-1] )
print( "Your Output    : ",end="" )
task2B_recursive( arr )
print()

# task2C
print("\nTask2C: ")
arr = np.random.randint(1, 10, size=6, dtype=int)
print("The Array: ",arr)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task2C(arr) )

# task2D_recursive
print("\nTask2D_recursive: ")
print("The Array: ",arr)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task2D_recursive( arr ) )

# task2E
print("\nTask2E: ")
arr = np.random.randint(1, 8, size=5, dtype=int)
print("The Array: ",arr)
if np.sum([e%2 for e in arr])==0:
    print( "Expected Output: ",-np.sum([e for e in arr if e%2==0]) )
else:
    print( "Expected Output: ",int(np.prod([e for e in arr if e%2!=0])-np.sum([e for e in arr if e%2==0])) )
print( "Your Output    : ",task2E( arr ) )


# task2F
print("\nTask2F_recursive: ")
print("The Array: ",arr)
if np.sum([e%2 for e in arr])==0:
    print( "Expected Output: ",-np.sum([e for e in arr if e%2==0]) )
else:
    print( "Expected Output: ",int(np.prod([e for e in arr if e%2!=0])-np.sum([e for e in arr if e%2==0])) )
print( "Your Output    : ",task2F_recursive( arr ))
