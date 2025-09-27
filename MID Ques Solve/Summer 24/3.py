## QUESTION 3
class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.items) == 0

def Do_Adjacent_Swap(st):
    aux_stack = Stack()

    # Step 1: Transfer all elements to an auxiliary stack (reversing order)
    while not st.isEmpty():
        aux_stack.push(st.pop())

    temp_stack = Stack()

    # Step 2: Swap adjacent elements while transferring to temp_stack
    while not aux_stack.isEmpty():
        first = aux_stack.pop()
        if not aux_stack.isEmpty():
            second = aux_stack.pop()
            temp_stack.push(second)  # Push swapped elements
            temp_stack.push(first)
        else:
            temp_stack.push(first)  # If odd count, push the last as it is

    # Step 3: Move elements back to the original stack to restore order
    while not temp_stack.isEmpty():
        st.push(temp_stack.pop())

    return st  # Return the modified stack

# **Test Case**
st = Stack()
for num in [8, 7, 6, 5, 4, 3, 2, 1]:  # Top -> 8 7 6 5 4 3 2 1
    st.push(num)

modified_stack = Do_Adjacent_Swap(st)

# **Printing the Stack (Top to Bottom)**
while not modified_stack.isEmpty():
    print(modified_stack.pop(), end=" ")  # Expected: 7 8 5 6 3 4 1 2
