
import heapq as hq
import math
def dijkstra(M,Pts, G, s):
  visited = {node:False for node in M}
  visitedPts = []
  path = {node:None for node in M}
  cost = {node:math.inf for node in M}
  cost[s] = 0
  queue = [(0, s)]
  while queue:
    if len(visitedPts) == len(Pts):
      break
    g_u, u = hq.heappop(queue)
    if visited[u] is False:
      visited[u] = True
      if u in Pts:
        visitedPts.append(1)
      for v in G[u]:
        if v not in M:
          continue
        f = g_u + 1
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  return path, cost
