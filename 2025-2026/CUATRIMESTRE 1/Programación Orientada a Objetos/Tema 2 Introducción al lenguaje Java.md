# Introducción a Java
## Compilación y ejecución
 ![[Tema 2 Introducción al lenguaje Java(compilacionYEjecución).png]]
## Los paquetes Java
![[Tema 2 Introducción al lenguaje Java(paquetesJava).png]]

## "Hola mundo"

```java 
/** Programa en Java que muestra un mensaje de bienvenida */ 
public class HolaMundo { 
	// El método en el que comienza la ejecución del programa:
	main public static void main (String [ ] arg) {
		 System.out.println("Bienvenidos a Java"); 
	 } 
}
```

## Juego de instrucciones de Java
*abstract* **boolean** break **byte** case catch *char* **class** *continue* default do *double* extend *false* **final** **finally** *float* for *if* *implements* instanceof **int** interface long *native* new **null** package **private** public *return* short static **super** *switch* **synchronized** *this* threadsafe **transient** true *try* **void** volatile when *while* yield 
## Tipos primitivos
abstract **boolean** break **byte** case catch **char** class continue default do double extend **false** final finally **float** for if implements instanceof **int** interface **long** native new **null** package private public return **short** static super switch synchronized this threadsafe transient **true** try **void** volatile when while
## Control de flujo
abstract boolean **break** byte **case** **catch** char class **continue** **default** **do** double extend false final **finally** float **for** **if** implements instanceof int interface long native new null package private public **return** short static super **switch** synchronized this threadsafe transient true **try** void volatile **when** **while** **yield** 
## Capacidades de POO
**abstract** boolean break byte case catch char **class** continue **default** do double **extend** false **final** finally float for if **implements** **instanceof** int **interface** long **native** **new** null **package private public** return short **static super** switch **synchronized this threadsafe transient** true try void **volatile** when while yield 

# Expresiones básicas
## Variables y expresiones con tipos primitivos
En Java todos los datos de un programa son objetos salvo 7 *tipos primitivos* que se añadieron por razones de *eficiencia*.
La definición de una variable a un tipo primitivo sigue la siguiente sintaxis:
```java
int mainCont, auxCont; //Declaración de dos enteros 
mainCont = 2; //Inicialización de un entero 
int i = 5; //Declaración e inicialización de un entero 
final double π = 3.1416; //Declaración e inicialización de una constante real
```

## Tipo carácter
 ![[Tema 2 Introducción al lenguaje Java(char).png]]
## Tipos numéricos
 ![[Tema 2 Introducción al lenguaje Java(tiposNuméricos).png]]
## Aritmética con tipos numéricos
 ![[Tema 2 Introducción al lenguaje Java(aritméticaConTiposNuméricos).png]]
## Operaciones relacionales en tipos numéricos
 ![[Tema 2 Introducción al lenguaje Java()operacionesRelacionalesTiposNumericos.png]]
## Operaciones de bit con tipos numéricos
![[Tema 2 Introducción al lenguaje Java(operacionesDeBitConTiposNumericos).png]]
## Tipo booleano y operaciones
![[Tema 2 Introducción al lenguaje Java(booleanoYOperaciones).png]]

# Control de flujo
## Ámbitos y sentencias
Un ámbito se inicia con el carácter de *llave* abierta hacia la derecha y se termina con el carácter de llave abierta hacia la izquierda.
Los ámbitos se utilizan para:
- *Definir qué sentencias* están afectadas por una declaración (función, clase...) o por una instrucción de *control de flujo* (if, while...)
- *Agrupar* lógicamente sentencias
Los ámbitos se pueden *anidar* y dentro de un ámbito siempre puede definirse otro.
Las declaraciones de *las veriables son locales al ámbito* en que se declaran
En Java, el tabulado a nivel de ámbito es una convención muy aconsejable, aunque no afecte a la compilación. El siguiente código es equivalente al anterior: 

```java
{int a;a = 25;int c = 15;{int b;b = 2;}}
```

