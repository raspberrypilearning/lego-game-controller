## Make your Pong screen

Turtle is a drawing and animation library and you can learn more about it with this [excellent project](https://projects.raspberrypi.org/en/projects/turtle-race).


First, create a window where the game will be played.

--- task ---

Open a new file in Thonny and add the following code to import the Turtle, time, and Build HAT libraries, and then set up a screen. Run the file and you should see a black window with the title "PONG" open. You don't need to include the `#` comments.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 1
line_highlights:
---

from turtle import Screen, Turtle from time import sleep from buildhat import Motor

game_area = Screen() #Create a screen   
game_area.title("PONG") #Give the screen a title   
game_area.bgcolor('black') #Set the background colour   
game_area.tracer(0) #Give smoother animations

--- /code ---

--- /task ---

The Turtle library also has a useful way of setting the coordinates for a screen area. Add this line to your program:

--- task ---

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 8
line_highlights: 9
---

game_area.tracer(0)   
game_area.setworldcoordinates(-200, -170, 200, 170)

--- /code ---

--- /task ---

This creates a rectangular window 400 pixels wide and 340 high, with 0 being in the centre.

![A screenshot of the game window, showing the co-ordinates of each corner and the centre. Top left is -200,170, top right is 200,170, bottom left is -200,-170, and bottom right is 200,-170. The centre is 0,0.](images/coords.png)

--- task ---

Now, you need to update your game area, to see the paddle and ball. Add a **game loop** to the bottom of your code, and call the `update()` method.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 10
line_highlights:
---

while True:   
game_area.update()

--- /code ---

Run your code and you should see a black window appear.

--- /task ---

--- task ---

Next, you can make a ball by using a Turtle that is set to be a white circle. The ball should start in the middle of the screen, and shouldn't draw a line when it moves.

**Above** your `while True` loop, add the following code:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 10
line_highlights:
---

ball = Turtle()   
ball.color('white')   
ball.shape('circle')   
ball.penup()   
ball.setpos(0,0)

while True:

--- /code ---

--- /task ---

--- task ---

Run your code again. You should see a white ball appear in your window.

--- /task ---

--- task ---

Next, you can set up a paddle in the same way. It will be a green rectangle, and positioned on the far left of the screen.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 17
line_highlights:
---

paddle_left = Turtle()   
paddle_left.color('green')   
paddle_left.shape('square')   
paddle_left.shapesize(4, 1, 1)   
paddle_left.penup()   
paddle_left.setpos(-190, 0)

--- /code ---

--- /task ---

--- task ---

Run your code and you should see your ball and paddle.

![A white ball in the centre of a black window, with a green paddle on the far left.](images/pong_static.png)

--- /task ---
