El estudio de las *Estructuras de Datos* es fundamental en la ingeniería del software, para diseñar soluciones computacionales eficientes, modulares y elegantes.
Tres pilares esenciales:
- **Abstracción**: Proceso mental que nos permite moldear la complejidad del mundo real identificando y aislando las características esenciales de un problema, evitando detalles superfluos. Se materializa en el código a través de los tipos de datos y su especificación formal, donde definiremos el comportamiento de nuestras estructuras
- Gestión de la **memoria dinámica** mediante *punteros*, una herramienta que nos permite crear estructuras de tamaño variable y relaciones complejas en tiempo de ejecución. 
# 1. La Abstracción
El diseño e implementación de software eficiente y fácil de mantener comienza con un concepto fundamental: la abstracción. Podemos definir **abstracción** como el proceso mental mediante el cual el humano extrae las características esenciales de un objeto, sistema o idea, ignorando deliberadamente detalles superfluos que no son relevantes para el propósito inmediato. 

El concepto *caja negra* implica estudiar un sistema centrándose exclusivamente en el comportamiento externo observable, obviando su comportamiento interno. Todo sistema complejo puede ser estudiado como una máquina cuyo interior se ignora.

La *interfaz* es el conjunto de elementos(operaciones, métodos y funciones) mediante los cuales se puede interactuar con un objeto visto como una caja negra. Es el medio de comunicación de los componentes software.

El *encapsulamiento* es el proceso que pone en práctica la ocultación de los detalles internos de una abstracción. En programación, es esencial para la reutilización y la robustez del código. Al ocultar cómo está hecho un módulo (su implementación) y solo exponer qué se puede hacer con él(su interfaz), logramos dos objetivos fundamentales:
- **Reutilización**: Podemos utilizar ese módulo en diferentes programas, confiando en que su comportamiento externo será constante.
- **Protección**: Impedimos que otros componentes del programa utilicen el objeto de modos no deseados o accedan directamente a su estado interno, lo que podría corromperlo. La interacción solo puede darse a través de las operaciones definidas, que actúan como guardianes.

Vinculado a todo lo anterior interfaz está el concepto de contrato, una metáfora poderosa introducida por Bertrand Meyer. Este contrato establece las obligaciones y los beneficios mutuos y públicamente declarados entre el diseñador de un componente y su usuario. 
- El diseñador (o implementador) se compromete a publicar en la interfaz un conjunto de operaciones que garantizan un comportamiento específico. Oculta todo lo demás mediante encapsulación. 
- El usuario (o cliente) se compromete a utilizar únicamente esas operaciones publicadas, confiando en que producirán los resultados esperados. 
Este "acuerdo" tiene un beneficio enorme: permite al diseñador cambiar completamente la implementación interna de un componente (por ejemplo, hacerlo más rápido o eficiente) sin que el usuario tenga que modificar ni una sola línea de su código, siempre y cuando se respete el contrato (la interfaz) establecido

# 2. Tipos de datos
Una vez comprendida la necesidad de abstraer, debemos encontrar la manera de representar estas abstracciones dentro de un lenguaje de programación, Aquí es donde entran en juego todos los tipos de datos.

Los lenguajes de programación nos ofrecen un amplio catálogo de tipos de datos que podemos clasificar de la siguiente forma:
- Tipos *predefinidos*. Son de uso muy común y pueden clasificarse en:
	- *Simples*: Modelan valores indivisibles. Algunos ejemplos en Pascal son integer(<u>enteros</u>), real(<u>coma flotante</u>), boolean(<u>valores lógicos True/False</u>) y char (<u>un carácter</u>).
	- *Estructurados*: Agrupan varios valores relacionados, por ejemplo el tipo string(<u>cadena de carácteres</u>) que es un tipo estructurado predefinido.
- Tipos *definidos por el usuario*. Dado que los tipos básicos predefinidos no dan normalmente cobertura a todas las necesidades de modelado de la información que necesitan nuestros programas, los lenguajes incluyen mecanismos para que el programador pueda crear sus propios tipos. En pascal:
	- *Simples*: subrango (<u>rango de valores</u>, ej: 1..10), enumerado (<u>lista de identificadores</u>, ej:(rojo, azul, verde)), o puntero(permite <u>referenciar a otra variable</u>).
	- *Estructurados*: array(<u>vector o matriz</u> de elementos), registro (<u>estructura que agrupa campos</u> generalmente de distintos tipos), conjunto (<u>set</u>) o archivo.

Un tipo de dato puede y debe verse como una abstracción en sí mismo. Cada instancia de un tipo está sujeta a  un "contrato" que define:
- Un <u>nombre</u> que lo identifica (boolean, integer).
- Un conjunto de <u>valores posibles</u> (para boolean son true y false).
- Un conjunto de <u>operaciones</u> válidas que se pueden realizar con el (para boolean: and, or, not).
- Las <u>reglas de interacción</u> con otros tipos (ej: un array de enteros utiliza el tipo integer para sus elementos).
Por ejemplo el tipo Boolean está definido mediante los siguientes datos:
- Nombre: Boolean
- Valores posibles: True, False
- Operaciones: AND, OR, NOT
- Uso de otros tipos: Normalmente, solo opera consigo mismo

## 2.1 Especificación formal
La especificación de un tipo de datos es la definición formal de su contrato. Podemos definirlo como todo aquello que el cliente(quien lo va a usar) necesita saber para utilizarlo correctamente, sin revelar cómo se implementa. Una especificación consta de dos partes:
- *Signatura*: Define la "forma" de las operaciones.
	- Nombre del tipo (ej: TipoCola).
	- Nombres de las operaciones (j: Encolar, Desencolar, EstaVacia))
	- Parámetros de entrada y tipo de resultado de cada operación.
- *Axioma*: Define la "semántica" o comportamiento de las operaciones. Describe cómo interactúan entre sí, a menudo mediante reglas o pre/postcondiciones. Por ejemplo: un axioma para una cola podría ser: "Desencolar aplicado a una cola resultante de Encolar(X, C)" debe devolver X y una cola equivalente a C".
Esta separación entre qué hace (especificación) y cómo lo hace (implementación) es el núcleo de la programación abstracta y permite diseñar programas más flexibles y fáciles de mantener, un objetivo fundamental dentro de la ingeniería del software.
# 3. Memoria dinámica