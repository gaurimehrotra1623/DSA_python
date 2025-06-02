#Recursive sum 
'''QUESTION'''
# Find the sum of all numbers upto 'n' recursively.
'''SOLUTION'''
def recursive_sum(n):
  if n==1:
    return 1
  return n + recursive_sum(n-1)
n= int(input())
print(recursive_sum(n))
