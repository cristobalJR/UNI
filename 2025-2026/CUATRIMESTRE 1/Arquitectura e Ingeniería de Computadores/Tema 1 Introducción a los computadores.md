![[Tema 1 Introducción a los computadores 2025-10-06 17.00.33.excalidraw]]# Conceptos básicos
## Arquitectura / Organización
- **Arquitectura**: Arquitectura (arquitectura de repertorio de instrucciones, instruction set architecture, ISA): atributos del sistema visibles a nivel de la programación en ensamblador o que tienen impacto directo en la ejecución lógica de un programa. Ejemplos: repertorio de instrucciones, tamaño de los datos y buses, mecanismos de E/S, modos de direccionamientos a memoria, etc.
- **Organización**:Organización (microarquitectura): unidades operacionales y sus interconexiones en la especificación de una arquitectura. Ejemplos: detalles del hardware que son transparentes a nivel de programación, como señales lógicas, interfaces ordenador‐periféricos, tecnología de memoria, memoria caché, memoria virtual, tipo de disco duro (magnético/estado sólido), sistema operativo, etc.
# Modelo de computador
## Operaciones de un Computador
  ![[Tema 1 Introducción a los computadores (OperacionesComputadores).png]]
  Operaciones que realiza un computador:
  - Almacenamiento
  - Procesamiento
  - Movimiento
  - Control
## Unidades Funcionales
 ![[Tema 1 Introducción a los computadores(EstructuraComputador).png]]
 La arquitectura de von Neumann es el modelo abstracto de computador que se usa desde los años 40, clasifica las partes internas del computador en 4 unidades funcionales:
 - **Unidad central de proceso** (microprocesador): 
	 - Es el elemento encargado de leer las instrucciones de los programas y ejecutarlas una a una.
	 - Controla y sincroniza todos los elementos del ordenador para que actúen ordenadamente.
	 - Está implementada en un circuito integrado o chip.
	 - Hoy en día decenas de miles de millones de transistores.
- **Memoria**:
	- Cada posición de memoria tiene una dirección que la identifica.
	- Organizada en jerarquía, entre otros niveles:
		- *Memoria principal*(Random Access Memory, RAM): Contiene los datos y los programas actualmente en uso.
		- *Memoria secundaria*(Discos duros, CDs, memorias USB...): Que también pueden considerarse periféricos de almacenamiento.
- **Unidad de entrada/salida**: Comunica el procesador con los periféricos.
	- *Entrada*
	- *Salida*
	- *Entrada/Salida*
- **Buses de interconexión**: El bus del sistema se divide en:
	- *Bus de datos*: Transporta datos que se transfieren entre dos elementos del computador.
	- *Bus de direcciones*: Transporta las direcciones o posiciones de memoria a las que se quiere acceder para leer o escribir.
	- *Bus de control*: Transporta el resto de las señales necesarias para activar o desactivar en el momento adecuado cada uno de los componentes del computador.

![[Tema 1 Introducción a los computadores (modelo von Neumann).png]]
> [!info] Modelo von Neumann
# Microprocesadores
La **CPU** se encarga de: 
- Ordenar a los restantes elementos del computador que realicen las funciones requeridas por las instrucciones. 
- Ejecutar las operaciones aritméticas y lógicas necesarias para la ejecución de las instrucciones.

Componentes de la CPU:
- *Unidad de tratamiento de datos.* 
- *Unidad de control.*

   ![[Tema 1 Introducción a los computadores(ComponentesCPU).png]]
   
## Unidad de tratamiento
La Unidad de tratamiento o procesamiento de datos, no toma decisiones, hace lo que la UC le ordene, su cometido es realizar las operaciones (procesar los datos), haciendo los cálculos necesarios para ejecutar los programas.
Se compone de:
- **Banco de registros**: Elemento de memoria que permite almacenar datos temporalmente a los que se accede muy rápidamente.
- **Unidad aritmético-lógica**(ALU): es un circuito combinacional relativamente simple capaz de realizar operaciones sencillas.
	- Operaciones aritméticas: Sumar, restar, multiplicar, dividir...
	- Operaciones lógicas: And, or, not...
	- Otras operaciones: Desplazamiento de bits,...

Al conjunto de registros, ALU, multiplexores, conectores, etc., por los que van pasando los datos que se utilizan en los programas se le denomina camino (ruta o cauce) de datos.
### Registros
Un registro es un conjunto de biestables sincronizados con la misma señal de reloj, es un elemento de memoria:
- Volátil (se borran al apagar el PC)
- De acceso muy rápido (cúspide jerarquía de memoria)
- De poca capacidad (8, 16, 32, 64,128 bits)
Se organizan en bancos de registros

## Unidad de control
Es la parte de la CPU que controlaba y coordinaba todos los componentes del computador, a modo de director de orquesta.
Normalmente se implementa mediante un circuito secuencial (máquina de estados) que trabaja en un bucle infinito pasando de estado a estado controlado por un reloj.
	Cada estado representa una configuración concreta del circuito, con algunos elementos activos y otros no.
Sus labores son:
- Leer una a una las instrucciones del programa en ejecución.
- Decodificarla (identificar que instrucción es), calcular donde están sus operandos, buscarlos, etc...
- Ejecutar la instrucción, para lo cual manda las señales que activan o desactivan el resto de componentes del computador en el instante adecuado. Para esto, se basa en la señal de reloj, y así sincronizar las operaciones.

Tiene registros especiales:
- *Contador de programa*(program counter, PC): Almacena de dirección de la siguiente instrucción que hay que ejecutar.
- *Registro de instrucción*(instruction register, IR): Almacena la instrucción que está ejecutando durante todo el tiempo que necesita para completar su ejecución.
	- Según el tipo de camino de datos, cada instrucción puede ejecutarse de principio a fin en un solo ciclo del reloj (uniciclo), o bien, en un número entero de ciclos, aunque diferente para cada tipo de instrucción (multiciclo).

 ![[Tema 1 Introducción a los computadores(UC).png]]
 La lógica de control es un circuito que, recibiendo como entrada una instrucción, devuelve como salida todas señales de control para cada componente del computador. Para una única instrucción normalmente hay que dar varias órdenes a diferentes componentes, y muchas veces estas órdenes deben ejecutarse en un orden determinado.

### La unidad de control además:
- Detecta y resuelve problemas, como situaciones anómalas de conflicto.
- Detecta y atiende interrupciones (Señalas enviadas por otros componentes al procesador para que interrumpa la ejecución de la instrucción actual para que pase a atenderlos).
- Se comunica con los periféricos.
### El circuito de la UC dispone de:
#### Entradas:
- Código de operación: Bits de la instrucción (almacenada en el IR) que identifican qué instrucción es exactamente.
- Señal de reloj: Sincroniza todas las operaciones mediante sus flancos.
- Registro de estado: Almacena información sobre las últimas operaciones realizadas (si la última operación dio cero como resultado, si fue negativo, si hubo desbordamiento aritmético, etc...). Estos valores se usan a veces en la toma de decisiones (saltos condicionales)
#### Salidas:
- Todas las señales de control que activan o desactivan el resto de los componentes del camino de datos.