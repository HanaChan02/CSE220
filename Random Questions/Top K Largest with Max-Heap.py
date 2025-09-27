#TASK-2
class MaxHeap:
    def __init__(self, capacity):
        self.__array = [None] * (capacity + 1)
        self.__heapSize = 0

    def __swim(self, i):
        while i > 1 and self.__array[i] > self.__array[i // 2]:
            self.__array[i], self.__array[i // 2] = self.__array[i // 2], self.__array[i]
            i = i // 2

    def __sink(self, i):
        while 2 * i <= self.__heapSize:
            j = 2 * i
            if j < self.__heapSize and self.__array[j + 1] > self.__array[j]:
                j += 1
            if self.__array[i] >= self.__array[j]:
                break
            self.__array[i], self.__array[j] = self.__array[j], self.__array[i]
            i = j

    def insert(self, value):
        if self.__heapSize >= len(self.__array) - 1:
            raise Exception("Heap is full")
        self.__heapSize += 1
        self.__array[self.__heapSize] = value
        self.__swim(self.__heapSize)

    def sort(self):
        original_size = self.__heapSize
        for i in range(original_size, 0, -1):
            self.__array[1], self.__array[i] = self.__array[i], self.__array[1]
            self.__heapSize -= 1
            self.__sink(1)
        self.__heapSize = original_size  # Restore original size
        return self.__array[1:original_size + 1][::-1]

    def extractMax(self):
        if self.__heapSize == 0:
            raise Exception("Heap is empty")
        max_val = self.__array[1]
        self.__array[1] = self.__array[self.__heapSize]
        self.__heapSize -= 1
        self.__sink(1)
        return max_val


def top_k_largest(nums, k):
    if k <= 0:
        return []
    
    # Use max-heap to track the k smallest elements
    # The root will be the largest among the k smallest
    heap = MaxHeap(k)
    
    for num in nums:
        if heap._MaxHeap__heapSize < k:
            heap.insert(num)
        else:
            # If current number is smaller than the largest in our k-smallest
            if num < heap._MaxHeap__array[1]:
                heap.extractMax()  # Remove the largest
                heap.insert(num)   # Add the smaller number
    
    # Extract all elements from heap and sort them
    result = []
    while heap._MaxHeap__heapSize > 0:
        result.append(heap.extractMax())
    
    # Return in ascending order (reverse of max-heap extraction)
    return result[::-1]

# Test the function
nums = [9, 1, 6, 4, 8, 2]
k = 3
print(top_k_largest(nums, k))
