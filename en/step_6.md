## Adding paddles

The turtle is the building block of the game.  It is already being used as the ball, now it can be used to create a paddle. 

### Creating a colour paddle

Add the code below to your program, before the `while True` loop. This should look similar to the way we created a ball. One new function is`turtle.shapesize(x,y,c)` which is used to stretch the size of a turtle's shape. Experiment with different values to see how this works.

--- task ---

```python
paddle_l = Turtle()
paddle_l.color('green')
paddle_l.shape('square')
paddle_l.shapesize(4,1,1)
paddle.penup()
paddle.setpos(-190,0)
```

--- /task ---

Run the code. You should see a green paddle on the left of the game area. Now to make this move using the LEGO technic motor.

### Moving the paddle

We can now integrate the code we wrote back in teh first step, to constantly read the position of a motor. 

--- task ---
First, add the line that imports the build_hat library to the top of your program. 

--- /task ---

--- task ---
Then add the Build Hat initialisation line and the motor variable creation line after the import lines. To help make the program easier to understand, use the variable name `motor_l` to indicate it s being used for the left hand paddle. 

--- /task ---

--- task ---
Now within the `while True` loop, add these lines which read the motor position into a variable and then use that to set the paddle's position. Because we chose our game area dimensions wisely there is no need for any conversion. 

```python
pos_l = motor_l.get()[2]
paddle_l.sety(pos_l)
```

--- /task ---

Your program should look like this:

```python
from turtle import *
from time import sleep
from build_hat import BuildHAT

bh = BuildHAT()

motor_l = bh.port.A.motor

game_area = Screen()
game_area.title('PONG')
game_area.setworldcoordinates(-200,-170,200,170)
game_area.tracer(0)
game_area.bgcolor('black')

ball = Turtle()
ball.color('white')
ball.shape('circle')
ball.pendown()
ball.setpos(0,0)

ball.speed(0)
ball.dx = 0.7
ball.dy = 0.7

paddle_l = Turtle()
paddle_l.color('green')
paddle_l.shape("square")
paddle_l.shapesize(4,1,1)
paddle_l.penup()
paddle_l.setpos(-190,0)


while True:
    game_area.update()
    pos_l = motor_l.get()[2]
    paddle_l.sety(pos_l)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 160: # or ball.ycor() < -165: # bottom
        ball.dy *= -1
    if ball.ycor() < -160: # or ball.ycor() < -165: # bottom
        ball.dy *= -1
    if ball.xcor() > 195: # or ball.ycor() < -165: # bottom
        ball.dx *= -1
```