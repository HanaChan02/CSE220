! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
#Run this cell
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()
#Task-3
def reverse_list(head):
  if not head:
    return None
  prev=None
  current=head
  while current:
    new_node=current.next
    current.next=prev

    prev=current
    current=new_node
  return prev

def idGenerator(head1, head2, head3):
  reversed_list1=reverse_list(head1)
  t2=head2
  t3=head3
  sum_head=None
  sum_tail=None

  while t2 and t3:
    sum_elem=t2.elem+t3.elem
    newNode=Node(sum_elem)
    if not sum_head:
      sum_head=newNode
      sum_tail=newNode
    else:
      sum_tail.next=newNode
      sum_tail=newNode
    t2=t2.next
    t3=t3.next

  if reversed_list1:
    temp=reversed_list1
    while temp.next:
      temp=temp.next
    temp.next=sum_head
  else:
    reversed_list1=sum_head
  return reversed_list1

print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5
