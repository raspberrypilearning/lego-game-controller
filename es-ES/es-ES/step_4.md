## Haciendo tu pantalla Pong

Turtle es una biblioteca de dibujo y animación y puedes aprender más sobre ella en este [proyecto excelente ](https://projects.raspberrypi.org/es-ES/projects/turtle-race).


Primero, crea una ventana donde se jugará el juego.

--- task ---

Abre un nuevo archivo en Thonny y agrega el siguiente código para importar las bibliotecas Turtle, time y Build HAT, y luego configura una ventana. Ejecuta el archivo y deberías ver una ventana negra con el título "PONG". No es necesario incluir los comentarios `#`.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 1
line_highlights:
---

from turtle import Screen, Turtle from time import sleep from buildhat import Motor

juego_area = Screen() #Cread una pantalla   
juego_area.title("PONG") #Da un título a la pantalla   
juego_area.bgcolor('black') #Fija el color de fondo   
juego_area.tracer(0) #Da animaciones más suaves

--- /code ---

--- /task ---

La biblioteca Turtle también tiene una forma útil de establecer las coordenadas de un área de la pantalla. Añade esta línea a tu programa:

--- task ---

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 8
line_highlights: 9
---

juego_area.tracer(0)   
juego_area.setworldcoordinates(-200, -170, 200, 170)

--- /code ---

--- /task ---

Esto crea una ventana rectangular de 400 píxeles de ancho y 340 de alto, con 0 en el centro.

![Una captura de pantalla de la ventana del juego, que muestra las coordenadas de cada esquina y el centro. La parte superior izquierda es -200,170, la parte superior derecha es 200,170, la parte inferior izquierda es -200, -170 y la parte inferior derecha es 200, -170. El centro es 0,0.](images/coords.png)

--- task ---

Ahora, necesitas actualizar tu área de juego, para ver la paleta y la pelota. Agrega un **bucle de juego** al final de tu código y llama al método `update()`.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 10
line_highlights:
---

while True:   
juego_area.update ()

--- /code ---

Ejecuta su programa y verás aparecer una ventana negra.

--- /task ---

--- task ---

A continuación, puede hacer una pelota usando una tortuga que está configurada para ser un círculo blanco. La pelota debe comenzar en el medio de la pantalla y no debe trazar una línea cuando se mueve.

**Por encima de** tu `while True`, agrega el siguiente código:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 10
line_highlights:
---

pelota = Turtle()   
pelota.color('white')   
pelota.shape('circle')   
pelota.penup()   
pelota.setpos(0,0)

while True:

--- /code ---

--- /task ---

--- task ---

Vuelve a ejecutar tu programa. Deberías ver aparecer una pelota blanca en tu ventana.

--- /task ---

--- task ---

A continuación, puedes configurar una paleta de la misma manera. Será un rectángulo verde y se colocará en el extremo izquierdo de la pantalla.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 17
line_highlights:
---

paleta_izquierda = Turtle()   
paleta_izquierda.color('green')   
paleta_izquierda.shape('square')   
paleta_izquierda.shapesize(4, 1, 1)   
paleta_izquierda.penup()   
paleta_izquierda.setpos(-190, 0)

--- /code ---

--- /task ---

--- task ---

Ejecuta tu programa para ver la pelota y paleta.

![Una pelota blanca en el centro de una ventana negra, con una paleta verde en el extremo izquierdo.](images/pong_static.png)

--- /task ---
