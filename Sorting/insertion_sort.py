#Implementing insertion sort 

'''QUESTION'''
# Given a sequence of size N, containing positive integers. You need to sort the elements of sequence using Insertion sort algorithm.

'''INPUT AND OUTPUT'''
# User Task
# This is a function problem. You don't have to take any input. You are required to complete the function insertion_sort() that takes an array seq as parameter.

# Custom Input
# The first line of the input denotes the number of test cases 'T'.
# The first line of the test case is the size of the array.
# The second line of the test case consists of array elements.

# Constraints
# 1 <= T <= 100
# 1 <= N <= 10^3
# 1 <= A[i] <= 10^3

# Sum of N over all test cases won't exceed 5 * 10^3

#Return Sorted list.

'''SOLUTION'''
def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        bucket = seq[i]  
        j = i - 1
        while j >= 0 and seq[j] > bucket:  
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = bucket  
    return seq
seq= list(map(int,input().split()))
print(insertion_sort(seq))
