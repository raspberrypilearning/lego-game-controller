## The legendary game of Pong

[Pong](https://en.wikipedia.org/wiki/Pong) was one of the earliest arcade video games, originally released in 1972 by Atari . It is a table tennis game featuring simple two-dimensional graphics.  The player controls an in-game paddle by moving it vertically across the left or right side of the screen. They can compete against another player controlling a second paddle on the opposing side. Players use the paddles to hit a ball back and forth and the first player earns a point if the second player fails to return the ball.

You can read more about the history of Pong and look at a another Python version of the game in the boom [Code the Classics](https://wireframe.raspberrypi.org/books/code-the-classics1/pdf)

### Creating a simple version of Pong with Python

There are lots of ways to create a Pong-style game with Python. One approach is to use the pygame or pg-zero libraries, but this project is goimng to use the turtle library. 

Turtle is a versatile drawing and animation library and you can learn more about it with this [excellent project](https://projects.raspberrypi.org/en/projects/turtle-race). 

### Creating a game area

First let's create a window where the game will be played. 

--- task ---

Open a new file in Thonny and add the follwoing code to import the turtle and time libraries and then set up a screen. Run the file and you should see a black window with the title "PONG" open. 

```python
from turtle import *
from time import sleep

game_area = Screen()
game_area.title("PONG")
game_area.bgcolor('black')
game_area.tracer(0)
```

--- /task ---

### Designing the controls

The LEGO Technic motor is going to be used to control the position of a paddle and there are few ways this could work. 

One approach is to have the zero position of the motor correspond to the midpoint of the vertical axis of the game area. The motor's axle can move through 360 degrees and we could let our paddle drop off the bottom of the game area and re-appear at the top, like Pac Man does in that other classic game.

However being clever about how coordinates are assigned to the game area will make it easier  easy to map motor position onto the paddle's position.  If the motion of the motor and wheel is limited to less than 180 degrees in either direction (clockwise or anti-clockwise) then the game area could have a corresponding height of less than 360 pixels. 

A simple way to limit the motion of the wheel is to add a LEGO element to prevent the wheel turning through a complete rotation.  

The Turtle library also has a useful way of setting the coordinates for a screen area. Add this line to your program

--- task ---

```python
game_area.setworldcoordinates(-200,-170, 200, 170)
```
--- /task ---

This creates a rectangular window 400 pixels wide and 340 high, with 0 being at the midpoint of each axis. 

--- task ---

### Moving turtles

To verify that the coordinates of the game area are set correctly, use a turtle "ball" to move from the centre to each corner in turn. Add this code to your program and then run it.

```python
ball = Turtle()
ball.color('white')
ball.shape('circle')

ball.setpos(0,0)
corners = [(-200,-170), (-200,170), (200,170), (200,-170)]
for c in corners:
    ball.setpos(-200,-170)
    game_area.update()
    sleep(1)

```

--- /task ---

 The `turtle.setpos(x,y)` function is used to move a turtle to a given position. The screen also needs to be updated after each change.  What would happen if the `game_area.update()` line is moved outside the loop?