## パドルの衝突

ゲーム完成に近づいてきましたが、パドルにボールを当ててカバーするための衝突検知を追加する必要があります。

--- task ---

`while True`ループ内で、ボールの`x`の位置がパドルの水平の領域内にかぶる場合をチェックします。 また、`and`を使って、ボールの`y`の位置が移動するパドルの垂直線に入っていることをチェックします。

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

プログラムを試してみましょう。 パドルでボールを跳ね返して'スカッシュ'のソロゲームがプレイできるようになったはずです。

これで、ボールが画面外に消えないようにできました。次に、ボールを打ち返すのに失敗した場合にどうするかを考えてみましょう。

ひとまずはボールを最初の状態にリセットしましょう。

--- task ---

`while True`ループ内にこのコードを追加してください:

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 52
line_highlights: 53-56
---

        ball.speed_x *= -1   
    if ball.xcor() < -195: #Left   
        ball.hideturtle()   
        ball.goto(0,0)   
        ball.showturtle()

--- /code ---

--- /task ---

さまざまな設定に満足したら、2番目のパドルを追加します。

最初に左側のパドル用に作成したのと同じようにして、ゲーム領域の右側に2つ目のパドルを追加します。

--- task ---

まず、2つめの LEGO® Technic™ モーターをBuild HAT (ポートB) に接続して、プログラムで設定します。

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

左側のパドルを設定するためのコードをコピーアンドペーストして、名前と値を右側のパドル用に変更します。

--- /task ---

--- task ---

それでは右側のパドルを作成しましょう。

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

右のパドル用に、位置の変数、パドルの関数、そして右のモーターが動かされたときに関数を呼び出す行を追加します。

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

画面上のパドルを更新するために、`while True`ループに1行を追加します:

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


現在は、ボールは右側の壁で跳ね返るようになっています。 代わりにボールが中央にリセットされるようするために、プログラムの行を変更します。

--- task ---

ボールの`xcor`の条件を変更して、リセットされるようにします。

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

そして、衝突を検知できるように、左側のパドルと同じような条件を右側のパドル用にも作成します。

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

これで、Pongの基本的な2人用ゲームを楽しむことができるようになりました。

![二人用ゲームのウィンドウ画面。 左側に緑色のパドル、右側に青色のパドルがあり、その間をボールがはねています。](images/2_player_pong.gif)

--- save ---
