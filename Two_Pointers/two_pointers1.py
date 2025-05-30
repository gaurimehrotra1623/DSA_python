# Minimum Size Subarray Sum K

'''QUESTION'''
# You are given an array arr of size n, and an integer k. You have to find the minimum length of a subarray of arr with sum greater than or equal to k.
# Note: A subarray of an array is defined as a sequence of consecutive elements of an array.

'''INPUT'''
# User Task
# This is a function problem. You don't have to take any input. You are required to complete the function minSubArray() which takes an array arr  and integer k as parameters.

# Custom Input
# The first line will take two space-separated integers representing n and k.
# The second line will take n space-separated integers representing elements of the nums array.

# Constraints:
# 1 ≤ n ≤ 105
# 1 ≤ arr[i] ≤ 105
# 1 ≤ k ≤ 109

'''OUTPUT'''
# Return a single integer representing the minimum length of subarray of arr with sum greater than or equal to k If no such subarray exist return 0.

'''SOLUTION'''
def minSubArray(arr, k):
    n= len(arr)
    left=0
    minn=float('inf')
    curr_sum=0
    for i in range(n):
        curr_sum+=arr[i]
        while curr_sum>=k:
            minn= min(minn, i-left+1)
            curr_sum-=arr[left]
            left+=1
    return minn

n, target= map(int,input().split())
arr= list(map(int,input().split()))
print(minSubArray(arr,target))


 