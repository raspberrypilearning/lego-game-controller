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

Jetzt kannst du den Motor anweisen, seine **absolute** Position zu melden. Diese liegt immer zwischen `-180` und `180`.

```python
motor_links.get_aposition()
```

Je nachdem, wie gut du den Motor beim Start positioniert hast, solltest du einen Wert nahe `0` bekommen.

Bewege den Motor und gib die Zeile ein zweites Mal ein, und schau, wie sich der Wert ändert.

--- /task ---

--- task ---

Du kannst auch die **relative** Position abfragen. Das zeigt an, wie viel es sich seit dem Programmstarts gedreht hat, so dass es bei jeder Umdrehung des Rades um `360` mehr oder weniger anzeigt.

```python
motor_links.get_position()
```
--- /task ---

--- task ---

Bewege den Motor hin und her und überprüfe seine absolute und relative Position, damit du verstehst, wie sich die Werte ändern.

--- /task ---


