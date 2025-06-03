#House of robbers 
'''QUESTION'''
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''INPUT'''
# User Task:
# Since this will be a functional problem, you don't have to take input. You just have to complete the function rob(nums) that takes one parameter nums array and returns the answer.

# Custom Input:
# First line contains a single integer n- number of houses.
# Second line contains n space-separated integers representing money in houses.

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 400
'''OUTPUT'''
# Return a single integer the maximum amount of money you can rob tonight without alerting the police.
'''SOLUTION'''
def robFrom(nums,i):
  if i>=len(nums):
    return 0
  rob_it= nums[i]+robFrom(nums,i+2)
  skip_it= robFrom(nums, i+1)
  return max(rob_it, skip_it)

def rob(nums):
  return robFrom(nums,0)

nums= list(map(int,input().split()))
print(rob(nums))
