## Реагирование на движение двигателя энкодера

Чтобы использовать моторы LEGO® Technic™ в качестве контроллера для игры, тебе необходимо иметь возможность постоянно считывать их абсолютные положения.

--- task ---

В главном окне Thonny над панелью Оболочки ты можешь использовать уже известные тебе команды, чтобы найти абсолютное положение двигателя. Затем в цикле `while True:` ты сможешь вывести на экранзначение этой позиции.

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights:
---

from buildhat import Motor   
motor_left = Motor('A')

while True:   
print(motor_left.get_aposition())

--- /code ---

--- /task ---

Ты должен увидеть, что твоя программа постоянно выводит на экран положение двигателя. Если ты вращаешь мотор, эти значения должны измениться.

Однако есть способ сделать это лучше. Тебе нужно считывать положение двигателя, только если он перемещается.

--- task ---

Удали цикл `while True` из твоей программы и создай эту простую функцию, которая печатает абсолютное положение мотора. Тебе также потребуется добавить еще одну строку импорта, чтобы использовать функцию `pause()`.

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights: 2,6,7
---

from buildhat import Motor  
from signal import pause motor_left = Motor('A')


def moved_left(motor_speed, motor_pos, motor_apos):   
print(motor_apos)

--- /code ---

--- /task ---

--- task ---

Теперь сделаем так, чтобы эта функция работала при перемещении энкодера двигателя:

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights: 9,10
---

from buildhat import Motor  
from signal import pause motor_left = Motor('A')


def moved_left(motor_speed, motor_pos, motor_apos):   
print(motor_apos)

motor_left.when_rotated = moved_left pause()

--- /code ---

Запусти свой код, и ты должен увидеть, как значения, печатаемые в окне Оболочки, меняются при перемещении двигателя.

--- /task ---

--- save ---
