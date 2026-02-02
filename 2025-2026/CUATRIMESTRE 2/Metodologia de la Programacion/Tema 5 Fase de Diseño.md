![[Tema 5 Fase de Diseño.png]]

# 1. Fase de diseño

- Es el proceso de definición de la arquitectura, componentes, módulos, interfaces, procedimientos de prueba y datos de un sistema software para satisfacer unos requisitos especificados.
- Se pasa del qué al cómo:
	- ¿Qué hay que hacer? -> Especificación de requisitos.
	- ¿Cómo hay que hacerlo? -> Especificaciones de diseño.
- En esta fase hay dos niveles:
	- *Alto* nivel.
	- *Bajo* nivel.
- La idea es ir detallando cada vez los aspectos del software que vamos a realizar.
- Para ello usaremos UML.
# 2. Unified Modeling Language(UML)
En los 90 *existían muchos* métodos de *análisis y diseño orientado a objetos*.
- Mismos conceptos, distinta notación.
- Mucha confusión.
- "Guerra de los métodos".
En *1994, Booch, Rumbaugh y Jacobson* deciden *unificar* los métodos (UML).
# 3. Ventajas de UML

- Reunir los puntos fuertes de cada método
- Idear nuevas mejoras
- Proporcionar estabilidad en el mercado
	- Proyectos basados en un lenguaje maduro
	- Aparición de potentes herramientas
- Eliminar la confusión de los usuarios
# 4. Objetivos en el diseño de UML

- Modelar sistemas, desde los requisitos hasta los artefactos ejecutables, utilizando técnicas orientadas a objetos.
- Cubrir las cuestiones relacionadas con el tamaño propias de los sistemas complejos y críticos.
- Lenguaje utilizable por personas y máquinas.
- Encontrar un equilibrio entre expresividad y simplicidad.
# 5. UML y modelado
UML es el lenguaje para visualizar, especificar, construir y documentar los artefactos (modelos) de un sistema que involucra una gran cantidad de software, desde la perspectiva Orientada a Objetos.
## 5.1 ¿Por qué modelamos?

- Una empresa software con éxito es aquella que produce de manera consistente software de calidad que satisface las necesidades de los usuarios
- El modelado es la parte esencial de todas las actividades que conducen a la producción de software de calidad
- Un modelo es una especificación de la realidad para comprender mejor el sistema que estamos desarrollando
- Cuatro utilidades de los modelos:
	- Visualizar cómo es o queremos que sea el sistema.
	- Especificar la estructura y comportamiento del sistema.
	- Proporcionan plantillas que guían la construcción del sistema.
	- Documentan las decisiones.
## 5.2 ¿Por qué las empresas no modelan?

- La mayor parte de las empresas software no realizan modelado.
- El modelado requiera:
	- Aplicar un proceso de desarrollo.
	- Formación del equipo en las técnicas.
	- Tiempo
# 6. Diseño UML
## 6.1 Modelado de la estructura
*Diagrama de Clases*.
- Clases y Objetos
 ![[Tema 5 Fase de Diseño(clasesObjetos).png]]
 - Todos los reyes tienen aspectos en común.
 - Podemos representar esos aspectos en una clase.
 - Reyes concretos serían instancias (objetos) de dicha clase.
   ![[Tema 5 Fase de Diseño(diseñoClasesObjetos).png]]
<div style="display:flex; gap:24px; align-items:flex-start;">

  <!-- COLUMNA IZQUIERDA -->
  <div style="flex:1; padding-right:14px; border-right:2px solid #888;">
    <p><strong>Clase</strong></p>

    <div style="line-height:1.9;">
      · Declara propiedades (atributos) de todas las instancias.<br>
      · Declara operaciones (métodos) aplicables a todas las instancias.<br>
    </div>
  </div>

  <!-- COLUMNA DERECHA -->
  <div style="flex:1; padding-left:14px;">
    <p><strong>Objeto</strong></p>

    <div style="line-height:1.9;">
      · Da valores a los atributos declarados en la clase.<br>
      · Reacciona a invocaciones de los métodos declarados en la clase, usando como estado los valores de sus atribu<br>
    </div>
  </div>

</div>
### Herencia
Las herencias son jerarquías de especialización de clases. Herencia de propiedades y operaciones.
![[Tema 5 Fase de Diseño(herencia1).png]]
![[Tema 5 Fase de Diseño(herencia2).png]]
- Un objeto de una clase hija hereda las propiedades de la clase padre.
- Podemos invocarle las operaciones definidas en la clase padre.
- La substitución segura de supertipos por subtipos.
	- Todas las tarjetas de crédito y de débito son tarjetas bancarias
	- Existen tarjetas bancarias que no son de crédito ni de débito
	- No hay tarjetas que sean de crédito y de débito a la vez
	![[Tema 5 Fase de Diseño(herencia3).png]]
