# Introducción
## Modelado conceptual
El modelado conceptual se realiza en la <u>etapa de análisis</u> es importante <u>abstraer</u> detalles y representar sólo información relevante.

De los aspectos de <u>implementación</u> nos ocuparemos en la etapa de <u>diseño</u>. Se podrán utilizar distintos mecanismos de persistencia (Sistemas de BD, Sistemas de Ficheros, etc.) dependiendo de:
- El tipo de sistema (más o menos orientado a los datos)
- El volumen de info
- Los requisitos de eficiencia, etc...

En <u>análisis</u> interesa recoger la máxima cantidad de info posible, por lo que <u>necesitamos una técnica</u>:
- Independiente de los modelos o lenguajes de implementación
- Con capacidad semántica alta
- Lo más cercana posible al usuario

### Modelado entidad-interrelación (modelo E/R)
El modelo E/E fue pretende establecer una visión global de los datos de una organización o de un sistema de info, en un nivel de abstracción próximo al usuario e Independiente de las características del equipo donde después se vaya a instrumentar el sistema.

# Modelo E/R extendido
## Entidad
Denominamos <u>entidad</u> a la abstracción que permite representar aquellos objetos del mundo real que comparten características comunes

Cada uno de los objetos concretos que pertenecen a la entidad es un <u>ejemplar</u> u <u>ocurrencia</u> de entidad
	La entidad en sentido abstracto o genérico se refiere a un conjunto de elementos con características comunes, como por ejemplo la entidad PERSONAL. Una ocurrencia, relación o instancia de esta entidad podría ser Ana
El conjunto de ejemplares de una entidad en un momento dado será la <u>extensión</u> de ese tipo de entidad
### Tipos de entidad:
**Regular**:
	Aquella entidad cuyos ejemplares tienen existencia por si mismos
	![[Tema 4 Modelo E-R Extendido(representacionEntidad).png]]
**Débil**:
	Aquella entidad en la cual la existencia de un ejemplar depende de la existencia de un cierto ejemplar de otro tipo de entidad
	![[Tema 4 Modelo E-R Extendido(entidadDebil).png]]
### Interrelación:
Asociación o correspondencia entre entidades. Puede haber más de una interrelación entre dos entidades.
Cada asociación que se establece entre ejemplares concretos de las entidades que intervienen en una interrelación se denomina ejemplar u ocurrencia de interrelación
![[Tema 4 Modelo E-R Extendido(interrelacion).png]]
#### Propiedades interrelación
1. *Nombre*: la distingue del resto
2. *Grado*: Número de entidades que participan en una interrelación
	![[Tema 4 Modelo E-R Extendido(gradoInterrelacion).png]]
3. *Papel (Rol)*: Función que cada una de las entidades realiza en la interrelación
	![[Tema 4 Modelo E-R Extendido(cardinalidadInterrelacion).png]]
4. *Cardinalidad*: de una Entidad en una interrelación, se define como el número mínimo y máximo de ejemplares de una entidad que pueden estar interrelacionadas con un ejemplar de la otra, u otras entidades que participan en la interrelación
	![[Tema 4 Modelo E-R Extendido(cardinalidad).png]]

- *Cardinalidad Máxima* y *Tipo de correspondencia*: <u>Número máximo</u> de ocurrencias de cada entidad que pueden intervenir en la interrelación por cada ocurrencia del otro tipo de entidad
	![[Tema 4 Modelo E-R Extendido(tipoDeCorrespondenciaInterrelacion).png]]
- *Cardinalidad mínima 0*: <u>Cuando la ocurrencia de la interrelación es opcional</u>. Interesa cuando queremos almacenar las ocurrencias de la entidad, aunque no se dé la interrelación
	![[Tema 4 Modelo E-R Extendido(cardinalidadMinima).png]]

#### Tipos de correspondencia
**1:1** · Un empleado dirige <u>un</u> departamento y un departamento tiene <u>un</u> director
**1:N** · Un empleado pertenece a <u>un</u> departamento y a un departamento pueden perteneces <u>varios</u> empleados
**N:M** · Un empleado puede trabajar en muchos proyectos y en un proyecto pueden trabajar muchos <u>empleados</u>

## Atributo 
Cada una de las propiedades características o unidades de info básicas de una entidad o interrelación. Los atributos toman valores de un dominio.
 ![[Tema 4 Modelo E-R Extendido(atributos).png]]
Las distintas propiedades o características de una entidad o de una interrelación toman valores para cada ejemplar de éstas.
El conjunto de posibles valores que puede tomar una cierta característica se llama dominio. Se define dominio como un conjunto de calores homogéneos con un nombre.
Un *dominio* puede definirse:
- Por *intensión*: especificando el tipo de datos (por ejemplo, carácter (30) para el Nombre_empleado o fecha para la Fecha_alta)
- Por *extensión*: declarando el valor de cada elemento del dominio (como es el caso de Nombre_departamento)
### Tipos de atributos:
**Atributo compuesto**: Es aquél que se define sobre más de un dominio
 ![[Tema 4 Modelo E-R Extendido(atributoCompuesto).png]]
 **Atributo multivaluado**: puede tomar varios valores para una misma entidad particular
  ![[Tema 4 Modelo E-R Extendido(atributoMultivaluado).png]]
  **Atributo opcional**: puede tomar valores nulos
   ![[Tema 4 Modelo E-R Extendido(atributoOpcional).png]]
   **Atributo derivado**: aquél cuyos valores se obtienen a partir de otros ya existentes (ha de controlarse la redundancia)
   ![[Tema 4 Modelo E-R Extendido(atributoDerivado).png]]
