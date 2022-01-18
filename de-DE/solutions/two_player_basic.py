from turtle import *
from time import sleep
from buildhat import Motor

motor_links = Motor('A')
motor_rechts = Motor('B')

spielflaeche = Screen()
spielflaeche.title('PONG')
spielflaeche.bgcolor('black')
spielflaeche.tracer(0)
spielflaeche.setworldcoordinates(-200,-170,200,170)

ball = Turtle()
ball.color('white')
ball.shape('circle')
ball.penup()
ball.setpos(0,0)

paddle_links = Turtle()
schlaeger.links.color('green')
schlaeger.links.shape("square")
schlaeger.links.shapesize(4,1,1)
schlaeger.links.penup()
schlaeger.links.setpos(-190,0)

schlaeger_rechts = Turtle()
schlaeger_rechts.color('blue')
schlaeger_rechts.shape("square")
schlaeger_rechts.shapesize(4,1,1)
schlaeger_rechts.penup()
schlaeger_rechts.setpos(190,0)

ball.speed_x = 0.4
ball.speed_y = 0.4

pos_links = 0
pos_rechts = 0

def drehung_links(motor_speed, motor_rpos, motor_apos):
    global pos_links
    pos_links = motor_apos


def drehung_rechts(motor_speed, motor_rpos, motor_apos):
    global pos_rechts
    pos_rechts = motor_apos


motor_links.when_rotated = drehung_links
motor_rechts.when_rotated = drehung_rechts

while True:
    spielflaeche.update()
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
    schlaeger_links.sety(pos_links)
    schlaeger_rechts.sety(pos_rechts)
    if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < schlaeger_links.ycor() + 20 and ball.ycor() > schlaeger_links.ycor() - 20):
        ball.setx(-180)
        ball.speed_x *= -1
    if (ball.xcor() > 180 and ball.xcor() < 190) and (ball.ycor() < schlaeger_rechts.ycor() + 20 and ball.ycor() > schlaeger_rechts.ycor() - 20):
        ball.setx(180)
        ball.speed_x *= -1
    if ball.xcor() < -195: # linker Rand
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()