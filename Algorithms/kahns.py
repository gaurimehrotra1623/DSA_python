#--PROBLEM STATEMENT--#
#------------------------------------------#
# You are given a directed graph with n vertices. Determine a valid topological ordering of all vertices, or report that no such ordering exists.
#------------------------------------------#
#--SOLUTION--#
from collections import deque 
def kahns(n,edges):
  adj = [[] for i in range(n)]
  ind = [0]*n
  ans = []
  for s,d in edges:
    adj[s].append(d)
    ind[d] += 1
  q = deque()
  for i in range(n):
    if ind[i] == 0:
      q.append(i)
  while q:
    node = q.popleft()
    ans.append(node)
    for nei in adj[node]:
      ind[nei] -=1 
      if ind[nei] == 0:
        q.append(nei)
  return ans 
#------------------------------------------#
#--EXAMPLE--#
n = 4
edges = [(1,0), (2,0), (3,1), (3,2)]
print(kahns(n, edges))
#------------------------------------------#
