## Improve your project

Es gibt einige zusätzliche Funktionen, die du hinzufügen kannst, um dein Spiel fertig zu stellen.

### Einen Punktestand hinzufügen

--- task ---

Behalte die Punktzahl im Auge, indem du zwei Variablen verwendest (eine für jeden Spieler) und aktualisiere sie, wenn eine Runde verloren geht.

--- hints --- --- hint ---

Deklariere zunächst die neuen Variablen irgendwo im oberen Bereich des Programms und setze die Startpunktzahl auf Null.

```python   
punkte_r = 0   
punkte_l = 0   
```

--- /hint --- --- hint ---

Erhöhe die entsprechende Wertungsvariable um eins, wenn ein Ball verfehlt wird,. Es gibt zwei bedingte Tests, die du ändern musst.


--- /hint ---

--- hint ---

```python
    if ball.xcor() > 195: #Right
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        punkte_r+=1
    if ball.xcor() < -195: #Left
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        punkte_l+=1
```

--- /hint ---

--- /hints --- --- /task ---

Jetzt musst du noch den Spielstand auf der Spielfläche anzeigen. Um das zu tun, kannst du eine vierte Turtle verwenden.

--- task ---

Füge deinem Programm nach der Erstellung der Schläger- und Ball-Turtles, jedoch noch vor der `while True-` Schleife, Folgendes hinzu.

```python
writer = Turtle()
writer.hideturtle()
writer.color('grey')
writer.penup()
style = ("Courier",30,'bold')
writer.setposition(0,150)
writer.write(f'{score_l} PONG {score_r}', font=style, align='center')
```

Du kannst in der Dokumentation der Turtle-Bibliothek nachsehen, welche anderen Optionen es für die Anzeige des Textes gibt.

--- /task ---

If you run your program now, the score and Pong legend should appear, but the scores themselves won't get updated.

--- task ---

Finde die beiden Bedingungen für jede der Scoring-Situationen – wenn also der Ball von einem Schläger verfehlt wird und nach links oder rechts verschwindet – und aktualisiere die Punktzahl, indem du den neuen Wert neu schreibst.

```python
     writer.clear()
     writer.write(f'{score_l} PONG {score_r}', font=style, align='center')
```

--- /task ---

![A view of the game window with the score displayed at the top.](images/score.png)

### Hinzufügen eines Summers

To include some simple sound effects, connect a buzzer to the GPIO pins on the Raspberry Pi.

[[[rpi-connect-buzzer]]]

Instead of using a breadboard, you could use jumper leads with female sockets at both ends and poke the legs of the buzzer into the socket. Then use some LEGO® elements to mount the buzzer so that it doesn't flop around and become disconnected during frantic gaming sessions.

![A photo of a Raspberry Pi mounted on a LEGO® Maker Plate, with a buzzer attached using LEGO elements.](images/buzzer.JPG)

--- task ---

Now add the `gpiozero` library to the list of imports at the start of you program:

```python
from gpiozero import Buzzer
```

Then, make the buzzer available for the program to use by setting which pin you have connected the positive (+) leg to. In this example, we used Pin 17.

```python
summer = Buzzer(17)
```

If you didn't use Pin 17, change the value to reflect the pin your buzzer is connected to.

--- /task ---

Now, whenever the paddle and ball make contact, you want the game to play a short tone.

--- task ---

Add this line to each action part of the collision detection `if` conditionals for the ball and paddle:

```python
summer.beep(0.1,0.1,background=True)
```

Then add a  line to play a longer tone whenever the player misses the ball

```python
summer.beep(0.5,0.5,background=True)
```

--- /task ---

You can read more about the options available with buzzers in the [GPIO Zero documentation](https://gpiozero.readthedocs.io/en/stable/api_output.html#buzzer).

### Anpassen deiner Controller

In your Python Turtle program, you have used different colours for the paddles. You can customise your LEGO® controllers by adding bricks and other LEGO® elements of the same colour.

![A photo of coloured blocks on a LEGO® wheel.](images/blue_wheel.JPG)

You could also design a handle for the motor to make it more comfortable to hold.

![A photo of a LEGO® handle added to the motor controller.](images/handle.JPG)


Your game should now be playable. Have some fun with it before seeing what else you can do next.

--- save ---
