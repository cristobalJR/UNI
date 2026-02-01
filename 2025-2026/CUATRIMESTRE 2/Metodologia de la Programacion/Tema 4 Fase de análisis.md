# 1. Fase de análisis

 ![[Tema 4 Fase de análisis.png]]
- El objetivo es extraer los requisitos que debe tener el software que se va a desarrollar.
- Análisis del problema y especificación completa del comportamiento externo que se espera del sistema software que se va a construir, así como de los flujos de información y control.
- Es sumamente importante porque errores en esta fase pueden generar un producto que no satisfaga las necesidades de los usuarios.
 ![[Tema 4 Fase de análisis(partesAnalisis).png]]
 - Se debe comprender el problema.
 - Los requisitos han de determinarse siguiendo una aproximación descendente.
 - Se debe representar la *información*, *función* y *comportamiento* del sistema.
 - Se debe separar el *qué* del *cómo*
## 1.1 Tareas Fase de Análisis
- **Educción de requisitos**:
	- Identificar los requisitos que se obtienen de los usuarios.
- **Análisis de los usuarios y tareas**:
	- Identificar potenciales usuarios del sistema, su jerarquía y las tareas a realizar.
- **Representación**(modelización):
	- Registrar los requisitos: lenguaje formal, UML, maquetas...
- **Validación**:
	- Examinar inconsistencias entre requisitos.
### 1.1.1 Educción de requisitos
Proceso por el cual los *clientes* exponen, formulan, *articulan* y comprenden sus *requisitos* mediante reuniones, brainstorming...
- Análisis del problema.
- Identificar usuarios potenciales.
- Identificar fuente de datos.
- Recopilar información y hechos.
- Preparar u preguntar cuestiones concisas y concretas.
- Analizar la información obtenida.
- Priorizar
## 1.2 Tipos de requisitos
**Funcionales**:
- Acciones fundamentales que tiene que hacer el sistema.
**No Funcionales**:
- Requisitos de interfaz: menús, ventanas...
- Requisitos operacionales: modos de operación, back-ups...
- Requisitos de seguridad: niveles de acceso...
- Requisitos de portabilidad y mantenimiento.
- Requisitos de recursos: memoria y almacenamiento...
- Requisitos de rendimiento: tiempo de respuesta, nº users...
- ...
## 1.3 Análisis de requisitos
- **Qué**:
	- Proceso mediante el cual se determina que requisitos son aceptables y definen cuáles van a formar parte del producto.
- **Cómo**:
	- Evaluación de la viabilidad técnica y económica.
	- Valoración de riesgos.
	- Clasificación de requisitos en: obligatorios, desechables,...
## 1.4 Representación de requisitos
- **Qué**:
	- Proceso de registrar los requisitos de una o más formas
- **Cómo**:
	- Lenguaje natural: catálogo de requisitos.
	- Lenguaje formal
	- Modelos
	- Diagramas
	- Maquetas
	- ...
*Especificación en lenguaje natural*:
- Se expresan de forma individual, organizados jerárquicamente(a distintos niveles de detalle), pueden enumerarse.
- Claros y concretos (sin ambigüedades)
	- Por ejemplo, sin puntos suspensivos, sin rodeos ni figuras retóricas.
- Completos y consistentes.
- Han de indicar lo que se espera que haga el sistema, su justificación y en su caso criterios de verificación aplicables.
<u>Los requerimientos funcionales</u>:
- Deben estar redactados de forma que sean entendibles por usuarios no técnicos.
- Deben especificar el comportamiento externo del sistema y, evitar si es posible, establecer características de su diseño.
- Se pueden numerar para establecer la prioridad (se distingue entre obligatorio y deseables)
<u>Los requisitos no funcionales</u>:
- Han de especificarse cualitativamente, siempre que sea posible (verificación de su cumplimiento).
## 1.5 Herramientas de especificación
Durante el desarrollo del sistema, se deberán moldear tanto los datos empleados por el sistema como los procesos que realizan tareas sobre esos datos:
*Modelado de datos*:
- Diagramas de entidad/relación
- Diagramas CASE*Method
- Diagramas de clases en UML
- Diccionarios de datos
- ...
*Modelado de procesos*:
- Diagrama de flujo de datos
- Diagramas de estados (autómatas finitos)
- Casos de Uso