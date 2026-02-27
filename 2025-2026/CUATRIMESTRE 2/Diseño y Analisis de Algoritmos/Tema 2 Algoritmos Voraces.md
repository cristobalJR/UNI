# 0. Voraces
(Greedy: Voraz, avaricioso, codicioso)
*Dado un problema con n entradas, el objetivo es obtener subconjuntos de estas, de tal forma que se satisfaga una determinada relación de forma óptima.*
La forma habitual de resolverlo es escoger las mejores entradas que verifiquen las restricciones hasta que se encuentra la solución que se busca.
## 0.1 Esquema de la técnica
- Conjunto de **candidatos** y conjuntos de **seleccionados**.
- Función de **selección**: ¿Qué candidato elijo?(candidato idóneo en cada etapa)
- Función **solución**: ¿Tengo ya la solución?(determina si los candidatos seleccionados son una solución)
- Función de **factibilidad**: determina si el conjunto seleccionado es prometedor.
- Función **objetivo**: determina el valor de la solución.
## 0.2 Características del esquema
- Se construye una solución *iterativamente*
- Se toma la decisión *óptima* en cada *iteración*
- Una vez analizado un candidato (introducir o excluir), *no se reconsidera* la decisión.
- Son voraces porque en cada etapa toman *la mejor decisión* sin preocuparse de los pasos posteriores
### Ventajas:
- *Implementación sencilla*
- Producen soluciones de forma muy *eficiente*
- Encuentran la *solución óptima* para un número *determinado* de problemas (*No* para *todos*)
### Desventajas:
- *No siempre* encuentran una *solución óptima*
	- Algunos criterios voraces no lo garantizan (ej: cambio de monedas de 11, 5 y 1)
- *No reconsiderar* decisiones pasadas puede conducir a no obtener el *óptimo global* (ej: Problema del viajante)
- Dificultad de encontrar la *función de selección* adecuada
- *Demostración* formal de optimalidad

# 1. Problema del Cambio
Dado un país con un sistema monetario cuyas monedas tienen los valores v1, v2, ..., v<sub>n</sub>, el problema del cambio se define:
	*Descomponer* una cantidad dada M de monedas de valores  v1, v2, ..., v<sub>n</sub>,de forma que el *número* de monedas utilizado sea el *mínimo*
 ![[Tema 2 Algoritmos Voraces(problemaCambioIcono).png]]
Datos relevantes:
- **Candidatos**: Monedas C = { v1, v2, ..., v<sub>n</sub>}.
- **Solución**: La suma de las monedas elegidas es igual al cambio.
- **Factibilidad**: La suma de las monedas no puede superar al cambio.
- **Objetivo**: Minimizar las monedas devueltas.
- **¿Selección?**: Moneda de mayor valor mientras sea factible.
![[Tema 2 Algoritmos Voraces(problemaCambioPython)-1.png]]
![[Tema 2 Algoritmos Voraces(problemaCambioPseudoCodigo).png]]

# 2. Tiempo Mínimo de Espera
- Un servidor debe dar servicio a n clientes
- El tiempo requerido por cada cliente t<sub>i</sub> es conocido
- Se desea *minimizar el tiempo medio de cada cliente* en el sistema:
$$
T_m = \frac{\sum_{i=1}^{n} t_i}{n}
$$
- Como *n es conocido, equivale a minimizar el tiempo total* invertido *por* cada *cliente*
$$
T = \sum_{i=1}^{n} t_i
$$
 ![[Tema 2 Algoritmos Voraces(problemaTiempoEsperaIcono).png]]
Datos relevantes:
- Conjunto de **candidatos**: n clientes
- Función de **solución**: todos los clientes han sido ordenados
- Función **factibilidad**: si han sido ordenados los clientes o no
- Función de **objetivo**: minimizar T
- Función **selección**: Elegir los candidatos por orden creciente de t<sub>i</sub> 

\* El algoritmo voraz consiste en ordenar de forma no decreciente en  t<sub>i</sub> los n clientes

![[Tema 2 Algoritmos Voraces(pseudoCodigo).png]]
### Ejemplo con 3 Clientes:
![[Tema 2 Algoritmos Voraces(clientesEjemploTiempoMinimo).png]]
![[Tema 2 Algoritmos Voraces(solucionTiempoMinimo).png]]

# 3. Problema de la mochila (Objetos Fraccionables)
- Supongamos que tenemos n tipos *objetos* y una *mochila* (<u>los objetos pueden fraccionarse</u>)
- Cada objeto i tiene un *peso* w<sub>i</sub> > 0 y un *valor* v<sub>i</sub> > 0
- La mochila puede llevar un *peso máximo* de W
$$
\sum_{i=1}^{n} x_i w_i \le W
$$
- Se desea llenar la mochila *maximizando* el valor de los objetos transportados
$$
\max \sum_{i=1}^{n} x_i v_i
$$

	$0 \le x_i \le 1 \text{ con } 1 \le i \le n$
  
  ![[Tema 2 Algoritmos Voraces(problemaMochilaObjetosFraccionadosIcono).png]]
Datos relevantes:
- Conjunto de **candidatos**: n objetos
- Función de **solución**: no puedo añadir más fracciones de objetos a la mochila
- Función **factibilidad**: el peso de los objetos no supera el máximo
- Función de **objetivo**: maximizar el beneficio de los objetos elegidos
- Función **selección**: Elegir los objetos con mejor relación Valor/Peso
![[Tema 2 Algoritmos Voraces(problemaMochilaPseudoCodigo).png]]
### Ejemplo con 5 Objetos:
![[Tema 2 Algoritmos Voraces(objetosEjemploMochila).png]]
![[Tema 2 Algoritmos Voraces(solucionEjemploMochila).png]]
# 4. Planificación con Plazo Fijo
- Tenemos n trabajos, donde cada trabajo i tiene una fecha limite f<sub>i</sub> >0 y un beneficio b<sub>i</sub> > 0
- El beneficio b<sub>i</sub> de un trabajo i se gana si y solo si se realiza antes de su fecha tope f<sub>i</sub>
- El trabajo se realiza en una maquina que consume una unidad de tiempo y solo hay una máquina disponible (En un instante solo se puede hacer una tarea)
 ![[Tema 2 Algoritmos Voraces(planificacionPlazoFijoIcono).png]]
 Datos relevantes:
- Conjunto de **candidatos**: n trabajos
- Función de **solución**: no quedan tareas por planificar
- Función **factibilidad**: las tareas asignadas se realizan dentro de plazo
- Función de **objetivo**: maximizar el beneficio de las tareas elegidas
- Función **selección**: ¿?
### Ejemplo con 4 Tareas
![[Tema 2 Algoritmos Voraces(plazoFijoTareasEjemplo).png]]
![[Tema 2 Algoritmos Voraces(plazoFijoSecuenciaEjemplo).png]]
![[Tema 2 Algoritmos Voraces(plazoFijosSolucionEjemplo).png]]