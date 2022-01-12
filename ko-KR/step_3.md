## React to motor encoder movement

LEGO® Technic™ 모터를 게임용 컨트롤러로 사용하려면 절대적 위치를 지속적으로 읽을 수 있어야 합니다.

--- task ---

쉘 위의 기본 Thonny 창에서 이미 알고 있는 명령을 사용하여 모터의 절대적 위치를 찾을 수 있습니다. 그런 다음 `while True:` 루프에서 위치값을 출력할 수 있습니다.

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

프로그램이 계속해서 모터의 위치를 출력하는 것을 볼 수 있습니다. 만약에 모터를 회전시키면 이 값이 변경되어야 합니다.

이 작업을 수행하는 더 좋은 방법이 있습니다. 모터가 움직이는 경우에만 모터 위치를 읽도록 하면 됩니다.

--- task ---

`while True` 루프를 삭제하고 모터의 절대적 위치를 출력하는 간단한 함수를 만듭니다. `pause()` 함수를 사용하려면 다른 import 명령을 추가해서 라이브러리를 불러와야 합니다.

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

이제 모터의 인코더가 움직일 때 이 기능이 실행되도록 설정합니다:

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

코드를 실행하면 모터가 움직일 때 쉘에 출력되는 값이 변경되는 것을 볼 수 있습니다.

--- /task ---

--- save ---
