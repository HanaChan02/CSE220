class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isEmpty(self):
        return len(self.items) == 0

def print_total_task(tasks):
  stack=Stack()
  stack.push(tasks[0])
  for i in range(1,len(tasks)):
    current=tasks[i]
    top_task=stack.peek()
    if current[0]<=top_task[1]:


# Driver code
def main():
    tasks = [
        [1, 5],
        [2, 3],
        [4, 6],
        [7, 10],
        [9, 11],
        [12, 15]
    ]

    print("Non-overlapping tasks in descending order of start time:")
    print_total_task(tasks)

# Run the driver code
if __name__ == "__main__":
    main()
