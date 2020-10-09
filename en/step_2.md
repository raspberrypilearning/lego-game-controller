## Motor encoders

Let's look at how motor encoders work.

A motor encoder, also called a rotary or shaft encoder, is an electro-mechanical device that allows you to record the angular position or motion of the axle. It normally does this by converting the angular position to an analog or digital output. 

If a motor has an encoder, that means you can very accurately set the position of the axle. It also allows you to use the motor as an input device so that if something changes the position of the axle, this can be registered and used to trigger other actions in a computer program. 

The LEGO motors all have encoders. If you look at the rotating disk part of the motor, you will see a mark shaped like a lollipop that can be lined up with the 0 mark on the white body of the motor itself. This is the encoder set to zero degrees and any angular movement of the motor shaft can be measured relative to this point.

Let’s see that in action with some code.

--- task ---

Open Thonny from the Raspberry Pi OS Desktop and click onto the REPL box at the bottom. 

--- /task ---

--- task ---

First import the BuildHAT library

```python
from build_hat import BuildHAT
```

Then initialise a connection to the HAT

```python
bh = BuildHAT()
```

--- /task ---

--- save ---