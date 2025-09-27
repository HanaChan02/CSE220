class MidStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

def conditional_reverse(stack):
  if stack.isEmpty():
    return MidStack()
  new_stack=MidStack()
  prev=None
  while not stack.isEmpty():
    current=stack.pop()
    if current!=prev:
      new_stack.push(current)
    prev=current

  return new_stack


### DRAVER CODE ###

def print_stack_bottom_to_top(stack):
    if stack.isEmpty():
        print("Stack is empty")
        return

    # Use a temporary stack to reverse the order for printing
    temp_stack = MidStack()
    while not stack.isEmpty():
        temp_stack.push(stack.pop())

    # Print the elements from the temporary stack (bottom to top)
    while not temp_stack.isEmpty():
        element = temp_stack.pop()
        print(element, end=' ')
        stack.push(element)  # Restore the original stack
    print()

# Example usage:
stack = MidStack()
stack.push(10)
stack.push(10)
stack.push(20)
stack.push(20)
stack.push(30)
stack.push(10)
stack.push(50)

# Print the input stack (bottom to top)
print("Input:")
print_stack_bottom_to_top(stack)

# Get the reversed stack
reversed_stack = conditional_reverse(stack)

# Print the output stack (bottom to top)
print("Output:")
print_stack_bottom_to_top(reversed_stack)
