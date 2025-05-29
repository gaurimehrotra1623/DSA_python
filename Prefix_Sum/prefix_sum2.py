#Prefix Removals
'''QUESTION'''
# You are given a string s consisting of lowercase letters of the English alphabet. You must perform the following algorithm on s: 

# Let x be the length of the longest prefix of s which occurs somewhere else in s as a contiguous substring (the other occurrence may also intersect the prefix). If x=0, break. Otherwise, remove the first characters of s,and repeat.

# A prefix is a string consisting of several first letters of a given string, without any reorders. An empty prefix is also a valid prefix. For example, the string "abcd" has 5 prefixes: empty string, "a", "ab", "abc" and "abcd".

# For instance, if we perform the algorithm on s = "abcabdc",

# Initially, "ab" is the longest prefix that also appears somewhere else as a substring in s, so s = "cabdc" after 1 operation.
# Then, "c" is the longest prefix that also appears somewhere else as a substring in s, sos = "abdc" after 2 operations.
# Now x=0 (because there are no non-empty prefixes of "abdc" that also appear somewhere else as a substring s), so the algorithm terminates.

# Find the final state of the string after performing the algorithm.

'''INPUT'''
# The first line of the input contains a single integer t.

# This is followed by t lines, each containing a description of one test case. Each line contains a string s. The given strings consist only of lowercase letters of the English alphabet and have lengths between 
# 1 to 2*10^5 inclusive.

# It is guaranteed that the sum of lengths of s over all test cases does not exceed 
# 2*10^5.

'''OUTPUT'''
# For each test case, print a single line containing the string s after executing the algorithm. It can be shown that such string is non-empty.

'''SOULTION'''

cases = int(input())
for i in range(cases):
    s = input()
    s1 = ''
    for i in range(1,len(s)+1):
        s1+=s[-i]
        if set(s)==set(s1):
            print(s1[::-1])
            break
  

