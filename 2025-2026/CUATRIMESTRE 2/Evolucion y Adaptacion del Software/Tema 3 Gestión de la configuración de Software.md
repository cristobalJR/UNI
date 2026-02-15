# 0. Ubicación
*Con respecto al tiempo*:
- **Mantenimiento**: Conjunto de actividades posteriores a la entrega del SW al cliente (actividades de soporte)$\neq$GCS
- **Gestión de la Configuración**: Conjunto de actividades de seguimiento desde el inicio hasta el final del proyecto software (circulación del sw)
**Gestión de la Configuración del Software** (GCS / SCM) $\equiv$ Gestión de los cambios
- *Definición*: Arte de identificar, organizar, revisar y controlar las modificaciones que sufre el software que construye un equipo de desarrollo
- Aplicado *durante* el proceso de software
- *Objetivo*: Maximizar la producción minimizando errores
## Estándar ISO 12207
- Este estándar establece un marco de referencia común *para los procesos del ciclo de vida software*, con unca terminología bien definida, que puede ser referenciada por la industria del software.
- En este marco se definen los *procesos*, *actividades*(que forman cada proceso) y *tareas*(que constituyen cada actividad) presentes en la adquisición, suministro, desarrollo, operación y mantenimiento del software.
- Entre los 8 *procesos de soporte*, está el de la Gestión de la Configuración del Software.
No prescribe una metodología concreta (cascada, ágil, etc.), sino que define **qué procesos deben existir y qué objetivos deben cumplir**.
### IEEE 1074
Su propósito es proporcionar un **marco detallado para definir y gestionar procesos de ciclo de vida del software dentro de una organización**.
- ISO/IEC 12207 → marco internacional general
- IEEE 1074 → interpretación/implementación detallada compatible
![[Tema 3 Gestión de la configuración de Software(ISO12207).png]]
## Ciclo Desarrollo y de Vida
- **Ciclo de desarrollo**: Requisitos, análisis, diseño, implementación y pruebas.
- **Ciclo de vida**: Adquisición, suministro, desarrollo, explotación y mantenimiento del sw (IEEE 1074/ISO 12207)
![[Tema 3 Gestión de la configuración de Software(UbicacionTemporal).png]]

# 0.5. Introducción al cambio
*Orígenes del cambio*:
- Cambios en el *mercado* o en el negocio que afectan a los requisitos
- Cambios hechos por el *cliente* en los datos o en la funcionalidad del sistema
- Reorganización de las *prioridades* del proyecto
- *Restricciones* de tiempo o dinero
![[Tema 3 Gestión de la configuración de Software(actividadesAutoproteccionCambio).png]]
# 1. Conceptos básicos
**Configuración software**:
- *Definición*: Conjunto de elementos que contienen toda la información producida por el proceso software.
- Los requisitos, diseño, e implementación que definen una versión particular de un sistema o de un componente del sistema *[IEEE Std. 610.12-1990]*
**Elemento de configuración**(EC):
- Agregación de hardware y/o software diseñada para la gestión de la configuración y que se trata como una única entidad en el proceso de gestión de configuración.
- <u>Ejemplos</u>:
	- Especificación de requisitos
	- Plan de gestión de configuración de software
	- Plan de proyecto
	- Modelo funcional del sistema
	- Código fuente
	- Plan de pruebas
- En definitiva *EC* es el <u>conjunto de partes</u> en las cuales se divide el <u>software</u> y sobre las que <u>se quieren controlar los cambios</u>.
**Línea base**(LB):
- Elemento central de la disciplina de GCS → Parte fundamental del desarrollo del software
- Marca el *final de una fase* del ciclo de vida del software
- Definición: Especificación o *producto* revisado que sirve como *base para el posterior desarrollo* y sólo puede cambiarse por procedimientos *formales* de control de cambios → *hito* en el plan de desarrollo
- Definición: Configuración operativa del sistema software *[IEEE Std. 610.12-1990]*
## Ejemplos
![[Tema 3 Gestión de la configuración de Software(Ejemplos).png]]
## Ejemplos EC y LB en un proyecto
![[Tema 3 Gestión de la configuración de Software(ejemplosECLB).png]]
## EC en un proyecto
![[Tema 3 Gestión de la configuración de Software(ECdeProyecto).png]]
## Procedimiento de modificación de una LB
![[Tema 3 Gestión de la configuración de Software(modificacionLineaBase).png]]
## Conceptos
**GCS**:
	Disciplina que identifica la configuración de un sistema en puntos discretos del tiempo, con el objetivo de controlar sistemáticamente los cambios de esa configuración y mantener su calidad y trazabilidad a través del ciclo de la vida del sistema.
