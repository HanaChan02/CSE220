! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, elem):
        new_node = Node(elem)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        removed_elem = self.front.elem
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_elem

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.front.elem

    def is_empty(self):
        return self.front is None

    def display_queue(self):
        print("Queue (front to rear):", end=" ")
        current = self.front
        while current:
            print(f"{current.elem} ->", end=" ")
            current = current.next
        print("NULL")
class CallQueue:
    def __init__(self):
        self.vip_queue = LinkedListQueue()
        self.regular_queue = LinkedListQueue()

    def enqueue_call(self, customer_id, is_vip):
        if is_vip==True:
          self.vip_queue.enqueue(customer_id)
          print(f"Customer {customer_id} added to VIP queue.")
        else:
          self.regular_queue.enqueue(customer_id)
          print(f"Customer {customer_id} added to Regular queue.")

    def dequeue_call(self):
        if not self.vip_queue.is_empty():
          id=self.vip_queue.dequeue()
          print(f"Processing VIP Customer {id}")
        elif not self.regular_queue.is_empty():
          id=self.regular_queue.dequeue()
          print(f"Processing Regular Customer {id}")

    def display_queue(self):
        print("VIP Queue:")
        self.vip_queue.display_queue()
        print("Regular Queue:")
        self.regular_queue.display_queue()



# YOU MUST RUN THIS CELL TO TEST YOUR CODE
# If you modify the method calls the outputs will be changed as well
call_center = CallQueue()
# Enqueueing customers
call_center.enqueue_call(101, False)  # Regular customer
call_center.enqueue_call(201, True)   # VIP customer
call_center.enqueue_call(102, False)  # Regular customer
call_center.enqueue_call(202, True)   # VIP customer
call_center.enqueue_call(103, False)  # Regular customer

call_center.display_queue()

# Processing calls
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()  # No more calls

call_center.display_queue()

#   ::Expected Ouput::

# Customer 101 added to Regular queue.
# Customer 201 added to VIP queue.
# Customer 102 added to Regular queue.
# Customer 202 added to VIP queue.
# Customer 103 added to Regular queue.

# VIP Queue:
# Queue (front to rear): 201 -> 202 -> NULL
# Regular Queue:
# Queue (front to rear): 101 -> 102 -> 103 -> NULL

# Processing VIP Customer 201.
# Processing VIP Customer 202.
# Processing Regular Customer 101.
# Processing Regular Customer 102.
# Processing Regular Customer 103.
# No calls in the queue.

# VIP Queue:
# Queue (front to rear): NULL
# Regular Queue:
# Queue (front to rear): NULL
