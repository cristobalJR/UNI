# Sistemas de ficheros
## 1. Estructura Física y Lógica del fichero
**Fichero**:
- <u>Colección nominada de datos</u> que tienen entre sí una relación lógica, almacenados en memoria no volátil (soporte secundario) con una cierta organización.
- Un Fichero está constituido por una colección de Registros.
- Ejemplo: Fichero de "Personal" de una Empresa.
**Registro**(lógico):
- Colección de información relativa a una entidad particular.
- Es la unidad básica de información procesada por las aplicaciones.
- Un Registro está constituido por una colección de Campos lógicamente relacionados.
- Ejemplo: Docente, Departamento, etc...
  ![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(Registro).png|270]]
**Campo**:
- Es la <u>unidad mínima de información</u> de un registro.
- En general describen <u>atributos</u> de una entidad
- Ejemplo: Nº Empleado, nombre, dirección, ciudad, etc...


**Definición de Campos**:
- Nombre
- Longitud o tamaño
- Tipo de dato
**Definición de tipo de registro o formato de registro**:
- Colección de nombres de campo y tipos de datos

En un fichero es necesario distinguir dos estructuras distintas:
- *Estructura Lógica*: organización de los datos para los usuarios
- *Estructura Física*: organización de los datos para los soportes () discos, cintas, etc...
 ![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(registroFísico).png]]
 ¿Quién conecta la estructura lógica y la física?:
 - Bajo nivel: Sistema Operativo
 - Alto Nivel: la Aplicación
## 2. Objetivos de Diseño y Gestión de Fichero
Los <u>diseños lógicos y físicos</u> de los ficheros, así como su gestión, son factores clave para el buen funcionamiento de un sistema de información
El diseño lógico y el diseño físico de un fichero deben cumplir unos determinados requisitos a fin de alcanzar los objetivos de <u>eficacia y eficiencia</u> del sistema.
![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(logicoFisicoEficaciaEficiencia).png]]
## 3. Operaciones sobre un Fichero
![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos.png]]
\* Exigen una previa selección de los registros.

## 4. Organizaciones y Métodos de Accesos
Organización del fichero: La forma en que los registros se <u>estructuran</u> en un fichero (constitutiva o direccionada).
Método de acceso: modo de <u>localizar</u> los registros en un fichero.

El tipo de organización y el método de acceso son conceptos distintos pero relacionados. Existen restricciones entre ambos.
¿Cómo se decide la organización del Fichero?
- Archivos estáticos o dinámicos (¿Varía la info a lo largo del tiempo?)
- Ejecutar de la manera más eficiente las operaciones más frecuentes (leer, actualizar,...).
- En caso de que exista más de una organización apropiada, tomar una decisión de compromiso
El almacenamiento de los registros en un soporte físico se puede hacer de diferentes maneras:
- *Organización Consecutiva*: "colocando" los registros según su orden de llegada
- *Organización Direccionada*: dando la dirección física de donde se va a situar el registro
- Luego será posible añadir estructuras complementarias que faciliten el acceso a los registros (*Índices*)
El tipo de organización y el tipo de soporte están estrechamente relacionados.

**Tipos de organizaciones básicas**:
- Consecutivas: los registros se colocan físicamente uno a continuación del otro.
	- Sin Orden (seriales): no mantienen un orden lógico.
	- Con Orden (secuenciales): mantienen un orden lógico según una clave de ordenación.
- Direccionadas: Existe una relación entre un valor del registro (clave de direccionamiento) y la dirección física del registro.
	- Directas: El valor de la clave proporciona su dirección física.
	- Dispersas (hashing): la dirección física se obtiene aplicando un determinado algoritmo o función de transformación al valor de la clave.
- Basadas en índices: organización (consecutiva o direccionada) con índices.

**Métodos básicos de acceso a un registro**:
- Secuencial: implica el acceso a un fichero según el orden de almacenamiento de sus registros.
- Directo: implica el acceso a un determinado registro, sin que ello implique el acceso a los registros precedentes.
	- Acceso a un determinado registro por su dirección obtenida a partir del valor de una clave(acceso por direccionamiento)
	- Acceso a un registro que ocupa una determinada posición relativa dentro del fichero (acceso indexado)
