# 1. Metodologías
Definición: Conjunto de métodos que se utilizan en una determinada actividad con el fin de formalizarla y optimizarla. Determina los pasos a seguir y cómo realizarlos para finalizar una tarea.
# 2. Metodología de la Programación
Optimización del proceso y el producto software. Métodos que guían la planificación y el desarrollo de software. Define qué hacer, cómo y cuándo durante todo el desarrollo y mantenimiento del proyecto.
# 3. Ciclo de Vida
Conjunto de fases por las que pasa el sistema que se está desarrollando desde que nace la idea inicial hasta que el software es retirado o reemplazado.
Debe definir los siguientes aspectos:
- Determinar el orden de las fases del proceso software
- Establecer criterios de transición para pasar de una fase a la siguiente
- Definir las entradas y salidas de cada fase
# 4. Tipos de Metodologías
**Metodologías pesadas o tradicionales**:
- Fases bien definidas, entregas al final, con requisitos y planificación bien definidos.
**Metodologías ágiles**:
- Continua interacción con el cliente, muchas entregas parciales y ciclos iterativos más cortos.
**Metodologías centradas en el usuario**:
- El enfoque y la interacción está en el usuario, pero las características prioritarias son la usabilidad y la accesibilidad.

## 4.1 Metodologías Tradicionales
Ciclo de vida en *cascada clásico*:
- El ciclo del desarrollo de sw es una sucesión de etapas que producen productos intermedios.
- Deben desarrollarse todas las fases para que el proyecto tenga éxito.
- Las fases continúan hasta que los objetivos se han cumplido.
- Si se cambia el orden de las fases el producto será de menor calidad
- *Limitaciones*:
	- No se permiten iteraciones.
	- Los requisitos se congelan al final del proyecto.
	- No existe un producto "enseñable" hasta el final del proyecto.
![[Tema 3 Metodologías y Ciclo software(cascadaClasico).png]]

## 4.2 Metodologías Ágiles
- La máxima prioridad es la satisfacción del cliente a través de entregas continuas evaluables.
- Mejora la motivación del equipo.
- Los cambios en los requisitos son bienvenidos en cualquier fase del desarrollo.
- Las entregas de software son frecuentes.
- Interesados y desarrolladores deben trabajar juntos.
- Los equipos reflexionan a intervalos frecuentes sobre  cómo ser más eficaces.
- Ls más usadas son:
	- XP (eXtreme Programming)
	- SCRUM
	- KANBAN
### 4.2.1 SCRUM
Se basa en **sprints**: iteraciones de desarrollo de duración recomendada 2-4 semanas.
- Durante cada *sprint* el equipo desarrolla  un incremento del software entregable.
- Existe un Product Backlog que contiene el conjunto de requisitos de alto nivel priorizados y que definen el trabajo a realizar.
- Existe una reunión de *Sprint Planning* donde se seleccionan (el Product Owner) los requisitos de alto nivel en los que se trabajará en el siguiente sprint.
Se centra en entregables pequeños y concretos trabajados por orden de prioridad.
*Roles* principales:
- **Product Owner**: Es la voz del cliente. Conoce las prioridades del proyecto, organiza y administra las tareas a realizar.
- **Scrum Master**: Asegura el seguimiento de la metodología guiando a los demás en la forma de actuar en cada fase.
- **Scrum Team**: Son los responsables de realizar las tareas asignadas.

<div style="display:flex; gap:24px; align-items:flex-start;">

  <!-- COLUMNA IZQUIERDA -->
  <div style="flex:1; padding-right:14px; border-right:2px solid #888;">
    <p><strong>Ventajas</strong></p>

    <div style="line-height:1.9;">
      · Flexibilidad a cambios<br>
      · Reducción del Time to Market<br>
      · Optimiza el proceso<br>
      · Alcance viable<br>
      · Mayor productividad del equipo<br>
      · Reducción de riesgos
    </div>
  </div>

  <!-- COLUMNA DERECHA -->
  <div style="flex:1; padding-left:14px;">
    <p><strong>Desventajas</strong></p>

    <div style="line-height:1.9;">
      · Equipo auto-organizado (puede ser ventaja pero tiene riesgos)<br>
      · Necesitas fuerte compromiso del equipo<br>
      · Y del cliente<br>
    </div>
  </div>

</div>

