import heapq
def dijkstra(n, src, edges):
  adj = [[] for i in range(n)]
  for s,d,w in edges:
    adj[s].append((d,w))
    adj[d].append((s,w))
  dist = [float('inf')]*n 
  dist[src] = 0 
  heap = [(0,src)]
  while heap:
    d, node = heapq.heappop(heap)
    for nei, weight in adj[node]:
      if d + weight < dist[nei]:
        dist[nei] = d+weight 
        heapq.heappush(heap, (dist[nei], nei))
  return dist

# Example usage:
n = 4
edges = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 3, 3)]
src = 0
print(dijkstra(n, src, edges))