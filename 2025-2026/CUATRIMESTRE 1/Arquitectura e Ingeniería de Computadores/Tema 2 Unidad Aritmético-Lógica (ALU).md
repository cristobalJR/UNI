

# Introducción
Una unidad aritmético-lógica es un circuito combinacional que realiza las operaciones aritméticas y lógicas básicas en el computador.
- Operaciones aritméticas básicas: *add, sub, mult, div*
- Operaciones lógicas básicas: *not, and, or, nand, nor*
- Operaciones de desplazamiento de bits: *srl, sll*
 ![[Tema 2 Unidad Aritmético-Lógica (ALU).png]]
 
 Es de tipo combinacional (No tiene memoria)
	 El valor del resultado se calcula en función del valor de las entradas en dicho instante.
Recibe 2 operandos, ya que la mayoría de las operaciones que realiza son binarias, si bien en ocasiones solo acepta 1 operando (ej. Si la operación que vamos a realizar es la función NOT o de de cambio de signo NEG).
Además de esas entradas, recibe señales de control que identifican la operación que se va a realizar.
La ALU proporciona como salida por un lado el resultado de la operación, y por otro lado una seria de indicadores del resultado obtenido, como si salió cero, negativo, desbordamiento, etc...
Tanto los operandos como el resultado están expresados en binario de tamaño n bits. Este tamaño es el de la **PALABRA** del computador.
# Conceptos Previos
Binario Puro, Hexadecimal, Complemento a 2, reglas aritméticas binario puro y de complemento a 2, puertas lógicas, decodificadores, funciones lógicas o de conmutación, mapas de Karnaug
# Circuitos aritmético-lógicos básicos
## Semisumador de 1 bit
El semisumador (half adder), es un circuito que suma dos bits de entrade <u>a</u> y <u>b</u>, y devuelve un bit de resultado <u>s</u> y un bit de acarreo<u> c<sub>out</sub></u>
	![[Tema 2 Unidad Aritmético-Lógica (ALU)(semisumador 1 bit).png]]
Se suele representar con este símbolo:
	![[Tema 2 Unidad Aritmético-Lógica (ALU)(simbolo semisumador).png]]
## Sumador completo de 1 bit

## Sumador completo de n bits
## Restador
## Sumador-restador



<span style="background:#b1ffff">hasta la 24</span>
# Construcción incremental de una ALU sencilla
Diseño modular de abajo arriba
............


## Operación suma: add
Complemento a dos (C2)
Añadimos el sumador completo a nuestra ALU, haciendo mas grande el multiplexor.
	![[Tema 2 Unidad Aritmético-Lógica (AluSuma).png]]
## Operación resta: sub
Resta en complemento a 2: suma del negado más 1
a- b = a + (-b) = a + not(b) + 1
## Operación lógica: nor
not(a+b) = not(a) · not(b)
## Operaión de activación condicional: slt (setLessThan)
Activar si es menor que
## ALU de 32 bits
Combinando adecuadamente las miniALU de 1 bit, se obtiene la ALU de 32 bits. • Cada miniALU recibe dos bits del mismo peso de a y de b y proporciona el bit del mismo peso del resultado. • El acarreo de salida de una miniALU se pasa al acarreo de entrada de la miniALU siguiente. • El acarreo de salida de la miniALU de peso 31 se ignora, ya que nunca forma parte del resultado de una suma o de una resta para datos en complemento a 2. • El acarreo de entrada de la miniALU de peso 0 es una entrada más del circuito (todavía no la hemos establecido de manera definitiva). • Todas las miniALU reciben la misma palabra de operación. • La salida Set de la miniALU de peso 31 es la entrada Less de la miniALU de peso 0. • El resto de las entradas Less de las otras miniALU están fijadas al valor 0. • Optimización: • Siempre que la señal de acarreo de entrada cin para la miniALU de peso 0 vale 0, la señal Binvert también vale 0. Y cuando la primera vale 1, la otra también. • Como ambas señales toman siempre los mismos valores, podemos unificarlas en una sola señal, que llamaremos a partir de ahora Bnegate (ver siguiente transparencia)
![[Tema 2 Unidad Aritmético-Lógica (ALU)-1.png]]
## Indicadores de resultado: Detectores de cero (Z) y desbordamiento (V)

# Otros circuitos aritmético-lógicos