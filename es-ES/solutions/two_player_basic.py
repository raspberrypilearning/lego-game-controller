from turtle import *
from time import sleep
from buildhat import Motor

motor_izquierda = Motor ('A')
motor_derecha = Motor ('B')

juego_area = Screen()
juego_area.title('PONG')
juego_area.bgcolor('black')
juego_area.tracer(0)
juego_area.setworldcoordinates(-200,-170,200,170)

pelota = Turtle()
pelota.color('white')
pelota.shape('circle')
pelota.penup()
pelota.setpos(0,0)

paleta_izquierda = Turtle()
paleta_izquierda.color('green')
paleta_izquierda.shape("square")
paleta_izquierda.shapesize(4,1,1)
paleta_izquierda.penup()
paleta_izquierda.setpos(-190,0)

paleta_derecha = Turtle()
paleta_derecha.color('blue')
paleta_derecha.shape("square")
paleta_derecha.shapesize(4,1,1)
paleta_derecha.penup()
paleta_derecha.setpos(190,0)

pelota.speed_x = 0.4
pelota.speed_y = 0.4

pos_izquierda = 0
pos_derecha = 0

def movido_izquierda(motor_speed, motor_rpos, motor_apos):
    global pos_izquierda
    pos_izquierda = motor_apos


def movido_derecha(motor_speed, motor_rpos, motor_apos):
    global pos_derecha
    pos_derecha = motor_apos


motor_izquierda.when_rotated = movido_izquierda
motor_derecha.when_rotated = movido_derecha

while True:
    juego_area.update()
    pelota.setx(pelota.xcor() + pelota.speed_x)
    pelota.sety(pelota.ycor() + pelota.speed_y)
    if pelota.ycor() > 160:
        pelota.speed_y *= -1
    if pelota.xcor() > 195:
        pelota.hideturtle()
        pelota.goto(0,0)
        pelota.showturtle()
    if pelota.ycor() < -160:
        pelota.speed_y *= -1
    paleta_izquierda.sety(pos_izquierda)
    paleta_derecha.sety(pos_derecha)
    if (pelota.xcor() < -180 and pelota.xcor() > -190) and (pelota.ycor() < paleta_izquierda.ycor() + 20 and pelota.ycor() > paleta_izquierda.ycor() - 20):
        pelota.setx(-180)
        pelota.speed_x *= -1
    if (pelota.xcor() > 180 and pelota.xcor() < 190) and (pelota.ycor() < paleta_derecha.ycor() + 20 and pelota.ycor() > paleta_derecha.ycor() - 20):
        pelota.setx(180)
        pelota.speed_x *= -1
    if pelota.xcor() < -195: # izquierda
        pelota.hideturtle()
        pelota.goto(0,0)
        pelota.showturtle()