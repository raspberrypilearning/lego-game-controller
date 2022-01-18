## Schlägerberührungen

Das Spiel ist fast fertig – aber zuerst musst du eine Kollisionserkennung hinzufügen, die sich um den Fall der Berührung des Balles mit dem Schläger kümmert.

--- task ---

Überprüfe innerhalb der `while True` Schleife, ob sich die `x` Position des Balls im horizontalen Bereich befindet, der vom Schläger verwendet wird. Verbinde mit einem `and` Eine Prüfung ob die `y` Position des Balls im vertikalen Bereich des Schlägers liegt

--- code ---
---
language: python filename: pong.py   
line_numbers: true   
line_number_start: 47
line_highlights: 48
---

schlaeger_linkst.sety(pos_left)   
if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < schlaeger_links.ycor() + 20 and ball.ycor() > schlaeger_links.ycor() - 20): 
    ball.setx(-180)  
    ball.speed_x *= -1

--- /code ---

--- /task ---

Probiere das Programm aus. Du solltest in der Lage sein, den Ball von deinem Schläger abprallen zu lassen und ein Solo-Spiel „Squash“ zu spielen!

Jetzt hast du eine Möglichkeit, zu verhindern, dass der Ball aus dem Bildschirm verschwindet. Überlege dir, was passiert soll, wenn du den Ball nicht erwischt.

Setzen wir den Ball vorerst einfach wieder an den Start zurück.

--- task ---

Füge diesen Code innerhalb der Schleife `while True` ein:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 52
line_highlights: 53-56
---

        ball.speed_x *= -1   
    if ball.xcor() < -195: #linker Rand   
        ball.hideturtle()   
        ball.goto(0,0)   
        ball.showturtle()

--- /code ---

--- /task ---

Sobald du mit den verschiedenen Einstellungen zufrieden bist, ist es an der Zeit, den zweiten Schläger hinzuzufügen.

Verwende das, was du für den linken Schläger erstellt hast als Ausgangspunkt, und füge einen zweiten Schläger auf der rechten Seite des Spielbereichs hinzu.

--- task ---

Verbinde zunächst einen zweiten LEGO® Technic™ Motor mit dem Build HAT (Port B) und richte ihn im Programm ein.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 5
line_highlights: 6
---

motor_links = Motor('A')   
motor_rechts = Motor('B')

--- /code ---

--- /task ---

--- task ---

Du kannst deinen Code zum Einrichten deines linken Schlägers kopieren und einfügen. Ändere dann den Namen und die Werte für deinen rechten Schläger.

--- /task ---

--- task ---

Erstelle deinen rechten Schläger.

--- code ---
---
language: python   
filename: pong   
line_numbers: true   
line_number_start: 20
line_highlights: 27-32
---

schlaeger_links = Turtle()   
schlaeger_links.color('green')   
schlaeger_links.shape("square")   
schlaeger_links.shapesize(4,1,1)   
schlaeger_links.penup()   
schlaeger_links.setpos(-190,0)

schlaeger_rechts = Turtle()   
schlaeger_rechts.color('blue')   
schlaeger_rechts.shape("square")   
schlaeger_rechts.shapesize(4,1,1)   
schlaeger_rechts.penup()   
schlaeger_rechts.setpos(190,0)

--- /code ---

--- /task ---

--- task ---

Füge eine Variable für die rechte Schlägerposition, eine Funktion für den Schläger und die Zeile hinzu, um die Funktion aufzurufen, wenn der rechte Motor bewegt wird.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 37
line_highlights: 38, 46-48, 52
---

pos_links = 0   
pos_rechts = 0


def drehung_links(motor_speed, motor_rpos, motor_apos):   
    global pos_links   
    pos_links = motor_apos


def drehung_rechts(motor_speed, motor_rpos, motor_apos):   
    global pos_rechts   
    pos_rechts = motor_apos


motor_links.when_rotated = drehung_links   
motor_rechts.when_rotated = drehung_rechts

--- /code ---

--- /task ---

--- task ---

Fügen Sie eine Zeile zur `while True` Schleife hinzu, um den Schläger auf dem Bildschirm zu aktualisieren:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 64
line_highlights: 65
---

    schlaeger_links.sety(pos_links)   
    schlaeger_rechts.sety(pos_rechts)

--- /code ---

--- /task ---


Derzeit prallt der Ball von der rechten Wand ab. Ändere die Zeilen deines Programms, die dies ermöglichen, so, dass der Ball stattdessen in die Mitte zurückgesetzt wird.

--- task ---

Ändere die Bedingung für `xcor` des Balls, sodass er zurückgesetzt wird.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 60
line_highlights:
---

    if ball.xcor() > 195:   
        ball.hideturtle()   
        ball.goto(0,0)   
        ball.showturtle()

--- /code ---

--- /task ---

--- task ---

Füge nun für den rechten Schläger eine ähnliche Bedingung hinzu um Kollisionen zu behandeln wie für den linken.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 68
line_highlights: 71-73
---

    if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < schlaeger_links.ycor() + 20 and ball.ycor() > schlaeger_links.ycor() - 20):
        ball.setx(-180)
        ball.speed_x *= -1   
    if (ball.xcor() > 180 and ball.xcor() < 190) and (ball.ycor() < schlaeger_rechts.ycor() + 20 and ball.ycor() > schlaeger_rechts.ycor() - 20):
        ball.setx(180)   
        ball.speed_x *= -1

--- /code ---

--- /task ---

Du solltest jetzt in der Lage sein, ein einfaches Pong-Spiel für zwei Spieler zu genießen.

![Eine Ansicht des Spielfensters mit einem Spiel für zwei Spieler. Links ist ein grüner und rechts ein blauer Schläger, zwischen denen der Ball hüpft.](images/2_player_pong.gif)

--- save ---
