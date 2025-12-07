# Introducción 

Los objetivos del modelo relacional son:
- **Independencia física**: Almacenamiento/manipulación. Un cambio físico no afecta a los programas
- **Independencia lógica**: Añadir, eliminar o modificar elementos en la BD no debe repercutir en los programas o en los usuarios que acceden a ellos
- **Flexibilidad**: Ofrecer al usuario los datos en la forma más adecuada a cada aplicación
- **Uniformidad**: Las estructuras lógicas de los datos son tablas. Facilita la concepción y utilización de la BD por parte de los usuarios
- **Sencillez**: Por las características anteriores  y por los lenguajes de usuario sencillos, el modelo relacional es fácil de comprender y utilizar por parte del usuario final.


# Estructura de modelo relacional

 ![[Tema 6a Modelado Relacional Estático(ejemploDeRelación).png]]
## Elementos del modelo relacional
- **Relación**: Es la estructura básica del modelo relacional. Se representa mediante una *tabla*
- **Atributo**: Representa las propiedades de la relación. Se representa mediante una *columna*
- **Dominio**: Es el conjunto de valores válidos que toma un atributo
- **Tupla**: Es una ocurrencia de la relación. Se representa mediante una *fila*
- **Grado**: Es el número de atributos de la relación (número de <u>columnas</u> en la tabla)
- **Cardinalidad**: Es el número de tuplas de una relación (número de <u>filas</u> de la tabla)

	Características:
	- No puede haber tuplas duplicadas
	- El orden de las tuplas es irrelevante
	- La tabla es plana, es decir, en el cruce de un atributo y una tupla, solo puede haber un valor
	- El orden de los atributos no es significativo

 ![[Tema 6a Modelado Relacional Estático(ejemploElementosModeloR).png]]
 ![[Tema 6a Modelado Relacional Estático(comparacionTerminologicaModeloR).png]]

- **Vistas**: Las vistas son "tablas virtuales" que se definen sobre una o más tablas. Las vistas son ventanas sobre tablas "reales" de las que solo se almacena su definición; no tienen representación directa en el almacenamiento.
  ![[Tema 6a Modelado Relacional Estático(ejemploVistas).png]]

Clases de relación:
![[Tema 6a Modelado Relacional Estático(clasesDeRelacion).png]]
## Definición formal de relación

El *Universo del Discurso* (UD) de una base de datos relacional está compuesto por un conjunto de dominios {D<sub>i</sub>} y de relaciones {R<sub>i</sub>} definidas sobre los dominios.

Un *dominio* es un conjunto nominado, finito y homogéneo de valores atómicos. Cada dominio se especifica lógicamente mediante un nombre y un formato, el cual puede definirse por extensión (dando sus posibles valores) o por intensión (mediante un tipo de datos y ciertas restricciones, como un rango de valores).

Un *atributo* (A) es la interpretación de un determinado dominio en una relación, es decir, el "papel" que juega en la misma, si D es el dominio de A se denota: **D = Dom (A)**

Una relación definida sobre un conjunto de dominios D<sub>0</sub>...D<sub>n</sub> (no necesariamente distintos) es un subconjunto del producto cartesiano de los n dominios (n es el grado de la relación).
 R$\subseteq$ D<sub>1</sub>xD<sub>2</sub>x...D<sub>n</sub>

Un *esquema de relación (intensión)* se compone de un nombre de relación R, de un conjunto de n atributos {A<sub>1</sub>} y de un conjunto de n dominios (no necesariamente distintos) {D<sub>i</sub>}, donde cada atributo será definido sobre un dominio:
R (A<sub>1</sub>: D<sub>1</sub>, A<sub>2</sub>:D<sub>2</sub>,...A<sub>n</sub>:D<sub>n</sub>)

Una *relación r(R) (extensión)* es un conjunto de m elementos denominados tuplas {t<sub>j</sub>}. Cada tupla j es un conjunto de pares (<A<sub>1</sub>:v<sub>1j</sub>>,...<A<sub>i</sub>:v<sub>ij</sub>>,...<A<sub>n</sub>:v<sub>nj</sub>>) donde cada A<sub>i</sub> es el nombre de un atributo y v<sub>ij</sub> es un valor del correspondiente dominio D<sub>i</sub> sobre el que está definido el atributo:
r(R) = t<sub>j</sub> {(<A<sub>1</sub>:v<sub>1j</sub>>,...<A<sub>i</sub>:v<sub>ij</sub>>,...<A<sub>n</sub>:v<sub>nj</sub>>): v<sub>ij</sub> $\in$ D<sub>i</sub>}

 ![[Tema 6a Modelado Relacional Estático(relacionIntensionYExtension).png]]
## Claves
- **Clave candidata**: Es el conjunto no vacío de atributos que identifica <u>unívoca</u> y <u>mínimamente</u> cada tupla en una relación
- **Clave primaria (primary key)**: Es la clave candidata que elige el usuario para identificar las tuplas de la relación. Se dice que una clave primaria es compuesta cuando está formada por más de un atributo.
	- **Regla de integridad de entidad**: Ningún atributo principal, es decir, ningún atributo que forme parte de la clave primaria puede tomar un valor nulo.
