# Algoritmo Silva Chocano

 Topic | Descripction
 -|-
  Autor | Alejandro Silva Chocano
  Técnica Principal | Fuerza Bruta
  
  
Primero tenemos un punto de distribución el cual se va a encargar de los nodos de una zona del mapa hasta ciertos 
límites y así con cada punto de distribución para que se pueda llega a todos los nodos. 

Por cada punto de distribución van a salir una cantidad de carros proporcional a la cantidad de puntos de 
entrega a los que tiene que llegar. Esto lo hacemos viendo el recorrido acumulado de cada uno de los vehículos, 
al asegurarnos que el vehículo no llegue hasta cierto limite de distancia en la ida. En caso si lo supere, 
tendría que salir otro vehículo para poder encargarse de los demás nodos. Esto lo haríamos con un algoritmo 
que recorra la lista de adyacencia para poder ver nuestro recorrido y a la vez ir sumando la distancia recorrida 
y poder determinar si necesita otro vehículo. Analizando este algoritmo apropiadamente podría tener un tiempo 
logarítmico.

Al final del algoritmo final haría que cada punto de distribución se haya encargado de sus puntos de entrega adyacentes, 
con la menor cantidad de vehículos en dentro de un rango de tiempo y distancia adecuado.
