class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()

def remove_Duplicates(head):
  if head is None:
    return head
  current=head
  while current!=None:
    prev=current
    while prev.next!=None:
      if prev.next.data==current.data:
        prev.next=prev.next.next
      else:
        prev=prev.next
    current=current.next
  return head



# Driver code
def main():
    # Example 1
    head1 = Node(101)
    head1.next = Node(103)
    head1.next.next = Node(101)
    head1.next.next.next = Node(102)
    head1.next.next.next.next = Node(103)
    head1.next.next.next.next.next = Node(104)
    head1.next.next.next.next.next.next = Node(105)
    head1.next.next.next.next.next.next.next = Node(105)

    print("Input Tickets:")
    print_list(head1)

    head1 = remove_Duplicates(head1)

    print("Fixed Tickets:")
    print_list(head1)

    print("------------------------------------------------------")

    # Example 2
    head2 = Node(102)
    head2.next = Node(101)
    head2.next.next = Node(101)
    head2.next.next.next = Node(102)
    head2.next.next.next.next = Node(102)
    head2.next.next.next.next.next = Node(103)
    head2.next.next.next.next.next.next = Node(104)
    head2.next.next.next.next.next.next.next = Node(104)

    print("Input Tickets:")
    print_list(head2)

    head2 = remove_Duplicates(head2)

    print("Fixed Tickets:")
    print_list(head2)

# Run the driver code
if __name__ == "__main__":
    main()
