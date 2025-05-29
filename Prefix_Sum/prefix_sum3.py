#Find The Highest Altitude
'''QUESTION'''

# There is a biker going on a road trip. The road trip consists of n+1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i+1 for all 0 <= i < n. Return the highest altitude of a point.

'''INPUT'''

# User Task
# This is a function problem. You don't have to take any input. You are required to complete the function largestAltitude() which takes an array gain as parameters.

# Custom Input
# The first line will take an integer representing n.
# The second line will take n space-separated integers representing elements of the gain array.

# Constraints:
# 1 ≤ n ≤ 100
# -100 ≤ nums[i] ≤ 100

'''OUTPUT'''
# Return the highest altitude of a point.

'''SOLUTION'''
def largestAltitude(gain):
    summ=0
    m=0
    for i in gain:
        summ+=i
        m= max(m,summ)
    return m
n= int(input())
gain= list(map(int,input().split()))
print(largestAltitude(gain))


