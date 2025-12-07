# Modelo Vs. Esquema
- **Modelo**: Construcción mental a partir de la realidad en la que se reproducen los principales componentes y relaciones del segmento de realidad analizada.
- **Modelo de datos**: Conjunto de conceptos, reglas y convenciones que permiten describir y manipular los datos de la parcela de un cierto mundo real que deseamos almacenar en la BDD
- **Esquema**: representación de un determinado mundo real en términos de un modelo de datos
![[Pasted image 20250922191416.png]]
# Clasificación de los modelos de datos
## Modelo de datos
- *Externo* (Punto de vista de cada usuario en particular)
- *Global* (punto de vista del conjunto de usuarios-empresa)
- *Interno* (Punto de vista de la máquina)

## Modelos de Datos Externos y Globales
- **Conceptuales** (Enfocados a describir el mundo real con independencia de la máquina)
- **Convencionales o Lógicos** (Implementados en SGBD)
### Conceptuales
- No suelen estar implementados en SGBD
- Independientes del SGBD
- Mayor nivel de abstracción
- Mayor capacidad semántica
- Más enfocados al diseño de alto nivel (Modelado conceptual)
- Interfaz usuario/informático

---
### Lógicos (Convencionales)
- Implementados en SGBD comerciales
- Dependen del SGBD
- Más próximos al ordenador
- Poca capacidad semántica
- Más enfocados a la implementación
- Interfaz informático/sistema
- Nivel de mediación entre el extremo e interno
# Propiedades de un modelo de datos
### Estáticas
- **Elementos permitidos**:
	- Objetos
	- Asociaciones
	- Características de los objetos
	- Dominios
- **Elementos no permitidos y restricciones**:
	- Inherentes
	- Semánticas

---
### Dinámicas (conjunto de operadores)
Cada operador tiene dos componentes:
- Localización (de un ejemplar o conjunto de ejemplares de un objeto)
- Acción (sobre el o los ejemplares seleccionados)

# Los modelos de datos en el diseño de una BD
![[Tema 3 Concepto de modelo de datos(modeloDeDatosBBDD).png]]
# Relación entre modelos de datos y lenguajes de datos
Lenguaje de Datos = Modelos de datos + Sintaxis
Algunos ejemplos:
- *SQL* = *MD Relacional + Sintaxis*
- QUEL = MD relacional + Sintaxis
- OQL = M Objetos + Sintaxis