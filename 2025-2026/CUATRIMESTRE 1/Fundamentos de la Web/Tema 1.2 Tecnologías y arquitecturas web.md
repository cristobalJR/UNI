# Web
Existen varios tipos de web, dependiendo de cómo usan las tecnologías de cliente y servidor.
## Página web (Servidor estático)
El servidor web sirve contenido almacenado en el disco duro
### Página web estática
- El navegador hace petición al servidor mediante http
- El servidor transforma la URL a ruta en el disco
- El servidor devuelve el fichero de disco al navegador
- El navegador visualiza la página HTML con CSS e imágenes (Sin JavaScript)
- Cuando el usuario hace clic en un enlace, el navegador repite el proceso con la URL del link y recarga por completo la página web
- Se implementa con HTML y CSS .Pueden usarse librerías CSS$\rightarrow$  Gestión del CSS de alto nivel, Diseño responsive (adaptativo a móviles), Componentes predeterminados.
#### Ventajas:
- Consume pocos recursos
- No suele tener problemas de seguridad
- Hay servicios gratuitos (GitHub pages)
#### Desventajas:
- La edición y publicación requiere de conocimientos técnicos
- El contenido es principalmente estático
### Página web interactiva
- El contenido de la página está alojado en el disco duro del servidor
- El cliente es dinámico porque las páginas incluyen código JavaScript que se ejecuta en el navegador.
- Este JavaScript se usa para incluir efectos gráficos:
	- Efectos gráficos que no se pueden implementar con CSS
	- Mostrar u ocultar información en función de los elementos que se seleccionan (para documentos largos)
	- Menús desplegables  
	- Buscadores
- Se implementan con HTML, CSS y JavaScript. Para implementar la interactividad se pueden usar librerías
#### Ventajas:
- Las mismas que las páginas web estáticas
- Prácticamente todas las páginas web tienen algo de JavaScript.
- Efectos gráficos y funcionalidad avanzada
#### Desventajas:
- El servidor estático impide gestión de usuarios, guardar información, etc...
## Aplicación web (Servidor dinámico)
El servidor web sirve contenido generado mediante código
### Aplicaciones web con cliente estático
- Cuando el servidor web recibe una petición, dependiendo de la URL:
	- Devuelve el contenido del disco
	- Ejecuta código para generar el recurso dinámicamente
- Cuando se ejecuta código, normalmente se hacen consultas a una base de datos para recuperar la información y generar la página HTML
- Si el usuario pulsa un enlace, se recarga la página al completo (Incluso las partes que no cambian)
#### Ventajas:
- Puede usarse desde navegadores muy antiguos
- Son muy ligeras(solo descargan HTML)
- No son muy comunes
#### Desventajas:
- Son poco interactivas
- Recargar la página completa puede ofrecer mala experiencia al usuario (navegación lenta)
## Aplicación web con JavaScript
Dependiendo de como se usa el JavaScript se pueden diferenciar tres tipos de aplicaciones:
### Aplicación web interactiva
- El JS se utiliza para crear efectos gráficos
- También para validación de datos en formularios
- Pueden tener lógica avanzada (editores interactivos, juegos...)
- La gran mayoría de las apps web disponibles en internet son de este tipo
 ![[Tema 1.2 Tecnologías y arquitecturas web(appWebInteractiva).png|350]]
### Aplicación web con AJAX
- **AJAX**(Asynchronous JavaScript And XML)
- JS se usa para no tener que recargar la página completamente al pulsar un link
- Permite hacer petición al servidor web en segundo plano
- Cuando llega al navegador la respuesta a la petición, el código JS actualiza aquellas partes de la página necesarias
 ![[Tema 1.2 Tecnologías y arquitecturas web(webAJAX).png]]
- Usar AJAX en una página mejora mucho la experiencia de usuario
- Solo se recargan aquellas partes que cambian en la página
- Se puede usar para simular el efecto de scroll infinito y evitar botones de cambio de página
- Se puede dar realimentación al usuario antes de enviar el formulario
 ![[Tema 1.2 Tecnologías y arquitecturas web(feedbackAJAX).png]]
- Cuando el JS hace peticiones, el server puede devolver:
	- *Fragmentos HTML*: Se incrusta directamente en la página (Scroll infinito)
	- *Información estructurada*: Se interpreta por JS para modificar la página (Error de validación). Se representa en formato JSON.
		- Si se siguen unas convenciones para las peticiones se puede crear una API REST
### Aplicación web SPA
- **SPA**(Single Page Application)
- La técnica AJAX se lleva al extremo y toda la información del servidor se obtiene con JS en segundo plano, haciendo peticiones a la API REST y obteniendo la información en JSON
- Solo se carga una única página, el index.html (que carga CSS y JS)
 ![[Tema 1.2 Tecnologías y arquitecturas web(appSPA).png]]
- Frameworks SPA:
	- React
	- Angular
	- Vue.js...
#### Ventajas:
- Ofrecen una experiencia muy interactiva y dinámica al usuario.
- Las interacciones son muy rápidas porque no recargan la página completa
- Hay una mejor separación cliente (interfaz) y servidor (lógica)
#### Desventajas:
- Son las más complejas de implementar porque requieren usar nuevos frameworks
- La carga inicial puede ser lenta (tiene que cargar la app completa)
- Los buscadores pueden tener dificultades para indexarlas