#Running Sum of 1D Array
'''QUESTION'''
# You have been given an array nums of integers. Your task is to calculate the running sum of this array. The running sum for an index i can be defined as:
# runningSum[i] = (a[0] + a[1] + ... + a[i])
'''INPUT'''
# User Task
# This is a function problem. You don't have to take any input. You are required to complete the function runningSum() which takes an array nums as parameters.
# Custom Input
# The first line will take an integer representing n.
# The second line will take n space-separated integers representing elements of the nums array.
# Constraints:
# 1 ≤ n ≤ 2 * 103
# -106 ≤ nums[i] ≤ 106
'''OUTPUT'''
# Return an array containing the running sum of nums
'''SOLUTION'''
def runningSum(arr):
  n= len(arr)
  prefix_arr=[0]*n
  prefix_arr[0]= arr[0]
  for i in range(0,n):
    prefix_arr[i]= prefix_arr[i-1]+ arr[i]
  return prefix_arr
n= int(input())
arr= list(map(int,input().split()))
print(*runningSum(arr))

