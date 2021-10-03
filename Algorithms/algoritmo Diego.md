 Topic | Descripction
 -|-
  Autor | Diego Rosado Iporre
  Técnica Principal | Binary space partitioning Tree
  
  Después de analizar el Travelling salesman problem que utiliza el algoritmo TSP para encontrar el camino más corto. En este problema, no podemos repetir ese mismo método debido a que no es solo
  un auto el que tiene que recorrer todos los puntos de entrega, sino son muchos vehículos y por muchas rutas, ya que hay muchos puntos de distribución. 
  <br>
  Por otro lado, creo que este algoritmo serviría ya que como entendí sirve para separar en polígonos algún grafico, y como lo que tenemos que graficar al terminar son rutas por cada vehículo y por cada punto de distribución, creo que sería de mucha ayuda utilizar este algortimo comprendiéndolo más.
  
  El VRP se encarga del servicio de una compañía de entrega, un depósito y un conjunto dado de vehículos, los cuales se mueven en una red de carretera dada, para entregar los productos a un conjunto de clientes. 
  <br>Cuando trabajamos con solo un punto de distribución o depósito. Se determina un conjunto de rutas, S, (una ruta para cada vehículo que inicia y termina en el depósito) tal que todas las demandas de los clientes son satisfechas y el coste de la transportación total está minimizado. 
  <br>Y este costo de transportación será calculado con el tiempo y distancia de cada arco que conecta a cada puntos de entrega. 
  <br>En la red de carretera se utilizará un grafo donde los arcos son las carreteras y los vértices representan la localización de los puntos de entrega y puntos de distribución. Cada arco tiene un coste asociado según la distancia y tiempo.
  
  **En este problema de VRP lo que buscaremos será minimizar el coste total del transporte basado en la distancia total recorrida con los vehículos utilizados.**
  
  Solo que para este caso, no trabajaremos solo con uno, sino con muchos puntos de distribución.
  
  Para empezar a resolver este problema se tiene que definir las variables del problema:
  Variable | Descripction
  -|-
  Clientes | Conjunto de clientes
  PuntosD | Conjunto de los puntos de distribución
  PuntosE o nodos | Conjunto de nodos que son los puntos de entrega
  Arcos | Conjunto de los arcos que conecta a cada nodo
  Cij | Distancia entre nodo i y nodo j que será medida en km y cada km se recorre en 1h
  
  Ahora a definir los restricciones del problema: 
  - Cada nodo solo podrá visitar 1 nodo siguiente.
  - A su vez, cada nodo solo puede ser visitado por 1 nodo anterior.
  - Cada nodo tendrá su carga. 
  
  Acerca del código: *Para un ejemplo de 10 clientes*
  
  Primero tendremos que crear una cantidad random que será la carga a entregar. O(n)
  <br>
  Q = {i:rnd.randint(1,10) for i in clientes
  
  Luego creamos la posición inicial o punto de distribución. O(n)
  <br>
  PuntosE = [0] + clientes
  
  Después se crearían las coordenadas x e y para cada punto de entrega o nodo. O(n)
  <br>
  CoorX = rnd.rand(len(PuntosE))
  CoorX = rnd.rand(len(PuntosE))
  
  Se crea las coordenadas para el punto inicial o puntoD: 
  <br>
  for i in clientes:<br>
           CoordX[0], CoordY[0]
    
  Luego se generan los arcos que unirán a cada nodo:
  <br>
  arcos={(i,j) for i in PuntosE for j in PuntosE if i!=j}
  
  Ahora se calculan las distancias de los arcos entre cada nodo: <br>
  distancia={(i,j):np.hypot(loc_x[i]-loc_x[j],loc_y[i]-loc_y[j]) <br>
           for i in PuntosE for j in PuntosE if i!=j}
           
  Luego haríamos la gráfica del problema con la ubicación de cada nodo. 
  
  Lo que seguiria a continuacion sería crear las funciones con las que trabajará el modelo y podrá calcular el menor costo para el transporte. O(n^2)
  
  minimize(mdl.sum(distancia[i,j]*x[i,j] for i,j in arcos))
  
  add_constraints((sum(arcos[i, j] for j in PuntosE if j != i) == 1 for i in clientes)
  <br>
  add_constraints((sum(arcos[i, j] for i in PuntosE if i != j) == 1 for j in clientes)
  <br>*De esta manera se agregan las restricciones del problema*
  <br>
  <br>
  Y bueno con estos datos se podría comparar cual es la menor distancia entre cada nodo y unirla. Y tambien se podria realizar el camino desde el punto de distribución 
  hacia cada punto de entrega. Lo siguiente sería graficar las distancias entre cada nodo y el recorrido o ruta que tendría cada vehículo. 
  
  Acerca del análisis asintótico. 
  
  En la parte de variables es O(n).
  <br>
  En la parte de definir las funciones es O(n^2)
  <br>
  En la parte final de graficar sería O(n!)
  
  El análisis asintótico final sería O(n!). Como se puede ver resulta con una alta complejidad, pero se puede ir trabajando y mejorando analizando más a profunidad el algoritmo
  y con los nuevos aprendizajes que tengamos.

  
  
 
  
  

  
  
 
