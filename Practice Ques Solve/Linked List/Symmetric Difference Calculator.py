def touchGb(head):
    elements = []
    current = head
    while current:
        elements.append(current.elem)
        current = current.next

    n = len(elements)
    total = 0
    for i in range(n // 2):
        diff = elements[i] - elements[n - 1 - i]
        total += diff

    print(total)

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# Helper function to create a linked list from a list of elements
def create_linked_list(elements):
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for elem in elements[1:]:
        current.next = Node(elem)
        current = current.next
    return head

# Test cases
def test_touchGb():
    # Test Case 1
    elements1 = [9, 11, 3, 4, 2, 1]
    head1 = create_linked_list(elements1)
    print("Test Case 1:")
    print("Expected Output: 16")
    print("Actual Output: ", end="")
    touchGb(head1)
    print()

    # Test Case 2
    elements2 = [1, 2, 3, 1]
    head2 = create_linked_list(elements2)
    print("Test Case 2:")
    print("Expected Output: -1")
    print("Actual Output: ", end="")
    touchGb(head2)
    print()

# Run the test cases
test_touchGb()
