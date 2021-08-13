## Reacting to motor encoder movement

To use the LEGO motors as a controller for a game, you'll ned to be able to constantly read their absolute positions so that the gameplay feels responsive and isn't too laggy. Let's a write a Python program to do that. 

--- task ---

In the main Thonny window above the REPL, write a program that uses the code you've already seen within a loop so that the position value is constantly displayed.

--- hints ---
--- hint ---
First of all, import the BuildHAT library and create a motor object.

```python
from buildhat import Motor
m1 = Motor('A')
```
--- /hint ---
--- hint ---
You need to read the absolute position of the motor.   Because you're running this as a program rather than line by line in the REPL, you'll need to use the `print()` function to display the values. 

```python

print(m1.get_aposition())
```
--- /hint ---

--- hint ---
Finally wrap the last line within a while loop so that the whole program looks like:

```python
from buildhat import Motor
motor = Motor('A')

while True:
    print(m1.get_aposition())
```
--- /hint ---

--- /hints ---

--- /task ---

You should see that your program continually prints the position of the motor. If you rotate the encode, these values should change. You could use this for your game controller as a way of having a character or object respond to movement. However, constantly checking for changes isn't the most efficient way to do this: the computer;s resources will be used even when the motor isn't being touched. Luckily we can make use of a *callback* to tell the program when the motor has been moved so they only need to take action when needed.

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
m1.when_rotated = moved
```

--- /task ---


Next you can start thinking about your game and how to integrate this code so that the motors can be used as controllers. 

--- save ---