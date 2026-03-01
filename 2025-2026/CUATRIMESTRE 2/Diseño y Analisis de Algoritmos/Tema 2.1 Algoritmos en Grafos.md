# 0. Definiciones
- Se suele definir un grafo G = (V,E) como un *conjunto de vértices V y aristas E* ∈ V x V
- Normalmente, la complejidad de los algoritmos sobre grafos suele medirse en función del:
	- Número de vértices  → |V| = n
	- Número de aristas  → |E| = m
 ![[Tema 2.1 Algoritmos en Grafos(iconoGrafo).png]]
## Grafo No Dirigido
![[Tema 2.1 Algoritmos en Grafos(GrafoNoDirigido).png]]
## Grafo Dirigido
![[Tema 2.1 Algoritmos en Grafos(grafoDirigido).png]]
# 1. Representaciones
## Matriz de adyacencia
- Asegura acceso rápido a la hora de comprobar si hay una arista entre dos vértices.
- Requiere memoria de 0(V<sup>2</sup>) y no depende de la densidad del grafo
- Permite comprobar adyacencia en tiempo constante
- No depende del número de aristas, por lo que es <u>adecuada para grafos densos</u>
![[Tema 2.1 Algoritmos en Grafos(matrizAdyacencia).png|550]]
### Implementación:
**Costos**:
- *Espacio* → O(V<sup>2</sup>)
- Agregar vértice → O(V<sup>2</sup>)
- Agregar arista → O(1)
- Ver si son adyacentes → O(1)
- Obtener vecinos → O(V<sup>2</sup>)
## Lista de adyacencia
- Representación compacta para<u> grafos dispersos (pocas aristas)</u>($|E| \ll|V|^2$).
- No aseguran acceso rápido a la hora de comprobar si hay una arista entre dos vértices.
![[Tema 2.1 Algoritmos en Grafos(listaAdyacencia).png|600]]
### Implementaciones:
**Lista de listas**: Para grafos no muy densos que den listas cortas.
 ![[Tema 2.1 Algoritmos en Grafos(costesListaDeListas).png|550]]
**Diccionario de listas**: parecido a lista de listas. (Misma complejidad menos acceso al vértice → O(1) promedio)
**Diccionario de diccionarios**: si es muy denso o no se sabe, conviene:
- *Espacio*, igual O(V+E).
	- n listas (una por vértice)
	- En total se almacenan E aristas
	- En no dirigido se almacenan 2E, pero sigue siendo O(V+E).
- Agregar vértice → Aunque quieras verificar si se repite O(1).
- Agregar arista → O(1).
- Ver si los vértices son adyacentes → O(1).
- Obtener los adyacentes de un vértice →O(grado(V))
- Encontrar la lista en diccionario → O(1), copiarla O(V)

## Cuando usarlas:
| Tipo de grafo                            | Mejor representación |
| ---------------------------------------- | -------------------- |
| Muy disperso                             | Lista de adyacencia  |
| Muy denso                                | Matriz de adyacencia |
| Necesito comprobar adyacencia muy rápido | Matriz o sets        |
| Necesito iterar vecinos rápido           | Lista                |

# 2. Recorridos
## Recorrido en profundidad (DFS):
El **depth-first search** profundiza en el grafo siempre que sea posible.
- Dado un vértice antes de visitar a su hermano, visita su hijo (Equivalente a un recorrido preorden).
- Suele implementarse de forma recursiva.
- Se incluye un conjunto verticesVisitados para evitar ciclos de búsqueda.
	![[Tema 2.1 Algoritmos en Grafos(recorridoProfundidad).png|521]]
### Pseudocódigo y características:
**DFS** 
- **Recursividad**(rp llama a rp):
	![[Tema 2.1 Algoritmos en Grafos(pseudocodigoDFS1).png]]
- *Complejidad*:
	- Cada vértice se visita una única vez → n
	- Llamadas al procedimiento recursivo → O(n)
	- El algoritmo examina todas las aristas → O(m)
	- Complejidad global del algoritmo → O(max(n,m))
