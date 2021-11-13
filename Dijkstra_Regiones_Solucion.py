from LeerCsv import leer_archivo
from Generar_Grafo import add,generateGridGraph
from Dijkstra import dijkstra
from Funciones_Agrupar import dist,limites

G = generateGridGraph(1000)

almacen = leer_archivo("dataset/warehouses.csv")
entrega = leer_archivo("dataset/delivery-points.csv")

#Nodos de todos los almacenes
almacenes = []
for x,y in almacen:
  almacenes.append(y*1000+x)

#Nodos de todos los puntos de entrega
ptsEntrega = []

for x,y in entrega:
  ptsEntrega.append(y*1000 +x)
  
  
#Le asignamos un almacen a cada uno de los 5000 puntos de entrega
group =[-1]*5000
for i in range(5000):
  m=0
  d=dist(entrega[i],almacen[0])
  for j in range(1,100):
    d2 = dist(entrega[i],almacen[j])
    if d2 < d:
      d=d2
      m = j
  group[i]=m
  

#Agrupamos todos los nodos en su correspondiente grupo  
groupNodes = [[] for _ in range(100)]
for i in range(5000):
  g = group[i]
  groupNodes[g].append(ptsEntrega[i])

#Dividimos el Grafo General en subgrafos o regiones donde en cada una estan un almacen y sus respectivos puntos de entrega asignados
regions = [[]for _ in range(100)]
for i in range(100):
  g = groupNodes[i]
  g.append(almacenes[i])
  limits = limites1(g)
  for y in range(limits[0],limits[1]+1):
    for x in range(limits[2],limits[3]+1):
      regions[i].append(y*1000+x)
      
      
#Aplicamos dijkstra para cada region desde su respectivo almacen
paths_costs=[([],[]) for _ in range(100)]
for i in range(100):
  g=groupNodes[i]
  g.append(almacenes[i])
  path, cost = dijkstra(regions[i],g,G,almacenes[i])
  paths_costs[i]=(path,cost)

#Imprimos el camino y los costos para cada Region  
for i,path_cost in enumerate(paths_costs):
  print(f"Region {i}:")
  print(f"Path: {path_cost[0]}")
  print(f"Cost: {path_cost[1]}")
