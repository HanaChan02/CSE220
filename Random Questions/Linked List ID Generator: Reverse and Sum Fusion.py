class Node:
    def __init__(self, elem, next=None):
        self.elem, self.next = elem, next

def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
    return head

def printLinkedList(head):
    temp = head
    while temp is not None:
        if temp.next is not None:
            print(temp.elem, end='-->')
        else:
            print(temp.elem)
        temp = temp.next
    print()

def reverseLinkedList(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def idGenerator(head1, head2, head3):
    # Step 1: Reverse head1
    reversed_head1 = reverseLinkedList(head1)

    # Step 2: Sum corresponding elements of head2 and head3
    sum_head = None
    sum_tail = None
    temp2 = head2
    temp3 = head3

    while temp2 is not None and temp3 is not None:
        sum_val = temp2.elem + temp3.elem
        new_node = Node(sum_val)
        if sum_head is None:
            sum_head = new_node
            sum_tail = new_node
        else:
            sum_tail.next = new_node
            sum_tail = new_node
        temp2 = temp2.next
        temp3 = temp3.next

    # Step 3: Combine reversed head1 and sum_head
    new_id_head = None
    new_id_tail = None

    # Add reversed head1 to the new ID
    temp = reversed_head1
    while temp is not None:
        new_node = Node(temp.elem)
        if new_id_head is None:
            new_id_head = new_node
            new_id_tail = new_node
        else:
            new_id_tail.next = new_node
            new_id_tail = new_node
        temp = temp.next

    # Add sum_head to the new ID
    temp = sum_head
    while temp is not None:
        new_node = Node(temp.elem)
        if new_id_head is None:
            new_id_head = new_node
            new_id_tail = new_node
        else:
            new_id_tail.next = new_node
            new_id_tail = new_node
        temp = temp.next

    return new_id_head

# DO NOT CHANGE THE CODE BELOW
import numpy as np

print('==============Test Case 1=============')
head1 = createList(np.array([0, 3, 2, 2]))
head2 = createList(np.array([5, 2, 2, 1]))
head3 = createList(np.array([4, 3, 2, 1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)  # This should print 2 → 2 → 3 → 0 → 9 → 5 → 4 → 2

print('==============Test Case 2=============')
head1 = createList(np.array([0, 3, 9, 1]))
head2 = createList(np.array([3, 6, 5, 7]))
head3 = createList(np.array([2, 4, 3, 8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)  # This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5
