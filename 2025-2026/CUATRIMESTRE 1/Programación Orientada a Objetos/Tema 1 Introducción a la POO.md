+Para recuperar los 30 días gratis de StarUML, borrar dentro de APPDATA/roaming la carpeta StarUML entera, y vuelves a tener 30 días
+Cuando queramos hacer cálculo científico, se usan flotantes, los números reales, solo son aproximaciones, por lo que estropean el programa
# Características de la POO
## Definición de objeto
Un *objeto* es un componente software que:
- Puede recibir mensajes y responder
- Tiene identidad
- Tiene un estado
- Tiene un comportamiento bien definido
## Lenguaje Unificado de modelado
Lenguaje gráfico para visualizar, especificar, construir y documentar los componentes de un software orientado a objetos.
### Ejemplo:
Los objetos se representan con rectángulos divididos en dos partes. La parte superior muestra la identidad del objeto y la inferior el estado del objeto
Un programa tiene 4 objetos de tipo cadena de texto modificable y un objeto de tipo imagen:
	![[Tema 1 Introducción a la POO (UML Objetos).png]]
## Lenguajes orientados a objetos
Las POO se basan en el uso de las siguientes capacidades primarias
- *Abstraer*
- *Encapsular*
- *Modularizar*
- *Jerarquizar*

También se pueden considerar estas capacidades secundarias:
- *Tipo*
- *Concurrencia*
- *Persistencia*
# Abstracción
## Definición
Abstraer es la capacidad que permite distinguir las características fundamentales de un objeto que lo hacen diferente del resto, y que proporcionen límites conceptuales bien definidos sobre la perspectiva del que lo visualiza (Crear un modelo simplificado)
## Soporte a la abstracción en los lenguajes
Los lenguajes de POO facilitan abstraer gracias a que permiten definir interfaces para comunicarse con los objetos.
Una *interfaz* es una declaración de los métodos u operaciones que debe tener una abstracción.
Un *método* es como una función que puede aplicarse sobre un objeto, o como un mensaje que puede enviarse a un objeto.
La interfaz declara un conjunto de métodos, pero no especifica cómo se implementan.
**Las interfaces** se representan en UML mediante un rectángulo con el nombre de la interfaz anteponiendo la palabra interfaz. Los métodos se añaden separados por una línea horizontal. Los identificadores suelen estar en cursiva para indicar que no tienen implementación.
	![[Tema 1 Introducción a la POO (Interfaz).png]]
## Creación de objetos basada en clases
Una clase es como un molde que permite crear objetos, y permite añadir a las interfaces una implementación.
La *implementación* consiste en la definición de propiedades y el código de programación interno de los métodos.
En UML las **clases** se representan mediante rectángulos. En el interior de cada rectángulo se indican, separados por líneas horizontales, el nombre de la clase, las propiedades y los métodos.
	![[Tema 1 Introducción a la POO (Clases).png]]
## Medir la calidad de una abstracción
Aspectos:
- *Acoplamiento*: Minimizar el grado de asociación entre diferentes abstracciones. Dos abstracciones están acopladas cuando para tener una, también hay que tener la otra.
- *Cohesión*: Maximizar el grado de asociación dentro de una abstracción. Hay cohesión cuando los métodos de una abstracción tienen una temática común, trabajan con tipos similares...
- *Suficiencia* y *completitud*: Que tenga las características precisas para permitir un funcionamiento eficiente y completo. No le faltan métodos para cumplir su objetico.
- *Primitividad*: Las operaciones de una abstracción deben ser lo más básicas posibles. No debe tener operaciones que ya se pueden construir con otras más básicas.
# Encapsulación











hata la diapositiva 62...
# Modularidad
Posibilidad de dividir los programas en agrupaciones lógicas de sentencias llamadas módulos
# Tipado
coercion si es a punteros, si no son punteros los elementos involucrados en el casting es conversion
# Concurrencia
## Definición 
Capacidad que permite que a la vez se ejecuten varias secuencias de instrucciones, hasta que llegó Java, esto era cosa del sistema operativo
	![[Tema 1 Introducción a la POO (Concurrencia).png]]
El pacman y el comecocos se ejecutan a la vez en el juego PACMAN
# Persistencia
## Definición
La persistencia es la capacidad que permite que la existencia de los datos trascienda en el tiempo y el espacio.
En POO no tienes que saber como es el objeto para guardarlo o cargarlo.
### Según su tiempo de vida:
**Expresiones:**
Con una vida inferior al de una línea de código.
**Variables Locales:**
Cuya vida se circunscribe a una función
**Variables Globales:**
viven mientras se ejecuta el programa
**Datos que persisten de una ejecución a otra**

# Ejercicio

![[Tema 1 Introducción a la POO (EjercicioUML).png]]