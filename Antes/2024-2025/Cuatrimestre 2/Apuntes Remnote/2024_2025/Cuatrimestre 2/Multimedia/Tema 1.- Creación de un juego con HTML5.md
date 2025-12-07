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