## 5. Estructuras de Índices para los Ficheros
**Índices**
Estructuras de acceso auxiliares, utilizadas para aumentar la velocidad de recuperación de los registros en respuesta a ciertas condiciones de búsqueda
- Proporcionan caminos de acceso secundarios o alternativos para poder acceder a los registros sin afectar a la posición física de los registros.
- Se construyen en base a campos de indexación.
- Cualquier campo puede usarse para crear un índice,
- Un fichero puede tener múltiples índices sobre varios campos.

**Clasificación de los índices**:
- Índices ordenados de un solo nivel:
	- Primarios
	- de Agrupación
	- Secundarios
- Índices multinivel
- Índices basados en árboles B y B+

### Índices ordenados de un solo nivel:
- Estructura similar a la de los libros de textos:
	- Términos importantes ordenados alfabéticamente
	- Lista de número de páginas en las que aparece
- Para un fichero, la estructura de acceso se define sobre un solo campo del registro llamado *campo de indexación*
- El índice contiene:
	- Los valores del campo de indexación
	- Puntero a bloques del disco que contienen registros con ese valor en ese campo
- Los valores en el índice están ordenados:
	- El fichero índice es mucho más pequeño que los datos.
	- Se pueden realizar búsquedas binarias.
	- Los índices multinivel construyen índices sobre el fichero índice
- Índices más comunes:
	- *Índice primario*: sobre el <u>campo de ordenación que es único</u> para cada registro
		![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(ejIndicePrimario).png]]
	- *Índice de agrupación*: sobre el campo de ordenación (no es clave, varios registros pueden tener el mismo valor en este campo)
		![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(ejIndiceAgrupacion).png]]
	- *Índice Secundario*: sobre cualquier campo que no sea el de ordenación
		![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(ejIndiceSecundario).png]]


# Sistemas de Gestión de Base de Datos
## 1. El SGBD como interfaz entre el usuario y la BD
- El Sistema de Gestión de Bases de datos (SGB) actúa como interfaz entre la base de datos y los distintos niveles de gestión de la organización
- Integra los distintos subsistemas atendiendo a las necesidades de los usuarios en los tres niveles
Usuarios en una base de datos:
- Usuarios informáticos:
	- Diseñadores (lógicos/físicos)
	- Administradores
	- Analistas y programadores (desarrolladores)
- Usuarios finales
 ![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(usuariosBDD).png]]
## 2. Concepto y funciones del SGBD
SISTEMAS DE GESTIÓN DE BASES DE DATOS 
Conjunto coordinado de <u>programas, procedimientos, lenguajes</u>, etc. que suministra a los distintos tipos de usuarios los medios necesarios para <u>describir y manipular</u> los datos almacenados en la BDD, garantizado su <u>seguridad</u>
**Funciones esenciales de un SGBD**
- Función de *definición* o *descripción*:
	Mediante un LDD (lenguaje de definición de datos) suelen ser autocontenidos
	Los elementos de datos con:
	- Su estructura
	- Sus interrelaciones
	- Sus validaciones
- Función de *manipulación*:
	Permite buscar*, añadir, suprimir* y modificar* datos de la BD
	Mediante un LMD (Lenguaje de Manipulación de Datos). Lo cual supone:
	- Definir un criterio de selección (resp. usuario)
	- Definir la estructura externa a recuperar (resp. usuario)
	- Acceder a la estructura física (resp. sistema)
	- Por tipo de función
		- Un mismo LMD puede actuar como huésped y como autocontenido 
		- La mayoría permiten el uso en diferido y en conversacional
		- El programador precisa de un LMD: embebido y bastante procedimental
		- El usuario no informático precisa LMD: autocontenidos, poco procedimentales (declarativo) e interactivos
- Función de *control*:
	- Reúne las interfaces de los usuarios (interactuar a través de distintos niveles)
	- Suministra procedimientos para el administrador (control de acceso, seguridad, gestión de transacciones, auditorias)
	Mediante un LCD (Lenguaje de control de datos)
Otras facilidades: 
- Procedimientos para el administrador (reorganizadores, copias de seguridad y recuperación, cargas de ficheros, estadísticas y generadores de listados, etc.
- Interfaces con monitores de transacciones
## 3. La arquitectura ANSI/X3/SPARC
![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(estandarizacionInternacional).png]]
![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(estandarizacion2).png]]
![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(niveles).png]]
## 4. La Arquitectura y la Independencia Físico/Lógica
![[Tema 2 Sistemas de ficheros  y sistemas de gestión de base de datos(independencia LogicoFísica).png]]