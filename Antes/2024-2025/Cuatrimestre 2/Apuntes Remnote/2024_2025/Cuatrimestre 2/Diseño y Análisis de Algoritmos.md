- Indice DAA
    - #  _**Fechas relevantes:**_  
    - ## Exámenes: 
        1. Prueba resolución de problemas(10%) (min:2/10) -  #[[Semana 7/8]] 
        2. Prueba resolución de problemas(60%) (min:5/10) - Convocatoria Ordinaria
    - ## Prácticas:
        1. Varias entregas a lo largo del cuatrimestre (30%) (min:4/10)
    - 
    - #  _**Profesorado:**_  
    - ### Abraham Duarte Muñoz
    - **Despacho: **109 Departamental II
    - **Email**: abraham.duarte@urjc.es
    - **Tutorías**: solicitar por el bloque de correo
    - ### Jesús Sánchez-Oro Calvo
    - **Despacho: **115 Departamental II
    - **Email**: jesus.sanchezoro@urjc.es
    - **Tutorías**: solicitar por el bloque de correo
    - ### Alejandra Casado Ceballos
        - **Despacho: **117 Departamental II
        - **Email**: alejandra.casado@urjc.es
        - **Tutorías**: solicitar por el bloque de correo
        - 
    - #  _**Índice:**_  
    - ## Modulo I
    - [Tema 0: Introducción a Python.](T0.-Introducción%20a%20Python.md) 
    - [Tema 1: Planteamiento general](T1.-Planteamiento%20General.md) 
        - [Tema 1.1: Eficiencia algorítmica ](T1.1-Eficiencia%20Algorítmica.md) 
    - [Tema 2: Algoritmos en grafos.](T2.-Algoritmos%20en%20Grafos.md) 
    - [Tema 3: Algoritmos Voraces.](T3.-Algoritmos%20Voraces.md) 
        - [Tema 3.1: Algoritmos Voraces sobre grafos.](T3.1-Algoritmos%20Voraces%20sobre%20Grafos.md) 
    - --------------------- Portal ---------------------
        - 
    - 
- T0.-Introducción a Python 
- T1.-Planteamiento General 
- T1.1-Eficiencia Algorítmica 
    - 
