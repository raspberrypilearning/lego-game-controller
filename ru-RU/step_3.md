## React to motor encoder movement

To use the LEGO® Technic™ motors as a controller for a game, you'll need to be able to constantly read their absolute positions.

--- task ---

In the main Thonny window above the shell you can use the commands you already know to find the absolute position of the motor. Then, in a `while True:` loop you can print the value of the position.

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

You should see that your program continually prints the position of the motor. If you rotate the motor, these values should change.

There is a better way of doing this though. You only need to read the motor position if it is moved.

--- task ---

Delete the `while True` loop from your program and create this simple function that prints the absolute position of the motor. You will also need to add another import line to use the `pause()` function.

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

Now set this function to run when the motor's encoder is moved:

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

Run your code and you should see the values printed out in the shell change when the motor is moved.

--- /task ---

--- save ---
