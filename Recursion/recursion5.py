#Frog jump-1
'''QUESTION'''
# There are N buildings, numbered 1, 2, 3, …, N. For each building i (1 ≤ i ≤ N), the height of building i is given by heights[i].

# A frog is initially on the roof of Building 1, and he wants to reach Building N.

# The frog can jump from one building to another, but there are some rules:

# If the frog is currently on Building i, he can jump to either building i+1 or building i+2.

# The energy used by the frog for a jump from building i to building j is
# |heights[i] - heights[j]|

# Your task is to compute the minimum total energy the frog needs to reach Building N.
'''INPUT'''
# User Task:
# Since this will be a functional problem, you don't have to input anything. You just have to complete the function frogJump() that takes heights as parameter.

# Custom Input:
# First line contains a single integer n- number of stairs in the staircase.
# Second line contains n integers representing heights array.

# Constraints:
# 1 ≤ heights. length ≤ 25
# 1 ≤ heights[i] ≤ 1000
'''OUTPUT'''
# Return the minimum total energy used by the frog to reach from '1st' stair to 'Nth' stair.
'''SOLUTION'''
def jump(heights, i):
    if i==0:
        return 0
    elif i==1:
        return abs(heights[1]-heights[0])
    else:
        one_step= abs(heights[i-1]-heights[i])+ jump(heights,i-1)
        two_step= abs(heights[i-2]-heights[i])+ jump(heights,i-2)
        return min(one_step,two_step)


def frogJump(heights):
    n= len(heights)
    return jump(heights,n-1)

nums= list(map(int,input().split()))
print(frogJump(nums))

