#Max element
'''QUESTION'''
# Find out the max number in the given array using recursion.
'''SOLUTION'''
def max_number(arr,i=0):
  if i==len(arr)-1:
    return arr[i]
  return max(arr[i] , max_number(arr, i+1))
arr= list(map(int,input().split()))
print(max_number(arr))
  