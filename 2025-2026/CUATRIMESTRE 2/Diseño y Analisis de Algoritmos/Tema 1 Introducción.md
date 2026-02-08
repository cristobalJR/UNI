# 1. ¿Qué es un algoritmo?
Secuencia ordenada de pasos exentos de ambigüedad tal que, al llevarse a cabo con fidelidad, dará como resultado que se realice la tarea para la que se ha diseñado en un tiempo finito.
## 1.1 Propiedades
- **Finitud**: La ejecución de un algoritmo debe terminar tras un número finito de pasos
- **Precisión**: Cada paso debe estar rigurosamente especificados
## 1.2 Características
- **Entradas**: Un algoritmo puede tener o no entradas
- **Salidas**: Un algoritmo tiene una o más salidas
# 2. Resolución de problemas
Para resolver problemas con un ordenador es necesario:
- *Diseñar* un algoritmo para resolver el problema
- *Expresar* el algoritmo como un programa
- *Ejecutar* el programa
![[Tema 1 Introducción(resolucionProblemas).png]]
### Un poco de historia:
![[Tema 1 Introducción(historiaAlgoritmos).png]]
## 2.1 Reducción de problemas y complejidad
- Si *reducimos* un problema A a otro B, entonces podemos obtener una solución con un algoritmo diseñado para B, y transformarla en una de A
- *¿P=NP?* Si se *conoce* un algoritmo P que resuelve un problema NP-Completo. todos los problemas de la clase NP se pueden resolver en tiempo polinómico
# 3. Algorítmica
Es la disciplina que estudia los algoritmos:
- *Diseño*: Conocimiento de las técnicas de diseño algorítmico (métodos exactos y heurísticos)
- *Validación*: Demostración de que la salida dada por el algoritmo es correcta para todas las posibles entradas (demostración formal)
- *Análisis*: Recursos que consume el algoritmo (espacio y tiempo) en la resolución de un problema
## 3.1 Análisis de la eficiencia
- Determina las *características* del algoritmo que permitan evaluar su *rendimiento*
	Ejemplo: Tiempo requerido para la ejecución de un algoritmo en término del número de veces que se ejecuta cada etapa.
- *Enfoques* (Son complementarios)
	- Empírico
	- Teórico
	- Híbrido
# 4. Comparación de algoritmos
- Un *problema* se puede resolver con *varios algoritmos*. ¿Como seleccionar el mejor?
- **Eficiencia**: Medida de los *recursos* que emplea un algoritmo en su ejecución
- Recursos *computacionales*: tiempo, espacio, nº de procesadores...
- Recursos *no computacionales*: dificultad de implementación, disponibilidad de bibliotecas...
- La comparación en *tiempo* depende de:
	- Datos de entrada
	- Calidad del código generado por el compilador
	- Rapidez del procesador
	- Complejidad intrínseca del algoritmo
- Estudios sobre el tiempo:
	- *Teórico*(a priori): función que acote el tiempo de ejecución para unos valores de los datos de entrada
		- Estimación del <u>comportamiento</u> de un algoritmo
		- <u>Independiente</u> del ordenador
		- No requiere una <u>ejecución</u>
	- *Real*(a posteriori): tiempo de ejecución para una determinada entrada y en un ordenador concreto
		- Medida del <u>tiempo</u> de ejecución del un algoritmo

## 4.1 Principio de invarianza
- Dado un algoritmo y dos implementaciones I<sub>1</sub> e I<sub>2</sub> , que tardan T<sub>1</sub>(n) y T<sub>2</sub>(n) respectivamente, existe una constante real positiva c y un natural n<sub>0</sub> tales que
$$
\forall n \ge n_0 \quad T_1(n) \le c \cdot T_2(n)
$$
- El tiempo de ejecución de dos implementaciones distintas no va a diferir más que en una constante multiplicativa
## 4.2 Complejidad algorítmica
- Determina la eficiencia de un algoritmo
- No proporciona medidas absolutas (segundos...), sino relativas al tamaño del problema
- Es independiente del ordenador en el que se ejecute el algoritmo
T(n): tiempo empleado para ejecutar el algoritmo con una entrada de tamaño n.
Dada una entrada de tamaño n, no se mide en unidades de tiempo si no en "pasos" o instrucciones.
![[Tema 1 Introducción(sumaVector).png]]
![[Tema 1 Introducción(producto2Matrices).png]]
![[Tema 1 Introducción(ordenarVectorComparando).png]]
![[Tema 1 Introducción(ordenarVectorComparando2).png]]
![[Tema 1 Introducción(busquedaSecuencial).png]]
### 4.2.1 Medidas asintóticas
- T<sub>max</sub>(n): complejidad en el caso -> tiempo máximo para una entrada de tamaño n
- T<sub>min</sub>(n): complejidad en el caso -> tiempo mínimo para una entrada de tamaño n
- T<sub>med</sub>(n): complejidad en el caso -> tiempo medio para una entrada de tamaño n
- Todas las entradas de un algoritmo se suponen equiprobables
	- Entonces ¿Cuál utilizamos?
		-  T<sub>max</sub>(n): más común
		- T<sub>min</sub>(n): poco representativo
		- T<sub>med</sub>(n): difícil de calcular
