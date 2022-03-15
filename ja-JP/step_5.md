## ボールを動かす

ボールが画面中を跳ね回るので、`x` と `y` 両方の向きのスピードを管理するために2つの変数が必要です。 これらの数字は大きいほどゲームが難しくなり、逆に小さいほどゲームが簡単になります。

--- task ---

次のコードをプログラムに追加します:

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

位置を確認するには、Turtleでは `turtle.xcor()` と `turtle.ycor()` を使うことで `x` と `y` の座標を求めることができます。

ボールを移動するには、位置とスピートを組み合わせます。

--- task ---

以下の行をプログラムに追加します:

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

プログラムを実行して、何が起こるか見てみましょう！

![Pongの画面でボールが右上に飛び去っていく](images/ball_diagonal.gif)

ボールはゲームエリアの右上の角に向かって斜め上に移動していき…そのまま行ってしまいました！ もしゲームを早くチャレンジングにしたいときは、 `speed_x` と `speed_y` の値を増やすとボールの移動をより素早くできます。

ボールは画面の外に去っていくのでなく上部の壁を跳ね返るべきです。 これを実現するには、`y` の位置が160より大きくなったら速度を逆にして、ボールを反対の向きに移動させれば可能です。

--- task ---

次のコードをゲームループ内に追加して実行します。

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

もう一度コードを実行すると、ボールは画面の上部で跳ね返りますが、画面の右に消えていきます。

--- /task ---

ボールの `y` の位置の上側をチェックするようにしたのと同じように、 `x` の位置の右側と `y` の位置の下側でもボールが跳ね返るように、ゲームループでチェックできるようにします。

--- task ---

ボールの位置のチェックを追加します。

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

ボールは画面中を跳ね回って、左の隅に飛び去っていくようになりました。 次は、パドルをコントロールしてボールを左の隅から跳ね返せるようにしていきましょう。

--- save ---
