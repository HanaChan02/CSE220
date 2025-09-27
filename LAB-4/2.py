! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
class Node:
  def __init__(self, value=None, next = None):
    self.value = value
    self.next = next

class HashTable:
  def __init__(self, length):
    n = Node()
    self.ht = [n] * length
    self.length = length

  def show(self):
    count = 0
    for i in self.ht:
      temp = i
      print(count, end=" ")
      while temp!=None:
        print (temp.value, end="-->")
        temp = temp.next
      count += 1
      print()


  #Do it by yourself
  def __hash_function(self, key):
    total_value=0
    if len(key)%2==0:
      for i in range(len(key)):
        if i%2==0:
          total_value+=ord(key[i])
    else:
      for j in range(len(key)):
        if j%2!=0:
          total_value+=ord(key[j])
    return total_value%len(self.ht)



  #Do it by yourself
  def insert(self, key, value):
    idx = self.__hash_function(key)
    node = Node((key, value))

    if self.ht[idx].value is None:
        self.ht[idx] = node
        return

    curr = self.ht[idx]
    prev = None
    while curr is not None:
      if curr.value is not None and curr.value[0] == key:
        curr.value = (key, value)
        return
      prev = curr
      curr = curr.next

    curr = self.ht[idx]
    if curr.value[1] < value:
      node.next = curr
      self.ht[idx] = node
    else:
      while curr.next is not None and curr.next.value[1] >= value:
        curr = curr.next
      node.next = curr.next
      curr.next = node


#Driver Code
ht = HashTable(3)


ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()
print("------------")
ht.insert("apple", 100)
ht.insert("guava", 10)
ht.show()

# Driver Code Output:
# 0 ('coconut', 90)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 100)-->('guava', 10) -->
# 2 ('cherry', 50)-->
