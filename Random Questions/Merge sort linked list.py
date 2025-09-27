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


def sortList(head):
    if head is None or head.next is None:
        return head

    sorted_head = None  # This will be the new sorted list
    current = head
    while current:
        next_node = current.next
        sorted_head = insertSorted(sorted_head, current)
        current = next_node

    return sorted_head

def insertSorted(sorted_head, node):
    # Helper function to insert a node into the sorted linked list
    if sorted_head is None or sorted_head.elem >= node.elem:
        node.next = sorted_head
        return node
    else:
        current = sorted_head
        while current.next and current.next.elem < node.elem:
            current = current.next
        node.next = current.next
        current.next = node
    return sorted_head

def mergeSortedLL(l1,l2):
  head=Node(0)
  temp=head
  while l1 and l2:
    if l1.elem<l2.elem:
      temp.next=l1
      l1=l1.next
    else:
      temp.next=l2
      l2=l2.next
    temp=temp.next
  if l1:
    temp.next=l1
  else:
    temp.next=l2
  return head.next


### DRIVER CODE ###
l1 = createList([4, 8, 10])
print('Sorted Linked List 1: ', end="")
printLL(l1)

l2 = createList([3, 6, 9])
print('Sorted Linked List 2: ', end="")
printLL(l2)

# Merge the sorted linked lists
merged_list = mergeSortedLL(l1, l2)
print('Merged Sorted Linked List: ', end="")
printLL(merged_list)

print('\n==================================\n')

l3 = createList([12, 5, 2, 14])
print('Sorted Linked List 3: ', end="")
printLL(l3)

l4 = createList([1, 7, 13])
print('Sorted Linked List 4: ', end="")
printLL(l4)

# Merge the sorted linked lists
merged_list = mergeSortedLL(l3, l4)
print('Merged Sorted Linked List: ', end="")
printLL(merged_list)
