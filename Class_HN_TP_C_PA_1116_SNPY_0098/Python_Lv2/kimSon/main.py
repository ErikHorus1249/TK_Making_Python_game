

import turtle
import time
import random

delay = 0.1

# Tỉ số
score = 0
high_score = 0
move_status = False

# thiết lập thông số màn hình
wn = turtle.Screen()
wn.title("Game by Kim son")
wn.setup(width=600, height=600)
wn.bgpic("bg.gif")
wn.tracer(0)  # Turns off the screen updates

# load ảnh vào để hiển thị
turtle.register_shape("head.gif")
turtle.register_shape("seg2.gif")
turtle.register_shape("apple.gif")


# Thiết lập đầu con rắn
head = turtle.Turtle()
head.speed(0)
head.shape("head.gif")
head.penup()
head.goto(100, 0)
head.direction = "stop"


# Thức ăn của con rắn
number_of_food = 2

# tạo một danh sách thức ăn

foods = []

for i in range(number_of_food):
    foods.append(turtle.Turtle())

for food in foods:
    food.shape("apple.gif")
    food.speed(0)
    food.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    food.goto(x, y)


# Tạo danh sách chứa từng khúc của con rắn

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("seg2.gif")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Hàm đi lên
def go_up():
    #if head.direction != "down":
        head.direction = "up"

# Hàm đi xuống

def go_down():
    #if head.direction != "up":
        head.direction = "down"

# Hàm đi sang trái

def go_left():
    if head.direction != "right":
        head.direction = "left"

# Hàm đi sang phải

def go_right():
    if head.direction != "left":
        head.direction = "right"



# Hàm chuyển động của rắn

def move():

    # đi lên
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        move_status = True
    # đi xuống
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        move_status = True
    # đi sang trái
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        move_status = True
    # đi sang phải
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        move_status = True


# Cài các nút di chuyển
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



while True:
    wn.update()

    # Kiểm tra va chạm biên khi di chuyển
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"


        for segment in segments:
            segment.goto(1000, 1000)

        # Xóa thân rắn
        segments.clear()

        # Đặt lại tỉ số
        score = 0

        # đặt lại độ trễ
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("arial", 24, "normal"))

        # Kiểm tra va chạm thức ăn
    for food in foods:
        if head.distance(food) < 24:

            # Tạo tọa độ ngẫu nhiên cho thức ăn
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)

            food.goto(x, y)

            #Thêm đoạn vào thân rắn
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("seg2.gif")
            new_segment.penup()
            segments.append(new_segment)


            delay -= 0.001

            # Tăng điểm
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("arial", 24, "normal"))

            # Chuyen dong cua phan than
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()


    # Kiểm tra chạm thân
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Ẩn phần thân
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            # Đặt lại tỉ số
            score = 0

            #  Đặt lại tốc độ
            delay = 0.1

            # Cập nhật màn hình
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("arial", 24, "normal"))


    time.sleep(delay)

wn.mainloop()
