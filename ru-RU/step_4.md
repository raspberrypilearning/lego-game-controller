## Делаем экран Понга

Черепашка - это библиотека для рисования и анимации. Ты можешь узнать больше о ней с этим [отличным проектом](https://projects.raspberrypi.org/en/projects/turtle-race).


Сначала создай окно, в котором будет проходить игра.

--- task ---

Создай новый файл в Thonny и добавь следующий код для импорта библиотек Turtle (Черепашка), time и Build HAT, а затем настрой экран. Запусти файл, и ты должен увидеть чёрное окно с открытым заголовком «ПОНГ». Тебе не обязательно включать комментарии `#` в твою программу.

--- code ---
---
language: python   
filename: pong.py   
line_numbers: true   
line_number_start: 1
line_highlights:
---

from turtle import Screen, Turtle from time import sleep from buildhat import Motor

game_area = Screen() #Создаём экран   
game_area.title("ПОНГ") #Даём экрану название   
game_area.bgcolor('black') #Устанавливаем цвет фона   
game_area.tracer(0) #Делаем анимации плавными

--- /code ---

--- /task ---

Библиотека Черепашка имеет также удобный способ задания кординат области экрана. Добавь эту строку в свою программу:

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

Это создаст прямоугольное окно шириной 400 пикселей и высотой 340 пикселей, где 0 находится в центре.

![Снимок экрана игрового окна, показывающий координаты каждого угла и центра. Верхний левый -200,170, верхний правый 200,170, нижний левый -200,-170 и нижний правый 200,-170. Центр 0,0.](images/coords.png)

--- task ---

Теперь тебе нужно обновить игровую зону, чтобы увидеть ракетку и мяч. Добавь **игровой цикл** в конец твоего кода и вызови метод `update()`.

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

Запусти свой код, и ты увидишь черное окно.

--- /task ---

--- task ---

Затем, используя черепаху, ты можешь сделать шар, который представляет собой белый круг. Мяч должен начинаться в середине экрана и не оставлять за собой линию при движении.

**Над** твоим циклом `while True` добавь следующий код:

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

Запусти свой код снова. В твоем окне должен появиться белый шар.

--- /task ---

--- task ---

Далее ты можешь настроить ракетку таким же образом. Это будет зеленый прямоугольник, расположенный в самой левой части экрана.

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

Запустите свой код, и ты должен увидеть свой мяч и ракетку.

![Белый шар в центре черного окна с зеленой ракеткой слева.](images/pong_static.png)

--- /task ---
