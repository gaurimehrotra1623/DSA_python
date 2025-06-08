#Print all subsequences equal to target 

'''QUESTION'''
# You are given an integer array arr of size n and a target integer target. Your task is to find and Return all the subsets of arr such that the sum of the elements in each subset is equal to target.

'''INPUT AND OUTPUT'''
# Custom Input
# The first line contains an integer representing n and k
# The next line contains n space-separated integers as input representing the nums.
# The third line contains an integer representing target
# Constraints:
# 1 ≤ n ≤ 20
# 1 ≤ arr[i] ≤ 100
# 1 ≤ sum ≤ 105
# Return a list of lists, where each inner list represents a subset whose sum equals the target. The subsets must be listed in the order they appear in the array. Each subset should maintain the sequence of elements as in the original array.
# Note: Return an empty list, if there is no subset with sum of elements equal to the target.

'''SOLUTION'''
def print_subsequence(arr,target):
  def helper(i, curr):
    if sum(curr)==target:
      print(*curr)
      return 
    if i==len(arr):
      return 
    helper(i+1, curr + [arr[i]])
    helper(i+1, curr)
  helper(0,[])
arr = list(map(int,input().split()))
target = int(input())
print_subsequence(arr,target)
    



