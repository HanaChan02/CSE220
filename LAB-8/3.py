#TASK-3
def assign_tasks(tasks,m):
  heap=MinHeap(m)
  for i in range(m):
    heap.insert(0)
  for x in tasks:
    min_load=heap.extractMin()
    heap.insert(min_load+x)
  result=[]
  for i in range(m):
    result.append(heap.extractMin())
  return result

  # Tester Code
print("Testing Task Scheduling:")
tasks = [2, 4, 7, 1, 6]
m = 4
print("Machine loads:", assign_tasks(tasks, m))
print("-----------------------------------")
print("Testing Task Scheduling:")
tasks = [8, 4, 5, 9, 11]
m = 3
print("Machine loads:", assign_tasks(tasks, m))