**Traza**:
	Relación existente entre dos items de configuración (e.j. un requisito y las clases que lo implementan, una clase y sus casos de prueba).
**Trazabilidad del software**:
	Creación y gestión de trazas entre artefactos software sujetos a evolución (e.j. ligar requisitos con artefactos de diseño y código mas casos de prueba).
![[Tema 3 Gestión de la configuración de Software(matrizTrazabilidad).png]]
# 2. Actividades de la Gestión de la Configuración del Software 
## 2.1 Identificación de la configuración
Actividades para identificar, nombrar y describir las características del código, de las especificaciones, del diseño y de los elementos de datos a controlar en un proyecto.
![[Tema 3 Gestión de la configuración de Software(identificacionConfiguracion).png]]
### Ej. de nombrado:
![[Tema 3 Gestión de la configuración de Software(idConfiguracionEjemploDeNombrado).png]]
![[Tema 3 Gestión de la configuración de Software(ejemplodeNombrado).png]]
## 2.2 Control de la configuración
![[Tema 3 Gestión de la configuración de Software(controlConfiguracion).png]]
1. *Identificación de la necesidad del cambio y documentación*:
![[Tema 3 Gestión de la configuración de Software(idNecesidadCambioDocumentacion).png]]
2. *Análisis y evaluación de la petición de cambio*:
![[Tema 3 Gestión de la configuración de Software(analisisEvPeticionCambio).png]]
3. *Aprobación o desaprobación del cambio*:
![[Tema 3 Gestión de la configuración de Software(aprobacionCambios).png]]
4. *Implementación de los cambios*:
![[Tema 3 Gestión de la configuración de Software(implementacionCambios).png]]
![[Tema 3 Gestión de la configuración de Software(verificacionCambios).png]]

## 2.3 Contabilidad del estado de la configuración
![[Tema 3 Gestión de la configuración de Software(contabilidadEstadoConfiguracion).png]]
![[Tema 3 Gestión de la configuración de Software(contabilidadEstadoConfiguracion2).png]]
## 2.4 Auditorías y revisiones de la configuración
- *Definición*: Medio por el cual una organización asegura que los desarrolladores han hecho su trabajo de forma que satisfacen todas las obligaciones externas
- *Objetivo*: Asegurarse de que un cambio ha sido implementado correctamente.
- *Actividad costosa en tiempo y recursos*:
	- Dificultad técnica
	- Experiencia de los auditores (igual o superior a la los desarrolladores)
	- Imprescindible si se desea estar "razonablemente seguro" de la calidad del producto
- *Características* de la auditorías de configuración
	- Garantiza que los elementos auditados están completos y siguen el plan del GCS.
	- Garantizan que la LB corresponde con la descripción de sus elementos.
¿Cómo puedo garantizar que un cambio ha sido implementado correctamente?
![[Tema 3 Gestión de la configuración de Software(auditoriasConfiguracion).png]]
Realizada por el Grupo de Calidad (Comité de Control de la Calidad).
<u>Factores que</u> tiene en cuenta/<u>analizan</u>:
- ¿Se han seguido las pautas descritas en la “Petición de Cambio”?
- ¿Se ha informado de los cambios?
- ¿Se han actualizado los EC relacionados?
- ¿Se ha seguido los procedimientos del Plan de Gestión de la Configuración?
- ¿Es correcto (técnicamente) el cambio? → ¿Revisión Técnica Formal?
- ¿Se han actualizado correctamente todos los ECS afectados?
- ¿Se han aplicado correctamente los estándares de Ing. SW?
# 3. Documento de Plan de CGS
Plan de gestión de configuración software
![[Tema 3 Gestión de la configuración de Software(planGCS).png]]
*IEEE Std. 828-2005*
## 3.1 Introducción
*Objetivo*: Visión general simplificada
<u>Elementos</u>:
- *Propósito*: razón de ser y audiencia. Sistema el que se aplicará (breve).
- *Alcance*:
	- Descripción del Proyecto Software
	- Identificación de los EC
	- Software a incluir dentro del plan (ej: Software de pruebas)
	- Limitaciones y suposiciones de impacto (coste, calendario, capacidad de realizar el GCS)
	- Intereses del Plan: qué incluye y que no
