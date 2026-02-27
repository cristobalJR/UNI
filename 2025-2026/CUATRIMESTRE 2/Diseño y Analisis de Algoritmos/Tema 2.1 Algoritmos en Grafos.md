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
## Recorrido en profundidad: