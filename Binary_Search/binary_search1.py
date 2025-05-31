#Find the target element in a sorted array 
'''QUESTION'''
# You are given a target element 'x'. Find 'x' in the given sorted array 'arr', if found print the index of 'x' in 'arr' else print -1.
'''INPUT'''
# The first line of input consists of a 0-indexed and sorted array 'arr'.
# The second line of input consists of the target element 'x'.
'''OUTPUT'''
# Print the index of 'x' if found else print -1.
'''SOULTION'''
def binary_search(arr,x):
  n= len(arr)
  l=0
  r=n-1
  ans=-1
  while l<=r:
    m= (l+r)//2
    if arr[m]==x:
      ans= m
      break 
    elif arr[m]>x:
      r=m-1
    elif arr[m]<x:
      l=m+1
  return ans 
arr= list(map(int,input().split()))
x= int(input())
print(binary_search(arr,x))