- *Definiciones*: basadas en definiciones estándar (Puntos de control, liberación, línea base, etc.)
- *Referencias*: políticas, directivas, procedimientos, estándares, terminología, etc. Lista los documentos citados en cualquier parte del plan.
## 3.2 Gestión de la GCS
*Objetivo*: Asignación de responsabilidades y autoridades para las actividades de GCS
<u>Elementos</u>:
- *Organización*: unidades organizativas (técnicas y de gestión), roles y relaciones entre las unidades
- *Responsabilidades* de la GCS: asignación de actividades de GCS a las autoridades organizativas
- *Políticas*, directivas u procedimientos aplicable: impacto y uso
## 3.3 Actividades de GCS
*Objetivo*:  identificar las funciones y tareas (tanto técnicas como de gestión) requeridas para gestionar la configuración del sistema.
<u>Partes</u>: 
- *Descripción de las tareas* de GCS:
	- Identificación
	- Control de la configuración (cambios y versiones)
	- Contabilidad del estado(informes)
	- Auditorias y revisiones
- *Control de la interfaz*: coordinación entre los ECS y los cambios en los elementos externos (HW, SW de soporte, etc)
	- Interfaz software: acuerdos compartidos entre el programa y las otras entidades software
	- Interfaz hardware: acuerdos compartidos entre el programa y las características de cualquier hw: del entorno
- *Control del "subcontratista/vendedor"*: gestión del software adquirido (tanto terminado como en producción)
## 3.4 Calendarios GCS
*Objetivo*: establecer la secuencia y coordinación para las actividades de GCS
## 3.5 Recursos de GCS
*Objetivo*: identificar las herramientas software, técnicas, equipamiento, personal y entrenamiento necesario para las tareas de GCS
## 3.6 Mantenimiento del plan de GCS
*Objetivo*: identificar las actividades y responsabilidades necesarias para asegurar la planificación continua de la GCS durante el ciclo de vida del proyecto

# 4. Control de cambios
- Generar un mecanismo para llevar el control de los cambios
	- Protocolos de actuación para personas
	- Herramientas de automatización de cambios
- Aplicación de políticas de gestión de cambios informales salvo en el proceso de conversión de EC a Línea Base (crítico)
- Procesos a controlar:
	- Baja del objeto en la biblioteca 
	- Alta del objeto en la biblioteca 
	- Aplicación de la política de versiones sobre los objetos → control de versiones
- Elementos a definir:
	- Control de acceso al repositorio (seguridad y permisos) → "Autoridad de Control de Cambios"
	- Control de sincronización (concurrencia de acceso al repositorio)
- Tipos de control de cambios:
	- Control *informal*(o individual), antes de aprobarse un nuevo elemento
	- Control de *gestión* (u organizado), conduce a la aprobación de un nuevo elemento.
	- Control *formal*, se realiza durante el mantenimiento
## Control informal (individual)
Antes de aprobarse un nuevo elemento:
	El técnico responsable cambia la documentación como se requiere.
	Aunque se mantiene un registro informal de revisiones, no se ponen generalmente en el documento.
	El control individual se aplica durante las etapas más importantes del desarrollo del documento y se caracteriza por los cambios frecuentes.
## Control de gestión (organizado)
Conduce a la aprobación de un nuevo elemento.
	Implica un procedimiento de revisión y aprobación para cada cambio propuesto en la configuración.
	Este tipo de control ocurre durante el proceso de desarrollo pero es usado después de que se haya aprobado un elemento en la configuración software
	Este nivel de control de cambios se caracteriza por tener menos cambios que el control individual.
	Cada cambio es registrado normalmente y es visible para la gestión.
## Control de cambios formal
Ocurre durante la fase de mantenimiento del ciclo de vida software.
	Es decir, que el producto ya está implantado.
	El impacto de cada terea de mantenimiento se evalúa por un Comité de Control de Cambios (CCC)
	Dicho CCC, aprueba las modificaciones de la configuración software.

### Comité de Control de Cambios
Formado por los miembros de las organizaciones de usuarios/solicitantes de cambios y de desarrolladores.
	Para pequeños proyectos el CCC puede estar formado por uno de los representantes de los usuarios, solicitantes de cambios y desarrolladores.
	Para grandes proyectos, el CCC puede estar organizado en una jerarquía que trate los problemas del sistema, del hardware y del software por separado.
	El *CCC* puede llegar a formar parte del desarrollo del proyecto software y hacer las siguientes tareas:
		1. Analizar el impacto de cambios "revolucionarios" en el sistema, usando para asesorarse, las disciplinas técnicas que se requieran.
		2. Categorizar y priorizar los cambios conforme son pedidos y aprobados.
		3. Intervenir en los conflictos entre disciplinas y organizaciones que surgen para ser cambiados.
		4. Garantizar que las propiedades de mantenimiento, de registro y contabilidad se cumplan.
# Proceso del Control de Cambios

![[Tema 3 Gestión de la configuración de Software(procesoGestionCambios).png]]
![[Tema 3 Gestión de la configuración de Software(procesoControlCambios).png]]