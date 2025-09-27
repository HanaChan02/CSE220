class MinHeap:
  def __init__(self,capacity):
    self.__array=[None]*(capacity+1)
    self.__heapSize=0

  def __swim(self,i):
    while i>1 and self.__array[i]<self.__array[i//2]:  #K//2==parent
      self.__array[i],self.__array[i//2]=self.__array[i//2],self.__array[i]
      i=i//2

  def __sink(self,i):
    while 2*i<=self.__heapSize:
      j=2*i
      if j<self.__heapSize and self.__array[j+1]<self.__array[j]:
        j+=1
      if self.__array[i]<=self.__array[j]:
        break
      self.__array[i],self.__array[j]=self.__array[j],self.__array[i]
      i=j


  def insert(self, value):
    if self.__heapSize>=len(self.__array)-1:
      raise Exception("Heap is full")
    self.__heapSize+=1
    self.__array[self.__heapSize]=value
    self.__swim(self.__heapSize)

  def sort(self):
    og_size=self.__heapSize
    for i in range(og_size,0,-1):
      self.__array[1],self.__array[i]=self.__array[i],self.__array[1]
      self.__heapSize-=1
      self.__sink(1)
    self.__heapSize=og_size
    return self.__array[1:og_size+1][::-1]

  def extractMin(self):
    if self.__heapSize==0:
      raise Exception("Heap is empty")
    min_val=self.__array[1]
    self.__array[1]=self.__array[self.__heapSize]
    self.__heapSize-=1
    self.__sink(1)
    return min_val


def load_balance_min(self,n,m):
  l=[]
  heap=MinHeap(m)
  for i in range(m):
    heap.insert(0)
  for a in n:
    min=heap.extractMin()
    heap.insert(min+a)
  for i in range(m):
    l.append()
