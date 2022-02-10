## 针对编码马达的移动的回应

如果想要利用乐高（LEGO®）Technic™ 马达作为游戏控制器，您需要能够不断读取马达的绝对位置。

--- task ---

在shell上方的主 Thonny 窗口中，您可以使用已知的命令来查询马达的绝对位置。 然后，利用`while True:` 循环，您可以打印（马达）位置的值。

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

您会看到您的程序不断地打印马达的当前位置。 如果您旋转马达，这些值就会改变。

不过，有一种更好的方法可以做到这一点。 您只需在马达移动的时候读取指数位置。

--- task ---

在程序中删除 `while True` 循环并创建下面这个简单的函数来打印马达的绝对位置。 您还需要添加另一个导入行以使用 `pause()` 函数。

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

现在将此函数设置为在编码马达移动时触发：

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

运行您的代码，当马达移动时，您应该看到shell窗口中的打印值发生了变化。

--- /task ---

--- save ---
