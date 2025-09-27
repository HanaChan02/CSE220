! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
class Node:
  def __init__(self, value=None, next = None):
    self.elem = value
    self.next = next
def showLL(head):
  if head!=None:
    n = head
    while n!=None:
        print(n.elem, end=' -> ')
        n = n.next
    print()

def arr2LL(arr):
  head = Node(arr[0])
  n = head
  for i in range(1,len(arr)):
      newNode = Node(arr[i])
      n.next = newNode
      n = newNode
  tail = n
  return head
#Task-3
def task3A( head ):
  temp=head
  while temp:
    print(temp.elem, end=" ")
    temp=temp.next

def task3B_recursive( head ):
    if head==None:
      return
    print(head.elem, end=" ")
    task3B_recursive(head.next)

def task3C( head ):
    summ=0
    tmp=head
    while tmp:
      summ+=tmp.elem
      tmp=tmp.next
    return summ

def task3D_recursive( head ):
    if head==None:
      return 0
    return head.elem+task3D_recursive(head.next)

def task3E( head ):
    summation=0
    multi=1
    new=head
    while new:
      if new.elem%2==0:
        summation+=new.elem
      else:
        multi*=new.elem
      new=new.next
    return multi-summation


def task3F_recursive( head ):
  Pass



# Driver Code for Task-3
arr = np.random.randint(1, 20, size=6, dtype=int)

# task3A
print("task3A: ")
print( "Expected Output: "+str(arr)[1:-1] )
print( "Your Output    : ",end="" )
head = arr2LL(arr)
task3A( head )
print()

# task3B_recursive
print("\ntask3B_recursive: ")
print( "Expected Output: ",str(arr)[1:-1] )
print( "Your Output    : ",end="" )
head = arr2LL(arr)
task3B_recursive( head )
print()

#--------------------------------------------------------

arr = np.random.randint(1, 10, size=6, dtype=int)

# task3C
print("\ntask3C: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task3C( head ) )

# task3D_recursive
print("\ntask3D_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
print( "Expected Output: ",sum(arr) )
print( "Your Output    : ",task3D_recursive( head ) )

#--------------------------------------------------------

arr = np.random.randint(1, 8, size=5, dtype=int)

# task3E
print("\ntask3E: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
if np.sum([e%2 for e in arr])==0:
    print( "Expected Output: ",-np.sum([e for e in arr if e%2==0]) )
else:
    print( "Expected Output: ",int(np.prod([e for e in arr if e%2!=0])-np.sum([e for e in arr if e%2==0])) )
print( "Your Output    : ",task3E( head ) )

#--------------------------------------------------------

# task3F
print("\ntask3F_recursive: ")
print("The LinkedList: ",end="")
head = arr2LL(arr)
showLL(head)
if np.sum([e%2 for e in arr])==0:
    print( "Expected Output: ",-np.sum([e for e in arr if e%2==0]) )
else:
    print( "Expected Output: ",int(np.prod([e for e in arr if e%2!=0])-np.sum([e for e in arr if e%2==0])) )
print( "Your Output    : ",task3F_recursive( head ) )
