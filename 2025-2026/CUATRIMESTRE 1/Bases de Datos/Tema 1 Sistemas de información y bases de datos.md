# Sistemas de información
## Concepto de Sistemas
*Sistema* puede definirse como un conjunto de cosas ordenadamente relacionadas entre sí, y contribuyen a un determinado objetivo
- Todos están limitados, natural o artificialmente
- Fuera de los limites del sistema: *entorno*
- El sistema toma elementos del entorno (entradas) para elaborar productos que se devuelven al entorno (salidas)
## Clasificación de sistema según:
### Su relación con el entorno:
- Sistemas *abiertos*: Interactúan con su entorno, intercambiando energía, materia o información.
- Sistemas *cerrados*: No intercambian energía, materia o información con su entorno.
### Su naturaleza:
- Sistemas *concretos*: Son tangibles y físicos (ej: sistema solar)
- Sistemas *abstractos*: Son conceptuales o simbólicos (ej. sistema de ecuaciones matemáticas)
### Su origen:
- Sistemas *naturales*
- Sistemas *artificiales*
### Su complejidad:
- Sistemas *simples*
- Sistemas  *complejos*
### Su cambio en el tiempo:
- Sistemas *estáticos*
- Sistemas *dinámicos*: Controla su actuación en función de cómo las salidas cumplen los objetivos marcados.
### Su finalidad:
- Sistemas de *control*: Dirigen y regulan otros sistemas
- Sistemas de *información*: Recolectan, procesan y distribuyen  información.
## Concepto de SI:
- ### Datos:
Los datos no son mas que elementos de cualquier tipo que permiten describir ciertos eventos, o transacciones. Se trata de elementos que pueden estar almacenados e incluso clasificados, pero no organizados para dar respuesta a cuestiones especificas o significados concretos.
- ### Información:
Proviene de la ordenación de los datos de forma que tengan un significado concreto para que el que los recibe e incluso un valor determinado. El destinatario puede analizar el significado y obtener conclusiones.
- ### Conocimiento:
La información evaluada por una persona dentro de un contexto se convierte en conocimiento.
 Aplicaciones distintas y específicas para cada tarea de rutina propias del nivel administrativo. La información para la ayuda a la decisión se elaboraba manualmente o por programas ad hoc. • Posteriormente, se optó por utilizar una BD común que incorporara, sin redundancias innecesarias, la información necesaria para las distintas funciones. De este modo, se dispone de un único SI capaz de dar respuesta tanto a las necesidades de gestión como a las de decisión.
# De los Sistemas de Ficheros a las BBDD

## Orientación clásica: Sistemas orientados al proceso:
- **Estructura**: Almacena datos en archivos individuales en el disco duro.
- **Acceso**: Gestiona solo el acceso físico a los datos
- **Organización**: Los datos no están necesariamente organizados de manera estructurada
- **Seguridad**: Menos opciones de seguridad y control de acceso
- **Escalabilidad**: Menos eficiente para manejar grande volúmenes de datos
- **Redundancia**: Mayor probabilidad de duplicación de datos
### Inconvenientes
Pone énfasis en los tratamientos que reciben los datos, los cuales se almacenan en ficheros diseñados para una determinada aplicación.
- Ocupación inútil de memoria.
- Aumento en los tiempos de proceso.
- Inconsistencias.
- Dependencia de los datos respecto al soporte físico y a los programas (falta de flexibilidad frente a cambios)
- No son apropiados para sistemas de ayuda a la toma de decisiones
![[Tema 1 Sistemas de información y bases de datos(inconvenientes enfoque orientado a proceso).png]]
## Organización en Bases de Datos. Sistemas orientados a los datos:
- **Estructura**: Almacena datos en estructuras (ej. tablas) organizadas que si pueden estar relacionadas entre sí.
- **Acceso**: Gestiona tanto el acceso físico como lógico a los datos
- **Organización**: Los datos están organizados de manera estructurada y pueden ser fácilmente consultados.
- **Seguridad**: Ofrece opciones avanzadas de seguridad y control de acceso.
- **Escalabilidad**: Mas eficiente para grandes volúmenes de datos.
- **Redundancia**: Minimiza y controla la duplicación de datos.
# Ventajas e inconvenientes de BBDD respecto a ficheros 
### Ventajas BBDD:
- **DATOS**:
	- Independencia de éstos respecto de los tratamientos y viceversa.
	- Mejor disponibilidad de los mismos (usuarios no propietarios de los datos)
	- Mayor eficiencia en la recogida, codificación y entrada en el sistema

- **RESULTADOS**:
	- Mayor coherencia
	- Mayor valor informativo
	- Mejor y más normalizada documentación (semántica junto con los datos)

- **USUARIOS**:
	- Acceso más rápido y sencillo de los usuarios finales
	- Más facilidades para compartir los datos por el conjunto de los usuarios
	- Mayor flexibilidad para atender a demandas cambiantes
### Inconvenientes BBDD:
- Coste de adquisición de los productos (PERO: soluciones gratuitas como MySQL o MaríaDB)
- Instalación costosa (hardware, requisitos software)
- Necesidad de personal especializado
- Implantación y optimización puede ser compleja
- Desfase entre teoría y práctica
# Concepto de Base de Datos
## Definiciones:
“Colección de datos interrelacionados almacenados en conjunto sin redundancias perjudiciales o innecesarias; su finalidad es servir a una aplicación o más, de la mejor manera posible; los datos se almacenan de modo que resulten independientes de los programas que los usan; se emplean métodos bien determinados para incluir nuevos datos y para modificar o extraer los datos almacenados”, (Martin, 1975).

“Colección o depósito de datos, donde los datos están lógicamente relacionados entre sí, tienen una definición y descripción comunes y están estructurados de una forma particular. Una base de datos es también un modelo del mundo real y, como tal, debe poder servir para toda una gama de usos y aplicaciones”, (Conference des Statisticiens Européens, 1977).

“Conjunto de datos de la empresa memorizado en un ordenador, que es utilizado por numerosas personas y cuya organización está regida por un modelo de datos”, (Flory, 1982)

“Conjunto estructurado de datos registrados sobre soportes accesibles por ordenador para satisfacer simultáneamente a varios usuarios de forma selectiva y en tiempo oportuno”, (Delobel, 1982).

“Colección no redundante de datos que son compartidos por diferentes sistemas de aplicación”, (Howe, 1983).

“Colección integrada y generalizada de datos, estructurada atendiendo a las relaciones naturales de modo que suministre todos los caminos de acceso necesarios a cada unidad de datos con objeto de poder atender todas las necesidades de los diferentes usuarios”, (Deen, 1985).

“Colección de datos interrelacionados”, (Elsmari y Navathe, 1989). 