# Definición
- Hojas de estilo en cascada
	- Se dice que son en cascada porque a los elementos se les aplican algunas de las propiedades del elemento padre (las heredan) 
	- Si no se quieren heredar, se puede indicar un estilo particular para dicho elemento 
	- Para saber si la propiedad se hereda o no hay que consultar la documentación
	- Es posible que se declaren algunas nuevas pero otras se sigan “heredando” del elemento padre
- Cascading Style Sheets (CSS)
- Es un lenguaje utilizado para dar estilo a contenido estructurados
- Se aplica principalmente a documentos HTML
- Se puede usar con otros documentos como SVG, XML, etc...
## Con CSS se puede especificar:
- *Colores*: principal, de fondo, degradados...
- *Tipografía*: familia, tamaños, estilos...
- *Layout*: Disposición de los elementos en el documento
- *Efectos*: Sombras, esquinas redondeadas...
- *Animaciones*: En el cambio de los estilos
## Separación presentación y contenido
Aunque se puede indicar en el HTML: En el head, o en el elemento.
**Ventajas** (fichero independiente):
- Facilita la coordinación entre diseñadores/maquetadores y programadores
- Se pueden usar distintos CSSs en función del tipo/tamaño del dispositivo
- La página es más accesible porque el contenido está separado de la presentación del mismo
- Un mismo fichero .css se puede aplicar a páginas HTML diferentes 
- Ese fichero puede estar cacheado por el navegador para que no se descargue repetidamente 
- Se pueden incluir varios ficheros css asociados al mismo HTML

# Formato 
![[Tema 2.2 CSS(formatoCSS).png]]
![[Tema 2.2 CSS(FormatoCSS2).png]]

# Colores
Existen varias formas de especificar el valor de la propiedad *color* en CSS:
- Utilizando el nombre del color ![[Tema 2.2 CSS(nombreColor).png]]
- Utilizando sus componentes RGB en formato hexadecimal![[Tema 2.2 CSS(colorHexadecimal).png]]
- Utilizando sus componentes en RGB o RGBA![[Tema 2.2 CSS(colorRGBRGBA).png]]

# Tamaño de texto
- Tamaño absoluto (*px*)![[Tema 2.2 CSS(tamañoPx).png]]
- Tamaño relativo a su contenedor (*%*)![[Tema 2.2 CSS(tamañoRelativo).png]]
- Tamaño absoluto (para impresión) (*pt*)![[Tema 2.2 CSS(tamañoPT).png]]
- Tamaño relativo a la fuente del elemento (*em*)![[Tema 2.2 CSS(tamañoEm).png]]
En general es recomendable usar medidas relativas en el tamaño del texto (font-size)
Esto permite adaptar la página a diferentes dispositivos y resoluciones

# Tipo de letra
- El tipo de letra (font-family) que se puede asociar a un texto depende de los tipos de letra del sistema o los que se pueden descargar de Internet 
- Como no se puede saber qué tipos de letra están instalados o se pueden descargar, hay que indicar una lista de tipos de letra 
- Es recomendable que el último sea un tipo de letra genérico que siempre existe: serif, sans-serif, monospace, cursive, fantasy

## Otros estilos de texto:
- Grosor (font-weight)
- Interlineado (line-height)
- Alineación (text-align)
- Text-decoration 
- text-shadow 
- text-transform 
- letter-spacing 
- word-spacing
# Bordes 
Hay muchos elementos HTML que pueden tener bordes.
Se configura con la propiedad *border* , formada por 3 elementos:
- Ancho del borde 
- Estilo: none, hidden, dotted, solid, dashed...
- Color

# Selectores CSS
Los selectores sirven para seleccionar los elementos a los que se les dará el estilo en CSS.
Cuando se usa como selector el nombre de un elemento, esas propiedades se aplicarán a todos los elementos de ese tipo en esa página:
 ![[Tema 2.2 CSS(estiloAElemento).png]]
 Existen otras formas de seleccionar elementos
## Elementos anidados
Elementos que están dentro de otros elementos
 ![[Tema 2.2 CSS(elementosAnidados).png]]
 Podemos seleccionar elementos dentro de otros elementos pero permitiendo que haya elementos entre medias
 *Quitamos el símbolo ">"* 
  ![[Tema 2.2 CSS(seleccionElementosAnidados).png]]