## If - else
La sentencia if lleva asociada una expresión booleana entre *paréntesis*. De cumplirse la expresión se ejecuta la sentencia o el ámbito siguiente al if. En otro caso se ejecuta, si existe, la rama else.

## for
La palabra reservada *for* permite repetir una sentencia o un ámbito cualquier número de veces. Su estructura es la siguiente:
Es buena práctica solo usarlo cuando se conoce el número de iteraciones de antemano y solo depende de una condición.

```java
for (<expresión inicialización>;<expresión booleana>;<expresión incremento>) <ámbito> | <sentencia>
--------------------------------------------------
for (int cont = 0; cont < 100; cont++) { a = a * B /c; //La primera vez que se ejecuta esta línea cont vale 0
 //La última vez que se ejecuta cont vale 99
  } //Aquí la variable cont no existe, pero si existiese valdría 100
```

## while y do-while
La palabra reservada *while* permite repetir un ámbito cualquier número de veces. Es buena práctica usarlo cuando el número de iteraciones no está definido a priori o depende de varias condiciones. Su estructura es la siguiente:
```java
while (<expresión booleana>) <ámbito> | <sentencia>

do <ámbito> | <sentencia> while (<expresión booleana>); 
----------------------------------------------------
while (a > b) { b = D * 25; a--; }
do { b = D * 25; a--; } while (a > b);
```

## break y continue
La instrucción *break* permite *interrumpir* en cualquier punto la ejecución normal de un bucle *for* o *while* y salir del mismo.
La instrucción *continue* permite interrumpir la ejecución normal de un bucle for o while y volver a la sentencia de evaluación para decidir si continuar o salir.
Tanto break como continue pueden utilizarse en combinación con *etiquetas* para salir de varios bucles simultáneamente hasta alcanzar el bucle etiquetado. Las etiquetas se definen mediante un identificador seguido del carácter de dos puntos.
 ![[Tema 2 Introducción al lenguaje Java(breakContinue).png]]
## Clásico switch-case-break-default
Permite evaluar una sola vez una expresión entera.
Basándose en su resultado, ejecuta las sentencias de un ámbito concreto.
Si las sentencias de un case no terminan en *break*, se ejecutan todas las sentencias siguientes, aunque pertenezcan a otros casos.
```java
switch (variable) { 
	case 5 : { System.out.println("cinco"); break;} 
	case 6 : { System.out.println("seis"); break; }
	default : { System.out.println("Más"); break; }
 }
```

## Nuevo return-switch-case-break-yield-default
- Hasta JDK 7 el switch solo admitía expresiones basadas en tipos enteros, pero JDK 8 amplia el uso a expresiones con tipos enumerados y String. 
- JDK 12 introduce sintaxis de flechas, múltiples valores por caso y *yield* para devolver valores. 
- JDK 18 introduce la posibilidad de usar match de tipos.
- JDK 21 introduce el uso de guardas (*when*).

# Las clases
Primero se define una clase y luego se pueden crear un número ilimitado de objetos de esa clase.
Al definir una clase se defina la interfaz y la implementación de los objetos que posteriormente se podrán crear.
En Java, la definición de una clase está constituida por:
- <font color="#00b050">Identificación</font>
- <font color="#ff0000">Miembros: Métodos o propiedades</font>
- <font color="#245bdb">Clases internas</font>
- <font color="#7030a0">Bosques de inicialización</font>
```java 
[Modificador de clase] class <identificador> [parámetros] [herencia] [excepciones] {
 [método|propiedad|inicializacion|clase|comentarios]* }
---------------------------------------------------------
 class Coche { //Aquí iría la implementación de la clase Coche 
 }
```

