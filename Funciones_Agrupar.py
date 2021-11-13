def dist(a,b):
  x1,y1=a
  x2,y2=b
  return abs(x1-x2) + abs(y1-y2)


def limites(group):
  node = group[0]
  levely = int(node/1000)
  levelx = node-levely*1000
  minX = levelx
  minY = levely
  maxX = levelx
  maxY = levely
  
  for n in group:
    levely = int(n/1000)
    levelx = n-levely*1000
    if levely>maxY:
      maxY=levely
    if levely<minY:
      minY=levely
    if levelx>maxX:
      maxX=levelx
    if levelx<minX:
      minX=levelx 

  return [minY,maxY,minX,maxX]
