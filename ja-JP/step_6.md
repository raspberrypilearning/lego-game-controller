## パドルを制御する

### コントロールの設計

LEGO® Spike™ モーターはパドルの位置を制御擦るために使用していきますが、完全に一周できるようにはしたくありません。

ホイールの動きを制限するには、LEGO® の要素を使ってホイールが一回転するのを防ぐのが簡単です。

--- task ---

以前と同じく、ホイールを回してモーターのエンコーダーマークを並べます。 ペグまたは車軸をマーカーとできるだけ同じ高さに差し込みます。

--- /task ---

![モーターとホイールを組み合わせたものが手で回されている様子を示すアニメーション。 ホイールにはLEGO®シリンダーが取り付けられているため、一周させることはできません。](images/motor_block.gif)

--- print-only ---

![モーターとホイールを組み合わせたものが手で回されている様子を示す2枚の写真。 ホイールにはLEGO®シリンダーが取り付けられているため、一周させることはできません。](images/sidebyside.png)

--- /print-only ---


--- task ---

`motor_left`オブジェクトを作成するために、import行のあとに1行追加します。

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 3
line_highlights: 5
---

from buildhat import Motor

motor_left = Motor('A')

--- /code ---

--- /task ---

ここで、パドルの位置を追跡するために新しい変数が必要です。 `pos_left`という変数に`0`をセットします。

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 26
line_highlights: 29
---

ball.speed_x = 0.4   
ball.speed_y = 0.4

pos_left = 0

--- /code ---

--- task ---

モーターエンコーダーが移動したときに実行されるパドル用の関数を作成します。 `pos_left` 変数の値を変更できるように `グローバル` 変数を使用する点に注意してください。

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 31
line_highlights:
---

def moved_left(motor_speed, motor_rpos, motor_apos):   
global pos_left   
pos_left = motor_apos

--- /code ---

--- /task---

--- task ---

次に、モーターが動いたときに動作する1本の線を追加します。 `while` ループの直前に次のコードを追加します。

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 35
line_highlights:
---

motor_left.when_rotated = moved_left

--- /code ---

--- /task ---

--- task ---

`while True` ループに行を追加して、画面上のパドルオブジェクトを新しい位置に更新します。

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 45
line_highlights: 47
---

    if ball.ycor() < -160:   
        ball.speed_y *= -1   
    paddle_left.sety(pos_left)

--- /code ---

--- /task ---

--- task ---

コードを実行して、モーターエンコーダー上のホイールを回します。 パドルが画面を上下に移動しているのが確認できるでしょう。

--- /task ---

![ボールの跳ね返りとパドルの移動を示すゲームウィンドウの図。](images/moving_paddle.gif)

念のため、コードは現在次のようになっているはずです:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start:
line_highlights:
---

from turtle import *   
from time import sleep   
from buildhat import Motor

motor_left = Motor('A')

game_area = Screen()   
game_area.title('PONG')   
game_area.bgcolor('black')   
game_area.tracer(0)   
game_area.setworldcoordinates(-200,-170,200,170)

ball = Turtle()   
ball.color('white')   
ball.shape('circle')   
ball.penup()   
ball.setpos(0,0)

paddle_left = Turtle()   
paddle_left.color('green')   
paddle_left.shape("square")   
paddle_left.shapesize(4,1,1)   
paddle_left.penup()   
paddle_left.setpos(-190,0)

ball.speed_x = 0.4   
ball.speed_y = 0.4

pos_left = 0


def moved_left(motor_speed, motor_rpos, motor_apos):   
    global pos_left   
    pos_left = motor_apos


motor_left.when_rotated = moved_left

while True:   
    game_area.update()   
    ball.setx(ball.xcor() + ball.speed_x)   
    ball.sety(ball.ycor() + ball.speed_y)   
    if ball.ycor() > 160:   
        ball.speed_y *= -1   
    if ball.xcor() > 195:   
        ball.speed_x *= -1   
    if ball.ycor() < -160:   
        ball.speed_y *= -1   
    paddle_left.sety(pos_left)

--- /code ---

--- save ---