## Referencias a objetos
Java permite definir variables que sean *referencias a objetos*.
```java 
<nombre_clase> <identificador> [,<identificador>]; <identificador> = <expresión de inicialización>; 
[final] <nombre_clase> <identificador> = <expresión de inicialización >;
```
 ![[Tema 2 Introducción al lenguaje Java(referenciaObjetos).png]]
 La expresión de inicialización puede ser de dos tipos:
 - *Creación* de un objeto, con la palabra reservada **new** seguida del nombre de la clase.
 - *Referencia* a otro objeto ya creado
	 ```java 
	 Coche a, b, c; //Se declaran tres variables que apuntarán a objetos. 
	 a = new Coche(); //Se crea un coche y la variable “a” lo apunta. 
	 b = new Coche(); //Se crea otro coche y la variable “b” lo apunta. 
	 c = a; //La variable “c” apunta al mismo coche que “a”.
	 ```

## Miembros de las clases
Los miembros de una clase pueden ser de dos tipos:
- *Propiedades*: variables que se declaran en el interior de una clase
- *Métodos*: funciones que tienen parámetros, que devuelven elementos y que pueden contener código
En java, el identificador de una clase suele estar en *UpperCamelCase* y los miembros de una clase suelen estar en *lowerCamelCase*.
 ![[Tema 2 Introducción al lenguaje Java(identificadorClaseYMiembros).png]]
## Definición de propiedades
Las propiedades, o campos, sirven para dorar de estado al objeto o a la propia clase.
Las propiedades son variables definidas dentro de una clase y que pueden tomar valores independientes en cada objeto.
Si no se indica otra cosa se inicializan a su valor por defecto (null los objetos, cero los tipos numéricos, false los booleanos...).
```java 
class Coche {
	boolean enMarcha; 
	int velocidad; 
	Rueda r1 = new Rueda(); 
	Rueda r2 = new Rueda(); 
	Rueda r3 = new Rueda(); 
	Rueda r4 = new Rueda(); 
} 
class Rueda {
	 int presion = 2000; 
	 float radio = 6.28f; }
```

## Definición de métodos
Los métodos son *funciones* definidas dentro de la clase. Se invocan sobre los objetos de esa clase o sobre la clase misma.
- El identificador del método está precedido por el *tipo* devuelto o *void* si no devuelve nada
- Al identificador lo siguen los parámetros del método
- Tras los parámetros puede haber un *ámbito* con la implementación
```java 
class Coche { 
	void parar() { // Código con la implementación
	 } 
	 void acelerar(int incremento) { // Código con la implementación
	} 
	int dameVelocidad() { // Código con la implementación 
	} 
}
```
## Ejemplo de definición de miembros
![[Tema 2 Introducción al lenguaje Java(ejDefinicionDeMiembros).png]]

## Diferencia entre objeto y referencia a objeto
En el ámbito de un método se opera con los parámetros que se le pasan y con los miembros (métodos y propiedades) de la propia clase.
El método main de JuegoCoches crea 2 objetos de la clase Coche.
 ![[Tema 2 Introducción al lenguaje Java(referenciaYobjeto).png]]

## Invocación de miembros de otros objetos
Para invocar a un miembro de otra clase se usa el identificador del objeto, un punto y el identificador del miembro que se desea invocar.
El método reparar de la clase coche invoca métodos de otro objeto (Taller)![[Tema 2 Introducción al lenguaje Java(metodosOtroObjeto).png]]
## Valores independientes de las propiedades
Cada objeto tiene valores independientes para sus propiedades.
El método main primero pone valor 10 en la propiedad velocidad de un coche, luego pone 20 en la propiedad velocidad del otro coche, finalmente pone a cero la propiedad velocidad del primero.![[Tema 2 Introducción al lenguaje Java(valoresIndependientesPropiedades).png]]

## Invocación de miembros del propio objeto
Para hacer referencia a un miembro de la propia clase se usa *simplemente el identificador* de dicho miembro
![[Tema 2 Introducción al lenguaje Java(miembrosMismoObjeto).png]]

## Valores devueltos
En el interior del método se usa *return* para indicar el valor devuelto.
Si un método indica que devuelve un valor, es imprescindible que todos los caminos del método terminen en un return.

## Parámetros
A los métodos se les pueden pasar tipos primitivos u otros objetos. Por ejemplo, podemos añadir la clase Taller que cambia las ruedas del coche
![[Tema 2 Introducción al lenguaje Java(parametros).png]]

