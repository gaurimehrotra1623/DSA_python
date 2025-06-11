#Generate Binary strings 
'''QUESTION'''
# Given a positive integer N. The task is to print all the binary strings of length N in ascending order.

# Note: A binary string contains only 0 and 1.
'''INPUT AND OUTPUT'''
# Input
# The first and only line of input contains a single integer N, representing the length of the binary string.

# Constraints
# 1 <= N <= 15
# Output
# Print all the binary strings of length N in ascending order.
'''SOLUTION'''
def generate_binary(n, curr=""):
  if len(curr)== n:
    print(curr)
    return 
  generate_binary(n, curr + "0")
  generate_binary(n, curr + "1")
n= int(input())
generate_binary(n, curr= "")
