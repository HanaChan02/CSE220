class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def smallest_number_product(head, n):
    if not head or n <= 0:
        return 0  # Return 0 if the list is empty or n is invalid

    product = 1
    current = head
    count = 0

    # Traverse the first n nodes and calculate the product
    while current is not None and count < n:
        product *= current.value
        current = current.next
        count += 1

    return product

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Driver code
def main():
    # Test Case 1
    values1 = [1, 2, 3, 4, 5, 6]
    head1 = create_linked_list(values1)
    n1 = 4
    print("Product of the first", n1, "smallest numbers:", smallest_number_product(head1, n1))  # Output: 24

    # Test Case 2
    values2 = [2, 3, 9, 20, 100, 110]
    head2 = create_linked_list(values2)
    n2 = 3
    print("Product of the first", n2, "smallest numbers:", smallest_number_product(head2, n2))  # Output: 54

# Run the driver code
if __name__ == "__main__":
    main()