- T2.-Algoritmos en Grafos 
    - # Definiciones
        - Se suele definir un grafo G=(V,E) como un conjunto de vertices V y de aristas $E \subseteq V \times V$.
        - Usualmente la complejidad de los algoritmos sobre grafos suele medirse en función del número de vértices |V|=n y el número de aristas |E|=m.
        - Existen dos representaciones típicas de grafos:
            - ### Lista de adyacencia:
                - Representación compacta para grafos dispersos (pocas aristas)($|E| \ll|V|^2$).
                - No aseguran un acceso rápido a la hora de comprobar si hay una arista entre 2 vértices dados.
                - **Implementaciones: **
                    - Lista de listas: Para grafos no muy densos que den listas cortas.
                    - Diccionario de listas: Parecido a lista de listas.
                    - Diccionario de Diccionarios: Si es muy denso o no se sabe, conviene.
                        - Espacio, igual O(V+E).
                        - Agregar vértice -> Aunque quieras verificar si se repite O(1)
                        - Agregar arista -> O(1)
                        - Ver si dos vértices son adyacentes -> O(1)
                        - Obtener los adyacentes de un vértice -> O(V) * [Encontrar la lista en diccionario O(1), copiarla O(V)]*  
                - **Costos:** 
                    - Espacio: -> O(V+E) * [Generalmente bastante menos espacio]*  
                    - Agregar vértice -> O(1)   *[O(V) Si queremos verificar que no está repetido en la lista]*   *[menos O() que en Matriz Ady.]*  
                    - Agregar arista -> O(V)
                    - Ver si dos vértices son adyacentes -> O(V)
                    - Obtener los adyacentes de un vértice -> O(V)
            - ### Matriz de adyacencia: 
                - Aseguran un acceso rápido a la hora de comprobar si hay una arista entre dos vértices dados
                - Se requiere una memoria de $O(V^2)$, y no depende de la densidad del grafo
                - Para grafos densos $|E| \cong |V|^2$
                - **Costos:**
                    - Espacio -> O(V^2^)
                    - Agregar vértice -> O(V^2^)
                    - Agregar arista -> 0(1)  *[Mucho menos O() que Lista Ady.]*  
                    - Ver si dos vértices son adyacentes -> O(1)  *[Mucho menos O() que Lista Ady.]*  
                    - Obtener los adyacentes de un vértice -> O(V)
                    - 
    - # Recorrido en profundidad
        - El depth-first search(dfs) profundiza en el grafo siempre que sea posible
        - Dado un vértice antes de visitar su hermano, visita su hijo (Equivalente a un recorrido preorden).
        - Suele implementarse de forma recursiva
        - Se incluye el conjunto verticesVisitados para evitar ciclos en la búsqueda.
        - ### Pseudocódigo:
            - 
                - 
                    - DFS Recursividad (rp llama a rp):
                    - ![](https://remnote-user-data.s3.amazonaws.com/pLaez664cP4P-QaWTYKOOqu2wEtoazA3CHxxK0CP_osIS7DbHWFZCeFMrDgR3kyfObSSV89UrkUYpHTNgfzwQezAK5RG-RkJHp7uF18OBxui7mvPRONV26n43P-f2VqE.png)
                    - ![](https://remnote-user-data.s3.amazonaws.com/rOSw7VYZCImAwo7iyUsgFHCJrbubD4WabUzgBmvr3M5sn8EMSakqdCbOuSFQSnYt5U89NVP12TgsfLQx2dT3q4ehAGgn7tBg0Jh7W3Kc_DSGo7cZIK2WtJ4s8hMrnlBO.png)
                - 
                    - DFS 
                    - Iterativo (con pila)  *[DPila]*  
                    - ![](https://remnote-user-data.s3.amazonaws.com/JOGgmNKPSJ-CxO44H4r8ZB84V7aqdBO6rb2xNVpv5cfqOCW-6XVAViOBiniBkP7aPMWTSUY4dBIaONujiD3QOrtBNS4-LrPC8VS9krV3yWoTUK2o9-Am7U3aTZlb1FE5.png)
                    - 
        - .
            ```
            def dfs_standard(graph, start_node):
    visited = set()
    result = []
    
    def dfs_recursive(node):
        # Marcar como visitado
        visited.add(node)
        # Procesar el nodo ahora
        result.append(node)
        
        # Explorar vecinos
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        # No hay procesamiento aquí
    
    dfs_recursive(start_node)
    return result
            ```
        - Complejidad global del algoritmo es: $O(max(V,E))$. Cada vértice se visita una vez O(V) y el algoritmo examina todas las aristas O(E).
        - El DFS de un grafo conexo G crea un árbol de recubrimiento T:
            - Las aristas de T son un subconjunto de las de G.
            - La raíz de T es el punto de partida de la exploración de G.
        - ![](https://remnote-user-data.s3.amazonaws.com/qSPTv7m_moqheQjXA9ufrRnH3W4SiLw-UH5IVdojWEdPEW1IZht2I0Yn8i7dy1FziDZGpEjMGrpNNTvA_JLpmvWM_Ib8ty240w-9OPklmYPFnjkRrdlH2LcA8MPjAge0.png)->![](https://remnote-user-data.s3.amazonaws.com/eHe2KA7T304d2eaJwcXnPOoQHegM3zRz4GJkzHfAw5s6Y-Y_gbqgLEbJkNRO8_O_0Zi1UClFPcfGd2RjJElT7nujqAqkzLSvzteoRZVP63c5xGve9pL296DZbfiN4qSN.png) 
        - Si el grafo no es conexo se obtiene un grafo por cada componente conexa (bosque).
            -  *Ejemplo de con grafo dirigido(distingue entre adyacentes e incidentes) no conexo:*  
                - ![](https://remnote-user-data.s3.amazonaws.com/jvNfPVLGxf6F1aTohm_gpoz384XaNkc_8ljVCZ-ut-7ehc-BJWNlxrpKN1CwizwHuW5fPJOwwRr5ol8QVTinsS_2Um-Qy2ncUAMoUEP47ltHwcNi5uZAkuBDOsgoZ0O8.png)->![](https://remnote-user-data.s3.amazonaws.com/MibyeH5bCReWpo1n-Vkkhd1Ojq9w6_xy4UfjQUU0MvE5DhMVQ0BlOusutTQKqeRuYZXrVhgPDsaxDjqP5rmNQkJk__T-7HKZ10QvT5rQVI_L68DT8VO4-dunOHMDQnKs.png)
        - Se emplea en utilidades concretas (debido a la información sobre la estructura que aporta el DFS) en algoritmos más avanzados *^Algunos al final del tema^(Puntos de articulación...).
        - Para muchos algoritmos es indiferente BFS y DFS.
    - 
    - # Recorrido en Anchura
        - El breath-first search(dfs) recorre la frontera en anchura.
        - Visita todos los vértices a una distancia k antes de descubrir el primer vértice a la distancia k+1.
        - Suele implementarse de forma iterativa.
        - Se tiene que incluir una cola con los vértices visitados para evitar ciclos y establecer el orden de la búsqueda.
        - Dado un grafo G=(V,E) y un vértice inicial S:
            - Calcula la distancia (menor número de vértices) desde S, hasta los vértices alcanzables.
            - Produce un árbol de recorrido en anchura donde la raíz es S.
            - Para cualquier V alcanzable desde S, la ruta en el árbol de recorrido de anchura de S a V es el camino más corto entre esos dos vértices.
            - Adecuado para dirigidos y no dirigidos. 
            - ### Pseudocódigo:
                - BFS Iterativo (ra no llama a ra): (COLA no pila como DFS) 
                - ![](https://remnote-user-data.s3.amazonaws.com/NRSfUddLc5Qo90FwcZ3I3lB8P4yQqzNEYs3K7CDxu9utJS_jqIhJuvUnbcS9iHmzimGPQ4pzFL3aKeyxQY9qOPpRpLI8iWDnYcqbZEqO0qDKgeTfGqNLXEDjnKZCmdmP.png)
                - ![](https://remnote-user-data.s3.amazonaws.com/i_hr7_Mc5Nlw729VipmifA4L8XwlrCHkEUOza9j6rAf6eD1yauDvLXPQ-1n6V_mSEDl9d9de1tfjzc8Mtm9GeZUVIcbjBktcuMyc2vYjsw4-Y2TLwCOwb8CMowXrZdVr.png)
            - 
                - 
                - 
        - Complejidad = BFS -> $O(max(V,E))$
        - También genera árboles de recubrimiento. Si el grafo es conexo, solo uno.
        - Se emplea en exploraciones parciales de grafos, para hallar el camino más corto entre dos puntos de un grafo, etc...
        - Ejemplo recorrido en anchura:
            - ![](https://remnote-user-data.s3.amazonaws.com/mg1sU6bka5H6wEtOD3ftWrimlTWt2KM5IJLecVgAskWtkWdIaYVmrPNUDCA0Qncc0X_90zZDmcgeMAn5AKy6smDg2mGZrNudj_AYNdbP2mGSo02NSR5kHeeKCGMoazkY.png)
            - ![](https://remnote-user-data.s3.amazonaws.com/nOJc55iVSMrDLqwEkm6QDAOt-XVr0pIg0Q1jW3-fqgfz8U7JsYRAAu9W0mIUrUQW0NgIxoA72Cw0vBKkWwntDs_hp5gvkq7zxUUWGEUgxcn-qMeS2D2GFFMOzbPxiQGA.png)
    - 
    - # Algoritmos sobre grafos y Ordenación Topológica
        - ## Ordenación Topológica (Una de las aplicaciones de BFS/DFS):
            - Ordenamiento no comparativo, no se tiene orden total (a<b<c) se tiene un orden parcial (a<b, c<b, no tenemos relación entre a y c (a,c,b / c,a,b) -> Los dos serían ordenes válidos (Orden de vestirse)). 
                - Aplicaciones teóricas:
                    - Tareas a realizar (algunas antes que otras).
                    - Makefile: algunas cosas se compilan antes que otras.
                    - Plan de estudios: Hay materias que deben hacerse antes que otras.
                    - ...
            - Opciones:
                - Similar a recorrido BFS (basado en los grados de entrada de cada uno de los vértices(cuantas aristas le llegan)).
                - ![](https://remnote-user-data.s3.amazonaws.com/dCJgL6w_l1OUJoUwGQzZUSRC4t5TCGxo_c7Ihl6FO8pMtcZixe3H_mN7U25IDg36kt4RiF8T3df4ZN1C0xxPnAby26oojm9S0Ar61uVz2MeZWR43oynsOcbq9vEU7mUa.png)
                - Usando un recorrido DFS con muy poca modificación. (va recorriendo hasta que llega a un final, por ejemplo taller 1 en el grafo de arriba y lo mete en una pila, asegurando que salga el último * [puede empezar desde cualquier nodo]* ) *. * Si prefieres profundizar antes de meterte en otras cosas usa este (ej: Ver el universo Marvel acabando primero las de Spiderman que no tengan la condición de verse después que otra). 
                    - .
                        ```
                        #topsort recursive DFS
def topological_sort(graph):
    visited = set()
    result = []
    
    def dfs_topo(node):
        # Marcar como visitado
        visited.add(node)
        # No hay procesamiento aquí
        
        # Explorar vecinos
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_topo(neighbor)
        
        # Procesar el nodo en backtracking
        result.append(node)
    
    # Iniciar desde cada nodo no visitado
    for node in graph:
        if node not in visited:
            dfs_topo(node)
    
    # Invertir el resultado para obtener la ordenación
    return result[::-1]
                        ```
            - Dado un grafo dirigido y acíclico, se denomina ordenación topológica a una disposición lineal de los nodos tal que, dado un arco (u,v), el nodo u esté antes que v en la ordenación.
                - Un vértice se visita sí y solo sí se han visitado todos sus predecesores.
                - En caso de grafos con ciclos, el algoritmo sigue siendo válido, pero la interpretación no es directa.
            - Aplicaciones prácticas:
                - Fases de un proyecto (PERT).
                - Evaluación de atributos en la fase semántica de un compilador.
            - Ejemplo con recorrido en profundidad. Distancia y finalización.
                - ![](https://remnote-user-data.s3.amazonaws.com/NBGIzEmGVLYLqgX2yA9jyVY3Pe1BC6byJfY56dPpnNxkLTJ4lnuOUNLp3ppYx54jEZZttQ12pnWjnZRQrUGnoVUoR6VcwCSc4-0_E_FN9ewnnRxl1Yw9di76FTyJC7Uq.png) ![](https://remnote-user-data.s3.amazonaws.com/KNbAwlh3VD-ktTp0729unsjprP2vEaw9Eow9DG3E6SpXs1KKh5cmUZlLS_59eeQiUfhJwbPvFihQr8o_uPXf6jY3qlc-P-8hKbvYnzI-BwmzoKB7Knn-gaZgDmxmXvto.png)
                - ![](https://remnote-user-data.s3.amazonaws.com/MjlVSXJhT3E0cg73_1VGoRltjJXR9pi5_Is2QMc1ksQhoikAkK6GjmpL9tux_FjhM0o73siwLKhMMV86oPMCS2t2S89yHBJ824IrjfjfPxHHhn4YDt2BuzK5Zo_ireBr.png)
        - ## Algoritmos sobre grafos  *(Términos, procedimientos,...)* :
            - Un **grafo conexo** es un grafo no dirigido donde existe un camino entre cualquier par de nodos. Un **grafo fuertemente conexo** es un grafo dirigido donde existe un camino entre cualquier par de nodos, considerando la dirección de las aristas  s.
            - 
            - 
            - ara descomponer un grafo G en sus componentes fuertemente conexas:
                - Aplicar la ordenación topológica sobre G.
                - Calcular el grafo traspuesto G^T^  *(Invertir el sentido de los arcos)* .
                - Aplicar DFS sobre G^T^ iniciando la búsqueda en los nodos de mayor a menor tiempo de finalización obtenidos en la primera ejecución de búsqueda en profundidad.
                - El resultado será un bosque de árboles. Cada árbol es una componente fuertemente conexa.
            - **Puntos de articulación: **Un vértice V de un grafo conexo es un punto de articulación si el subgrafo que se obtiene al eliminarlo (Junto con sus aristas) no es conexo.
            - **Grafo biconexo****(o no articulado)**: aquél grafo que no tiene puntos de articulación.
            - **Grafo bicoherente (o 2-arista conexo): **aquél grafo cuyos puntos de articulación están unidos a cada componente del subgrafo restante por, al menos, dos aristas. 
            - Si el grafo representa una red de comunicaciones:
                - Si es **biconexo ** nos asegura el correcto funcionamiento de la red, aunque falle uno de los equipos.
                - Si es **bicoherente **nos asegura el correcto funcionamiento de la red, aunque falle una de las líneas de transmisión. 
            - ### Cálculo de los puntos de articulación g dirigido(Variacion del tarjan  *(tb:Algoritmo puntos articulación g no dirigidos y componentes fuertemente conexas)* DFS):
                - ![](https://remnote-user-data.s3.amazonaws.com/2EuDoKYtFyo3gr5WEfqjam82HpY4-V5tK8VQIM4OkR01vOsShys5CucRH1hZO88rUuZq-YNZwHgGmR_a4ggbGHxP7IzkyVxUZhw6b2gvlwY3-b9bf4OUdXRKj_XSb4RB.png)
                - Sea V cualquier vértice del árbol (excepto la raíz) y X un hijo de V:
                    - Si masAlto[X] < preOrden[V] implica que se puede llegar desde x a regiones más altas sin pasar por (V,U). Entonces U no es un punto de articulación. (con mis palabras: Si alguno de sus hijos, a través de sus hijos puede llegar a un nodo más alto, sin pasar por la arista del padre(él) al primer hijo, no es punto de articulación(los puentes con líneas intermitentes valen como camino de subida))
                    - Si preOrden[X] ≥ masAlto[V] no se puede llegar desde U a regiones más altas del grafo sin pasar por (V,U). Entonces U es un punto de articulación.
                - Si U es la raíz del árbol y tiene más de un hijo, es un punto de articulación, si no, no.
                - *****En el ejemplo anterior los puntos de articulación son 1 y 4, el 1 en el árbol del recorrido es la raíz del árbol y tiene 2 hijos, por lo que es **punto de articulación**, además, alguno(en este caso ninguno) de los hijos de 4 (7 en este caso), puede llegar a un nivel más alto que 4, por lo que 4 es **punto de articulación**. 
                - Ejemplo de pseudo-código con DFS:
                    - ![](https://remnote-user-data.s3.amazonaws.com/mAEhhnKkI0VMwxIdyR9YqVoBjzQAkALknieIA3hZ4S8jR8o4jvN_uBrHDdkMs132szun5SdKgBWmdyXA3oUSsvHvnViGlCrZMorkhISi_Dkodzbx8kCAjVu3_rZ_hMK9.png)
            - Otras aplicaciones interesantes:
                - Comprobar que un grafo es bipartito.
                - Detectar ciclos en grafos.
                - Camino más largo en un DAG.
                - Determinar si dos nodos están conectados o no.
                - Caminos y ciclos eulerianos
                - Cierre transitivo.
                - Caminos entre un origen y un destino con K aristas.
    - 
- T3.-Algoritmos Voraces 
    - Greedy: Voraz, avaricioso, codicioso...
    -  *Dado un problema con n entradas, el objetivo es obtener un subconjuntos de estas, de tal forma que se satisfaga una determinada restricción de forma óptima.* 
    - La forma habitual de resolverlo:
        - Escoger las mejores entradas que verifiquen las restricciones hasta que se encuentra la solución que se busca.
    - Ejemplo:
        - Supongamos un país tiene un monedas con valores v~1~ ,v~2,...,~v~n~ .
        - Descomponer una cantidad dada M, en monedas, de forma que el número de monedas utilizadas sea mínimo.
            - Datos relevantes:
                - **Candidatos:** Monedas C ={v~1~ ,v~2,...,~v~n~}.
                - **Solución:** La suma de las monedas elegidas es igual al cambio. 
                - **Factibilidad:** La suma de monedas no puede superar al cambio. 
                - **Objetivo:** Minimizar las monedas devueltas. 
                - **¿Selección? -> **Moneda de mayor valor mientras sea factible. 
        - ![](https://remnote-user-data.s3.amazonaws.com/fl48WiqhibIfEGUmVlPzNu4hXryvmvv47Cmo5JWLO10RKsHGiEUJGLc60uTQzgWtnSC2FOdY_yuH6pDURIimaHsa83DECvEjpvN1cQO3HMh3pUZ3YG7RREUVOoAAeYdV.png)
    - ## Identificar:
        - Conjunto de **candidatos **y conjunto de **seleccionados**.
        - Función de **selección**: elige el candidato idóneo en cada etapa.
        - Función **solución**: determina si los candidatos seleccionados son una solución.
        - Función de **factibilidad**: determina si el conjunto de seleccionados es prometedor.
        - Función **objetivo:** determina el valor de la solución. 
    - ## Esquema de la técnica:
        - ![](https://remnote-user-data.s3.amazonaws.com/EGh3Cl9KUR6ZZHJxFDFHDIQ_QF2RuohU1-5FBVTh-v2CB-Wrb8vvA8dZCJK5fbHEfu2t9i_WcJoNSLvfcuCLEBqwpNZhskQFBqEIcvM82roN7xqtVnJjpz9Nb2aKbpeT.png)
        - ## Características del esquema:
            - Se construye una solución **iterativamente.**. 
            - Se toma la decisión **óptima **en cada **iteración**.
            - Una vez analizado un candidato (introducir o excluir), **no se reconsidera ** la decisión.
            - Son voraces por que en cada etapa toman **la mejor decisión **sin preocuparse del mañana.
        - ## Ventajas:
            - Implementación sencilla.
            - Soluciones de forma muy eficiente (Complejidad polinómica).
            - Encuentran la solución óptima para un número determinado de problemas.
        - ## Desventajas:
            - No siempre encuentra la óptima (ej: cambio con monedas de 11, 5 y 1).
            - No reconsiderar decisiones pasadas puede conducir a no obtener el óptimo global (ej: problema del viajante).
            - Encontrar la función de selección que garantice la optimalidad.
            - Demostración formal de la optimalidad (encuentra el óptimo global).
    - ## Aplicaciones de los algoritmos voraces:
        - ### Minimización del tiempo en el sistema:
            -  Un servidor tiene que dar servicio a un cliente, el tiempo por cliente t ~i ~es conocido. Se desea minimizar el tiempo medio de cada cliente en el sistema.
                - ![](https://remnote-user-data.s3.amazonaws.com/I_boIgyjZ3nY8U0VflDX2Rea8hWjFsz0nJzxJ3_SD6mKMwlfHK7AVxJ6G0rgbGkiEOOGlOucgl2jUuQ4zS5xfRwNRRTz9lNMz1XQ4Pl-GBTcotYkbW7prUzYzxi09USQ.png) 
                - Como n es conocido, equivale a minimizar el tiempo total invertido por cliente en el sistema.
                - ![](https://remnote-user-data.s3.amazonaws.com/zC7Xv_3fHuEp26GXWwmc_KvlvxAglNPm2H8qdHduOWkfBcbPKs9wucIMyyLPtqRveblbNnCfsbBENfz36nmcBssP45Ej7BmkfZ7PVz9YDzmHhdab794_JYEODu8bQ8Ie.png)
                - Conjunto **candidatos**: **n** clientes. 
                - Función **solución**: todos los clientes han sido ordenados.
                - Función de **factibilidad**: si han sido ordenados los clientes o no.
                - Función **objetivo**: minimizar T.
                - Función de **selección**: Elegir los candidatos por orden creciente de t ~i.~
            - El algoritmo voraz se reduce a ordenar de forma no decreciente en t ~i~ los n clientes.
            - **Pseudocódigo:**
                - [https://remnote-user-data.s3.amazonaws.com/Ij9MRqWYw9iJLouKYZyEKrhrQurFsc6SdMFYIv3mKkHMSritAXy4wijVi_OUtLMp3ktjzfl1wTQOmeu5PF7y8CY6emWTtYnt04P3__eX18_zJMy1YNGhP118ShZ-UuoD.png](../../Uploaded%20Files/Tema3_DAA/Highlights/Page%2015/Untitled.md)
            - 
        - ### Problema de la mochila:
            - Tenemos n objetos y una mochila. Cada objeto i tiene un peso W~i~ > 0 y un valor V~i~ > 0. La mochila puede llevar un peso que no sobrepase W. Se desea llenar la mochila **maximizando** el valor de los objetos transportados.
                - [https://remnote-user-data.s3.amazonaws.com/DZWsqk0yRMcUdLytzLiAo2vqNgy-GAdh7-R7szyJl7NRb--07Ko8-G0WiESYa0bl15Qm-MTjL9pERtB70iIZh_KjdxLxc96VU-g7uazHJGG8HPorjMldfJr4n8Jk_THc.png](../../Uploaded%20Files/Tema%203_%20Algoritmos%20Voraces%20(Dise%C3%B1o%20y%20An%C3%A1lisis%20de%20Algoritmos)/Highlights/Page%2016/Untitled.md)
            - Con las restricciones:
                - [https://remnote-user-data.s3.amazonaws.com/7aPAlsBRJ_wkmoe0PSbRqpAIcrejQXLd0OsDXQ7vyiW7PqgRCuu7cTQBLhcnB_X1DzdGjxPdR_P3QfqU0kd1QTAZ9_Qv2VEoYXxqdIGbTXyuoMpQoOS49H2jopUoJO27.png](../../Uploaded%20Files/Tema%203_%20Algoritmos%20Voraces%20(Dise%C3%B1o%20y%20An%C3%A1lisis%20de%20Algoritmos)/Highlights/Page%2016/Untitled.md)
                - Conjunto **candidatos**: **n** objetos. 
                - Función **solución**: Cuando no puedan añadirse más fracciones de objetos a la mochila.
                - Función de **factibilidad**: [https://remnote-user-data.s3.amazonaws.com/A8entDtsmOsOAvk-702qatsm3k3P60Zjqi-xsM7JOe14fdfBFzzGHQ7z7S-nD97hs3o3jNMtsVyZ3gTtMkmZGpwnFqV7HqnKca1bqAdlVTPR0D9Kec6xKPutJ-AjRnKo.png](../../Uploaded%20Files/Tema%203_%20Algoritmos%20Voraces%20(Dise%C3%B1o%20y%20An%C3%A1lisis%20de%20Algoritmos)/Highlights/Page%2017/Untitled.md)
                - Función **objetivo**: [https://remnote-user-data.s3.amazonaws.com/ZNN2pE91BkJqs7tU2ZGDo3Cw0pAbtXqF-ekL59q0yAFsm-lrV_0pgY9ZbO6Dk7SdDz8utJZsqzm6U697KfImZ4zmzNJVK81LeRSqiF-cgdJsev_RmDCHVlbLlQPmEBki.png](../../Uploaded%20Files/Tema%203_%20Algoritmos%20Voraces%20(Dise%C3%B1o%20y%20An%C3%A1lisis%20de%20Algoritmos)/Highlights/Page%2017/Untitled.md)
                - Función de **selección**: Elegir los candidatos por orden decreciente de V ~i.~
                - Encuentra solución óptima si los objetos se pueden partir.
            - **Pseudocódigo:**
                - [https://remnote-user-data.s3.amazonaws.com/PYe1r4MqnV0lZqGLXHbwNFP9RPgL5rXzvWpON1O3GwQNncZJheaoRLN1M6mIIR7rt9KOcLxW__HI4raTKBMrbDY294Eqm_aJ5fBMHdyFsO9Mu-3EWVd0usvH4QLQ-ls0.png](../../Uploaded%20Files/Tema%203_%20Algoritmos%20Voraces%20(Dise%C3%B1o%20y%20An%C3%A1lisis%20de%20Algoritmos)/Highlights/Page%2019/Untitled.md)
        - ### Planificación con plazo fijo:
            - Tenemos n trabajos, donde cada trabajo i tiene una fecha tope de realización    f ~i~ > 0 y un beneficio b ~i~ > 0.
                - Entonces:
                    - Para cualquier trabajo i, el beneficio b ~i~ se gana si y sólo sí se realiza antes (o coincidiendo) con su fecha tope f ~i.~
                    - El trabajo se realiza en una máquina que consume una unidad de tiempo y sólo hay una máquina disponible(i.e., en un instante de tiempo solo se puede ejecutar una tarea)
                - Conjunto **candidatos**: **n** trabajos a realizar. 
                - Función **solución**: cuando se hayan planificado todas las tareas.
                - Función de **factibilidad**: conjunto T de trabajos que todavía se pueden completar antes de su tope.
                - Función **objetivo**: [https://remnote-user-data.s3.amazonaws.com/_7uVxYu3ayUrUp5PLd7FaqC8Y_WAg3SwWIBtLIPyN8-IbXLhwNUgz385vaDO_p7aUv9iE_EsgRBgL0pIqkFysTnuT7OM5v6DnX0UotVRAcYO7CPDx_iufLY0twDthSht.png](../../Uploaded%20Files/Tema%203_%20Algoritmos%20Voraces%20(Dise%C3%B1o%20y%20An%C3%A1lisis%20de%20Algoritmos)/Highlights/Page%2022/Untitled.md)
                - Función de **selección**: considerar trabajos en orden decreciente de los beneficios~.~ 
        - **([HASTA AQUI EXAMEN PARCIAL 1 Jueves 27/3/2025])** 
        - ## Activity Selection.
        - ### [Problemas en grafos (árboles de recubrimiento y caminos más cortos).](T3.1-Algoritmos%20Voraces%20sobre%20Grafos.md) 
    - 
- T3.1-Algoritmos Voraces sobre Grafos 
    - ## Introducción:
        - Árboles de recubrimiento (expansión/generador) mínimo:
            - Algoritmo de Prim.
            - Algoritmo de Kruskal.
        - Caminos mínimos:
            - Algoritmo de Dijkstra.
        - Heurísticas voraces:
            - Coloreado de grafos.
            - Viajante de comercio.
    - ## Árboles de recubrimiento mínimo:
        - **Problema:**
        - Dado el grafo G = (V,E) no dirigido y ponderado con pesos positivos, calcular el subgrafo conexo [T ⊆ G](../../Uploaded%20Files/Tema3.1_DAA/Highlights/Page%2003/T%20%E2%8A%86%20G.md), que conecte todos los V del G y que la suma de las aristas seleccionadas sea mínima
        - **Solución:**
        - Si el grafo es conexo, el subgrafo resultante es necesariamente un árbol.
        - Estrategias para resolver el problema:
            - Seleccionar la arista **más corta **en cada iteración
                - Algoritmo de Kruskal.
            - Seleccionar un **vértice al azar **y construir el árbol a partir de él, añadiendo las aristas de menor peso que tenga un extremo en la solución y otro no
                - Algoritmo de Prim.
        - Aplicaciones:
            - Diseño de redes.
                - Mínimo coste.
                - Refuerzo de líneas críticas.
                - Identificación de cuellos de botella.
                - Enrutamiento (evitar ciclos).
            - Soluciones aproximadas a problemas NP.
            - Algoritmos de agrupamiento (clustering).
            - ...
        - Datos relevantes:
            - **Candidatos: c**onjunto de aristas E.
            - **Solución: **se ha construido un árbol con |V| vértices y |V|-1 aristas (extensible a grafos no conexos).
            - **Factibilidad: n**o existe ningún ciclo.
            - **Objetivo: **minimizar la suma de los pesos de las aristas seleccionadas.
            - **Selección: d**epende del algoritmo.
        - ### Algoritmo Kruskal O(|V| |E|):
            - Ordena las aristas de **mayor ** a ** menor **peso.
            - El árbol se construye a partir de ** varias **componentes **conexas**.
            - Sólo se incluye una arista si se une **dos **componentes **conexas**.
            - El algoritmo termina cuando sólo hay **una **componente **conexa**
                - Encuentra la **solución óptima **al problema.
            - Ejemplo de Kruskal:
                - [https://remnote-user-data.s3.amazonaws.com/tedtlFz5ZoLdpjLSWJyRqGp-mJlyPSmwExWjJKeU3b4cPrnv5vIh_hi5ucvjf0r2--JCXdnqZH4RdeIKr8t4jLePZ1qLO7RrPhCvTowqvstlzjNjzbYNq3sv5RVDnyte.png](../../Uploaded%20Files/Tema3.1_DAA/Highlights/Page%2008/Untitled.md)
            - **Esquema:**
                - [https://remnote-user-data.s3.amazonaws.com/bkSpVh2VnprfQr9DOhIynlmrZy5nRbWZ4fROm1cIVho6ZiqlmIPse2XCY29TQiuc6KMled4UVQ0EtQ9YWr3zu7FduLkI1YRuUc6qpecV9IHsTyGu5rp8JR4_YnJ4cq7h.png](../../Uploaded%20Files/Tema3.1_DAA/Highlights/Page%2010/Untitled.md)
        - ### Algoritmo de Prim O(|V| |E|):
            - El árbol se construye a partir de una **raíz**.
            - En cada iteración se añade una nueva rama (arista) al árbol.
            - Sólo se incluye una arista si no **genera ciclos**.
            - El algoritmo termina cuando sólo se han añadido **todos **los vértices
                - Encuentra la **solución óptima** al problema.
            - Ejemplo algoritmo Prim:
                - [https://remnote-user-data.s3.amazonaws.com/nLvNAjAFohXBOE5odQ8eEcOCi4DWwBDQgiXPrKpxiJe1gw0STH-0TxzuzKMyrrFw9uDegdYKn7IJ9HL3J3LvzpussrQ251P2WjjL-AxZrxsPXxpbZQGmkfpAD47NjsGB.png](../../Uploaded%20Files/Tema3.1_DAA/Highlights/Page%2013/Untitled.md)
            - **Esquema:**
                - [https://remnote-user-data.s3.amazonaws.com/iEYOSgMiSTf-Cj7VhGnot9PnUgKnEIjzeR7d0AH3I3GZ3JCKjxLprYc0IGHW89gvZjq5mRNIwsiOlVYON9cye_4CNAe5NX-1BGbUy5Adjnp1s8nXADvwHlUnzo8Y0pRi.png](../../Uploaded%20Files/Tema3.1_DAA/Highlights/Page%2014/Untitled.md)
    - ## Caminos mínimos:
        - **Problema:**
        - Dado un grafo conexo G = (V,E), dirigido y ponderado con pesos positivos, se toma uno, v, de los vértices como origen. El problema consiste en determinar la longitud mínima del camino que empieza en v hasta el resto.
        - Estrategias para resolver el problema:
            - Mantener un conjunto de nodos ya explorados para los cuales ya se ha determinado el camino más corto desde v
                - Algoritmo de Dijkstra.
            - Propiedades de los caminos mínimos:
                - Si d(v, u) es la longitud del camino mínimo para ir desde v a u, entonces se satisface:
                    - d(v, u) <= d(v, s)+d(s, u)
            - Datos relevantes:
                - **Candidatos:** conjunto de vértices de los que se conoce la distancia mínima desde el origen.
                - **Solución:** cuando no quedan candidatos.
                - **Factibilidad:** siempre es factible.
                - **Objetivo:** minimizar el camino de origen al resto de nodos.
                - **Selección:** candidato con menos distancia al origen.
            - ### Algoritmo de Dijkstra O(|V|^2^)  :
                - Se parte de dos conjuntos de nodos (V = S ∪ C)
                    - S: nodos seleccionados para los que se conoce el camino mínimo.
                    - C: resto de nodos del grafo.
                - En cada iteración se escoge el nodo de C con menor distancia y se añade a S. Se recalculan los caminos a través del nodo seleccionado.
                - Si no existe arista, se considera distancia infinita
                    - Encuentra la **solución óptima** al problema
                - Ejemplo algoritmo Dijkstra:
                    - [https://remnote-user-data.s3.amazonaws.com/W44S_vO-mt_yqRZDDWIBkYnj5NAkgOA6x9hd1kNiSDCcgKQUb7nt2eL6NlGphBKXI4cvq0xDUl-6asj5YYBRgeZ2XSnKGwN_ILqxWJgwZ34LNNoBIos4VqTJG7Z4ZF-9.png](../../Uploaded%20Files/Tema3.1_DAA/Highlights/Page%2020/Untitled.md)
                - **Esquema:**
                    - [https://remnote-user-data.s3.amazonaws.com/Nr9ZrLvsGzjlG2PfsiJ5fj5mxXacWnFApQIs49LkhnQne10pX4hAqQ1NQQsMk5RMn5xnhq_Zw2gPZucH0Er3azfnLT18yowql7ved-iPKybfH2BEjiQX_wBI-JXqCsID.png](../../Uploaded%20Files/Tema3.1_DAA/Highlights/Page%2021/Untitled.md)
    - ## Heurísticas voraces:
        - **Problema del coloreado de grafos: **Dado un grafo G = (V, E) no dirigido, asignar un color a cada vértice de tal forma que dos adyacentes no tengan el mismo color.
        - **Objetivo:** Minimizar el número de colores utilizados.
        - **Problema NP: **no existe ningún algoritmo eficiente que garantice un número mínimo de colores para grafos generales
            - Grafos planos: **4 colores** (Teorema de Appel-Hanke)
            - ![](https://remnote-user-data.s3.amazonaws.com/OL9P4-s1cuvrKWIroYL2_OX4tP4I7a1OluDB20_orgHmNXGqHhxLhBTOAMIv_5ZwBzx9emZ2K1QhGXNsY8M7eS2c_rZmiHmMbKfqIlc3D9TPEpYZ6OAP_ETG0HAzBF-M.png)
            - ![](https://remnote-user-data.s3.amazonaws.com/LuU9Fa3XMMHrPgRZgyXqbgVRugAl2iq9G6RuKHWiThNVriOVjEI3VMyyzXFKtlv-2OWxoaARlXU_1p9RoQaGB3Ud6n-Y6VGciF3RUL2ZqBrHwVrKoMPb8CPvbPiN5Mgl.png)
            - 
        - **Problema del viajante: **Dado un grafo G = (V, E), encontrar un camino que empiece y acabe en un vértice v, pasando una única vez por cada vértice de V.
        - **Objetivo:** Obtener el circuito hamiltoniano de coste mínimo.
        - **Problema NP:** no existe ningún algoritmo eficiente que garantice la optimalidad 
            - ![](https://remnote-user-data.s3.amazonaws.com/YGRkIeXcSpE0uz_RWtzvDWMjdFXgQABCBP85LfD1NgKCt6jVnN78lnAemATgELhgDlxg4XWAjAi8-FzzDw63Au8eAI-1Mom6ei_cB7593T8PEinYq2IE-3lNDH9shLWu.png)
            - **Heurística 1: **escoger en cada iteración el vértice más cercano al último nodo añadido al circuito siempre que:
                - No se haya seleccionado previamente
                - No se cierre el circuito
            - **Heurística 2: **escoger las aristas de coste mínimo (como en kruskal) pero garantizando que al final se forme un circuito. 