## Interior de los métodos
La palabra reservada *this* sirve para referirnos al propio objeto.
Por ejemplo, para que el coche pueda pasarse él mismo al taller.![[Tema 2 Introducción al lenguaje Java(interiorMetodos).png]]

## Control de acceso a los miembros
Por defecto, si no se pone modificador de acceso, el miembro es *friendly*: visible desde las clases que pertenezcan al mismo paquete(*directorio*) e inaccesible desde fuera del paquete (~ en UML).
Los más habituales son:
- *public*: <u>permite</u> acceder al miembro desde fuera de la clase
- *private*: <u>no permite</u> acceder al miembro desde fuera de la clase
	- Las propiedades suelen ser siempre privadas
	- Los métodos privados suelen corresponder a funciones auxiliares

## Clases públicas
Una *clase* con modificador *public* indica que la clase es *visible desde otros paquetes* diferentes al paquete en el que se implementa.
Si la clase no es definida pública, solo es visible en el paquete que se implementa
*Solo puede existir una clase pública por fichero* y el nombre de tal clase debe de coincidir con el nombre del fichero.

## Clases internas y clases internas privadas
Una *clase interna* es una clase que se define anidada dentro de otra.
```java 
public class Coche { 
	class Rueda { 
		private int radio = 3;
		 ... 
	 } 
	 private Rueda r = new Rueda(); 
	 ...
} 
```
Una *clase interna* definida *private* solo es visible desde dentro de la clase en la que está definida.
```java 
public class Stack { 
	private class Node { 
		private Node next; 
		private int value; 
	} 
	private Node top = new Nodo(); 
	... 
}
```
## Todo junto en un ejemplo
![[Tema 2 Introducción al lenguaje Java(todoJuntoEjemplo).png]]

# Detalles de las propiedades
## Propiedades privadas
Normalmente las propiedades de los objetos se mantienen *privadas*
Si se desea  que una propiedad privada sea consultada o modificada desde fuera de la clase se suelen añadir métodos públicos *getters* y *setters*.
Estos permiten consultar o modificar variables privadas de forma controlada, *evitando romper el invariante* de una clase.
```java 
class Coche { 
	private int speed; 
	public int getSpeed() { 
		return speed; 
		} 
	public void setSpeed(int speed) { 
		if (speed > 120) 
			this.speed = 120; 
		else if (speed < 0) 
			this.speed = 0; 
		else this.speed = speed; 
	} 
}
```

## Propiedades final
*final* es un modificador que se usa para indicar que el valor de una propiedad no va a cambiar. Así, las propiedades final son *constantes* a lo largo de la vida del objeto. Su valor puede definirse en compilación o en ejecución.
Las referencias a objetos declaradas final no pueden cambiarse, aunque los objetos en sí mismos pueden cambiar su estado.
Una variable final de tipo primitivo, por su carácter inmutable, pueden decidirse declararla pública

## Propiedades de objeto o de clase
Al definir propiedades se pueden distinguir dos tipos:
- **Propiedades de objeto**: que se pueden consultar en los objetos que se creen en esa clase.
- **Propiedades de clase** (o *estáticas*), que se pueden consultar sobre la propia clase. Las *propiedades estáticas son compartidas* por los todos los objetos de la clase (comparten valor). Para indicar que una propiedad es estática se usa el modificador de uso *static* (en UML se subrayan).
*Final puede usarse combinado con static* para definir propiedades constantes para todos los objetos de una clase.

## Acceso a propiedades de la clase
Para acceder a las propiedades de la clase *desde fuera* de la clase se utiliza el nombre de la clase, o de una referencia a un objeto, seguido del nombre de la propiedad separados por un punto.

## Otros modificadores de uso en propiedades
Las propiedades *transient no persisten* aunque el objeto tenga la capacidad de persistencia.
Una propiedad *volatile* no se copia a la cache del procesador sino que se mantiene en memoria principal. Esto evita problemas cuando la variable pueda ser utilizada desde varios threads de manera simultánea.