- *¿Para qué sirve?*
	- El recorrido en profundidad de un grafo conexo G crea un *árbol de recubrimiento* T
		- Las aristas de T son un subconjunto de aristas de G
		- La *raíz* de T es el punto de partida de la exploración de F
	- Si el grafo no es conexo, se obtiene un árbol por cada *componente conexa* → bosque
	- La exploración en profundidad de un grafo visita todos los nodos del grafo en preorden
	- Se emplea en utilidades concretas (debido a la información sobre la estructura que aporta el DFS) en algoritmos más avanzados *Algunos al final del tema(Puntos de articulación...).
    - Para muchos algoritmos es indiferente BFS y DFS.
- *Implementación* **Iterativa**(con pila): \* "Dpila"
 ![[Tema 2.1 Algoritmos en Grafos(DFSIterativo).png|354]]
## Recorrido en anchura (BFS):
El **breath-first search**(bfs) recorre la frontera en anchura
- Visita todos los vertices a una *distancia k* antes de descubrir el primer vértice a la distancia k+1
- Suele implementarse de forma *iterativa* utilizando una *cola* de vértices visitados para evitar *ciclos* y establecer el *orden* de la búsqueda.
 ![[Tema 2.1 Algoritmos en Grafos(recorridoBFS).png|561]]
### Pseudocódigo y características:
**BFS**
- **Iterativo** (ra no llama a ra): (COLA no pila como DFS) \*"B cola"
	![[Tema 2.1 Algoritmos en Grafos(pseudocodigoBFS1).png|487]]
	![[Tema 2.1 Algoritmos en Grafos(pseudocodigoBFS2).png|491]]
- *Complejidad*:
	- El *tiempo requerido* para realizar un recorrido en anchura de un grafo es el mismo que para un recorrido en profundidad → O(max(n,m))
- *¿Para qué sirve?*
	- También genera *árboles de recubrimiento*, si el grafo es conexo, solo uno
	- Permite encontrar el *camino más corto* entre dos puntos en grafos *no ponderados*, hacer exploraciones parciales, etc...
![[Tema 2.1 Algoritmos en Grafos(recorridoEnAnchura).png|612]]

# 3. Algoritmos Sobre Grafos
## Ordenación topológica:
Ordenamiento no comparativo, no se tiene un orden total (a<b<c), se tiene un orden parcial (a<b, c<b, no tenemos relación entre a y c (a,c,b / c,a,b ) → Los dos serían ordenes válidos (Orden de vestirse)).
Dado un grafo dirigido y acíclico, se denomina ordenación topológica a una disposición lineal de los nodos tal que, dado un arco (u,v), el nodo u esté antes que v en la ordenación.
- Un vértice se visita solo si se han visitado sus predecesores
- En caso de los grafos cíclicos, el algoritmo sigue siendo válido, pero la interpretación no es directa
*Aplicaciones teóricas*:
- Tareas a realizar (algunas antes que otras).
- Makefile: algunas cosas se compilan antes que otras.
- Plan de estudios: hay materias que tienen que hacerse unas antes que otras.
- Fases de un proyecto (PERT).
**Técnica**:
Usando un recorrido DFS con muy poca modificación. (va recorriendo hasta que llega a un final, por ejemplo taller 1 en el grafo de arriba y lo mete en una pila, asegurando que salga el último)
- Se realiza un recorrido en profundidad "coloreando" los nodos.
- Inicialmente los todos nodos son blancos
- Cuando se visitan, se colorean de gris
- Cuando toda la adyacencia se ha visitado, se colorea de negro
	- En este punto se almacena en una lista
	- La ordenación topológica no es única
