## QUESTION 2
class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next
# Helper function to create a linked list from a list of elements
def create_linked_list(elements):
    head = None
    tail = None
    for elem in elements:
        if head is None:
            head = Node(elem)
            tail = head
        else:
            tail.next = Node(elem)
            tail = tail.next
    return head
def IsSumPossible(head,n):
  curr=head
  if curr.next==None:
    return False
  while curr.next!=None:
    sum=curr.elem+curr.next.elem
    if sum==n:
      return True
    curr=curr.next.next
  return False




# Driver code
def main():
    # Test Case 1
    list1 = create_linked_list([1, 2, 3, 4, 5])
    n1 = 7
    print("Test Case 1:")
    print("IsSumPossible:", IsSumPossible(list1, n1))  # Output: True

    # Test Case 2
    list2 = create_linked_list([1, 2, 4, 5, 6])
    n2 = 4
    print("\nTest Case 2:")
    print("IsSumPossible:", IsSumPossible(list2, n2))  # Output: False

    # Test Case 3
    list3 = create_linked_list([5])
    n3 = 5
    print("\nTest Case 3:")
    print("IsSumPossible:", IsSumPossible(list3, n3))  # Output: False

# Run the driver code
if __name__ == "__main__":
    main()
