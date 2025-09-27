def weirdCombination(array, head):
    linked_list_elements = []
    current = head
    while current:
        linked_list_elements.append(current.elem)
        current = current.next

    total = 0
    for i in range(len(array)):
        total += (linked_list_elements[i] - array[i])

    return total
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# Test cases
def test_weirdCombination():
    # Test Case 1
    linked_list_elements1 = [10, 23, 30, 14]
    array1 = [15, 10, 56, 65]
    head1 = create_linked_list(linked_list_elements1)
    print("Test Case 1:")
    print("Expected Output: -69")
    print("Actual Output:", weirdCombination(array1, head1))
    print()

    # Test Case 2
    linked_list_elements2 = [5, 10, 15, 20]
    array2 = [1, 2, 3, 4]
    head2 = create_linked_list(linked_list_elements2)
    print("Test Case 2:")
    print("Expected Output: 40")
    print("Actual Output:", weirdCombination(array2, head2))
    print()

# Run the test cases
test_weirdCombination()
