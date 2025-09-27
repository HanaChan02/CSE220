import numpy as np
class Node:
  def __init__(self, elem, next=None):
    # Initialize the node with an element and a reference to the next node (default is None)
    self.elem = elem
    self.next = next

def createList(arr):
  if len(arr)==0:
    return None
    # Create the head node with the first element of the array
  head = Node(arr[0])
  tail = head
    # Iterate through the array to create linked list nodes
  for i in range(1,len(arr)):
    newNode = Node(arr[i])  # Create a new node for each element
    tail.next = newNode  # Link the current tail node to the new node
    tail = newNode  # Update the tail to be the new node

  return head  # Return the head node of the linked list

def printLL(head):
  t=head
  while t!=None:
    print(t.elem, end=" -> ")
    t=t.next
  print()

a=np.array([1,2,3,4,5,6,7])
LL=createList(a)
printLL(LL)
