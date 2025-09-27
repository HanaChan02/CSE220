class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

# Standalone function to print the linked list
def printLL(head):
    temp = head  # Start from the head of the linked list
    while temp is not None:  # Traverse until the end of the list
        print(temp.elem, end=' -> ' if temp.next else '')  # Print the element
        temp = temp.next  # Move to the next node
    print()  # Print a newline after the list

def reverseAndSwap(head,i):
  if not head or i<0:
    return head
  curr=head
  for x in range(i):
    if curr.next:
      curr=curr.next
    else:
      break
  first_head=head
  second_head=curr.next
  curr.next=None

  ## PREPEND FOR REVERSAL
  prev=None
  current=first_head
  while current:
    node2=current.next
    current.next=prev

    prev=current
    current=node2
  first_head=prev

  if second_head:
    new_node=second_head
    while new_node.next:
      new_node=new_node.next
    new_node.next=first_head
    return second_head
  else:
      return first_head


# Creating the linked list: 5 -> 7 -> 6 -> 3 -> 8 -> 2 -> 1
head = Node(5, Node(7, Node(6, Node(3, Node(8, Node(2, Node(1)))))))

print("Original list:")
printLL(head)

# Reversing and swapping with i = 3
head = reverseAndSwap(head, 3)
print("List after reverse and swap with i = 3:")
printLL(head)

# Reversing and swapping with i = 0
head = reverseAndSwap(head, 0)
print("List after reverse and swap with i = 0:")
printLL(head)

# Reversing and swapping with i = 6
head = reverseAndSwap(head, 6)
print("List after reverse and swap with i = 6:")
printLL(head)
