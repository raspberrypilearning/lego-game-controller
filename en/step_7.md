## Finishing touches

There are few additional features you can add to finish off your game.

### Adding a score

--- task ---
Keep tack of the score using two variables (one for each player) and update them whenever a round is lost.

--- hints ---
--- hint ---
First of all, declare the new variables somewhere towards the top of the program and set the starting score to zero.

```python
score_r = 0
score_l = 0
```
--- /hint ---
--- hint ---

Whenever a ball is missed, increment the appropriate score variable by one. There are two conditional tests you'll need to modify.


--- /hint ---

--- hint ---
```python
    if ball.xcor() > 195: # right
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        score_r+=1
    if ball.xcor() < -195: # left
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        score_l+=1
```
--- /hint ---

--- /hints ---
--- /task ---

Now you need to display the score on the game area. You can use a fourth turtle to handle this job.

--- task ---
Add the following to your program after the creation of the paddle and ball Turtles, but before the `while True` loop.

```python
writer = Turtle()
writer.hideturtle()
writer.color('grey')
writer.penup()
style = ("Courier",30,'bold')
writer.setposition(0,150)
writer.write(str(score_l) +" PONG " + str(score_r), font=style, align='center')
```

You can look at the documentation for the Turtle library to see what other options there are for how the text is displayed. 
--- /task ---

If you run your program now, the score and Pong legend should appear, but the scores themsleves won't get updated.  

--- task ---
Find the two conditionals for each of the scoring sitautions - whnen ball is missed by a paddle and disappears to the left or right - and update the scrore by re-writing the new value. 

```python
     writer.clear()
     writer.write(str(score_l) +" PONG " + str(score_r), font=style, align='center')
```

--- /task ---

You can look at the documentation for the Turtle library to see what other options there are for how the text is displayed. 

![bounce](images/score.png)

### Adding a buzzer

To include some simple sound effects, connect a buzzer to the GPIO pins on the Raspberry Pi.

[[[rpi-connect-buzzer]]]


Instead of using a breadboard, you could use jumper leads with female sockets at both ends and poke the legs of the buzzer into the socket. Then use some LEGO elements to mount the buzzer so that it doesn't flop around and become disconected during frantic gaming sessions.


![buzzer mount](images/buzzer.JPG)

--- task ---

Now add the `gpiozero` library to the list of imports at the start of you program:

```python
from gpiozero import Buzzer
```

Then make the buzzer availble for the programn to use to by setting which pin you have connected the positive (+) leg to.

```python
buzz = Buzzer(17)
```
If you didn't use pin 17, change the value to reflect the correct pin.


--- /task ---

Now whenever the paddle and ball make contact, you can play a short tone.

--- task ---

Add this line to each action part of the collision detection `if` conditionals for the ball and paddle:

```python
buzz.beep(0.1,0.1,background=True)
```

Then add a  line to play a lonegr tone whenever the player misses the ball

```python
buzz.beep(0.5,0.5,background=True)
```

--- /task ---


You can read moer about the options available with buzzers in the [GPIO Zero documenation](https://gpiozero.readthedocs.io/en/stable/api_output.html#buzzer)



### Customising your controllers

In your Python Turtle program you have used different colours for the paddles. You can customise your LEGO controllers by adding bricks and other LEGO elemnets of the same solour.

![coloured blocks on wheel](images/blue_wheel.JPG)

You could also design a handle for the motor to make it more comfortable to hold.

![handle for controller](images/handle.JPG)

### Adding some randomness

At the moment, the motion of ther ball will always start exactly the same way each time. let's add some randomness to make the game more interesting.

--- task ---
First of all, add the rndom library to the imports section at the start of the program.

```python
import random
```

Then fimd the line where you set the ball's initial position and  speed so that the x and y components of the motion both incorporate an inital random offset. Then this is multiplied either by 1 or -1 (chosen at random) so that the ball's initial trajectory can be anywhere in the game area and not just diagonally towards the top right corner. Let's wrap this up as a function so we can call it whenevr we need to restart the game without duplicating all these lines. 
 
```python
def ball_start(start_value):
    ball.setpos(0,0)
    ball.speed(0)
    ball.dx = start_value * random.uniform(0.8,1.5) * random.choice([-1,1])
    ball.dy = start_value * random.uniform(0.8,1.5) * random.choice([-1,1])
```
You can monify the range for which the first random numbers can cover to tweak the feel of the game. 
 
--- /task ---

--- task ---
Now add a call to this function at the start of the game (just before the `while True` loop and at both points where the ball is reset to the centre after a miss.

```python

ball_start(0.7)
```
--- /task ---

Your game should now be playable. Have some fun with it before seeing what else you can do next. 

--- save ---