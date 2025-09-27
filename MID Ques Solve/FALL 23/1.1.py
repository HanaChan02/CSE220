def pairWiseEqual(h1, h2):
  while h1!=None and h2!=None:
    a1,a2=h1.elem,h1.next.elem
    b1,b2=h2.elem,h2.next.elem
    if not ((a1 == b1 and a2 == b2) or (a1 == b2 and a2 == b1)):
      return False
    h1=h1.next.next
    h2=h2.next.next

  return True

def createLL(elements):
    head = None
    tail = None
    for elem in elements:
        if head is None:
            head = Node(elem)
            tail = head
        else:
            tail.next = Node(elem)
            tail = tail.next
    return head

# Example usage:
head1 = createLL([10, 15, 34, 41])
head2 = createLL([15, 10, 34, 41])
print(pairWiseEqual(head1, head2))  # Output: True

head1 = createLL([10, 15, 34, 42])
head2 = createLL([15, 10, 34, 41])
print(pairWiseEqual(head1, head2))
