from LeerCsv import leer_archivo
from Generar_Grafo import add,generateGridGraph
from Dijkstra import dijkstra

G = generateGridGraph(1000)

almacen = leer_archivo("dataset/warehouses.csv")
entrega = leer_archivo("dataset/delivery-points.csv")

almacenes = []
for x,y in almacen:
  almacenes.append(y*1000+x)

ptsEntrega = []

for x,y in entrega:
  ptsEntrega.append(y*1000 +x)

reg= [i for i in range(1000000)]
for i in range(100):
  g=ptsEntrega
  g.append(almacenes[i])
  path,cost = dijkstra(reg,g,G,almacenes[i])
