## Reacción al movimiento del codificador del motor

Para usar los motores LEGO® Technic ™ como controlador de un juego, tendrás que poder leer constantemente sus posiciones absolutas.

--- task ---

En la ventana principal de Thonny encima del shell, puedes usar los comandos que ya conoces para encontrar la posición absoluta del motor. Luego, en un bucle `while True:` puedes imprimir el valor de la posición.

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights:
---

from buildhat import Motor   
motor_izquierda = Motor('A')

while True:   
print(motor_izquierda.get_aposition())

--- /code ---

--- /task ---

Tu programa debe imprimir continuamente la posición del motor. Si gira el motor, estos valores deberían cambiar.

Sin embargo, hay una manera mejor de hacerlo. Solo necesitas leer la posición del motor si se mueve.

--- task ---

Elimina el `while True` de tu programa y crea esta función simple que imprime la posición absoluta del motor. También necesitarás agregar otra línea de importación para usar la función `pause()`.

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights: 2,6,7
---

from buildhat import Motor  
from signal import pause motor_izquierda = Motor('A')


def movido_izquierda (motor_speed, motor_pos, motor_apos):   
print (motor_apos)

--- /code ---

--- /task ---

--- task ---

Ahora configura esta función para que se ejecute cuando se mueva el codificador del motor:

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights: 9,10
---

from buildhat import Motor  
from signal import pause motor_izquierda = Motor('A')


def movido_izquierda(motor_speed, motor_pos, motor_apos):   
print(motor_apos)

motor_izquierda.when_rotated = movido_izquierda pause()

--- /code ---

Ejecuta tu programa y deberías ver que los valores impresos en el shell cambian cuando se mueve el motor.

--- /task ---

--- save ---
