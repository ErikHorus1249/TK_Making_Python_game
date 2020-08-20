import turtle
import os

wm = turtle.Screen()
wm.bgcolor("black")
wm.title("Space invader")
wm.bgcolor("black")
wm.title("Space invader")
#

while 1:
    border_pen = turtle.Turtle()
    border_pen.speed()
    border_pen.color("white")
    border_pen.penup()
    border_pen.pendown()
    border_pen.setposition(-300, -300)
    border_pen.pensize(3)

    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    player = turtle.Turtle()
    player.color("blue")
    player.shape("triangle")
    player.penup()
    player.speed(0)
    player.setposition(0,-250)
    player.setheading(90)
