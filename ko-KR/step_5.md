## Move the ball

`x` 및 `y` 방향 모두에서 공의 속도를 알아내기 위해서는, 두 개의 변수가 필요합니다. 이 숫자는 게임을 더 어렵게 만들기 위해 더 크게 하거나 게임을 더 쉽게 만들기 위해 더 작게 할 수 있습니다.

--- task ---

다음 코드를 당신의 프로그램에 추가해 보세요:

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

You can check where a Turtle is by using `turtle.xcor()` and `turtle.ycor()` to find the `x` and `y` coordinates, respectively.

따라서 공을 움직이게 하려면 위치와 속도를 결합할 수 있습니다.

--- task ---

Add the lines below to your program:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 27
line_highlights: 30, 31
---

while True:   
game_area.update()   
ball.setx(ball.xcor() + ball.speed_x)   
ball.sety(ball.ycor() + ball.speed_y)

--- /code ---

--- /task ---

프로그램을 실행해서 어떤 일이 발생하는지 확인하세요!

![공이 오른쪽 상단 모서리로 이동하는 탁구 화면](images/ball_diagonal.gif)

공은 게임 영역의 오른쪽 상단 모서리를 향해 대각선 위쪽으로 움직여야 합니다... 그런 다음 계속 진행하도록 합니다! 빠르고 도전적인 게임을 원한다면 `speed_x` 및 `speed_y` 값을 높게 바꾸어 공이 더 빨리 움직이도록 할 수 있습니다.

공은 화면에서 사라지지 않고 상단 벽에서 튀어나오도록 해야 합니다. 이를 구현하기 위해서는, `y` 위치가 160보다 큰 경우 속도를 역전시켜 공이 반대 방향으로 이동하도록 할 수 있습니다.

--- task ---

게임 루프에 다음 코드를 추가하고 실행합니다.

--- code ---
---
language: python   
filename: pong.py     
line_numbers: true   
line_number_start: 27
line_highlights: 32, 33
---

while True:   
game_area.update()   
ball.setx(ball.xcor() + ball.speed_x)   
ball.sety(ball.ycor() + ball.speed_y)   
if ball.ycor() > 160: ball.speed_y *= -1

--- /code ---

--- /task ---

--- task ---

코드를 다시 실행하면 공이 화면 상단에서 튀어나오지만 화면 오른쪽에서 사라져야 합니다.

--- /task ---

`y` 위치를 확인하는 것과 같은 방식으로 볼이 튕기도록 하려면, `x` 위치와 아래쪽 `y` 위치를 확인할 수 있습니다.

--- task ---

공의 포지션에 대해 아래와 같이 조건문을 추가하세요.

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

이제 공이 화면 주위를 튀고 왼쪽 가장자리에서 날아가야 합니다. 다음으로 왼쪽 가장자리에서 공을 다시 반사하도록 패들을 제어하세요.

--- save ---
