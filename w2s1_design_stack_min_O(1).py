'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. These are the operations you should implement for this data structure.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
get_min() -- Retrieve the minimum element in the stack.
Example input:

min_stack = new MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
min_stack.get_min()   # Returns -3.
min_stack.pop()
min_stack.top()       # Returns 0.
min_stack.get_min()   # Returns -2.

[1]
[5 ,1]
[2, 5 ,1] minEle = 1
stack = [-7, 2, 5, 1] minEle = -3 
stack = [1, 5, 2, -3] 
stack = [1, 5, 2] minStack = [1]
stack = [1, 5] minStack = [1]

stack = [1] minStack = [1]
stack = [1, 2] minStack = [1]
stack = [1, 2, 1] minStack = [1, 1]


minElement = 1
minLement = -3
Alternate solution: 
Push(x): if( x< minele)
  2*x - minele 
  minele = x

Pop()
  if(y >= minele)
  else
  minele = 2*minele - y
'''
class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []
  
  def push(self, value):
    self.stack.append(value)
    if not self.min_stack or value <= self.min_stack[-1]:
      self.min_stack.append(value)
  
  def pop(self):
    if self.stack[-1] == self.min_stack[-1]:
      self.min_stack.pop()
    return self.stack.pop()
  
  def top(self):
    return self.stack[-1]
  
  def get_min(self):
    return self.min_stack[-1]

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())   # Returns -3.
print(min_stack.pop())
print(min_stack.top())     # Returns 0.
print(min_stack.get_min())
print("well done everyone!")

'''Test 2'''
testStack = MinStack();
testStack.push(3)
print(testStack.get_min())
testStack.push(5)
print(testStack.get_min())
testStack.push(2)
print(testStack.get_min())
testStack.push(1)
print(testStack.get_min())
testStack.push(1)
print(testStack.get_min())
testStack.push(-1)
print(testStack.get_min())
print(testStack.pop())
print(testStack.get_min())
print(testStack.pop())
print(testStack.get_min())
print(testStack.pop())
print(testStack.get_min())
print(testStack.pop())
print(testStack.get_min())
print(testStack.pop())
print(testStack.get_min())


