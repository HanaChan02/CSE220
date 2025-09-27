import numpy as np
def countNode(head):
  if head==None:
    return 0
  new_node=head
  count=0
  while new_node!=None:
    new_node=new_node.next
    count+=1
  return count


#### DRIVER CODE ####
arr = np.array([10, 20, 30, 40, 50])
head3 = createList(arr)

print("Linked List:")
printLL(head3)

# Count nodes in the linked list
node_count = countNode(head3)
print(f"Number of nodes in the linked list: {node_count}")

print('-'*50)
arr = np.array([10, 20])
head3 = createList(arr)

print("Linked List:")
printLL(head3)

# Count nodes in the linked list
node_count = countNode(head3)
print(f"Number of nodes in the linked list: {node_count}")


print('-'*50)
arr = np.array([])
head3 = createList(arr)

print("Linked List:")
printLL(head3)

# Count nodes in the linked list
node_count = countNode(head3)
print(f"Number of nodes in the linked list: {node_count}")
