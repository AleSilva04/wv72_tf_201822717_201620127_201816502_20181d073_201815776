from LeerCsv import leer_archivo
from Generar_Grafo import add,generateGridGraph
from Dijkstra import dijkstra
from Funciones_Agrupar import dist,limites

#Esta funcion halla el camino que se tiene que hacer para ir desde un nodo a otro desde una lista de adyacencia
def hallarCamino(u,v,G):
  camino=[]
  yu = int(u/1000)
  xu = u - yu*1000
  yv = int(v/1000)
  xv = v - yv*1000
  if yu<yv:
    if xu>xv:
      while xu>xv:
        camino.append(yu*1000+xu-1)
        xu-=1
      while yu< yv:
        camino.append((yu+1)*1000+xu)
        yu+=1
    else:
      while yu< yv:
        camino.append((yu+1)*1000+xu)
        yu+=1
      while xu<xv:
        camino.append(yu*1000+xu+1)
        xu+=1
  else:
    if xu>xv:
      while xu>xv:
        camino.append(yu*1000+xu-1)
        xu-=1
      while yu> yv:
        camino.append((yu-1)*1000+xu)
        yu-=1
    else:
      while yu> yv:
        camino.append((yu-1)*1000+xu)
        yu-=1
      while xu<xv:
        camino.append(yu*1000+xu+1)
        xu+=1

  return camino

#Esta funcion calcula el camino que se tiene que seguir de un nodo a otro dentro de un diccionario que contiene todos los caminos
def camino(s,u,dic):
  path=[]
  path.append(u)
  aux=dic[u]
  path.append(aux)
  while True:
    aux=dic[aux]
    if aux == s:
      break
    path.append(aux)
  return path


#Generamos Grafo de un millon de nodos
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
  groupNodes[i].append(almacenes[i])
  limits = limites1(groupNodes[i])
  for y in range(limits[0],limits[1]+1):
    for x in range(limits[2],limits[3]+1):
      regions[i].append(y*1000+x)




#Aca empieza el algortimo de vrp
vrp = []

#Vamos a calcular que deben de seguir los vehiculos para cada almacen, tomando solo los primeros 24 almacenes
for ind in range(24):
  
  #Primero aplicamos dijkstra desde almacen en el que estemos a todos los puntos de entrega de su region
  g = groupNodes[ind]
  path,_= dijkstra(regions[ind],g,G,almacenes[ind])
  caminos=[]
  paths=[]
  n=len(g)-1
  
  #De ahi calculamos los caminos de nodos que se tienen que seguir para ir desde el almacen hacia cada punto de entrega
  for i in range(n):
    a= camino(almacenes[ind],g[i],path)
    paths.append(a)

    
  #Despues eliminamos los caminos que tengan nodos que ya se estan vistando en otros caminos
  ptsVisitado = [False]*n
  idx=0
  for j,p in enumerate(paths):
    for i in range(n):
      if g[i] in p:
        ptsVisitado[i]=True
    idx=j
    if ptsVisitado.count(False)==0:
      break
  aux=n-1
  while aux>idx:
    paths.pop(len(paths)-1)
    aux-=1

    
  #Luego unimos caminos en pares sin repetir hasta unir todos, si tiene un numero de caminos impar el ultimo camino considera el regreso como el mismo camino de ida
  agregado = [False]*len(paths)
  for j,p in enumerate(paths):
    if agregado.count(False) ==1:
      c = paths[0].copy()
      c.reverse()
      c.pop(len(c)-1)
      cam = paths[0]+c
      caminos.append(cam)
      break
    if agregado.count(False) == 0:
      break
    if agregado[j] is True:
      continue
    d = 1000000
    y1 = int(p[0]/1000)
    x1 = p[0] - y1*1000
    m = 0
    #Calculamos el mejor par de caminos que se pueden ir dentro de los caminos que todavia no hemos agregado, consideramos mejor como que sus ultimos nodos son las cercanos
    #para asi a la hora de unirlos el recorrido agregado sea el menor posible
    for i in range(len(paths)):
      if p == paths[i]:
        continue
      if agregado[i] is True:
        continue
      node = paths[i][0]
      y2 = int(node/1000)
      x2 = node -y2*1000
      auxd = dist((x1,y1),(x2,y2))
      if auxd < d:
        d = auxd
        m = i
        
    #Calculamos el camino extra que se debe de hacer para unir los caminos
    c = hallarCamino(p[0],paths[m][0],G)
    
    #unimos los 3 caminos, el par de caminos y el camino extra para la union
    cam = p.copy() + c.copy() + paths[m].copy()
    agregado[j]=True
    agregado[m]=True
    caminos.append(cam)
  
  #Agregamos todos los caminos finales
  vrp.append(caminos)
  

#Finalmente imprimimos por cada almacen, la cantidad de vehiculos que se necesita, los caminos que debe de hacer y los kms por cada camino
for i,cams in enumerate(vrp):
  print(f"Almacen {i}:")
  print(f"Vehiculos: {len(cams)}")
  print("Caminos:")
  for p in paths:
    print(p)
    print(f"Kms del camino: {len(p)+2}")
  print("\n")