- **Clave alternativa**: Aquella clave candidata que no halla sido elegida como clave primaria.
- **Clave ajena**: La clave ajena de una relación R2 es un conjunto no vacío de atributos cuyos valores han de coincidir con los valores de la clave primaria de una relación R1 referenciada (R1 y R2 no son necesariamente distintas)
	- La clave ajena y la correspondiente clave primaria han de estar definidas sobre los mismos dominios
	- La clave ajena sirve para relacionar tablas.
 ![[Tema 6a Modelado Relacional Estático(grafoRelacional).png]]
 ![[Tema 6a Modelado Relacional Estático(ejRelacionTablas1N).png]]
 Nombre-e es la clabe ajena de LIBRO, y referencia a EDITORIAL (nombre-e es clave primaria de EDITORIAL). Esta última tabla se denomina tabla referenciada.
 ![[Tema 6a Modelado Relacional Estático(reglaDeIntegridadReferencial).png]]
## Restricciones
### Derivadas de la definición de la relación:
- No hay dos tuplas iguales (obligatoriedad de la clave primaria)
- El orden de las tuplas no es significativo
- El orden de los atributos no es significativo
- Cada atributo sólo puede tomar un único valor del dominio sobre el que está definido, no admitiéndose por tanto, los grupos repetitivos. Se dice que una tabla que cumple esta condición está normalizada (o también que está en primera forma normal)
### Regla de integridad de entidad:
Ningún atributo que forme parte de la clave primaria puede tomar valor nulo

### Regla de integridad referencial:
Si una relación R2 tiene atributo(s) que es clave primaria de la relación R1, entonces los valores de dicho(s) atributo(s) deben concordar con los de la clave primaria o tener valores nulos.

### Restricciones semánticas:
- <u>Clave primaria</u> (PRIMARY KEY): Permite declarar un atributo o un conjunto de atributos como clave primaria de una relación por lo que sus valores no se podrán repetir ni se admitirán los nulos (o desconocidos).
- <u>Unicidad</u> (UNIQUE): Mediante la cual se indica que los valores de un conjunto de atributos (uno o más) no pueden repetirse en una relación. Esta restricción permite la definición de claves alternativas.
- <u>Obligatoriedad</u> (NOT NULL) de uno o mas atributos, con lo que se indica que el conjunto de atributos no admite valores nulos.
- <u>Integridad referencial</u> (FOREING KEY). Si una relación R2(relación que referencia) tiene un descriptor que es clave principal de una relación R1(relación referenciada), todo valor de dicho descriptor debe, bien concordar con un valor de la clave principal referenciada de R1, bien ser nulo. El descriptor es, por tanto, una clave ajena de la relación R2. Las relaciones R1 y R2 no son necesariamente distintas. Además, cabe destacar que la clave ajena podría ser a su vez parte (o la totalidad) de la clave primaria de R2.
 ![[Tema 6a Modelado Relacional Estático(ejemploSQL).png]]

### Opciones de borrado y actualización en la clave ajena:
- <u>NO ACTION</u>: Rechazar la operación
- <u>CASCADE</u>: propagar la modificación o borrar las tuplas de la tabla que referencia
- <u>SET NULL</u>: Poner valor nulo en la Clave Ajena de la tabla que referencia.
- <u>SET DEFAULT</u>: Poner valor por defecto en la Clave Ajena de la tabla que referencia.

 ![[Tema 6a Modelado Relacional Estático(ejemplo).png]]

### Otras restricciones semánticas:
- <u>Verificación</u> (CHECK): Comprueba, en toda la operación de actualización, si el predicado es cierto o falso y, en el segundo caso, rechaza la operación. La restricción de verificación se define sobre un único elemento (dominio, relación) y puede o no tener nombre.
- <u>Aserción</u> (ASSERTION): Actúa de forma idéntica a la anterior, pero se diferencia de ella en que puede afectar a varios elementos (por ejemplo a dos relaciones distintas) y su definición, por tanto, no va unida a la de un determinado elemento por lo que siempre ha de tener un nombre ya que la aserción es un elemento mas del esquema que tiene vida por si mismo.
- <u>Disparador</u> ("trigger"): Restricciones en las que el usuario pueda especificar libremente la respuesta (acción) ante una determinada condición. Así como las anteriores reglas de integridad son declarativas, los disparadores son procedimentales, siendo preciso que el usuario escriba el procedimiento que ha de aplicarse en caso de que se cumpla la condición.
# El modelo relacional y la arquitectura ANSI

![[Tema 6a Modelado Relacional Estático(modeloRArquitecturaANSI).png]]

