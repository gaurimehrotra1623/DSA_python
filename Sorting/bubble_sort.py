#Implementing Bubble Sort
'''QUESTION'''
# Given a sequence of size N containing positive integers. You need to print the elements of sequence in increasing order using Bubble sort.
'''INPUT AND OUTPUT'''
# User Task:
# This is a function problem. You don't have to take any input. You are required to complete the function bubbleSort() that takes an array seq as parameter.

# Custom Input
# The first line of the input denotes the number of test cases 'T'.
# The first line of the test case is the size of the array.
# The second line of the test case consists of array elements.

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 1000
# 1 ≤ A[i] ≤ 1000

# Sum of N over all test cases doesn't exceed 5000.

# Return sorted list.
'''SOLUTION'''
def bubbleSort(seq):
    n= len(seq)
    for i in range(n-1):
        for j in range(n-i-1):
            if seq[j]> seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq
arr= list(map(int,input().split()))
print(bubbleSort(arr))
