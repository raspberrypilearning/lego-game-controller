## 移动(Pong) 球

球将在屏幕上跳动，因此需要两个变量来跟踪它在 `x` 和 `y` 方向上的速度。 调大速度可以使游戏更难，调小速度可以使游戏更容易。

--- task ---

将以下代码添加到程序中：

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

您可以通过`turtle.xcor()` 和 `turtle.ycor()` 来找到某个Turtle所在位置的 `x` 和 `y` 坐标。

您可以结合位置和速度的设置来移动球。

--- task ---

将以下代码添加到您的程序中：

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

运行程序，看看会发生什么！

![球从Pong屏幕右上角飞出的图片。](images/ball_diagonal.gif)

球应该会沿着对角向上移动到游戏区域的右上角……然后继续前进！ 如果您希望您的游戏更快且更有挑战性，您可以增大 `speed_x` 和 `speed_y` 的值，以使球移动得更快。

球应该从顶墙上反弹而不是从屏幕上消失。 为了实现这个功能，可以在球的`y` 位置大于 160的时候，反转速度，使球沿相反方向行进。

--- task ---

将以下代码添加到您的游戏循环中并运行。

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

再次运行您的代码，球应该会在屏幕顶部弹回，但会从屏幕右侧消失。

--- /task ---

与检查球的 `y` 位置上边界相同，为了让球反弹，可以在你的游戏循环中检查球的 `x` 位置的右边界和 `y`位置的下边界。

--- task ---

添加这些对球的位置的检查。

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

球现在应该在屏幕的各边缘反弹，但会从左边缘飞出。 接下来，您将控制您的球拍将球从左边缘反弹回去。

--- save ---
