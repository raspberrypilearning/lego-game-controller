## Use LEGO® Spike™ motor encoders

Motor-Encoder können sich nicht nur drehen, sondern auch genau erkennen, um wie viel Grad sie gedreht wurden.

![Motor mit der Lollipop-Markierung in einer Linie mit einem Kreis.](images/aligned_symbols.jpg)

Alle LEGO® Spike™ Motoren haben Encoder. Wenn du dir die rotierende Scheibe am Motor ansiehst, siehst du eine Markierung in Form eines Lutschers, die mit der 0-Markierung auf dem weißen Gehäuse des Motors selbst ausgerichtet werden kann. Das ist die null Grad Position des Encoders und jede Winkelbewegung der Motorwelle kann relativ zu diesem Punkt gemessen werden.

--- collapse ---
---
title: Wie Motor-Encoder funktionieren
---

Ein Motorgeber, auch Dreh- oder Winkelgeber genannt, ist ein elektromechanisches Gerät, mit dem du die Winkelposition oder Bewegung der Achse erfassen kannst. Dies geschieht normalerweise durch die Umwandlung der Winkelposition in einen analogen oder digitalen Wert.

Wenn ein Motor einen Encoder hat, kannst du die Position der Achse sehr genau einstellen. Es ermöglicht dir, den Motor auch als Eingabegerät zu verwenden, so dass wenn sich die Position der Achse ändert, dies erkannt wird und zum Auslösen anderer Aktionen in einem Computerprogramm verwendet werden kann.

--- /collapse ---

--- task ---

Schließe einen Monitor, eine Tastatur und eine Maus an deinen Raspberry Pi an.

Verbinde deinen Build HAT, mit dem gedruckten Logo nach oben, mit deinem Raspberry Pi und stelle sicher, dass du alle Pins richtig bedeckt hast.

Schließe nun die Stromversorgung an; entweder über die Build HAT Hohlstecker-Buchse oder den USB-C-Port am Raspberry Pi.

--- /task ---

--- task ---

Schließe einen Motor an Port A des Build HAT an.

![Motor über ein Flachbandkabel an Port A des Build-HAT angeschlossen.](images/motor_attached.jpg)

--- /task ---

--- task ---

Befestige ein großes Rad mit vier Verbindungsstiften am Motor. Drehe das Rad so, dass die Lollipop-Markierung mit der Null-Position übereinstimmt.

![Motor mit angebrachten Verbindungsstiften.](images/motor_with_pegs.jpg) ![Motor mit angebautem großen Rad.](images/motor_with_wheel.jpg)

--- /task ---

--- task ---

Öffne Thonny aus dem **Entwicklung**-Menü und klicke auf den Reiter **Shell** im unteren Teil des Fensters.

--- /task ---

--- task ---

Importiere zuerst die Build HAT-Bibliothek.

```python
from buildhat import Motor
```
Drücke Enter.

--- /task ---

--- task ---

Erstelle dann ein Motorobjekt, das Python mitteilt, dass der Motor mit Port `A` verbunden ist. Tippe:

```python
motor_links = Motor('A')
```
Drücke Enter. (Es wird eine leichte Verzögerung geben, hab etwas Geduld!)

--- /task ---

--- task ---

Now, you can ask the motor to report its **absolute** position. This will always be between `-180` and `180`.

```python
motor_links.get_aposition()
```

Depending on how well you positioned the motor at the start, you should get a value close to `0`.

Move the motor and type the line a second time, and see how the value changes.

--- /task ---

--- task ---

You can also keep track of the motor's **relative** position. This is how far it has moved from the time the program starts, so it will increase or decrease by `360` for every turn of the wheel.

```python
motor_links.get_position()
```
--- /task ---

--- task ---

Move the motor around and check its absolute and relative positions, so that you understand how the values change.

--- /task ---


