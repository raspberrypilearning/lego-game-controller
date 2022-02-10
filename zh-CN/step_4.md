## 绘制您的Pong屏幕

Turtle 是一个绘图和动画的库，您可以通过这个 [优秀的项目](https://projects.raspberrypi.org/en/projects/turtle-race)了解更多信息。


首先，创建一个游戏窗口。

--- task ---

在 Thonny 中打开一个新文件并添加以下代码以导入 Turtle、time 和 Build HAT 库，然后设置一个屏幕。 运行该文件，您应该会看到一个新的标题为“PONG”的黑色窗口。 您不需要包含 `#` 后面的评论。

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 1
line_highlights:
---

from turtle import Screen, Turtle from time import sleep from buildhat import Motor

game_area = Screen() #创建一个屏幕   
game_area.title("PONG") #给屏幕一个标题   
game_area.bgcolor('black') #设置背景颜色   
game_area.tracer(0) #给更流畅的动画

--- /code ---

--- /task ---

Turtle 库也有一种有效的方法来设置屏幕区域的坐标。 将这行添加到您的代码中：

--- task ---

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 8
line_highlights: 9
---

game_area.tracer(0)   
game_area.setworldcoordinates(-200, -170, 200, 170)

--- /code ---

--- /task ---

这将创建一个 400 像素宽和 340 像素高的矩形窗口，中间点坐标为 0。

![游戏窗口的屏幕截图，显示了每个角和中心的坐标。 左上角是-200,170，右上角是200,170，左下角是-200,-170，右下角是200,-170。 中心为 0,0。](images/coords.png)

--- task ---

现在，您需要不断更新您的游戏区域以查看球拍和球。 在代码底部添加一个 **游戏循环** ，调用`update()` 函数。

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 10
line_highlights:
---

while True:   
game_area.update()

--- /code ---

运行您的代码，您应该会看到一个黑色窗口。

--- /task ---

--- task ---

接下来，您可以用Turtle 来制作球，一个被设置为白色的圆圈。 球应该从屏幕中间开始移动，并且在移动时不会画线。

将下面的代码添加到您的 **while True** 循环`之前`：

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 10
line_highlights:
---

ball = Turtle()   
ball.color('white')   
ball.shape('circle')   
ball.penup()   
ball.setpos(0,0)

while True:

--- /code ---

--- /task ---

--- task ---

再次运行您的代码。 您会看到一个白球出现在您的窗口中。

--- /task ---

--- task ---

接下来，您可以用相同的方式设置球拍。 它将是一个绿色矩形，位于屏幕的最左侧。

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 17
line_highlights:
---

paddle_left = Turtle()   
paddle_left.color('green')   
paddle_left.shape('square')   
paddle_left.shapesize(4, 1, 1)   
paddle_left.penup()   
paddle_left.setpos(-190, 0)

--- /code ---

--- /task ---

--- task ---

运行您的代码，您应该会看到您的球和球拍。

![黑色窗口的中央有一个白色球，最左边有一个绿色球拍。](images/pong_static.png)

--- /task ---
