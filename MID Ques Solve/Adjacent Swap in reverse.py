class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.IsEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.IsEmpty():
            return self.items[-1]
        return None

    def IsEmpty(self):
        return len(self.items) == 0

def Do_Adjacent_Swap(st):
    if st.IsEmpty():
        return st

    # Temporary stacks
    temp_stack1 = Stack()
    temp_stack2 = Stack()

    # Reverse the original stack into temp_stack1
    while not st.IsEmpty():
        temp_stack1.push(st.pop())

    # Swap adjacent elements and push into temp_stack2
    while not temp_stack1.IsEmpty():
        first = temp_stack1.pop()
        if not temp_stack1.IsEmpty():
            second = temp_stack1.pop()
            temp_stack2.push(second)
            temp_stack2.push(first)
        else:
            temp_stack2.push(first)

    # Reverse back to the original stack
    while not temp_stack2.IsEmpty():
        st.push(temp_stack2.pop())

    return st

# Driver code
def main():
    # Create a stack and push elements
    st = Stack()
    elements = [1, 2, 3, 4, 5, 6, 7, 8]
    for elem in elements:
        st.push(elem)

    print("Original Stack:")
    temp = Stack()
    while not st.IsEmpty():
        elem = st.pop()
        print(elem, end=' → ' if not st.IsEmpty() else '')
        temp.push(elem)
    print()

    # Restore the original stack
    while not temp.IsEmpty():
        st.push(temp.pop())

    # Perform adjacent swap
    modified_stack = Do_Adjacent_Swap(st)

    print("Modified Stack:")
    while not modified_stack.IsEmpty():
        elem = modified_stack.pop()
        print(elem, end=' → ' if not modified_stack.IsEmpty() else '')
    print()

# Run the driver code
if __name__ == "__main__":
    main()
