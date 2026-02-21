# 1. Diagrama de Clases
Los diagramas de clases UML nos permiten denotar el contenido estático de, y las relaciones entre, clases. Se pueden dibujar todas las dependencias del código fuente entre clases.
![[Tema 5.1 UML(ejDiagramaClases).png]]

## 1.1 Asociación
Una asociación se puede dividir en *Agregación* si tiene una relación débil o *Composición* si tiene una relación fuerte. Gráficamente se representan con un rombo.
**Agregación**:  Si podemos hablar de que puede o no tener algo 0..1, 0..5, 0..many.
**Composición**: Las partes sólo existen asociadas al compuesto. (Sólo se accede a ellas mediante el compuesto, dicho de otra manera, ninguna otra clase las usa)
![[Tema 5.1 UML(agregacionComposicion).png]]
## 1.2 Herencia
![[Tema 5.1 UML(herencia).png]]
Las *subclases* heredan *características* de las clases de las que se *derivan y añaden* características específicas que las diferencias.
En el diagrama de clases, los atributos, métodos y relaciones de una clase se muestran en el nivel más alto de la jerarquía en el que son aplicables
# 2. Diagrama de Objetos
Muestra un conjunto de *objetos* u sus *relaciones* en un *momento particular* de la ejecución del sistema. Lo puedes considerar como una *instantánea de memoria*.
Es perfecto para describir un ejemplo de uso del sistema.
![[Tema 5.1 UML(diagramaObjetos).png]]
# 3. Diagrama de Secuencia
El diagrama de secuencia es un tipo de diagrama usado para modelar interacción entre objetos en un sistema según UML.
Solo hay que usarlos para representar partes complejas del programa.
![[Tema 5.1 UML(diagramaSecuencia).png]]
![[Tema 5.1 UML(diagramaSecuencia2).png]]
![[Tema 5.1 UML(diagramaSecuencia3).png]]

# 4. Diagrama de Colaboración
Los diagramas de colaboración contienen la misma información que los diagramas de secuencia. Sin embargo, mientras que los de *secuencia clarifican el orden de los mensajes*, los de *colaboración clarifican las relaciones entre objetos* 

Los objetos están conectados por relaciones llamadas enlaces. Existe un enlace donde un objeto puede enviar un mensaje a otro. Lo que viaja por esos enlaces son también mensajes.  Se dibujan como flechas más pequeñas. Los mensajes están etiquetados con el nombre del mensaje, su número de secuencia y las guardas que aplicar.

La estructura de puntos de la secuencia de números muestra la jerarquía de llamada. “1. Abro la nevera” “2. Cojo el jamón” “3. Me lo como como si no hubiera un mañana”.
![[Tema 5.1 UML(diagramasSecuenciaYColaboracion).png]]![[Tema 5.1 UML(diagramasSecuenciaYColaboracion2).png]]
# 5. Diagrama de Estado
Representan los flujos de trabajo de forma gráfica. Pueden utilizarse para describir el flujo de trabajo empresarial o el flujo de trabajo operativo de cualquier componente del sistema.
- Los rectángulos redondeados representan estados.
- El nombre de cada estado está en su compartimento superior.
- En el compartimento inferior están las acciones especiales que nos dicen qué hacer cuando se entra o se sale del estado.
- El punto de partida se representa con un circulo negro.
![[Tema 5.1 UML(diagramasEstado).png]]
![[Tema 5.1 UML(diagramasEstado2).png]]
# 6. Diagrama de Casos de Uso
Un caso de uso es una descripción del comportamiento de un sistema. Esa descripción está escrita desde el punto de vista de un usuario que acaba de oír que el sistema hace algo en particular. Un caso de uso captura la secuencia visible de eventos por los que pasa un sistema como respuesta a un estímulo de un único usuario.

Un evento visible es visible por un usuario. Los casos de uso no describen en ningún caso el comportamiento oculto. No discuten los mecanismos ocultos del sistema. Sólo describen aquellas cosas que un usuario puede ver.

![[Tema 5.1 UML(diagramaCasoDeUso).png]]