**Valor NULO**: Se utiliza para representar información desconocida, inaplicable, inexistente, no válida, no proporcionada, indefinida, etc.
Necesidad de los valores nulos en base de datos:
- *Crear tuplas* (filas) con ciertos atributos desconocidos en ese momento
- *Añadir un nuevo atributo* a una relación existente; atributo que, en el momento de añadirse, no tendría ningún valor para las tuplas existentes en la relación.
- *Atributos inaplicables* a ciertas tuplas, por ejemplo, la editorial para un artículo (ya que un artículo no tiene editorial) 
# Las 12 reglas de Codd
Codd definió un conjunto de reglas que un SGBD debe satisfacer para que sea considerado relacional.
Se denominan las 12 Reglas de Codd, aunque en realidad definió 13 reglas para considerar un sistema relacional (Regla 0 - Regla 12). 

## Regla 1: Representación de la información
Toda información almacenada en una base de datos relacional debe representarse *explícitamente a nivel lógico*, y de manera *única*, por medio de *valores en tablas*. Podríamos decir que éste es el <u>principio básico del modelo relacional</u>

Los nombres de las tablas, nombres de los atributos y toda la info necesaria para el funcionamiento de la BD se representa mediante tablas: <u>Catálogo del sistema es una base de datos relacional</u>

## Regla 2: Acceso garantizado
Todo dato debe ser *accesible* mediante una combinación de un nombre de *tabla*, un valor de su *clave*, y el nombre de una *columna*. Es una forma de <u>insistir en la obligatoriedad de la clave primaria</u>.

## Regla 3: Tratamiento sistemático de valores nulos
Los valores nulos, información desconocida o inaplicable, han de ser tratados sistemáticamente por el sistema, el cual ha de ofrecer las facilidades necesarias para su tratamiento.

## Regla 4: Catálogo activo en línea basado en el modelo relacional
La representación de la metainformación (descripción de la base de datos) debe ser igual a la de otros datos y su acceso debe poder realizarse por medio del mismo lenguaje relacional que se utiliza para los demás datos; es decir, el *modelo de datos para la metainformación debe de ser también relacional*

## Regla 5: Sub-lenguaje de datos completo
Debe existir un lenguaje que permita un <u>completo manejo</u> de la base de datos (definición de datos, de vistas, manipulación de datos, restricciones de integridad, autorizaciones y gestión de transacciones). (SQL aporta todas)

## Regla 6: Actualización de vistas
- Toda vista teóricamente actualizable debe poder ser actualizada por el sistema
- Esta regla obliga al SGBD a ser capaz de <u>actualizar cualquier vista</u> que se haya definido en el sistema y que cumpla con las <u>condiciones teóricas</u> que hagan posible la actualización de los datos a través de ella.

## Regla 7: Inserciones, modificaciones y eliminaciones de alto nivel
- Todas las operaciones de manipulación de datos (consulta, inserción, modificación y borrado) deben operar sobre conjuntos de filas. (lenguaje no navegacional)
- Los sistemas existentes hasta el momento en el que surge el modelo relacional actuaban registro a registro, obligando al programador de una BD a navegar por la misma

## Regla 8: Independencia física de los datos
El acceso lógico a los datos debe mantenerse incluso cuando cambien los métodos de acceso o la forma de almacenamiento

## Regla 9: Independencia lógica de los datos
Los programas de aplicación no deben verse afectados por los cambios realizados en las tablas que estén permitidos teóricamente y que preserven la información
No habrá que modificar los programas de las aplicaciones, aunque se realicen cambios sobre las tablas, siempre que esos cambios mantengan la información que en ellas hubiese.

## Regla 10: Independencia de la integridad
Las reglas de integridad de una base de datos deben de ser definibles por media del sublenguaje de datos relacional y habrán de almacenarse en el catálogo de la base de datos (metabase), no en los programas de aplicación.

## Regla 11: Independencia de la distribución
- Debe existir un sublenguaje de datos que pueda soportar bases de datos distribuidas sin alterar los programas de aplicación cuando se distribuyan los datos por primera vez o se redistribuyan éstos posteriormente
- Un programa de aplicación no debe notar la diferencia entre trabajar sobre la base de datos cuando esta se encuentra centralizada en una máquina y cuando los datos de distribuyen entre varias máquinas. el sistema debe ser responsable de presentar los datos al usuario fina como si estuvieran en una única máquina
- Pero, para que un sistema sea relacional, no tiene obligatoriamente que dar soporte a las BBDD distribuidas.

## Regla 12: Regla de la no subversión
- Si un SGBD soporta un lenguaje de bajo nivel que permite el acceso fila a fila, éste no puede utilizarse para saltarse las reglas de la integridad expresadas por medio del lenguaje de más alto nivel
- EL SGBD debe controlar todos los accesos a la base de datos de forma que la integridad de la BD no pueda verse comprometida sin conocimiento del usuario y el admin de la BD.

## Regla 0: Regla básica
- Cualquier sistema que se anuncie como sistema gestor de bases de datos relacionales debe ser capaz de gestionar por completo las bases de datos utilizando sus capacidades relacionales.
- El SGBD relacional NO debe recurrir a operaciones NO relacionales para completar sus capacidades de gestión de datos (definición y manipulación).