# Detalles de los métodos
## Paso de parámetros en Java
En los métodos de Java el paso de parámetros se realiza *siempre por valor*.
El paso de parámetros por valor consiste en *copiar el contenido* de la variable que se pasa en otra *variable local al método*.
Los parámetros que se le pasan a un método son:
- Tipos primitivos, que se pasan por valor.
- Referencias a objetos, que también se pasan por valor. Obsérvese en este caso que, al ser referencias, el estado del objeto pasado puede ser modificable.

## Métodos de objeto o de clase
En java se distinguen dos tipos de métodos:
- Métodos de *objeto* (o instancia), que se puede invocar sobre los objetos que se creen de esa clase.
- Métodos de *clase* (o *estáticos*), que se pueden invocar sobre la propia clase. En UML, los miembros estáticos se distinguen porque el nombre del método está subrayado.
 ![[Tema 2 Introducción al lenguaje Java(metodosObjetoOClase).png]]
## Detalles del modificador static
En Java, para indicar que un método es de clase (estático) se debe declarar usando la palabra *static*.
Dentro de un método estático no se pueden usar las propiedades de instancia de la propia clase, porque no hay instancia, aunque si se pueden usar propiedades estáticas
 ![[Tema 2 Introducción al lenguaje Java(detallesStatic).png]]
## Acceso a los métodos de clase
Para acceder a un método de clase *desde dentro* de la clase solo hace falta utilizar el identificador del método seguido de los paréntesis y los parámetros en su caso
Para acceder a un método de clase *desde fuera* de la clase se utiliza el identificador de la clase seguido del identificador del método, los paréntesis y los parámetros.
Todo programa en Java comienza su ejecución en un método static denominado *main*.

## Sobrecarga estática de los métodos
En una clase de Java es posible tener *dos métodos con el mismo identificador*, aunque los parámetros o el tipo devuelto deben ser diferentes.
Esto se conoce como *sobrecargar* el método.

## El constructor
La palabra reservada *new* seguida del nombre de la clase y unos paréntesis con o sin parámetros invoca al *constructor de la clase*. El constructor es una función especial que se ejecuta cuando se crea un objeto y se usa para *indicar sus propiedades*.
Un constructor puede o no tener *parámetros*, pero *no tiene tipo de retorno*. Siempre tienen el *nombre* de la clase a la que pertenecen.
Si no se define un constructor, Java añade un *constructor por defecto* sin parámetros. Este constructor no aparece en el código y solo crea el objeto.
 ![[Tema 2 Introducción al lenguaje Java(constructor).png]]
## Varios constructores
Una clase puede tener varios constructores, aunque no puede tener dos constructores que reciban los mismos parámetros.
En un constructor se pueden *iniciar incluso propiedades* finales.
Desde un constructor se puede llamar a otros constructores en la misma clase usando la palabra reservada *this* seguida de paréntesis con los parámetros correspondientes.
Habitualmente desde un constructor se *llama a otro*, si este último rellena parámetros básicos.
 ![[Tema 2 Introducción al lenguaje Java(variosCanstructores).png]]
## Destrucción de objetos y finalizadores
La máquina virtual de Java revisa periódicamente los bloques de memoria reservados buscando los que no están referenciados por ninguna variable para liberarlos.
La terea que realiza esta operación se llama *recolector de basura* (garbage collector) y se ejecura en segundo plano aprovechando los tiempos de baja intensidad de proceso.
Los *finalizadores* son métodos que se ejecutan *antes de la liberación* de la memoria ocupada por los objetos. Permiten tareas como cerrar ficheros, avisar a otros objetos...
El finalizador será el método llamado *void finalize()*.
Desde Java 9 *se desaconseja su uso (deprecated)* por la no determinidad de su momento de ejecución.

## Otros modificadores de uso en los métodos
Los métodos *native* se implementan en un lenguaje nativo de la máquina (C, C++…) y se asocian a Java usando bibliotecas de enlace dinámico mediante la Java Native Interface (JNI). 
Los métodos *synchronized* solo pueden ser ejecutados por un hilo en cada momento para cada objeto. 
Un método *strictfp* fuerza a Java a utilizar una aritmética flotante independiente del procesador para asegurar compatibilidad multiplataforma.

