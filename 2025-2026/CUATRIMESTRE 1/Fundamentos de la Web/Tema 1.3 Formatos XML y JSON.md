# XML
- **XML**(eXtensible Markup Lenguaje): lenguaje de marcado extensible
- Utilizado para el almacenamiento en intercambio de datos estructurados
- Existen librerías de manipulación en prácticamente todos los sistemas, facilitando la interoperabilidad
- Estandarizado por W3C
- Marcado por etiquetas, similar a HTML
- Un documento XML contiene uno o más elementos, cada uno viene delimitado por las etiquetas inicial y final.
 ![[Tema 1.3 Formatos XML y JSON(elementoXML).png]]
- Pueden contener:
	- Texto
	- Elementos
	- Atributos: Puede tener varios de distinto nombre, se usan para añadir info sobre el elemente en el que se definen
	- Combinación de ellos
	 ![[Pasted image 20250925201606.png]]
## Documento XML
Es conveniente que tenga cabecera indicando la versión y la codificación.
 ![[Tema 1.3 Formatos XML y JSON(cabeceraXML).png]]
- No está permitido: 
	![[Tema 1.3 Formatos XML y JSON(XMLnoPermite).png]]
- Los caracteres usados en castellano están permitidos, pero se aconseja utilizar el código ASCII para ellos
- Se aconseja evitar el "-" y el "."
## Atributo XML
- No está permitido repetir nombres
- Atributos especiales:
	- *id*: asigna un identificador único al elemento
	- *lang*: especifica el idioma
## Comentarios XML
<!-- Inicio de comentario
--> final de comentario
## Validación XML
- Se pueden especificar qué elementos y atributos están permitidos
- Existen librerías y herramientas que pueden validar los documentos
- Formatos:
	- **DTD**(Document Type Definition)
	- **XSD**(XML Schema Definition)
# JSON
- **JSON**(JavaScript Object Notation): Notación de objetos JS
- Al igual que XML:
	- Se utiliza para el almacenamiento e intercambio de datos estructurados
	- Existen librerías de manipulación en prácticamente todos los sitemas
	- Estandarizado por ECMA-404
 ![[Tema 1.3 Formatos XML y JSON(ejXMLJSON).png|400]]
## Objeto JSON
- Un objeto JSON se inicia con **{** y finaliza con **}**
- Tiene cero, uno o más atributos **"name": value**
- Separados por comas (**,**)
- El value puede ser:
	- *String*: Caracteres entre comillas
	- *Number*: Enteros o decimales
	- *Boolean*: true o false
	- *Array de values*: \[value, value, value]
	- *Objeto*: {...}
	- *null*
 ![[Tema 1.3 Formatos XML y JSON(objetoJSON).png|300]]
## Formato JSON
- Caracteres Unicode
- Por defecto la codificación es UTF-8, se admiten también 16 y 32.
- No se admiten comentarios
## JSON VS XML
- JSON se popularizó frente a XML:
	- Es mucho más sencillo de enviar y recibir objetos JS(Traducción directa)
	- Generalmente ocupa menos espacio para la misma info(no etiquetas de cierre)
	- Es menos pesado de escribir
	- Inicialmente se analizaba(parseaba) más rápido
## Validación JSON
- Se puede especificar que atributos están permitidos (esquema)
- Existen librerías y herramientas para validar documentos
- Formatos:
	- JSON Schema