- Definimos clases de equivalencia correspondientes a las funciones que *crecen de la misma forma*
- *Asintótico*: valores de los datos suficientemente grandes
	- Para datos pequeños las diferencias son marginales
- Medidas de *comportamiento asintótico* de complejidad:
	- Θ → Orden exacto de la función
	- Ο → cota superior
	- Ω → cota inferior
### 4.2.2 Notación O
- Dada una función f, estudiaremos funciones que, a lo sumo, crezcan *tan deprisa* como f
- Al conjunto de esas funciones se las llama *cota superior* de f y se denota como O(f)
- Conociendo O(f) de un algoritmo, se puede asegurar que en ningún caso, el tiempo será de un orden superior a la cota
- **Definición**: sean f,g: ℤ<sup>+</sup> → ℝ<sup>+</sup> , se dice que f ∈ O(g) si existen dos constantes n<sub>0</sub> ∈ℕ y λ∈ℝ<sup>+</sup> tales que:
$$
\forall n \ge n_0 \quad f(n) \le \lambda \cdot g(n)
$$
- La función no crece más deprisa que ninguna función proporcional a g
- Si f(n)∈O(g(n)), se dice que f(n) está en O de g(n) para todo n suficientemente grande
 ![[Tema 1 Introducción(crecimientoCota).png]]
	·n<sup>2</sup> +100 está inicialmente por encima de 2n<sup>2</sup> , pero solo hasta n<sub>0</sub>
	·Si tomamos f(n)=n<sup>2</sup> +100 entonces f(n)∈O(n<sup>2</sup>)
- Una cota superior siempre se puede estimar al alza:
 ![[Tema 1 Introducción(estimarCotaSuperior).png]]

##### Propiedades de la notación O
1. Para cualquier f se tiene que f ∈ O(f) → reflexibilidad
2. f ∈ O(g) → O(f) ⊂ O(g) 
3. O(f) = O(g) ↔ f ∈ O(g) y g ∈ O(f)
4. Si f ∈ O(g) y g ∈ O(h) → f ∈ O(h) → transitividad
5. Si f ∈ O(g)→f ∈ O(kg) ∀ k ∈ R<sup>+</sup>→escalabilidad →O(log<sub>a</sub> n)=O(log n)
6. Si f ∈ O(g) y f ∈ O(h) → f ∈ O(min(g,h)) 
7. Si f ∈ O(g<sub>1</sub>) y f<sub>2</sub> ∈ O(g<sub>2</sub>) → f<sub>1</sub> + f<sub>2</sub> ∈ O(max(g<sub>1</sub>, g<sub>2</sub>))
8. Si f<sub>i</sub> ∈ O(f) ∀ i=1, ..., k, → c<sub>1</sub>f<sub>1</sub> + ... + c<sub>k</sub>f<sub>k</sub> ∈ O(f)
9. Si f<sub>1</sub> ∈ O(g<sub>1</sub>) y f<sub>2</sub> ∈ O(g<sub>2</sub>) → f<sub>1</sub> · f<sub>2</sub> ∈ O(g<sub>1</sub> · g<sub>2</sub>)
### 4.2.3 Cálculo de la eficiencia
- **Bucles**:
	- *Suma* de los tiempos de cada iteración (incluida la evaluación de la condición)
	- Iteraciones idénticas → número de iteraciones *multiplicado* por el tiempo de iteración
