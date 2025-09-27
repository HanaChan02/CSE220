## QUESTION 4
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 3
        self.back = 3

    def enqueue(self, item):
        if (self.back + 1) % self.size == self.front:
            print("Queue Overflow")
            return
        self.back = (self.back + 1) % self.size
        self.queue[self.back] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.front == self.back:
            print("Queue Underflow")
            return None
        self.front = (self.front + 1) % self.size
        item = self.queue[self.front]
        self.queue[self.front] = None
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.front == self.back:
            print("Queue Underflow")
            return None
        item = self.queue[(self.front + 1) % self.size]
        print(f"Peeked: {item}")
        return item

    def print_queue(self):
        print(f"Queue: {self.queue}")
        print(f"Front Index: {self.front}, Back Index: {self.back}")

class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

def test(head, queue):
    temp = head
    while temp.next is not None:
        if temp.next.elem < temp.elem:
            queue.enqueue(temp.next.elem)
        elif temp.next.elem > temp.elem:
            queue.dequeue()
        else:
            queue.peek()
        temp = temp.next
        queue.print_queue()
        print("-----------------------------")

# Driver code
def main():
    # Create the linked list
    linked_list = Node(-1, Node(5, Node(-12, Node(-20, Node(9, Node(-43, Node(-67, Node(-67, Node(-85, Node(-91, Node(-90)))))))))))

    # Create the circular queue
    queue = CircularQueue(4)

    # Perform the test function
    test(linked_list, queue)

# Run the driver code
if __name__ == "__main__":
    main()
