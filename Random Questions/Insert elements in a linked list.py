import numpy as np
def insertAt(head,idx,element):
  size=countNode(head)
  if idx<0 or idx>size:
    print("Insertion Failed, Not valid index")
    return None
  newNode=Node(element)
  if idx==0:
    newNode.next=head
    head=newNode
    return head
  t=head
  for i in range(idx-1):
    t=t.next
  newNode.next=t.next
  t.next=newNode
  return head


### DRIVER CODE ###
               # 0   1   2   3   4
arr = np.array([10, 20, 30, 40, 50])
head3 = createList(arr)

print("Original Linked List:")
printLL(head3)
print('-'*50)

# Insert elements at various positions
head3 = insertAt(head3, 0, 5)  # Insert at the head
print("After inserting 5 at index 0 (head):")
printLL(head3)
print('-'*50)

head3 = insertAt(head3, 3, 25)  # Insert in the middle
print("After inserting 25 at index 3 (middle):")
printLL(head3)
print('-'*50)

head3 = insertAt(head3, 7, 60)  # Insert at the end
print("After inserting 60 at index 7 (after tail, size):")
printLL(head3)
print('-'*50)

# Attempt to insert at an invalid index
head3 = insertAt(head3, 10, 100)
