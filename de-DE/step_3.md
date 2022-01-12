## React to motor encoder movement

Um die LEGO® Technic™ Motoren als Controller für ein Spiel zu verwenden, musst du ihre absolute Position ständig ablesen können.

--- task ---

Im Thonny-Hauptfenster über der Shell kannst du die bereits bekannten Befehle verwenden, um die absolute Position des Motors zu ermitteln. Dann kannst du in einer `while True:` Schleife den Wert der Position ausgeben.

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights:
---

from buildhat import Motor   
motor_links = Motor('A')

while True:   
print(motor_links.get_aposition())

--- /code ---

--- /task ---

Du solltest sehen, dass dein Programm ständig die Position des Motors ausgibt. Wenn du den Motor drehst, sollten sich diese Werte ändern.

Es gibt jedoch einen besseren Weg, dies zu tun. Du musst die Motorposition nur ablesen, wenn das Rad bewegt wird.

--- task ---

Lösche die `while True` Schleife aus deinem Programm und erstelle diese einfache Funktion, die die absolute Position des Motors ausgibt. Du musst noch eine weitere Importzeile hinzufügen, um die Funktion `pause()` verwenden zu können.

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights: 2,6,7
---

from buildhat import Motor  
from signal import pause motor_links = Motor('A')


def links_bewegt(motor_speed, motor_pos, motor_apos):   
print(motor_apos)

--- /code ---

--- /task ---

--- task ---

Diese Funktion soll ausgeführt werden, wenn der Encoder des Motors bewegt wird:

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights: 9,10
---

from buildhat import Motor  
from signal import pause motor_links = Motor('A')


def links_bewegt(motor_speed, motor_pos, motor_apos):   
print(motor_apos)

motor_left.when_rotated = links_bewegt pause()

--- /code ---

Führe deinen Code aus und du solltest sehen, dass sich die in der Shell angezeigten Werte ändern, wenn der Motor bewegt wird.

--- /task ---

--- save ---
