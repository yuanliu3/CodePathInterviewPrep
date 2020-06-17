'''Suppose you are at a party with n people (labeled from 0 to n - 1) and among 
them, there may exist one celebrity. The definition of a celebrity is that 
all the other n - 1 people know him/her but he/she does not know any of them.

Goal: You want to find out who the celebrity is or verify that there is not one.
Output: The number associated with the celebrity, or -1 if no celebrity present.

The only thing you are allowed to do is to ask questions like: 
    "Hi, A. Do you know B?" to get information of whether A knows B. 
    
You need to find the celebrity (or verify there is not one) by asking as few 
questions as possible (in the asymptotic sense).

You are given a helper function knows(a, b)-->bool which tells you whether 
A knows B. 

Implement a function findCelebrity(n)-->int, your function should minimize the 
number of calls to knows(a, b).

Case 1:
Input: 5
   0  1  2  3  4
0 |0  0  1  0. 0
1 |0  0  1  0  0
2 |0  0  0  0  0
3 |0  0  1  0  0
4 |0  0  1  0  0

Output: 2

Case 2:
Input: 5
   0  1  2  3  4
0 |0  0  0  0  1
1 |0  0  0  1  0
2 |0  1  0  0  0
3 |0  0  0  0  0
4 |1  0  0  1  0

Output: -1

Match:
2 Dictionaries, 
out_degree[2: connection]++
in_degree[2: connection]++

n - 1 knows, and he knows 0

Possible plan:
Have a stack of potential celebrities; it starts out with everyone
[1, 2, 3, 4]
Pop 1 and 2 off the stack
know(1, 2) ->
if 1 knows 2, then add 2 back
if 1 doesn't know 2, add 1 back

If there are two people left and they both know each other, there's no celebrity
If there's one person left, he/she is a celebrity


Another possible plan
candidate k
scan to find the potential celeb
k = know(i, k)? k, i
'''

def celebrity_stack(mat):
  stack = [i for i in range(len(mat))] # store potential celebs
  # set up initial stack
  while (len(stack) > 2):
    print(stack)
    comparison = stack[0:2]
    stack = stack[2:]
    secondWorks = know(comparison[0], comparison[1])
    if secondWorks:
      stack = [comparison[1]] + stack
    else:
      stack = [comparison[0]] + stack
  
  if len(stack) == 0:
    return -1
  if len(stack) == 2 and know(stack[0], stack[1]) and know(stack[1], stack[0]):
    return -1
  return stack[0]

mat1 = [
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0]
]

def know(a, b, mat = mat1):
  return mat[a][b] == 1

print(celebrity_stack(mat1))
 
def findCeleb(n):
  k = 0
  # during this iteration, if any k is not valid, it will be switched to the next possible i, then the remaining i will be the potential valid one
  for i in range(n):
    if not know(i, k):
      k = i
  find = True
  # then verify the potential one by iterating through the list
  for i in range(n):
    if i!=k and not know(i, k):
      find = False
  if find:
    return k
  else:
    return -1

print(findCeleb(5))