**Pseudocódigo**:
![[Tema 2.1 Algoritmos en Grafos(ordenacionTopologicaPseudocodigo).png|428]]
![[Tema 2.1 Algoritmos en Grafos(procesoOrdenacionTopologicaDFS).png|532]]
****
El algoritmo anterior tiene el problema de no garantizar determinismo
- Misma entrada → Misma salida
Lo habitual es establecer un orden entre las tareas que pueden realizarse en el mismo momento del tiempo
- Orden lexicográfico
**Implementación alternativa**:
Similar a recorrido BFS (basado en los grados de entrada de cada uno de los vértices(cuantas aristas le llegan)). ==// No estoy seguro de esto==
- Basada en contar aristas incidentes a cada nodo para ver cuándo pueden comenzar a realizar sus tareas
- Primero se realizan las tareas con 0 aristas incidentes
- A continuación actualizamos el valor para cada vértice y continuamos
![[Tema 2.1 Algoritmos en Grafos(ordenacionTopologicaBFS).png]]
# 4. Conectividad
Un *grafo conexo* es un grafo no dirigido donde existe un camino entre cualquier par de nodos. Un *grafo fuertemente conexo* es un grafo dirigido donde existe un camino entre cualquier par de nodos, considerando la dirección de las aristas.
Para descomponer un grafo G en sus componentes fuertemente conexas:
- Aplicar ordenación topológica sobre G
- Calcular grafo traspuesto G<sup>T</sup> *(Invertir el sentido de los arcos)*
- Aplicar DFS sobre G<sup>T</sup> iniciando en los nodos de mayor a menor tiempo de finalización de la ordenación topológica
- El resultado es un bosque donde cada árbol es una componente fuertemente conexa
# 5. Otros Algoritmos
- **Puntos de articulación**: un vértice v de un grafo conexo es un punto de articulación si el subgrafo que se obtiene al eliminarlo (junto con sus aristas) no es conexo.
- **Grado biconexo**(o no articulado): grafo sin puntos de articulación. En una red de comunicaciones, asegura su funcionamiento incluso si falla un dispositivo.
- **Grafo bicoherente**(o 2-arista conexo): sus puntos de articulación están unidos a cada componente del subgrafo restante por, al menos, dos aristas. En una red de comunicaciones, asegura su funcionamiento incluso si falla una línea de transmisión.
# 6. Cálculo de Puntos de Articulación
Se basa en un recorrido DFS, pero almacenando dos nuevos valores:
- *Tiempo de descubrimiento*:  momento en el que el nodo fue visitado por primara vez durante el DFS
- *Valor de low*:  tiempo de descubrimiento más bajo alcanzable desde un nodo a través del subárbol de DFS con raíz en ese nodo y, como mucho, una arista de retorno
Un vértice u será punto de articulación si cumple al menos una de las dos siguientes condiciones:
1. Si u es la raíz del árbol DFS, debe tener dos o más hijos en el árbol DFS
2. Para cualquier otro nodo, si tiene un hijo v tal que low\[v] ≥ disc\[u]
	- Esto implica que el subgrafo con raíz en v no tiene una arista de retorno hacia un ancestro directo de u, por lo que eliminar u desconectaría todo el subgrafo de v del resto del grafo
****
Sea V cualquier vértice del árbol (excepto la raíz) y X un hijo de V:
- Si masAlto\[X] < preOrden\[V] implica que se puede llegar desde x a regiones más altas sin pasar por (V,U). Entonces U no es un punto de articulación. (con mis palabras: Si alguno de sus hijos, a través de sus hijos puede llegar a un nodo más alto, sin pasar por la arista del padre(él) al primer hijo, no es punto de articulación(los puentes con líneas intermitentes valen como camino de subida))
- Si preOrden\[X] ≥ masAlto\[V] no se puede llegar desde U a regiones más altas del grafo sin pasar por (V,U). Entonces U es un punto de articulación.
- Si U es la raíz del árbol y tiene más de un hijo, es un punto de articulación, si no, no.
- En el ejemplo posterior los puntos de articulación son 1 y 4, el 1 en el árbol del recorrido es la raíz del árbol y tiene 2 hijos, por lo que es **punto de articulación**, además, alguno(en este caso ninguno) de los hijos de 4 (7 en este caso), puede llegar a un nivel más alto que 4, por lo que 4 es **punto de articulación**.  (creo que en el ejemplo de abajo, los números que están a la derecha están mal en el nodo 4,7 y 8, ya que ese numero no es 6, es 4, el nodo mas alto alcanzable?)
****
![[Tema 2.1 Algoritmos en Grafos(calculoPuntosArticulacion).png]]
**Pseudocódigo**(con DFS):
![[Tema 2.1 Algoritmos en Grafos(puntosArticulacionPseudocodigo).png]]
*Aplicaciones*:
- Comprobar que un grado es bipartito.
- Detectar ciclos en grafos.
- Camino más largo en un DAG.
- Determinar si dos nodos están conectados o no.
- Caminos y ciclos eulerianos.
- Cierre transitivo.
- Caminos entre un origen y un destino con K aristas.