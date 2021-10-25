import numpy as np
def crear_grafo(datos):
  n = len(datos)
  G = [[None]*n]*n
  G = np.array(G)

  for f in range(n):
    for c in range(f+1,n):
      x1,y1 = datos[c][0],datos[c][1]
      x2,y2 = datos[f][0],datos[f][1]
      d = ( ((x1-x2)**2) + ((y1-y2)**2) )**(0.5)
      G[f,c] = d
      G[c,f] = d
  return G
