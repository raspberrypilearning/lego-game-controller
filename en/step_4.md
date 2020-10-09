## Keepimg the ball in play

Let's keep track of the ball's speed in both the x and y direction using a couple of variables:

--- task ---
Add the following code to your program:

```python
ball.dx = 1
ball.dy = 1
```
--- /task ---
You can check where a turtle is by using `turtle.xcor()` and `turtle.ycor()` to find the x and y coordinates respectively. 

So to make the ball move you can combine the position and speed. 

--- task ---
Add the lines below to your program:

```python
while True:
    game_area.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
```
--- /task ---

Instead of using `ball.setpos()`, this approach sets the x and y coordinates indivdually to make the program more readable.  Run the program. What happens?

The ball should move diagonally upwards towards the top right corner of the game area... and then keep on going! 

Now that you know how to move a ball/turtle, you need to constrain that motion to the game area. The top and bottom of the area will have invisible walls that the ball will bounce off.


--- task ---
Add the following code to your program and run it. 

```python
if ball.ycor() > 160:
    ball.dy *= -1
```
--- /task ---

Now the ball should bounce off the top wall because once its y position exceeds 160, its speed is reveresed - so it will travel in the opposite direction. 

--- task ---

Duplicate the added in the step above and modify it to add the same effect to the wall at the bottom of the game area.

--- hints ---
--- hint ---
The bottom wall will have a y-axis boundary value of -160
--- /hint ---
--- hint ---
In order for the ball to remaion in play, its y coordinate needs to be greater than this boundary value.  So, reversing that logic, the ball should change direction if its y coordinate gets smaller than -160.

--- /hint ---

--- hint ---
So your conditional test should look like this:

```python
if ball.ycor() < -160:
    ball.dy *= -1
```
--- /hint ---

--- /hints ---
--- /task ---

While you're testing the game, it will be easier to also have one side wall be bonucy, so that you can test out a paddle on the opposite end, like you are playing squash. 

--- task ---

Duplicate the added in the step above and modify it to add the same effect to the wall at the right hand side of the game area.

--- hints ---
--- hint ---
The right wall will have an x-axis boundary value of 195.

--- /hint ---
--- hint ---
In order for the ball to remaion in play, its x coordinate needs to be less than this boundary value.  So, reversing that logic, the ball should change direction if its x coordinate gets greater than 195.

--- /hint ---

--- hint ---
So your conditional test should look like this:

```python
if ball.xcor() > 195:
    ball.dx *= -1
```
--- /hint ---

--- /hints ---
--- /task ---

Test you program and make sure that the ball bounces off all walls except for the one on the left hand side. 

The next step is to add paddles and link them to the LEGO motors.
