#Climbing stairs 
"""QUESTION"""
# You have two choices, either one step or two steps. Find out all possible ways to climb stairs.
'''SOLUTION'''
def helper(curr,n):
  if curr==n:
    return 1 
  if curr>n:
    return 0
  return helper(curr+1,n) + helper(curr+2,n)
def climbing_stairs(n):
  return helper(0,n)
n= int(input())
print(climbing_stairs(n))