def rearrangeNodes(head, x):
    # Dummy nodes to simplify the merging process
    greater_head = Node(0)
    less_equal_head = Node(0)

    # Pointers to build the two lists
    greater = greater_head
    less_equal = less_equal_head

    current = head
    while current:
        if current.elem > x:
            greater.next = current
            greater = greater.next
        else:
            less_equal.next = current
            less_equal = less_equal.next
        current = current.next

    # Connect the two lists
    greater.next = less_equal_head.next
    less_equal.next = None  # Terminate the list

    # Return the head of the modified list
    return greater_head.next

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.elem))
        current = current.next
    print(" -> ".join(result))

# Test cases
def test_rearrangeNodes():
    # Test Case 1
    elements1 = [1, 4, 3, 2, 5, 2]
    head1 = create_linked_list(elements1)
    print("Test Case 1:")
    print("Original List: ", end="")
    print_linked_list(head1)
    x1 = 3
    modified_head1 = rearrangeNodes(head1, x1)
    print("Modified List: ", end="")
    print_linked_list(modified_head1)
    print()

    # Test Case 2
    elements2 = [2, 3]
    head2 = create_linked_list(elements2)
    print("Test Case 2:")
    print("Original List: ", end="")
    print_linked_list(head2)
    x2 = 2
    modified_head2 = rearrangeNodes(head2, x2)
    print("Modified List: ", end="")
    print_linked_list(modified_head2)
    print()

# Run the test cases
test_rearrangeNodes()
