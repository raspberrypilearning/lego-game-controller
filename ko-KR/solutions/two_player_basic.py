from turtle import *
from time import sleep
from buildhat import Motor

motor_left = Motor('A')
motor_right = Motor('B')

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

paddle_right = Turtle()
paddle_right.color('blue')
paddle_right.shape("square")
paddle_right.shapesize(4,1,1)
paddle_right.penup()
paddle_right.setpos(190,0)

ball.speed_x = 0.4
ball.speed_y = 0.4

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

while True:
    game_area.update()
    ball.setx(ball.xcor() + ball.speed_x)
    ball.sety(ball.ycor() + ball.speed_y)
    if ball.ycor() > 160:
        ball.speed_y *= -1
    if ball.xcor() > 195:
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
    if ball.ycor() < -160:
        ball.speed_y *= -1
    paddle_left.sety(pos_left)
    paddle_right.sety(pos_right)
    if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < paddle_left.ycor() + 20 and ball.ycor() > paddle_left.ycor() - 20):
        ball.setx(-180)
        ball.speed_x *= -1
    if (ball.xcor() > 180 and ball.xcor() < 190) and (ball.ycor() < paddle_right.ycor() + 20 and ball.ycor() > paddle_right.ycor() - 20):
        ball.setx(180)
        ball.speed_x *= -1
    if ball.xcor() < -195: # left
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()