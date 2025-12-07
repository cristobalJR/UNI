# Binario puro
 ![[Repaso de Binario 2025-09-17 20.11.38.excalidraw]]
 *Solo hemos adquirido 7 bits con la operación, por lo que añadimos el 0 al principio para hacer una representación de 8 bits*
 ![[Repaso de Binario 2025-09-17 20.20.25.excalidraw]]
# Complemento a 2
- **Tamaño**: n bits donde el bit n-1 representa el signo ( 0 = +, 1 = -).
- **Rango**: $(-2^{\,n-1},\,2^{\,n-1}-1)$ 
- Si el número es positivo y está dentro del rango, se representa igual que en binario puro.
- Si es negativo, primero se calcula su representación positiva y luego se cambia el signo.
	- Operación complemento: Se copia bit a bit de derecha a izquierda hasta el primer 1. A partir de ahí, se intercambian 0s por 1s y 1s por 0s.
- Si n = 8 bits, el rango es $[-128,+127]$
- 81 en C2 con 8 bits se representa igual que en BP.	<center>81<sub>10</sub>=<font color="#ff0000"><u>0</u></font>1010001<sub>C2</sub></center>
- Por el contrario, para -81 aplicamos la operación complemento:![[Repaso de Binario 2025-09-25 16.16.29.excalidraw]]
- **C2 $\rightarrow$ decimal:** Suma de potencias de 2 elevado a la posición de cada bit, donde la potencia correspondiente a $2^{\,n-1}$   va con signo menos.![[Repaso de Binario 2025-09-25 16.46.54.excalidraw|130%]]
# Hexadecimal
- Si un número se representa en binario puro con 16 bits, ¿Cómo se representarán en **hexadecimal** los siguientes números?
	- El número más bajo del rango![[Repaso de Binario 2025-09-25 17.22.00.excalidraw]]
	- El número más alto del rango![[Repaso de Binario 2025-09-25 17.25.22.excalidraw]]
	- El número situado en la mitad + 1![[Repaso de Binario 2025-09-25 17.32.50.excalidraw|130%]]
# Aritmética Binario Puro
## Suma
 ![[Repaso de Binario 2025-09-25 18.22.05.excalidraw]]
## Resta
 ![[Repaso de Binario 2025-09-25 18.33.50.excalidraw|130%]]]

## Multiplicación
 ![[Repaso de Binario 2025-09-25 18.49.39.excalidraw|50%]]
## División
 ![[Repaso de Binario 2025-09-25 18.57.53.excalidraw|50%]]
# Aritmética Complemento a 2