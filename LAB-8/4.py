#TASK-4
def TopKLargest(nums,k):
  heap=MaxHeap(len(nums))
  for i in nums:
    heap.insert(i)
  ans=[]
  for i in range(k):
    ans.append(heap.extractMax())
  return ans

  # Tester Code
print("Testing Top K Largest:")
nums = [4, 10, 2, 8, 6, 7]
k = 3
print("Top", k, "largest:", TopKLargest(nums, k))
print("-----------------------------------")
print("Testing Top K Largest:")
nums = [4, 10, 2, 5, 21, 11]
k = 3
print("Top", k, "largest:", TopKLargest(nums, k))
