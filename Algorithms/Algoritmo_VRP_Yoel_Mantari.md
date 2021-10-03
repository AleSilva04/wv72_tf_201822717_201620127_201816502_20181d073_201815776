#**Restricciones**


1.   Cada vehiculo tiene un limite de abastecer 5 puntos de entrega
2.   Todos los vehiculos son iguales y tienen una misma velocidad
3.   No hay un tiempo de entrega




---

##Primero


1.   Agregamos cada las distancia entre los punto a una matriz de adyacencia llamada "M"  #........................ n^2
2.   guardamos el punto de partida llamado "nodo_actual" #……………………………  1
3.   agregamos todos los puntos menos el de partida
 a una lista llamada **"Puntos_actuales"** #…………………………… n-1

##Segundo

1.   Mientras la lista "Puntos _actuales" no esta vacia se ejecutara:#…………… n
2.  Permutamos la lista **"Puntos_actuales"**{#…………………………… !(n-1)
3.   Recorremos los puntos obtenidos de lista **"Puntos_actuales"** hasta el numero de abastecimiento del carro  #…………………………… n-1{
3. ingresamos los datos de la list **"Puntos_actuales"**  en la Matriz "M", y obtenemos la distancia recorrida lo guardamos en "Dist_actual" #…………………………… 1
4. actualizamos el valor de "nodo_actual" con su vertice adyacente #……………… 1 }
5. si el numero de abastecimiento de un carro es que el tamaño de la lista de **"Puntos_actuales"** entonces: #{…………………………… 1
6. Creamos una lista llamada **"min_trayectoria"** que guarde como primer parametro la distancia actual "Dist_actual" y como segundo parametro una lista con los 5 primeros puntos de la lista**"Puntos_actuales"** }………………… 1

7. caso contrario:
se guarde los puntos restantes en y su Dist_actual en al lista **"min_trayectoria"** ………………… 1

```
//ejemplo
Puntos_actuales=[1,2,3,4,5,6,7,8,9,10,11,12]
Dist_actual=22 ... //primeros 5 puntos
min_trayectoria=[(22,[1,2,3,4,5])]
```
9. fin de la permutacion si realiza todas las permutaciones de la lista **"Puntos_actuales"** ………………… }
```
//ejemplo
Puntos_actuales=[4,2,3,5,6,9,8,7,1,10,11,12]
Dist_actual=19 ... //primeros 5 puntos
min_trayectoria=[(22,[1,2,3,4,5]), ........ , (19,[4,2,3,5,6])]
```
10. obtenemos el menor valor de la lista **"min_trayectoria"** y lo guardamos en **trayectoria_optima"** ………………… 1

11. eliminamos los puntos visitados de **"Puntos_actuales"** segun los puntos obtenidos en **trayectoria_optima"**………………… 1
```
//ejemplo
Puntos_actuales=[4,2,3,5,6,9,8,7,1,11,12,10]
trayectoria_optima=[(15,[3,5,9,7,2])]
Puntos_actuales=[4,6,8,1,11,12,10]
```
12. Crear lista **trayectoria_definitiva"** e insertar **trayectoria_optima"**………………… 1
13. fin de la ejecucion de Lista **"Puntos_actuales"** si  queda vacia
14. retornar **trayectoria_definitiva"**………………… 1

##Tercero
1. cada vehiculo se le asignara la trayectoria definida por lista **trayectoria_definitiva"**, hasta el final ………………… n/5

```
//ejemplo
trayectoria_definitiva=[(15,[3,5,9,7,2]),(18,[1,12,10,4,8],(8,[6,11])]
carro 1=[3,5,9,7,2]
carro 2=[1,12,10,4,8]
carro 3=[6,11]
```
#Analisis Asintotico
##parte 1
n^2+1+n-1	= n^2+n=O(n^2)
##parte 2
n{!(n-1)[(n-1)(1+1)+1+1]+1+1+1}=   n*!(n-1)[2(n-1)+3]=O(!n)
##parte 3
n/5=O(n)
##Analisis Asintotico Final  
O(!n)




