class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def getNodeByValue(head, value):
    current = head.next  # Skip the dummy head
    while current != head:
        if current.value == value:
            return current
        current = current.next
    return None

def reverseDLLBetweenTwoValues(head, x, y):
    if not head or not head.next:
        return head

    # Find the nodes corresponding to x and y
    node_x = getNodeByValue(head, x)
    node_y = getNodeByValue(head, y)

    if not node_x or not node_y:
        return head  # One or both values not found

    # Initialize pointers for reversal
    prev_node = node_x.prev
    current = node_x
    next_node = None

    # Reverse the sublist from node_x to node_y
    while current != node_y:
        next_node = current.next
        current.next = current.prev
        current.prev = next_node
        current = next_node

    # Adjust the pointers for node_x and node_y
    node_x.next = node_y.next
    node_y.next.prev = node_x
    node_y.prev = prev_node
    prev_node.next = node_y

    return head

# Helper function to create a dummy-headed circular doubly linked list from a list of elements
def createDLL(elements):
    head = Node(None)  # Dummy head
    head.prev = head
    head.next = head
    current = head
    for elem in elements:
        new_node = Node(elem)
        new_node.prev = current
        new_node.next = head
        current.next = new_node
        head.prev = new_node
        current = new_node
    return head

# Helper function to print the linked list
def printDLL(head):
    current = head.next  # Skip the dummy head
    result = []
    while current != head:
        result.append(str(current.value))
        current = current.next
    print(" => ".join(result))

# Test cases
def test_reverseDLLBetweenTwoValues():
    # Test Case 1
    elements1 = [10, 20, 30, 90, 40, 50]
    head1 = createDLL(elements1)
    print("Test Case 1:")
    print("Original List: ", end="")
    printDLL(head1)
    x1, y1 = 20, 40
    modified_head1 = reverseDLLBetweenTwoValues(head1, x1, y1)
    print("Modified List: ", end="")
    printDLL(modified_head1)
    print()

    # Test Case 2
    elements2 = [5, 15, 25, 35, 45]
    head2 = createDLL(elements2)
    print("Test Case 2:")
    print("Original List: ", end="")
    printDLL(head2)
    x2, y2 = 15, 35
    modified_head2 = reverseDLLBetweenTwoValues(head2, x2, y2)
    print("Modified List: ", end="")
    printDLL(modified_head2)
    print()

    # Test Case 3 (Additional test case)
    elements3 = [1, 2, 3, 4, 5]
    head3 = createDLL(elements3)
    print("Test Case 3:")
    print("Original List: ", end="")
    printDLL(head3)
    x3, y3 = 2, 4
    modified_head3 = reverseDLLBetweenTwoValues(head3, x3, y3)
    print("Modified List: ", end="")
    printDLL(modified_head3)
    print()

# Run the test cases
test_reverseDLLBetweenTwoValues()
