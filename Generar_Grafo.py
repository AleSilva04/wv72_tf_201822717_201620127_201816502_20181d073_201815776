def add(G, u, n, i, j):
  if i < 0 or i >= len(G) or j < 0 or j >= len(G):
    return
  v = i * n + j
  G[u].append(v)

def generateGridGraph(n):
  G = [[] for _ in range(n**2)]
  for i in range(n):
    for j in range(n):
      u = i * n + j
      add(G, u, n, i, j - 1)
      add(G, u, n, i, j + 1)
      add(G, u, n, i - 1, j)
      add(G, u, n, i + 1, j)

  return G
