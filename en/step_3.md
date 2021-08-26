## Reacting to motor encoder movement

To use the LEGO motors as a controller for a game, you'll ned to be able to constantly read their absolute positions.

--- task ---

In the main Thonny window above the shell you can use the commands you already know to find the absolute position of the motor. Then in a `while True:` loop you can print the value of the position.

```python
from buildhat import Motor
motor_left = Motor('A')

while True:
    print(motor_left.get_aposition())
```

--- /task ---

You should see that your program continually prints the position of the motor. If you rotate the motor, these values should change.

There better way of doing this though. You only need to read the motor position, if it is moved.

--- task ---

Delete the `while True` loop from your program and create this simple function that prints the absolute position of the motor.

```python
def moved(motor_speed, motor_pos, motor_apos):
    print(motor_apos)
```

--- /task ---

--- task ---

Now set this function to run when the motor's encoder is moved:

```python
motor_left.when_rotated = moved
```

Run your code and you should see the values printed out in the shell change when the motor is moved.

--- /task ---

--- save ---