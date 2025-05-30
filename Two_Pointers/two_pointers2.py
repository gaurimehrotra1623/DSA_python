#Max Sum Subarray of Size K

'''QUESTION'''
# Given a list of integers A and a number K, find the maximum sum among all subarrays of size K.
# Note:
# A subarray of A is a contiguous part of the array, i.e., the array A[i], A[i+1], ..., A[j] for some 0 ≤ i ≤ j ≤ len(A) - 1.

'''INPUT'''
# Input Format:
# The first line of input contains two integers N and K, denoting the number of elements in the list and the size of the subarray respectively.
# The next line contains N integers denoting the elements of the list.
# Constraints:
# 1 ≤ K ≤ N ≤ 2 * 10^5  
# -2 * 10^5 ≤ A[i] ≤ 2 * 10^5

'''OUTPUT'''
# Print a single integer denoting the maximum sum among all subarrays of size K.

'''SOLUTION'''
def max_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1 
    
    curr_sum = sum(arr[:k]) 
    max_sum = curr_sum
    
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]  
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(max_subarray(arr, k))
