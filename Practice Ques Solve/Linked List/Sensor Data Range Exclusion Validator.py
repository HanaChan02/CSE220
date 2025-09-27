def validate_readings_outside(head, low, high):
    current = head
    inside_range = False
    while current:
        if low <= current.value <= high:
            inside_range = True
            break
        current = current.next

    if inside_range:
        print("Reading inside the range detected.")
    else:
        # Print the linked list
        current = head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        print(" > ".join(result))


# Test cases
def test_validate_readings_outside():
    # Test Case 1
    elements1 = [25, 18, 55, 20, 12]
    head1 = create_linked_list(elements1)
    print("Test Case 1:")
    print("Expected Output: Reading inside the range detected.")
    print("Actual Output: ", end="")
    validate_readings_outside(head1, 10, 20)
    print()

    # Test Case 2
    elements2 = [14, 12, 17, 20]
    head2 = create_linked_list(elements2)
    print("Test Case 2:")
    print("Expected Output: 14 > 12 > 17 > 20")
    print("Actual Output: ", end="")
    validate_readings_outside(head2, 30, 40)
    print()

# Run the test cases
test_validate_readings_outside()
