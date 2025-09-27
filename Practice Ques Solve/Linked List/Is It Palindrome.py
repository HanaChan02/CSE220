class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

def isPalindrome(head):
    if not head:
        return True

    # Step 1: Find the middle of the linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Step 3: Compare the first half with the reversed second half
    first_half = head
    second_half = prev
    while second_half:
        if first_half.elem != second_half.elem:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

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
    values1 = [10, 43, 54, 43, 10]
    head1 = create_linked_list(values1)
    print("Is the linked list a palindrome?", isPalindrome(head1))  # Output: True

    # Test Case 2
    values2 = [1, 41, 4, 3, 10]
    head2 = create_linked_list(values2)
    print("Is the linked list a palindrome?", isPalindrome(head2))  # Output: False

# Run the driver code
if __name__ == "__main__":
    main()
