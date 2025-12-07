- Índice Multimedia
    - #  _**Fechas relevantes:**_  
        - ## Prácticas(min:5/10) : 
            1. Entrega Práctica 1 - 10 de Marzo (P1: 10%) (Video P1: 20%)
            2. Entrega práctica 2 - 10 de Abril (P2: 10%) (Video P2: 20%)
            3. Entrega Práctica 3 - 8 de Mayo (P3: 10%) (Video P3: 30%)
    - 
    - #  _**Profesorado:**_  
        - ### Liliana Patricia Santacruz Valencia
            - **Despacho: **2016, Amplificación del Rectorado.
            - **Email**: liliana.santacruz@urjc.es
            - **Tutorías**:  Lunes [13:00/15:00] y  Miércoles [17:00/19:00] o solicitar por el bloque de correo del Aula virtual
    - 
    - #  _**Índice:**_  
        - # Bloque 1: Tecnologías Multimedia
            1. Fundamentos y Caracterización // Creación de un juego con HTML5
                1. Mundo Básico
                2. Simulación
                3. Integración
            2. Fundamentos de Realidad Aumentada// Objetos RA

        - # Bloque 2: Accesibilidad
            - 3. Contenido Web Accesible
    - 
- Tema 1.- Creación de un juego con HTML5
    1. #  _**Canvas**_  
        - El elemento lienzo proporciona scripts con un lienzo de mapa de bits que depende de la resolución, puede servir para renderizar sobre la marcha.
        - Permite dibujar figuras y texto, optimizado para uso rápido.
        - .
            ```
            <canvas width="600" height="400" id="testcanvas" style="border: 1px solid black;"> 
            ```
            - Atributos obligatorios para el Canvas.
        - 
        - Ejemplo:
            - .
                ```
                // Rectángulos rellenos
// Dibutar un cuadrado sólido con ancho y alto de 100 pixels en (200,10)
context. fillRect (200,10,100,100):
// Dibujar un cuadrado sólido con ancho de 90 y alto 30 pixels en (50,70)
context. fillRect (50,70,90,30);
// Contornos rectangulares
// Dibujar un contorno rectangular de ancho y alto de 50 pixels en (110,10)
context. strokeRect (110,10,50,50);
// Dibujar un contorno rectangular de ancho y alto de 50 pixels en (30,10)
context. strokeRect (30,10,50,50):

                ```
        - Ejemplo para inicializarlo en JS y poder pintar de forma programática:
            - .
                ```
                <canvas id="main-canvas" width="900" height="900"> </canvas> 
                ```
            - .
                ```
                const mainCanvas = document.getElementById("main-canvas");
const context = mainCanvas.getContext("2d"); 

let initialX;
let initialY;
                ```
        - 
