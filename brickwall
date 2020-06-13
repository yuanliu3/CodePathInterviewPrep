'''There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

 

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2
U: See example
M: Hash map (mapping positions to the number of "gaps" it crosses through)
P: Go one row at a time, and at all of the gaps, set key : value as position: # of edges it goes through
Example: After going through the first row, we'd have: {1: 1, 3: 1, 5: 1}
After the second row, we'd have: {1: 1, 3: 2, 4: 1, 5: 1}
After the third row, we'd have: {1: 2, 3: 2, 4: 2, 5: 1}
After the fourth row, we'd have: {1: 2, 2: 1, 3: 2, 4: 2, 5: 1}
After the fifth row, we'd have: {1: 2, 2: 1, 3: 1, 4: 3, 5: 1}
After the sixth row, we'd have: {1: 3, 2: 1, 3: 1, 4: 4, 5: 2}

Final calculation: maximum value is 4, so then output 6-4 = 2
'''

def leastBricks(wall) -> int:
  count_dict, max_freq = {}, 0

  for i in range(0, len(wall)):
    pos_sum = 0
    for j in range(0, len(wall[i]) - 1):
      pos_sum += wall[i][j]
      
      if pos_sum not in count_dict:
        count_dict[pos_sum] = 1
      else:
        count_dict[pos_sum] += 1
      max_freq = max(count_dict[pos_sum], max_freq)

  return len(wall) - max_freq

# Time: O(N) where N is the number of bricks
  
# Test case
wall1 = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]
print(leastBricks(wall1))

wall2 = [[1, 2, 3],
        [1, 3, 2],
        [4, 1, 1]  
        ]
print(leastBricks(wall2))

wall3 = [[1], [1], [1]]
print(leastBricks(wall3))


wall4 =  [[3],
        [1, 1, 1],
        [2, 1]
        ]
print(leastBricks(wall4))
# Output: 1

wall5 = [[3], [3], [3]]
print(leastBricks(wall5))
# Output: 3