### Clases Abstractas
Una clase abstracta no puede instanciarse.
![[Tema 5 Fase de Diseño(clasesAbstractas).png]]
### Herencia Múltiples
- Una clase puede heredar de varias.
- No es posible en Java, pero sí en otros lenguajes de programación como C++.
![[Tema 5 Fase de Diseño(herenciaMultiple).png]]
### Asociaciones
Los objetos no están aislados, necesitan "conocerse" para poder invocar métodos de otros objetos.
- Esta funcionalidad se implementa mediante colaboraciones de objetos.
Conceptualmente, se representa mediante un enlace (una línea) entre las dos clases.
- En programación, esto significa que un objeto tiene una referencia a otro objeto (un atributo).
**Multiplicidad**:
	Con cuantos objetos de destino se puede relacionar un objeto fuente y viceversa.
**Roles**:
	Nombres en los extremos de las asociaciones.
![[Tema 5 Fase de Diseño(rolesMultiplicidad).png]]
**Navegación**:
	Indica si un objeto puede acceder al otro.
	![[Tema 5 Fase de Diseño(navegacionAsociaciones).png]]
**Herencia de asociaciones**:
	Una asociación declara en la clase base, se hereda en las clases hijas.
### Composición y Agregación
Hay relaciones con semánticas especiales:
- $\blacklozenge$ *Composición* (una hecha de partes)(partes en solo un compuesto)
- $\diamondsuit$ *Agregación* (composición débil)(partes pueden estar en varios compuestos)
![[Tema 5 Fase de Diseño(composicionAgregacion).png]]
![[Tema 5 Fase de Diseño(composicionAgregacion2).png]]
## 6.2 Modelado de comportamiento
Un diagrama de clases nos dice la estructura de la aplicación, pero no el comportamiento.
- ¿Qué hace cada método?
- ¿Cómo cambia el estado de un objeto ante invocaciones de métodos?
- ¿Cómo colabora con un conjunto de objetos para realizar una tarea?
- ¿Qué hace cada método?
	- Pseudocódigo
	- Diagrama de actividad
- ¿Cómo cambia el estado de un objeto ante invocaciones de métodos?
	- Diagrama de transición de estados
- ¿Cómo colabora un conjunto de objetos para realizar una tarea?
	- Diagramas de secuencias
### 6.2.1 Diagrama de Transición de Estados
- Van asociados a una clase.
- Describen cómo evoluciona cuando se le invocan métodos.
- Similar a un autómata finito.
- Van asociados a una clase
	 ![[Tema 5 Fase de Diseño(claseDiagramaEstados).png]]
- Describen cómo evoluciona cuando se le invocan métodos.
	![[Tema 5 Fase de Diseño(diagramaTransicionEstados).png]]
- Estados jerárquicos.
- Guardas y acciones en las transiciones.
	![[Tema 5 Fase de Diseño(estadosJerarquicos).png]]
### 6.2.2 Diagrama de Secuencias
- Representa una secuencia de mensajes que intercambia un conjunto de objetos.
- Cada objeto tiene una línea de vida (representada verticalmente)
	- El paso del tiempo se representa de manera descendente.
	- Invocación de mensaje: flechas entre líneas de vida.
	- Cajas de activación.
![[Tema 5 Fase de Diseño(diagramaSecuencia).png]]
![[Tema 5 Fase de Diseño(diagramaSecuencia2).png]]

**Operadores**: 
![[Tema 5 Fase de Diseño(diagramaSecuenciaOperadores).png]]
- *Alternativa(alt)*: elección (mediante una guarda) de una interacción. Múltiples fragmentos, sólo se ejecuta el que cumple la guarda.
- *Opción(opt)*: equivalente a un operador alt con un solo fragmento. Equivalente al if en programación.
- *Bucle(loop)*: el fragmento se ejecuta múltiples veces. La guarda indica cómo realizar la iteración.
- Existen otros como neg, par, critical, ref...
## 6.3 Matriz de Trazabilidad
Al finalizar el diseño (detallado) de la aplicación, es necesario comprobar que todos los requisitos educidos en la fase de análisis del problema tienen su correspondiente representación en el dominio de la solución a implementar.
![[Tema 5 Fase de Diseño(matrizTrazabilidad).png]]