## Столкновение с ракеткой

Игра почти завершена, но сначала тебе нужно добавить дополнительное обнаружение столкновения, которое закроет вопрос удара мяча по ракетке.

--- task ---

Within the `while True` loop, check if the ball's `x` position is within the horizontal area covered by the paddle. Also use an `and` to check the ball's `y` position is in the vertical line in which the paddle moves

--- code ---
---
language: python filename: pong.py   
line_numbers: true   
line_number_start: 47
line_highlights: 48
---

paddle_left.sety(pos_left)   
if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < paddle_left.ycor() + 20 and ball.ycor() > paddle_left.ycor() - 20): ball.setx(-180)  
ball.speed_x *= -1

--- /code ---

--- /task ---

Попробуй, как работает программа. Ты должен иметь возможность отбивать мяч от ракетки и играть в одиночную игру в «сквош»!

Теперь, когда у тебя есть способ предотвратить исчезновение мяча за границами экрана, пора подумать о том, что произойдет, если тебе не удастся сохранить игру.

А пока давай просто вернём мяч в исходное положение.

--- task ---

Добавьте этот код в цикл `while True`:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 52
line_highlights: 53-56
---

        ball.speed_x *= -1   
    if ball.xcor() < -195: #Лево   
        ball.hideturtle()   
        ball.goto(0,0)   
        ball.showturtle()

--- /code ---

--- /task ---

Как только ты будешь доволен различными настройками, приступай к добавлению второй ракетки.

Используя то, что ты создал для левой ракетки в качестве отправной точки, добавь вторую ракетку с правой стороны игровой области.

--- task ---

Прежде всего, подключи второй мотор LEGO® Technic™ к плате Build HAT (порт B) и настрой его в программе.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 5
line_highlights: 6
---

motor_left = Motor('A')   
motor_right = Motor('B')

--- /code ---

--- /task ---

--- task ---

Ты можешь скопировать и вставить свой код для настройки левой ракетки и изменить имя и значения для своей правой ракетки.

--- /task ---

--- task ---

Создай свою правую ракетку.

--- code ---
---
language: python   
filename: pong   
line_numbers: true   
line_number_start: 20
line_highlights: 27-32
---

paddle_left = Turtle()   
paddle_left.color('green')   
paddle_left.shape("square")   
paddle_left.shapesize(4,1,1)   
paddle_left.penup()   
paddle_left.setpos(-190,0)

paddle_right = Turtle()   
paddle_right.color('blue')   
paddle_right.shape("square")   
paddle_right.shapesize(4,1,1)   
paddle_right.penup()   
paddle_right.setpos(190,0)

--- /code ---

--- /task ---

--- task ---

Добавь переменную для положения правой ракетки, функцию для ракетки и строку для вызова функции при перемещении правого двигателя.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 37
line_highlights: 38, 46-48, 52
---

pos_left = 0   
pos_right = 0


def moved_left(motor_speed, motor_rpos, motor_apos):   
global pos_left   
pos_left = motor_apos


def moved_right(motor_speed, motor_rpos, motor_apos):   
global pos_right   
pos_right = motor_apos


motor_left.when_rotated = moved_left   
motor_right.when_rotated = moved_right

--- /code ---

--- /task ---

--- task ---

Добавь строку для обновления ракетки на экране в цикл `while True`:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 64
line_highlights: 65
---

    paddle_left.sety(pos_left)   
    paddle_right.sety(pos_right)

--- /code ---

--- /task ---


В настоящее время мяч отскакивает от правой стены. Измени строки твоей программы таким образом, что как только это произошло, мяч вместо этого был перемещен в центр.

--- task ---

Измените условие для свойства `xcor` мяча, чтобы он возвращался в центр.

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

Теперь добавь такое же условие для правой ракетки, как ты сделал и для левой для обработаки столкновений.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 68
line_highlights: 71-73
---

    if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < paddle_left.ycor() + 20 and ball.ycor() > paddle_left.ycor() - 20):   
        ball.setx(-180)   
        ball.speed_x *= -1   
    if (ball.xcor() > 180 and ball.xcor() < 190) and (ball.ycor() < paddle_right.ycor() + 20 and ball.ycor() > paddle_right.ycor() - 20):   
        ball.setx(180)   
        ball.speed_x *= -1

--- /code ---

--- /task ---

Теперь у тебя должна быть возможность насладиться базовой игрой в Понг для двух игроков.

![Вид окна игры, в котором показана игра с двумя игроками. Слева есть зеленая ракетка, а справа синяя, и мяч прыгает между ними.](images/2_player_pong.gif)

--- save ---
