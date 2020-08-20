import turtle
import math
import random


import time
import time
#Si tặp the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders Game")
wn.bgpic("background.gif")

#Thêm photos
turtle.register_shape("ga.gif")
turtle.register_shape("xwing.gif")
playerShape = turtle.register_shape("player.gif")

#Khung
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Điểm
score = 0

#Bảng tỉ số :)
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Tạo nhân vật
player = turtle.Turtle()
player.shape("xwing.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#Số quái
number_of_enemies = 5
#List để thêm quái
enemies = []

#Thêm quái vào list
for i in range(number_of_enemies):
    #Thêm quái
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.shape("ga.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y =  random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#Đạn của người chơi
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

# ready and fire
bulletstate = "ready"


#Di chuyển
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
#Pằng
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#Va chạm giữa quái và đạn
def isCollision_enemy_bullet(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False

#Va chạm người và quái
def isCollision_enemy_player(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 40:
        return True
    else:
        return False

turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main

while True:


    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)


        #Di chuyển địch
        if enemy.xcor() > 270:
            #Di chuyển địch xuống
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Thay đổi hướng địch
            enemyspeed *= -1

        if enemy.xcor() < -270:
            #Quái đi xuống
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #đổi hướng quái
            enemyspeed *= -1

        #Va chạm đạn và quái(RIP)
        if isCollision_enemy_bullet(bullet, enemy):
            #Nạp đạn
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset quái
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update điểm
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        #Va chạm người chơi và quái
        if isCollision_enemy_player(player, enemy):
            player.hideturtle()
            for e in enemies:
                e.hideturtle()
            wn.bgpic("end.gif")
            break

    #Di chuyển đạn
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Đạn chạm biên
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

delay = input("Press enter to finish")
