## Control the paddle

### Designing the controls

The LEGO® Spike™ motor is going to be used to control the position of the paddle but you don't want to be able to make full turns. 

A simple way to limit the motion of the wheel is to add a LEGO® element to prevent the wheel turning through a complete rotation.

--- task ---

Line up the encoder marks on your motor using the wheel, like before. Insert a peg or axle as close to level with the markers as possible.

--- /task ---

![An animation showing a motor and wheel combination being turned by hand. There is a LEGO® cylinder attached to the wheel so that it can't be fully rotated.](images/motor_block.gif)

--- print-only ---

![Two photos of a motor and wheel combination being turned by hand. There is a LEGO® cylinder attached to the wheel so that it can't be fully rotated.](images/sidebyside.png)

--- /print-only ---


--- task ---

Add a line to create the `motor_left` object after the import line.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 3   
line_highlights: 5   
---

from buildhat import Motor

motor_left = Motor('A')

--- /code ---

--- /task ---

Now a new variable is needed to keep track of the location of the paddle. This will be called `pos_left` and set to `0`.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 26   
line_highlights: 29   
---

ball.speed_x = 0.4   
ball.speed_y = 0.4   

pos_left = 0

--- /code ---

--- task ---

Create a function for the paddle that will run when the motor encoder moves. Note that it uses a `global` variable so that it can change the value of the `pos_left` variable.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 31   
line_highlights:  
---

def moved_left(motor_speed, motor_rpos, motor_apos):   
    global pos_left   
    pos_left = motor_apos   

--- /code ---

--- /task---

--- task ---

Now add a single line that will use that function each time the motor is moved. It can be just before your `while` loop.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 35   
line_highlights:   
---

motor_left.when_rotated = moved_left

--- /code ---

--- /task ---

--- task ---

Then, add a line to the `while True` loop to update the paddle object on the screen to the new position. 

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 45    
line_highlights: 47   
---

    if ball.ycor() < -160:   
        ball.speed_y *= -1   
    paddle_left.sety(pos_left)  

--- /code ---

--- /task ---

--- task ---

Run your code and then turn the wheel on your motor encoder. You should see your paddle moving up and down the screen.

--- /task ---

![A view of the game window showing the bouncing ball and moving paddle.](images/moving_paddle.gif)

In case there are errors, your code should currently look like this:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start:    
line_highlights:    
---

from turtle import *   
from time import sleep   
from buildhat import Motor   

motor_left = Motor('A')

game_area = Screen()   
game_area.title('PONG')   
game_area.bgcolor('black')   
game_area.tracer(0)   
game_area.setworldcoordinates(-200,-170,200,170)   

ball = Turtle()   
ball.color('white')   
ball.shape('circle')   
ball.penup()   
ball.setpos(0,0)   

paddle_left = Turtle()   
paddle_left.color('green')   
paddle_left.shape("square")   
paddle_left.shapesize(4,1,1)   
paddle_left.penup()   
paddle_left.setpos(-190,0)   

ball.speed_x = 0.4   
ball.speed_y = 0.4   

pos_left = 0


def moved_left(motor_speed, motor_rpos, motor_apos):   
    global pos_left   
    pos_left = motor_apos   


motor_left.when_rotated = moved_left

while True:   
    game_area.update()   
    ball.setx(ball.xcor() + ball.speed_x)   
    ball.sety(ball.ycor() + ball.speed_y)   
    if ball.ycor() > 160:   
        ball.speed_y *= -1   
    if ball.xcor() > 195:   
        ball.speed_x *= -1   
    if ball.ycor() < -160:   
        ball.speed_y *= -1   
    paddle_left.sety(pos_left) 
      
--- /code ---

--- save ---