# Los arrays
## Declaración de arrays
Java proporciona una *clase array* como contenedor básico de objetos.
Para la declaración de una referencia a un objeto array se utiliza el tipo de objetos o tipo primitivo que contendrá el array seguido de una pareja de corchetes vacía.

## Inicialización de arrays
Como siempre, si una referencia a un array *no se inicializa* su valor es *null*.
Para crear un array, se utiliza la palabra reservada *new* seguida de una pareja de corchetes con las dimensiones del array.

Inicialmente, cada posición del array se rellena con el valor por defecto del tipo de datos asignado al array.
Una vez demensionad un array, *no es posible redimensionarlo*.
 ![[Tema 2 Introducción al lenguaje Java(inicializacionArray).png]]

## Declaración implícita
Java también permite declarar *implícitamente* la dimensión de un array inicializándolo con los elementos que contiene y sin especificar su dimensión.![[Tema 2 Introducción al lenguaje Java(eclaracionImplicitaArray).png]]

## Acceso a los elementos de un Array
El acceso a un elemento de un array se realiza utilizando la *variable y entre corchetes el índice del elemento* al que se desea acceder.
Los índices *comienzan por 0* y alcanzan como máximo un valor = a la dimensión del array menos 1
Java no permite sobrecargar símbolos para ejecutar métodos, pero en el caso de los array se ha hecho una excepción con los corchetes.

## Arrays de arrays de...
Java permite definir un *array compuesto de otros arrays* de tamaños variables.
Esta posibilidad se potencia con el uso de la propiedad *lenght* que tiene la clase array y que devuelve la dimensión del mismo.

## Métodos para el tratamiento de arrays
 java.util.Arrays incluye:
  ![[Tema 2 Introducción al lenguaje Java(javaUtilArrays).png]]

# Los paquetes
## Definición de paquetes en Java 
Las clases de Java se organizan en ficheros y los ficheros en paquetes. Java define una *correspondencia* entre los *directorios*, que contienen físicamente a los ficheros, y los *paquetes*, que los contienen lógicamente.
Java permite *organizar en forma de árbol los paquetes* gracias al uso de los directorios de ficheros.

## Declaración de los paquetes
La pertenencia de un fichero a un paquete se declara en la primera línea de código del fichero usando la palabra reservada *package* seguida del nombre del paquete.
Los nombres de los paquetes se suelen escribir en *minúsculas*, los nombres de las clases usando *UpperCamelCase* y los de los miembros usando *lowerCase*.
El anidamiento de paquetes en Java se representa usando el punto como separador.

## CLASSPATH
Un paquete debe residir en un directorio con su mismo nombre localizable a partir de alguno de los directorios declarados en la variable de entorno CLASSPATH o en el parámetro classpath en la invocación a la máquina virtual Java. 
En el ejemplo, el fichero Parking.java estará en el directorio automovilismo, que estará dentro del directorio util, que estará dentro del direcrtorio urjc, que será accesible desde el CLASSPATH.
 ![[Tema 2 Introducción al lenguaje Java(CLASSPATH).png]]

## Acceso a un paquete desde otro
Para acceder a un tipo definido en un fichero se puede usar su *nombre completamente calificado*, que consiste en separar por puntos los nombres ordenados de toda la rama de paquetes hasta el tipo.
Se puede utilizar la palabra reservada *import* al principio de un fichero para evitar usar nombre completamente calificados para acceder a un tipo.

## Visibilidad de los elementos de un paquete
Dentro de un paquete se comparten los elementos *friendly*.
No se puede acceder a los elementos friendly de otro paquete *aunque exista relación de anidamiento*.
En el ejemplo Coche ve la propiedad friendly radio de la rueda, pero Taller no la ve porque no está en el mismo paquete. 
El anidamiento de paquetes no tiene consecuencias en la visibilidad.
 ![[Tema 2 Introducción al lenguaje Java(visibilidadElementosPaquete).png]]