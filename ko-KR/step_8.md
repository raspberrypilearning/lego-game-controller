## Improve your project

게임을 마무리하기 위해 추가할 수 있는 몇 가지 부가 기능이 있습니다.

### 점수 추가하기

--- task ---

두 개의 변수(각 플레이어에 대해 하나씩) 를 사용하여 점수를 기록하고 라운드를 질 때마다 업데이트하세요.

--- hints --- --- hint ---

먼저 프로그램 상단에 새 변수를 선언하고 시작 점수를 0으로 설정합니다.

```python   
score_r = 0   
score_l = 0   
```

--- /hint --- --- hint ---

공을 놓칠 때마다 score 변수를 1씩 증가시킵니다. 수정해야 할 두 가지 조건문이 있습니다.


--- /hint ---

--- hint ---

```python
    if ball.xcor() > 195: #Right
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        score_r+=1
    if ball.xcor() < -195: #Left
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        score_l+=1
```

--- /hint ---

--- /hints --- --- /task ---

이제 게임 영역에 점수를 표시해야 합니다. fourth Turtle을 사용해서 이름을 지을 수 있습니다.

--- task ---

클럽과 공 터틀을 만든 후 `while True` 루프 앞에 다음을 추가하십시오.

```python
writer = Turtle()
writer.hideturtle()
writer.color('grey')
writer.penup()
style = ("Courier",30,'bold')
writer.setposition(0,150)
writer.write(f'{score_l} PONG {score_r}', font=style, align='center')
```

Turtle 라이브러리 문서를 보면 텍스트가 표시되는 방식에 대한 다른 옵션이 무엇인지 확인할 수 있습니다.

--- /task ---

If you run your program now, the score and Pong legend should appear, but the scores themselves won't get updated.

--- task ---

공이 패들에 의해 놓쳐 왼쪽이나 오른쪽으로 사라지는 경우와 같은 각 득점 상황에 대한 두 가지 조건을 찾고 새로운 값을 다시 작성하여 점수를 업데이트합니다.

```python
     writer.clear()
     writer.write(f'{score_l} PONG {score_r}', font=style, align='center')
```

--- /task ---

![A view of the game window with the score displayed at the top.](images/score.png)

### 타이머 추가하기

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
buzz = Buzzer(17)
```

If you didn't use Pin 17, change the value to reflect the pin your buzzer is connected to.

--- /task ---

Now, whenever the paddle and ball make contact, you want the game to play a short tone.

--- task ---

Add this line to each action part of the collision detection `if` conditionals for the ball and paddle:

```python
buzz.beep(0.1,0.1,background=True)
```

Then add a  line to play a longer tone whenever the player misses the ball

```python
buzz.beep(0.5,0.5,background=True)
```

--- /task ---

You can read more about the options available with buzzers in the [GPIO Zero documentation](https://gpiozero.readthedocs.io/en/stable/api_output.html#buzzer).

### Customising your controllers

In your Python Turtle program, you have used different colours for the paddles. You can customise your LEGO® controllers by adding bricks and other LEGO® elements of the same colour.

![A photo of coloured blocks on a LEGO® wheel.](images/blue_wheel.JPG)

You could also design a handle for the motor to make it more comfortable to hold.

![A photo of a LEGO® handle added to the motor controller.](images/handle.JPG)


Your game should now be playable. Have some fun with it before seeing what else you can do next.

--- save ---
