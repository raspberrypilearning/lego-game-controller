## Collisions

You should find that the paddle moves up and down as you turn the wheel on your LEGO Technic motor.  The game is nearly complete - but first you need to add some extra collision detection that covers the ball hitting the paddle. In the Scratch programming environment there are dedicated functions such as the `touching?`{:class="block3events"} and in game development libraries like pygame there are similar functions to handle collisions.

Using the Turtle library you can easily replicate this by checking if the two objects - the paddle and the ball - are in the same location at the same time. 

--- task ---
Within the existing `while True` loop, add this conditional test that checks if the balls y position is in the vertical channel in which the paddle moves. The conditional clause also includes an `and` because the ball's x position must also be within the horizontal area covered by the paddle. If you've chosen a different paddle size, you will need to adjust the range of the values that match the paddle's `ycor`. 

```python
    if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < 
paddle_l.ycor() + 20 and ball.ycor() > paddle_l.ycor() - 20):
        ball.setx(-180)
        ball.dx *= -1
```

--- /task ---

Try the program out. You should be able to bounce the ball off you paddle and play a solo game of squash. However you will probably see that the ball slows down as the game progresses, especially if you are using an older Raspberry Pi. This is because drawing the trail of the ball use a lot of the computer's resources. 

--- task ---
Turn off the drawing for the ball in the same way as you have for the paddle.

```python
ball.penup()
```

--- /task ---

Now you have a way of preventing the ball from disappearing off-screen, it's time to think about what happens if you fail to make a save. 

For now let's just reset the ball back to start.

--- task ---
Add this code within the `while True` loop:

```python
    if ball.xcor() < -195: # left
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
```

--- /task ---

Once you're happy with the various settings, it's time to add in the second paddle.

--- task ---
  Using what you've created for the left hand paddle as a starting point, add a second paddle on the right hand side of the game area. 

--- hints ---
--- hint ---
First of all, connect a second motor to the Build HAT (port B) and set it up in the program 

```python
motor_r = Motor('B')
```

Now duplicate the code for creating a paddle and change its colour and starting position.

```python
paddle_r = Turtle()
paddle_r.color('blue')
paddle_r.shape("square")
paddle_r.shapesize(4,1,1)
paddle_r.penup()
paddle_r.setpos(190,0)
pos_r = 0
```
And add callback function to update the paddle's position based on the motor position. 

```python
def moved_r(motor_speed, motor_rpos, motor_apos):
    global pos_r
    pos_r = motor_apos
 ```
and add a line to update the paddle on screen to the `while True` loop:

```python
paddle_r.sety(pos_r)
```
--- /hint ---
--- hint ---

Currently the ball will bounce off the right hand wall. Modify the lines of your program that make that happen so that the ball is instead reset to the centre.

```python
   if ball.xcor() > 195: # right
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
```

--- /hint ---

--- hint ---
Finally replace the block of code that causes the ball to bounce of the right hand wall with a modified version of the code you wrote to handle collisions with the first paddle. 

```python
   if (ball.xcor() > 180 and ball.xcor() < 190) and (ball.ycor() < pa
ddle_r.ycor() + 20 and ball.ycor() > paddle_r.ycor() - 20):
        ball.setx(180)
        ball.dx *= -1
```
--- /hint ---

--- /hints ---

--- /task ---

You should now be able to enjoy a basic 2 player game of pong.

![A view of the game window showing a 2 player game. There is a green paddle on the left and a blue one on the right](images/game.png)

--- save ---