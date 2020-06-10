'''Challenge 1 - Implement a list representation of a minimum heap
Write a heap class that represents a minimum heap using an array. Implement the insert method for this min heap class.

min_heap = MinHeap()
min_heap.insert(2)
min_heap.insert(4)
min_heap.insert(1)
# Underlying array should look like: [1, 4, 2]
'''
#planing
'''
append the node to the end of the array,
compare the node to the parent to decide if it needs to be switched
'''

class MinHeap:
  def __init__(self, lst=[]):
    self.minHeap = lst

  def __str__(self):
    return str(self.minHeap)
  
  def insert(self, n):
    self.minHeap += [n]
    index = len(self.minHeap) - 1
    parent = (index - 1) // 2
    while index > 0 and self.minHeap[index] < self.minHeap[parent]:
      # swap child and parent
      temp = self.minHeap[parent]
      self.minHeap[parent] = self.minHeap[index]
      self.minHeap[index] = temp

      # resent indices
      index = parent
      parent = (index - 1) // 2
    return self.minHeap

  def delete_min(self):
    self.minHeap[0] = self.minHeap[-1]
    self.minHeap.pop() # does -1 work
    index = 0
    child1 = index * 2 + 1
    child2 = index * 2 + 2
    while (child1 < len(self.minHeap) and self.minHeap[index] > self.minHeap[child1]) or (child2 < len(self.minHeap) and self.minHeap[index] > self.minHeap[child2]):
      if self.minHeap[index] > self.minHeap[child1]:
        # swap child and parent
        temp = self.minHeap[child1]
        self.minHeap[child1] = self.minHeap[index]
        self.minHeap[index] = temp
        index = child1
        child1 = index * 2 + 1
        child2 = index * 2 + 2
      elif self.minHeap[index] > self.minHeap[child2]:
        # swap child and parent
        temp = self.minHeap[child2]
        self.minHeap[child2] = self.minHeap[index]
        self.minHeap[index] = temp
        index = child2
        child1 = index * 2 + 1
        child2 = index * 2 + 2
    return self.minHeap

    

min_heap = MinHeap()
print(min_heap.insert(4))
print(min_heap.insert(3))
print(min_heap.insert(2))
print(min_heap.insert(1))
print(min_heap.delete_min())
print('yay!')