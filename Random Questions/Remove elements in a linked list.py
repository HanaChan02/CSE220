import numpy as np
def removeAt(head,idx):
  size=countNode(head)
  if idx<0 or idx>=size: # Invalid index
    print("deletion Failed, Not valid index")
    return head
  elif idx == 0:
    return head.next
  t=head
  for i in range(idx-1):
    t=t.next
  t.next=t.next.next
  return head


### DRIVER CODE ###

               # 0   1   2   3   4
arr = np.array([10, 20, 30, 40, 50])
head3 = createList(arr)

print("Original Linked List:")
printLL(head3)

# Remove elements at various positions
head3 = removeAt(head3, 0)  # Remove head
print("After removing element at index 0 (head): remove 10")
printLL(head3)

head3 = removeAt(head3, 2)  # Remove element at index 2
print("After removing element at index 2 (middle): remove 40")
printLL(head3)

head3 = removeAt(head3, 2)  # Remove element at index 2
print("After removing element at index 2 (tail), remove: 50:")
printLL(head3)

### Attempt to remove at an invalid index--
#Remove the comment at line 3 to see the error
head3 = removeAt(head3, 3)  # # Invalid index--Currently there are only 3 elements. So indexing 0 to 2
print("After removing element at index 3:")
printLL(head3)
