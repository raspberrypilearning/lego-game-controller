## モーターエンコーダーの動きに対応する

LEGO® Technic™ モーターをゲームのコントローラーとして使うには、常に絶対位置を読み取れる必要があります。

--- task ---

Thonnyウィンドウのシェルの上にあるメイン部分に、先ほど紹介したコマンドを入力します。 そして、 `while True:` のループの中で位置の値をプリントさせます。

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights:
---

from buildhat import Motor   
motor_left = Motor('A')

while True:   
print(motor_left.get_aposition())

--- /code ---

--- /task ---

プログラムがモーターの位置をプリントし続ける様子が見られるはずです。 モーターを回転させると、値が変化します。

しかし、もっと良い方法があります。 モーターが動いたときにだけ読み取れば良いのです。

--- task ---

`while True` ループをプログラムから削除して、モーターの絶対位置をプリントするシンプルな関数を作成します。 また、 `pause()` 関数を使うために、別の import 行を追記します。

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights: 2,6,7
---

from buildhat import Motor  
from signal import pause motor_left = Motor('A')


def moved_left(motor_speed, motor_pos, motor_apos):   
print(motor_apos)

--- /code ---

--- /task ---

--- task ---

次に、モーターエンコーダーが動いた時にこの関数を実行するように設定します:

--- code ---
---
language: python   
filename: game_controller.py   
line_numbers: true   
line_number_start: 1
line_highlights: 9,10
---

from buildhat import Motor  
from signal import pause motor_left = Motor('A')


def moved_left(motor_speed, motor_pos, motor_apos):   
print(motor_apos)

motor_left.when_rotated = moved_left pause()

--- /code ---

コードを実行して、モーターが動いた時に値がシェルにプリントされることを確認します。

--- /task ---

--- save ---
