# Introducción
La dinámica del modelo relacional permite la transformación entre estados de la base de datos que se realiza aplicando un conjunto de operadores al estado de origen, para obtener el estado destino

Estado origen (i) y estado final (j)  deben satisfacer las restricciones de integridad estática y dinámica (entre estados).

Lenguajes relacionales (lenguajes de especificación):
- *Algebraicos*, las operaciones se aplican sobre los operandos (relaciones) y el resultado es otra relación. (ej: Álgebra Relacional)
- *Predicativos*, (orientados a tuplas o a dominios), se define como el estado sin indicar las operaciones. (ej: Cálculo Relacional)

## Álgebra relacional
<u>Cierre relacional</u>: tanto los operandos como el resultado son relaciones.

| *Operadores primitivos* | ↘                                        | *Operadores derivados* | ↘                                                          |
| ----------------------- | ---------------------------------------- | ---------------------- | ---------------------------------------------------------- |
| Unarios:                | Proyección $\color{red}\pi$              | Binarios:              | Combinación o Join $\color{red}\theta$                     |
|                         | Selección $\color{red}\sigma$            |                        | Intersección $\color{red}\cap$                             |
|                         |                                          |                        | División $\color{red}:$                                    |
| Binarios:               | Unión $\color{red}\cup$                  |                        |                                                            |
|                         | Diferencia $\color{red}-$                |                        |                                                            |
|                         | Producto Cartesiano $\color{red} \times$ |                        | Se pueden expresar en función de los operadores primitivos |

## Proyección ($\color{red}\pi$):
La proyección de una relación sobre un conjunto de sus atributos es otra relación definida sobre estos, eliminando las tuplas duplicadas que hubieran podido resultar.
![[Tema 6b Modelado Relacional Dinámico(proyección).png]]
## Selección ($\color{red}\sigma$):
La selección de una relación mediante una expresión lógica (predicado de selección) da como resultado una relación formada por el conjunto de tuplas que satisfacen dicha expresión
![[Tema 6b Modelado Relacional Dinámico(seleccion).png]]
# Operadores primitivos
Dos relaciones son compatibles en si esquema si:
- Tienen el mismo <u>grado</u>.
- Si se puede hacer una <u>correspondencia</u> de cada uno de los atributos de las dos relaciones y si esos están definidos sobre el mismo dominio
## Unión ($\color{red}\cup$):
La unión de dos relaciones R1 y R2, compatibles en su esquema, es otra relación definida sobre el mismo esquema de relación, cuya extensión estará constituida por el conjunto de tuplas que pertenezcan a R1, a R2 o a ambas (<u>sin duplicar</u>).
![[Tema 6b Modelado Relacional Dinámico(union).png]]
## Diferencia ($\color{red}-$):
La diferencia de dos relaciones R1 y R2, compatibles en su esquema, es otra relación definida sobre el mismo esquema de relación, cuya extensión estará constituida por el conjunto de tuplas que pertenecen a R1 y no pertenecen a R2.
![[Tema 6b Modelado Relacional Dinámico(diferencia).png]]
## Producto Cartesiano ($\color{red} \times$):
El producto cartesiano de dos relaciones R1 y R2 de cardinalidades m1 y m2, respectivamente, es una relación definida sobre la unión de los atributos de ambas relaciones y cuya extensión estará constituida por las m1 x m2 tuplas formadas concatenando cada tupla de la primera relación R1 con cada una de las tuplas de la segunda relación R2.
![[Tema 6b Modelado Relacional Dinámico(productoCartesiano).png]]

## Resumen:
![[Tema 6b Modelado Relacional Dinámico(resumen).png]]
# Operadores derivados
## Combinación o Join ($\color{red}\theta$):
La combinación $\theta$ de dos relaciones R1 y R2 respecto a una cierta condición de combinación, es otra relación constituida por todos los pares de tuplas ti y tj concatenadas, tales que en cada par, las tuplas satisfacen la condición especificada.
La condición de combinación, en el caso más sencillo, está referida a dos atributos A1i y A2j, cada uno de los cuales pertenece a una de las relaciones, unidos por un operador de comparación. Cuando el operador es igualdad, se denomina combinación neutral (\*). 
![[Tema 6b Modelado Relacional Dinámico(combinacionJoin).png]]

"combinación expresada en función de operadores primitivos":
![[Tema 6b Modelado Relacional Dinámico(joinFuncionTiposPrimitivos).png]]
![[Tema 6b Modelado Relacional Dinámico(joinOperadoresPrimitivos).png]]
![[Tema 6b Modelado Relacional Dinámico(joinOperadoresPrimitivos)-1.png]]
## Intersección ($\color{red}\cap$):
La intersección de dos relaciones R1 y R2 compatibles en su esquema es otra relación definida sobre el mismo esquema de relación y cuya extensión estará constituida por las tuplas que pertenecen a ambas relaciones.
![[Tema 6b Modelado Relacional Dinámico(interseccionComparada).png]]
![[Tema 6b Modelado Relacional Dinámico(interseccion).png]]
## División ($\color{red}:$):
La división de una relación R1(dividendo) por otra R2 (divisor) es una relación R (cociente) tal que, al realizarse su combinación con el divisor, todas las tuplas resultantes se encuentran en el dividendo.
![[Tema 6b Modelado Relacional Dinámico(divisionFormula).png]]
![[Tema 6b Modelado Relacional Dinámico(division).png]]