## Selector comodín
Selector * para seleccionar cualquier elemento:
 ![[Tema 2.2 CSS(selectorComodin).png]]
 Es útil cuando se quiere dar un estilo a elementos concretos (usando el nombre del elemento como selector) y se quiere configurar un estilo para todos los demás.
 Se puede usar para elementos dentro de otros
  ![[Tema 2.2 CSS(comodinElementosAnidados).png]]

<font color="#00b050">-->Siempre se aplica el selector más específico</font>
## Selectores de clase e ID
- Es habitual dar un nombre a un elemento concreto para poder darle estilo independientemente de su tipo y su posición en el HTML (*ip*)![[Tema 2.2 CSS(id).png]]![[Tema 2.2 CSS(estiloIp).png]]
- También se puede crear una clase de elementos, de forma que a todos los elementos de esa clase (o tipo) se les aplicará el estilo (*clase*)![[Tema 2.2 CSS(class).png]]![[Tema 2.2 CSS(estiloClase).png]]
Usando el atributo class podemos reutilizar los estilos de esa clase en varias partes de la página.
Asignaremos el class correspondiente al elemento que queramos que tenga el estilo

## Pseudo-clase
El sistema de selectores permite seleccionar elementos del HTML.
También se pueden usar los selectores para aplicar estilos diferentes dependiendo del estado de un elemento (pseudo-class) ![[Tema 2.2 CSS(pseudoClase).png]]
Por ejemplo, se puede cambiar el estilo de los links cuando el usuario pasa encima de ellos con el ratón
 ![[Tema 2.2 CSS(ejPseudoClase).png]]
 Otras pseudo-clases interesantes:
 - De link:
	 - a:link --> Enlace no visitado
	 - a:visited --> Enlace visitado
- elem:first-child --> aplicado al primer elemento hijo
- elem:nth-child(n): Hijo n

# Tamaño, margen y posición
Por defecto, los elementos de una página se comportan como palabras en un texto
Pero su tamaño, margen y posición es altamente configurable en base al *box model*
Cada elemento está en una caja que tiene:
- *Margen*: Espacio transparente alrededor del elemento
- *Borde*: Línea que rodea el elemento
- *Relleno(padding)*: Relleno del elemento desde su contenido hasta el borde
- *Contenido*: Info del propio elemento
 ![[Tema 2.2 CSS(tamañoMargenPosicion).png]]
Por defecto, los elementos \<div> ocupan todo el ancho de la página.
Propiedad **display**:
- *display: block*
	- No se permite otros elementos en la misma línea (por defecto)
	- Se puede cambiar su alto y ancho
- *display: inline-block*
	- Permite otros elementos en la misma línea
	- Se puede cambiar su alto y Ancho
- *display: inline*
	- Permite otros elementos en la misma línea
	- **No** se puede cambiar su alto y ancho
- *display: none*
	- Oculto

Propiedad **margin**(controla el espacio al rededor de un elemento):
- *margin: auto*
	- Pone el mismo margen a la izq y a la dcha. Centra el elemento horizontalmente
- *margin-top, margin-right, margin-bottom, margin- left*
	- Permiten cambiar el margen individualmente a cada lado
- *margin: 1px 2px 3px 4px*
	- Forma compacta de cambiar todos los márgenes a la vez (top right bottom left)
- *margin: 1opx*
	- El mismo margen a cada lado

Propiedad **border**(Controla el borde del elemento):
- *border-width*: Ancho del borde
- *border-color*: Color del borde
- *border-style*: Estilo del borde: solid, dotted, ...
- *border:4px solid \#FF0000
	- Forma compacta de cambiar todas las propiedades a la vez

Propiedad **padding**(entre contenido y borde):
- *padding-top, padding-right, padding-bottom, padding-left*: Permiten cambiar el relleno individualmente a cada lado 
- *padding: 1px 2px 3px 4px*
	- Forma compacta de cambiar todos los rellenos a la vez 
- *padding: 10x*
	- Forma compacta de poner el mismo padding en todos los lados

## Posición de los elementos
Antes usadas --> position y float --> Muy limitadas y complejas
Se crearon nuevos sistemas de posicionamiento:
- **Flexbox**:
	- Elementos en una dimensión: Filas *o* columnas
	- Barras de navegación, alineación de botones, ...
- **Grid**:
	- Elementos en dos dimensiones: Filas *y* columnas
	- Layouts de páginas completos, Galerías de imágenes
## Flexbox
hasta pag 63