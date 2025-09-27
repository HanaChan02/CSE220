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

  # Tester Code
print("-----MaxHeap-----")
max_heap = MaxHeap(5)
max_heap.insert(19)
max_heap.insert(9)
max_heap.insert(8)
max_heap.insert(1)
max_heap.insert(31)
print("Extracted Max:", max_heap.extractMax())
print("Sorted Heap:", max_heap.sort())
