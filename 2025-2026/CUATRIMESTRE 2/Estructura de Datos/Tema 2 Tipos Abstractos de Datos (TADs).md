Si la abstracción de la que se habló en el anterior tema forma parte del pensamiento, el TAD es su expresión formal dentro de la ingeniería de software.
Un TAD representa la cristalización de los principios de abstracción, encapsulamiento e interfaz que ya hemos estudiado.
Es la herramienta que nos permite definir nuevos tipos de datos que no existen nativamente en el lenguaje de programación, pero que son esenciales para modelar información
# 1. Definición y esencia de los TADs
Un **tipo abstracto de dato**(TAD) es una descripción de alto nivel de una colección de datos junto con el conjunto completo de operaciones que pueden realizarse sobre ellos.
Define *estructura lógica* y *comportamiento* esperado mediante un contrato bien especificado, pero deliberadamente omite cualquier detalle sobre cómo se implementa internamente.
La esencia de un TAD radica en su independencia de la implementación. Podemos considerarlo una "caja negra" perfecta. 
Esta separación entre *qué* hace y *cómo* lo hace es precisamente la materialización práctica del principio de abstracción.
Consideremos un TAD Cola. Su especificación nos dice que permite las siguientes operaciones:
- *enqueue(elemento)*: Añade un elemento al final de la cola
- *dequeue()*: Elimina y devuelve el elemento del frente de la cola
- *isEmpty()*: Consulta si la cola no contiene elementos
- *front()*: Consulta cuál es el primer elemento sin eliminarlo
- *back()*: Consulta cuál es el último elemento
Internamente, esta cola podría implementarse de múltiples formas: Usando un array con índices para marcar el frente y el final, empleando una lista enlazada con nodos que apuntan al siguiente elemento, usando dos pilas de manera creativa o empleando un buffer circular para optimizar el uso de la memoria
 ![[Tema 2 Tipos Abstractos de Datos (TADs)(Cola).png]]
 Lo más reseñable, es que a pesar de que existe tal amplitud en las posibilidades de implementación interna, desde la perspectiva del usuario del TAD, todas esas implementaciones son intercambiables. El comportamiento externo es idéntico porque respetan el mismo contrato.
 Los *operadores* de un TAD pueden clasificarse *según su propósito*, lo que ayuda a diseñar interfaces completas y coherentes:
 - **Operaciones de Creación**(Constructores): Permiten inicializar u obtener nuevos objetos del tipo que corresponde al TAD. En programación orientada a objetos se denominan constructores. Ej: *crearColaVacia()*.
 - **Operaciones de Modificación**(Mutadores): Alteran el estado interno del TAD, cambiando los valores almacenados o as relaciones entre ellos,  Ej: *enqueue()*, *dequeue()*.
 - **Operaciones de Consulta**(Observadores): Extraen información de los TAD sin modificarlo, lo cual proporciona una "ventana" al estado interno, Ej: *front()*, *isEmpty()*.
 - **Operaciones propias del TAD**: funciones específicas que tienen sentido solo para ese tipo de abstracto particular y que por tanto no son aplicables a cualquier tipo. Ejemplos: el determinante de una matriz, la conjugación de un número complejo, o el cálculo de la distancia entre dos puntos del espacio,
Esta clasificación guía no solo el diseño del TAD, sino también su documentación y uso.