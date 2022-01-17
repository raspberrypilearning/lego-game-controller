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
stift = Turtle()
stift.hideturtle()
stift.color('grey')
stift.penup()
schrift = ("Courier",30,'bold')
stift.setposition(0,150)
stift.write(f'{punkte_l} PONG {punkte_r}', font=schrift, align='center')
```

Du kannst in der Dokumentation der Turtle-Bibliothek nachsehen, welche anderen Optionen es für die Anzeige des Textes gibt.

--- /task ---

Wenn du dein Programm jetzt ausführst, sollten die Punktestände und der Pong-Titel erscheinen. Die Punktestände selbst werden aber nicht aktualisiert.

--- task ---

Find the two conditionals for each of the scoring situations — when ball is missed by a paddle and disappears to the left or right — and update the score by re-writing the new value.

```python
     stift.clear()
     stift.write(f'{punkte_l} PONG {punkte_r}', font=schrift, align='center')
```

--- /task ---

![Eine Ansicht des Spielfensters mit den Punktzahlen am oberen Rand.](images/score.png)

### Hinzufügen eines Summers

Um einige einfache Soundeffekte hinzuzufügen, schließe einen Summer an die GPIO-Pins des Raspberry Pi an.

[[[rpi-connect-buzzer]]]

Anstatt ein Steckbrett zu verwenden, kannst du Überbrückungskabel mit Buchsen an beiden Enden verwenden und die Beine des Summers in die Buchsen stecken. Verwende dann einige LEGO®-Elemente, um den Summer zu montieren, damit er nicht während hektischer Spielsitzungen herumflattert und getrennt wird.

![Ein Foto eines Raspberry Pi, der auf einer LEGO® Maker Plate montiert ist, mit einem Summer, der mit LEGO-Elementen befestigt ist.](images/buzzer.JPG)

--- task ---

Füge nun beim Start deines Programms die `gpiozero` Bibliothek zur Liste der Importe hinzu:

```python
from gpiozero import Buzzer
```

Stelle dann den Summer dem Programm zur Verfügung, indem du einstellst, an welchen Pin du das positive (+) Bein angeschlossen hast. In diesem Beispiel haben wir Pin 17 verwendet.

```python
summer = Buzzer(17)
```

Wenn du nicht Pin 17 verwendet hast, ändere den Wert so, dass er den Pin angibt, mit dem dein Summer verbunden ist.

--- /task ---

Der Summer soll einen kurzen Ton abspielen, wenn Schläger und Ball Kontakt haben.

--- task ---

Füge diese Zeile zu jedem Aktionsteil der `if` Bedingungen der Berührungserkennung zwischen Ball und den Schlägern hinzu:

```python
summer.beep(0.1,0.1,background=True)
```

Füge dann eine Zeile hinzu, um einen längeren Ton zu spielen, wenn der Spieler den Ball verfehlt

```python
summer.beep(0.5,0.5,background=True)
```

--- /task ---

Weitere Informationen zu den mit Summern verfügbaren Optionen findest du in der [GPIO Zero-Dokumentation](https://gpiozero.readthedocs.io/en/stable/api_output.html#buzzer).

### Anpassen deiner Controller

In deinem Python Turtle-Programm hast du verschiedene Farben für die Schläger verwendet. Du kannst deine LEGO® Controller anpassen, indem du Steine und andere LEGO® Elemente derselben Farbe hinzufügst.

![Ein Foto mit einem farbigen Baustein auf einem LEGO® Rad.](images/blue_wheel.JPG)

Du kannst auch einen Griff für den Motor entwerfen, um ihn bequemer zu halten.

![Ein Foto eines LEGO®-Griffs, der der Motorsteuerung hinzugefügt wurde.](images/handle.JPG)


Dein Spiel sollte jetzt spielbar sein. Viel Spaß damit, bevor du schaust, was du als nächstes tun könntest.

--- save ---
