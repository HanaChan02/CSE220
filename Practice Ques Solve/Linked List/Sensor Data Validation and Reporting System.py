def validate_readings(head, low, high):
    current = head
    out_of_range = False
    while current:
        if not (low <= current.elem <= high):
            out_of_range = True
            break
        current = current.next

    if out_of_range:
        return "Reading out of range detected."
    else:
        # Print the linked list
        current = head
        result = []
        while current:
            result.append(str(current.elem))
            current = current.next
        print(" > ".join(result))


# Test cases
def test_validate_readings():
    # Test Case 1
    elements1 = [15, 18, 10, 20, 12]
    head1 = create_linked_list(elements1)
    print("Test Case 1:")
    print("Expected Output: 15 > 18 > 10 > 20 > 12")
    print("Actual Output: ", end="")
    result1 = validate_readings(head1, 10, 20)
    if result1:
        print(result1)
    print()

    # Test Case 2
    elements2 = [25, 15, 30, 18, 10, 22]
    head2 = create_linked_list(elements2)
    print("Test Case 2:")
    print("Expected Output: Reading out of range detected.")
    print("Actual Output: ", end="")
    result2 = validate_readings(head2, 10, 20)
    if result2:
        print(result2)
    print()

# Run the test cases
test_validate_readings()
