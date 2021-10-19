## Introduction

In this project, you will use the Raspberry Pi Build HAT, a LEGO® Technic™ motor encoder and wheel, and the Python Turtle library to make a simple game controller that you can use to play Pong.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">[Pong](https://en.wikipedia.org/wiki/Pong)</span> is one of the earliest arcade video games, originally released in 1972 by Atari. It is a table tennis game featuring simple two-dimensional graphics. Players control paddles on each side of the screen, which they use to hit a ball back and forth.
</p>

You will:
- Learn how to read the degrees of rotation from LEGO® Technic™ motors
- Learn to draw and move Turtle graphics using LEGO® Technic™ motors
- Learn to detect collisions between graphics using `x` and `y` coordinates

--- no-print ---

![A movie showing a pong game being controlled by two LEGO® Technic™ motors with large blue wheels.](images/pong_gif.gif)

--- /no-print ---

--- print-only ---

![Complete project.](images/finished.JPG)

--- /print-only ---

### You will need

+ A Raspberry Pi computer
+ A Raspberry Pi Build HAT
+ At least one LEGO® Technic™ motor
+ Assortment of LEGO®, including wheels (we used a selection from the [LEGO® Education SPIKE™ Prime kit](https://education.lego.com/en-gb/product/spike-prime))
+ A small breadboard (optional)
+ A buzzer (optional)
+ Some breadboard jumper leads (optional)
+ A 7.5V power supply with a barrel jack (optional). You can use an official Raspberry Pi power supply for this project, as the motor encoders will not be using any power

### Software

+ Python 3
+ Build HAT Python library

--- collapse ---
---
title: Additional information for educators
---

You can download the completed project [here](https://rpf.io/p/en/lego-game-controller-get){:target="_blank"}.

If you need to print this project, please use the [printer-friendly version](https://projects.raspberrypi.org/en/projects/lego-game-controller/print){:target="_blank"}.

--- /collapse ---

Before you begin, you'll need to have set up your Raspberry Pi computer and attached your Build HAT:

--- task ---

Mount your Raspberry Pi on to the LEGO Build Plate using M2 bolts and nuts, making sure the Raspberry Pi is on the side without the 'edge':

 ![Raspberry Pi bolted to a magenta LEGO Build Plate.](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot. The Build Plate will allow you to connect the Raspberry Pi to the main structure of your dashboard more easily.

--- task ---

Line up the Build HAT with the Raspberry Pi, ensuring you can see the `This way up` label. Make sure all the GPIO pins are covered by the HAT, and press down firmly. (The example uses a [stacking header](https://www.adafruit.com/product/2223){:target="_blank"}, which makes the pins longer.)

![Image of GPIO pins poking through the top of the Build HAT.](images/build_15.jpg)
![Animation showing Buildhat fitting to Raspberry Pi](images/haton.gif)

--- /task ---

You should now power your Raspberry Pi using the 7.5V barrel jack on the Build HAT, which will allow you to use the motors. 

--- task ---

If you have not already done so, set up your Raspberry Pi by following these instructions:

[Setting up your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Once the Raspberry Pi has booted, open the Raspberry Pi Configuration tool by clicking on the Raspberry Menu button and then selecting “Preferences” and then “Raspberry Pi Configuration”.

Click on the “interfaces” tab and adjust the Serial settings as shown below:

![Image showing Raspberry Pi OS config screen with serial port enabled and serial console disabled](images/configshot.jpg)

--- /task ---

--- task ---

You will also need to install the buildhat python library by following these instructions: 

--- collapse ---
---
title: Install the buildhat Python library
---

Open a terminal window on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

At the prompt type: `sudo pip3 install buildhat`

Press <kbd>Enter</kbd> and wait for the "installation completed" message.

--- /collapse ---

--- /task ---