- **Llamadas a funciones**: Equivalente a la complejidad de la propia *función*
- **Recursividad**:
	- Método de *sustitución*
	- *Árbol* de recursividad
	- *Expansión* de recurrencias
	- *Ecuación* característica
##### Órdenes de eficiencia habituales:
![[Tema 1 Introducción(ordenesEficiencia).png]]

### 4.2.4 Notación Ω
- Es una cota inferior
- Dada una función f, estudiar funciones g que, a lo sumo, crezcan tan lentamente como f
- Al conjunto de esas funciones se les llama cota inferior de f y es Ω(f)
- Conociendo Ω(f), se puede asegurar que el tiempo nunca será de orden inferior al de la cota
- Sean f,g: ℤ<sup>+</sup> → ℝ<sup>+</sup> se dice que f ∈ Ω(g) si existen dos constantes n<sub>0</sub>∈ ℕ y λ∈ℝ<sup>+</sup> tal que:
$$
\forall n \ge n_0 \quad f(n) \ge \lambda\, g(n)
$$
- La función f crece más deprisa que alguna función proporcional a g
- Si f(n)∈Ω(g(n)) se dice que f(n) está en Ω de g(n) para todo n suficientemente grande
- La función f necesita para su ejecución un tiempo mínimo dado por la función g
##### Propiedades de la notación Ω
1. Para cualquier f se tiene que f ∈ Ω(f) → reflexibilidad
2. f ∈ Ω(g) → O(f) ⊆ Ω(g)
3. Ω(f) = Ω(g) ↔ f ∈ Ω(g) y g ∈ Ω(f)
4. Si f ∈ Ω(g) y g ∈ Ω(h) → f ∈ Ω(h) → transitividad
5. Si f ∈ Ω(g) → f ∈ Ω(kg) ∀ k ∈ ℝ<sup>+</sup>→ escalabilidad → Ω(log<sub>a</sub> n) = Ω(log n)
6. Si f ∈ Ω(g) y f ∈ Ω(h) → f ∈ Ω(min(g,h))
7. Si f<sub>1</sub> ∈ Ω(g<sub>1</sub>) y f<sub>2</sub> ∈ Ω(g<sub>2</sub>) → f<sub>1</sub> + f<sub>2</sub> ∈ Ω(max(g<sub>1</sub>, g<sub>2</sub>))
8. Si f<sub>1</sub> ∈ Ω(g<sub>1</sub>) y f<sub>2</sub> ∈ Ω(g<sub>2</sub>) → f<sub>1</sub> · f<sub>2</sub> ∈ Ω(g<sub>1</sub> · g<sub>2</sub>)
### 4.2.5 Notación Θ
- Es el orden *exacto*
- Dada una función f , estudiaremos funciones g que crecen asintóticamente de la misma forma
- Al conjunto de esas funciones se las llama orden exacto de f u es Θ(f)
- Conociendo Θ(f) de un algoritmo, se puede asegurar que el tiempo es de dicho orden
- Sean f,g: ℤ<sup>+</sup> → ℝ<sup>+</sup> , se dice que f ∈ Θ(g) si f ∈ O(g) ⋂ Ω(g), es decir, f pertenece tanto a O(g) como a Ω(g)
##### Propiedades de la notación Θ
1. Para cualquier f se tiene que f ∈ Θ(f) → reflexibilidad
2. f ∈ Θ(g) → Θ(f) = Θ(g)
3. Θ(f) = Θ(g) ↔ f ∈ Θ(g) y g ∈ Θ(f)
4. Si f ∈ Θ(g) y g ∈ Θ(h) → f ∈ Θ(h) → transitividad
5. Si f ∈ Θ(g) → f ∈ Θ(kg) ∀ k ∈ ℝ<sup>+</sup> → escalabilidad
6. Si f<sub>1</sub> ∈ Θ(g<sub>1</sub>) y f<sub>2</sub> ∈ Θ(g<sub>2</sub>) → f<sub>1</sub> + f<sub>2</sub> ∈ Θ(max(g<sub>1</sub>, g<sub>2</sub>))
7. Si f<sub>1</sub> ∈ Θ(g<sub>1</sub>) y f<sub>2</sub> ∈ Θ(g<sub>2</sub>) → f<sub>1</sub> · f<sub>2</sub> ∈ Θ(g<sub>1</sub> · g<sub>2</sub>)
