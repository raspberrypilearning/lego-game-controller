## Den Ball bewegen

Der Ball wird auf dem Bildschirm herumspringen. Daher sind zwei Variablen erforderlich, um seine Geschwindigkeit sowohl in der `x-` als auch in der `y-`Richtung festzulegen. Diese Zahlen können größer sein, um das Spiel schwieriger zu machen, oder kleiner, um das Spiel zu vereinfachen.

--- task ---

Füge deinem Code die folgenden Zeilen hinzu:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 23
line_highlights:
---

ball.speed_x = 1   
ball.speed_y = 1

--- /code ---

--- /task ---

Du kannst überprüfen, wo sich eine Turtle befindet, indem du `turtle.xcor()` und `turtle.ycor()` verwendest, um die `x-` bzw. `y-`Koordinaten zu finden.

Um den Ball in Bewegung zu setzen, kannst du Position und Geschwindigkeit kombinieren.

--- task ---

Füge diesen Code deinem Programm hinzu:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 27
line_highlights: 30, 31
---

while True:   
spielflaeche.update()   
ball.setx(ball.xcor() + ball.speed_x)   
ball.sety(ball.ycor() + ball.speed_y)

--- /code ---

--- /task ---

Führe das Programm aus und schau, was passiert!

![Pong-Bildschirm mit dem Ball, der in die obere rechte Ecke fliegt.](images/ball_diagonal.gif)

Der Ball sollte sich schräg nach oben in Richtung obere rechte Ecke der Spielfläche bewegen... und dann weiterfliegen! Wenn du möchtest, dass dein Spiel schnell und herausfordernd ist, kannst du die `speed_x` und `speed_y` Werte erhöhen, damit sich der Ball schneller bewegt.

Der Ball sollte aber von der oberen Wand abprallen und nicht vom Bildschirm verschwinden. Dazu kann die Geschwindigkeit umgekehrt werden, so dass sich der Ball in die entgegengesetzte Richtung bewegt, wenn seine `y-`Position größer als 160 ist.

--- task ---

Füge den folgenden Code in deine Spielschleife ein und führe ihn aus.

--- code ---
---
language: python   
filename: pong.py     
line_numbers: true   
line_number_start: 27
line_highlights: 32, 33
---

while True:   
spielflaeche.update()   
ball.setx(ball.xcor() + ball.speed_x)   
ball.sety(ball.ycor() + ball.speed_y)   
if ball.ycor() > 160: ball.speed_y *= -1

--- /code ---

--- /task ---

--- task ---

Führe deinen Code erneut aus, und der Ball sollte vom oberen Bildschirmrand abprallen und rechts vom Bildschirm verschwinden.

--- /task ---

Auf die gleiche Weise, wie der Code die obere `y-`Position des Balls überprüft, kann er die rechte `x-`Position und die untere `y-`Position in deiner Spielschleife überprüfen, damit er springt.

--- task ---

Füge diese Kontrollen der Ball-Position hinzu.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 32
line_highlights:
---

    if ball.ycor() > 160:   
        ball.speed_y *= -1   
    if ball.xcor() > 195:   
        ball.speed_x *= -1   
    if ball.ycor() < -160:   
        ball.speed_y *= -1

--- /code ---

--- /task ---

Der Ball sollte nun um den Bildschirm herumspringen und über den linken Rand hinausfliegen. Als nächstes steuerst du deinen Schläger, um den Ball von der linken Kante zurück zu reflektieren.

--- save ---