Entre todos los atributos de un tipo de entidad han de existir uno o varios, que pueden ser simples o compuestos (pero mínimos), que identifiquen unívocamente cada uno de los ejemplares de este tipo de entidad. Se denominan **Identificador Candidato** (<u>IC</u>).
Uno de ellos se elige como **Identificador Principal** (<u>IP</u>), y el resto serán **Identificadores Alternativos** (<u>IA</u>)
 ![[Tema 4 Modelo E-R Extendido(identificadores).png]]

Cada uno de los objetos que pertenecen a la entidad es un ejemplar u ocurrencia de la entidad.
 ![[Tema 4 Modelo E-R Extendido(ocurrenciaEjemplar).png]]

### Dependencia en existencia y en identificación
Al igual que los tipos de entidad, los tipos de interrelación se clasifican en:
- *Regulares*: asocian dos tipos de entidades regulares
- *Débiles*: asocian un tipo de entidad débil con un tipo de entidad regular
 ![[Tema 4 Modelo E-R Extendido(dependenciaExistencia).png]]
Dependencia en *identificación*: tipo especial de dependencia en existencia
![[Tema 4 Modelo E-R Extendido(dependenciaIdentificacion).png]]
![[Tema 4 Modelo E-R Extendido(interrelacionesGrado2).png]]
![[Tema 4 Modelo E-R Extendido(coexistenciaInterrelacionesG2G3).png]]
### Generalización/Especialización 
\* diapo 29 HERENCIA
En el modelo E/R, se considera como un caso especial de asociación entre varias entidades(subtipos) y una entidad más general (supertipo), cuyas características 
son comunes a todos los subtipos.
La asociación que se establece entre los subtipos y el supertipo corresponde a la noción de es_un.
 ![[Tema 4 Modelo E-R Extendido(es_un).png]]
 
**Posibles generalizaciones**:
 ![[Tema 4 Modelo E-R Extendido(tiposGeneralizaciones).png]]

### Restricción de exclusividad
Dos o mas tipos de interrelaciones tienen una restricción de Exclusividad con respecto a un tipo de entidad que participa en ambas interrelaciones si cada ejemplar de dicho tipo de entidad sólo puede participar en uno de los tipos de la interrelación a la vez (en el momento en el que participa en uno, no puede en el otro)
 ![[Tema 4 Modelo E-R Extendido(exclusividad).png]]
 \* Un ejemplar de profesor participa en alguna de las dos interrelaciones una o varias veces
### Restricción de exclusión
Un profesor no puede estar impartiendo y recibiendo el mismo curso a la vez
 ![[Tema 4 Modelo E-R Extendido(exclusion).png]]
\* Todo ejemplar de profesor que este unido a ejemplar de curso mediante imparte, no podrá estar unido al mismo ejemplar de curso mediante recibe
### Restricción de inclusividad
Todo ejemplar del tipo entidad afectado que participa en uno de los tipos de interrelación tiene necesariamente que participar en la otra
 ![[Tema 4 Modelo E-R Extendido(inclusividad).png]]
\* El numero mínimo y máximo de cursos que tiene que recibir un determinado profesor para que se le permita impartir cursos (3 a n)
### Restricción de inclusión
Todo ejemplar de profesor que está unido a un ejemplar de curso mediante la interrelación imparte tiene necesariamente que estar unido al mismo ejemplar de curso mediante la interrelación recibe
 ![[Tema 4 Modelo E-R Extendido(inclusión).png]]
\* Si un profesor participa en imparte, tiene que participar en recibe
### Agregación
Interrelación que permite representar <u>tipos de entidad compuestos</u> que se obtienen por unión de otros más simples.
Al tipo compuesto nos referimos como el <u>todo</u>, mientras que los componentes son las <u>partes</u>.
En la agregación las cardinalidades mínima y máxima del tipo de entidad agregada siempre son (1,1) , y por eso no se indican.
Existen dos clases de agregaciones:
- *Compuesto*/*Componente*: Abstracción que permite representar que un <u>todo o agregado se obtiene por la unión de diversas partes o componentes</u> que pueden ser tipos de entidades distintas y que juegan diferentes roles en la agregación ![[Tema 4 Modelo E-R Extendido(compuestoComponente).png]]
- *Miembro*/*Colección*: Abstracción que permite representar un todo o agregado como una colección de miembros, todos de un mismo tipo de entidad y todos jugando el mismo rol![[Tema 4 Modelo E-R Extendido(miembroColeccion).png]]

# Resumen
![[Tema 4 Modelo E-R Extendido 2025-11-10 17.19.12.excalidraw|1000]]
![[Tema 4 Modelo E-R Extendido 2025-11-10 18.17.58.excalidraw|1000]]
![[Tema 4 Modelo E-R Extendido 2025-11-10 19.07.20.excalidraw]]
![[Tema 4 Modelo E-R Extendido 2025-11-10 19.32.12.excalidraw|800]]
![[Tema 4 Modelo E-R Extendido 2025-11-10 20.11.02.excalidraw]]