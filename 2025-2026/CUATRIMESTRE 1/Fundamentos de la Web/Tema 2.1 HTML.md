# Introducción al HTML
- Hiper Text Markup Language (HTML)
- Es el lenguaje utilizado para crear documentos en la web
- El navegador web es el encargado de visualizar los documentos HTML
- Cuando un navegador realiza una petición http a un servidor web, el servidor le suele devolver un documento HTML
## HTML, XML y XHTML
- HTML es parecido a XML (etiquetas, atributos, comentarios...)
- No igual:
	- Existen elementos que no se cierran \<br>
	- XML comienza con \<?xml ...> mientras que HTML con \<!DOCTYPE html>
	- En HTML algunos atributos no llevan comillas
- XHTML
	- Estándar para escribir HTML como XML
	- Ya no se usa
# Contenido
Estructura básica de un HTML:
 ![[Tema 2.1 HTML(estructuraHTML)-1.png]]
 ![[Tema 2.1 HTML(estructuraElemento).png]]

## Etiquetas HTML
- Un documento está formado por etiquetas entre ángulos \<html>
- La mayoría de ellas viene en pares: (etiqueta apertura \<html> , etiqueta cierre \</html>)
- Entre las etiquetas de apertura y cierre se puede incluir texto que será visualizado en el navegador
 ![[Tema 2.1 HTML(textoEtiquetasHTML).png]]
- *Título*:
	- \<h1>...\</h1>
	- Se pueden poner hasta 6 niveles de importancia
- *Párrafos*:
	- \<p>Esto es un párrafo\</p>
- *Secciones*:
	- Las secciones \<section> se usan para indicar contenidos relacionados entre sí que tienen un título
	- Es recomendable que lleven un título
![[Tema 2.1 HTML(titulosParrafosSecciones).png]]
## Tipos de elementos
- Bloque: div, header, footer, section, aside, h, p, ul, li, ...
	- Son elementos que comienzan en una línea nueva
	- Tratan de ocupar todo el espacio disponible
	- Pueden anidarse tantos bloques de cualquier tipo como sea necesario
- Texto: a, strong, em, small, del, mark, span, ...
	- Son elementos que continúan con el flujo normal del texto
	- Ocupan el espacio necesario de su contenido
	- No aceptan elementos de bloque en su interior

## Resaltar texto
- Texto muy importante : \<strong>Texto\</strong> 
- Texto enfatizado: \<em>Texto\</em>
## Comentarios
Se escriben entre \<!-- y -->
## Imágenes
Etiqueta:
\<<font color="#f79646">img</font> <font color="#938953">scr</font> = <font color="#9bbb59">"URL_IMAGEN"</font>/>
Formatos de imágenes:
- *PNG*: Ideal para imágenes con pocos colores diferentes o transparencias
- *JPG*: Imágenes con muchos colores (fotos)
- *GIF*: Imágenes animadas
- *WEBP*: Formato que permite lo mejor de PNG,JPG y GIF y está más optimizado
- *SVG*: Imágenes vectoriales (cualquier tamaño sin perder calidad)
Imágenes de ejemplo:
- Programas que generan imágenes con la dimensión solicitada
- Ideal para diseño web sin dedicar tiempo a la creación de imágenes
- picsum.photos
- dummyimage.com

## Hiperenlaces
Los enlaces son textos o imágenes del documento que si se pulsan se carga una nueva página en el navegador
- Enlaces en texto
\<<font color="#f79646">a</font> <font color="#938953">href</font> = <font color="#9bbb59">"https://www.urjc.es/"</font>>URJC\</<font color="#f79646">a</font>>
- Enlaces en imágenes
\<<font color="#f79646">a</font> <font color="#938953">href</font> = <font color="#9bbb59">"https://www.urjc.es/"</font>>\<<font color="#f79646">img</font> <font color="#938953">scr</font> = <font color="#9bbb59">"URL_IMAGEN"</font>>\</<font color="#f79646">a</font>>

## Listas de elementos
- Listas ordenadas:
	- Lista: \<ol>...\</ol> (ordered list)
	- Elemento: \<li>...\</li> (list item)
	 ![[Tema 2.1 HTML(listasOrdenadas).png]]
- Listas no ordenadas:
	- Lista: \<ul>...\</ul> (unordered list)
	- Elemento: \<li>...\</li> (list item)
	 ![[Tema 2.1 HTML(listasNoOrdenadas).png]]
- Listas anidadas:...
## Tablas
 ![[Tema 2.1 HTML(tablas).png|500]]
## Multimedia
- Audio
- Video
- Google maps
# Estructura de un HTML
- Los documentos HTML suelen tener partes semánticamente diferentes:
	- Cabecera, pie, contenido principal, menú de navegación, menú lateral...
- Si esas partes se indican en el documento son más accesibles
- También se mejora su aparición en las búsquedas (indexado por Google)
- Y simplifica la conversión a otros formatos
  ![[Tema 2.1 HTML(estructuraHTML)-2.png]]
# Formularios
Los formularios HTML permiten que un usuario inserte datos y seleccione preferencias
- Nombres, fechas, textos largos, numeros, opciones...
Los datos introducidos por el usuario pueden procesarse
- En el servidor web
- En el navegador
De momento solo crearemos el formulario (sin ningún procesamiento)
### En el servidor web:
- El usuario pulsa el botón
- El navegador pide una nueva página al servidor enviando los datos del formulario
- El servidor procesa esos datos y genera una nueva página
### En el navegador:
- Se ejecuta código JavaScript mientras el usuario escribe o cuando pulsa el botón
- El código decide qué hacer: validar, enviar, realizar cálculos en el propio navegador, ... 

## 
![[Tema 2.1 HTML(ejFormulario).png]]
<font color="#00b050">-->REPASAR TODOS LOS TIPOS DE FORMULARIOS</font>
# Estilos en HTML
## Estilos de los elementos
- El formato HTML permite indicar el contenido de forma estructurada y semántica
- Se puede dar estilo CSS a los elementos del documento
	- Color, tamaño, tipo de letra, posición, bordes, etc...
- Los estilos CSS se pueden indicar en el propio documento : atributo *style*
- Es preferible usar ficheros CSS para separar el contenido del estilo
<font color="#00b050">-->REPASAR TODOS LOS TIPOS DE ESTILOS EN LOS ELEMENTOS</font>
## Elementos div y span
 \<div> y  \<span> son elementos genéricos en HTML que no tienen semántica ni estilo
- Se usan para agrupar partes del documento (para manipulación conjunta, aplicar estilos, etc...)
-  \<div> se usa para zonas de la página
-  \<span> para palabras o frases en un texto
-  **\<div>**:
	- Los elementos *div* son partes rectangulares de la página que pueden contener elementos HTML y estilo propio
	 ![[Tema 2.1 HTML(ejDiv).png|470]]
- **\<span>**:
	- Los elementos *span* permiten marcar partes del texto para cambiarles el estilo
	 ![[Tema 2.1 HTML(ejSpan).png|370]]