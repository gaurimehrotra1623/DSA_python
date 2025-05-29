#Minimum Value to Get Positive Step by Step Sum
'''QUESTION'''
# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

'''INPUT'''
# User Task
# This is a function problem. You don't have to take any input. You are required to complete the function minStartValue() which takes an array nums as parameter.

# Custom Input
# The first line contains a single integer n, representing the size of array nums.
# The second line will take n space-separated integers representing elements of the nums array.

# Constraints:
# 1 ≤ n ≤ 105
# -103 ≤ nums[i] ≤ 103

'''OUTPUT'''
# Return a single integer representing the minimum positive value of startValue such that the step by step sum is never less than 1.

'''SOLUTION'''
def minStartValue(arr):
  minn=0
  curr_sum=0
  for num in arr:
    curr_sum+=num 
    if curr_sum<minn:
      minn= curr_sum
  return max(1,1-minn)
n= int(input())
arr= list(map(int,input().split()))
print(minStartValue(arr))