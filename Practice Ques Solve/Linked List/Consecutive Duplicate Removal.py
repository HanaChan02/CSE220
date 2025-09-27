class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def multi_delstel(head):
    if not head or not head.next:
        return head

    current = head.next  # Start from the first actual node after the dummy head
    while current and current.next != head:  # Traverse until we loop back to the dummy head
        if current.value == current.next.value:
            # Remove the next node
            current.next = current.next.next
            if current.next:
                current.next.prev = current
        else:
            current = current.next

    return head

# Helper function to create a dummy-headed doubly circular linked list from a list of elements
def create_doubly_circular_linked_list(elements):
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
def print_linked_list(head):
    current = head.next  # Skip the dummy head
    result = []
    while current != head:
        result.append(str(current.value))
        current = current.next
    print("DH <-> " + " <-> ".join(result))

# Test cases
def test_multi_delstel():
    # Test Case 1
    elements1 = [2, 3, 1, 1, 1, 9]
    head1 = create_doubly_circular_linked_list(elements1)
    print("Test Case 1:")
    print("Original List: ", end="")
    print_linked_list(head1)
    modified_head1 = multi_delstel(head1)
    print("Modified List: ", end="")
    print_linked_list(modified_head1)
    print()

    # Test Case 2
    elements2 = [2, 3, 1, 9]
    head2 = create_doubly_circular_linked_list(elements2)
    print("Test Case 2:")
    print("Original List: ", end="")
    print_linked_list(head2)
    modified_head2 = multi_delstel(head2)
    print("Modified List: ", end="")
    print_linked_list(modified_head2)
    print()

# Run the test cases
test_multi_delstel()
