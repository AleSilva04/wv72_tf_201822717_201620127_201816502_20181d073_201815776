**INTEGRANTES:**
* Ronaldo David Cornejo Valencia
* Alejandro Silva Chocano
* Yoel Gonzalo Mantari Sairitupac

**CURSO:** complejidad Algorítmica
**SECCIÓN:** WV72

**INTRODUCCIÓN**

El problema de enrutamiento de vehículos (VRP) se centra en encontrar el conjunto óptimo de rutas para una flota 
de vehículos que debe satisfacer las demandas de un conjunto de clientes, esto considerando minimizar el costo de 
operación y tiempo de distribución. Además, aquel problema ha sido estudiado por diferentes autores, generalmente 
por especialistas en las áreas de investigación de Operación y Logística. Esto se debe a que la gestión logística 
se ha convertido en uno de los factores prioritarios en una empresa, puesto que, gracias a ello, se puede determinar 
el fracaso o éxito en la comercialización de algún producto. Por ello, las decisiones de enrutamiento se han vuelto 
un factor muy importante para diferenciarse en el desempeño con empresas rivales y ayudaría a garantizar un lugar 
relevante en el mercado.

**MARCO TEÓRICO**

El problema VRP tiene diferentes variantes:

* VRP con múltiples puntos de distribución: Los vehículos que componen la flota son de diferentes puntos de distribución.
* VRP con flota heterogénea: Los vehículos que componen la flota son diferentes entre sí.
* VRP con rutas abiertas: Los vehículos no vuelven al punto de iniciación de rutas.
* VRP con ventanas de tiempo: Los pedidos tienen que ser entregados dentro de un rango horario predefinido.
* VRP con Pick up and delivery: Los vehículos, como parte de su ruta, tienen que pasar a los centros de abastecimiento para obtener los paquetes a ser distribuidos.

![image](https://user-images.githubusercontent.com/66271146/143674967-45ea312c-25de-418d-9252-a81babdd3cc3.png)

**Grafo:** Un grafo es un modelo para representar relaciones entre elementos de un conjunto. Gráficamente se representa como 
un conjunto de vértices o nodos unidos por líneas que representan las aristas.

![image](https://user-images.githubusercontent.com/66271146/143675000-1f96c724-0386-41b9-8c47-2180bf41917f.png)

**Algoritmo de Dijkstra:** es un algoritmo para la determinación del camino más corto, dado un vértice origen, hacia el resto 
de los vértices en un grafo que tiene pesos en cada arista.

![image](https://user-images.githubusercontent.com/66271146/143675017-4a6bdf5e-0db8-4f8d-b03a-ad483a01c4e1.png)

**CONTEXTO DEL TRABAJO**

En este trabajo, nos estamos ubicando en una ciudad rectangular donde todas las calles son horizontales o verticales. Esta ciudad 
está representada por un grafo de un millón de nodos, en donde cada nodo representa las intersecciones entre calles, y cada uno de 
estos está conectado nomás con sus nodos de arriba, abajo, derecha e izquierda.

Estamos considerando que nuestro problema de enrutamiento de vehículos tiene unos 100 almacenes o puntos de distribución de donde 
van a partir los vehículos, y 5000 puntos de entrega a donde los vehículos tienen que llegar hasta haber cumplido con todas las entregas. 
Cada almacén cuenta con una cantidad ilimitada de vehículos a su disposición y la distancia entre nodo y nodo se considera como 1 km.

**ESPACIO DE BÚSQUEDA DE VRP**

La primera dificultad que vimos al analizar el Vehicle Routing Problem fue el gran espacio de búsqueda que tiene. Estamos hablando de una 
cantidad de almacenes n y cada uno de esos almacenes puede recorrer cualquier camino e ir hacia cualquier punto de entrega. Por ende, nuestro 
primer objetivo fue simplificar dicho espacio de búsqueda. 

La forma en que decidimos simplificar el problema fue dividiéndolo en pequeños subgrafos, para que por cada subgrafo haya un almacén encargado 
de los puntos de entrega dentro del mismo. Esto simplifica bastante el problema, porque ahora pasamos a tener un espacio de búsqueda por cada 
almacén mucho menor del que teníamos anteriormente, antes era todo el grafo que en nuestro sería un grafo de un millón nodos, ahora cada almacén 
solo se encargaria de un subgrafo mucho menor de unos miles de nodos.
