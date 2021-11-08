import turtle
import time
import random
delay = 0.1

Score = -10

Pen = turtle.Turtle()
Pen.speed(0)
Pen.shape("square")
Pen.color("red")
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 0)

# setup the screen

wn = turtle.Screen()
wn.title("Snake game!")
wn.bgcolor("light green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

segments = []
Pen.write("Will Start in... 5", align="center", font=("Courier", 24, "normal"))
time.sleep(1)
Pen.clear()
Pen.write("Will Start in... 4", align="center", font=("Courier", 24, "normal"))
time.sleep(1)
Pen.clear()
Pen.write("Will Start in... 3", align="center", font=("Courier", 24, "normal"))
time.sleep(1)
Pen.clear()
Pen.write("Will Start in... 2", align="center", font=("Courier", 24, "normal"))
time.sleep(1)
Pen.clear()
Pen.write("Will Start in... 1", align="center", font=("Courier", 24, "normal"))
time.sleep(1)
Pen.clear()
Pen.write("GO!", align="center", font=("Courier", 24, "bold"))
time.sleep(1)
Pen.clear()

# snake head
Head = turtle.Turtle()
Head.speed(0)
Head.shape("square")
Head.color("green")
Head.penup()
Head.goto(0, 100)
Head.direction = "right"

# Snake food
Food = turtle.Turtle()
Food.speed(0)
Food.shape("circle")
Food.color("red")
Food.penup()
Food.goto(0, 100)

# Pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.shape("square")
Pen.color("red")
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 269)


# Functions
def go_up():
    if Head.direction != "down":
        Head.direction = "up"


def go_down():
    if Head.direction != "up":
        Head.direction = "down"


def go_left():
    if Head.direction != "right":
        Head.direction = "left"


def go_right():
    if Head.direction != "left":
        Head.direction = "right"


def move():
    if Head.direction == "up":
        Head.sety(Head.ycor() + 20)
    if Head.direction == "down":
        Head.sety(Head.ycor() - 20)
    if Head.direction == "left":
        Head.setx(Head.xcor() - 20)
    if Head.direction == "right":
        Head.setx(Head.xcor() + 20)

# keyboard bindings


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# --------------------------------------------Main game loop----------------------------------------
while True:

    # Check for collision with the border
    if Head.xcor() > 290 or Head.xcor() < -290 or Head.ycor() > 290 or Head.ycor() < -290:
        time.sleep(1)
        Head.goto(0, 0)
        Head.direction = "stop"
        exit()

    # Check for collision with food
    if Head.distance(Food) < 20:
        # Move to random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        Food.goto(x, y)

        # Add a segment
        New_seg = turtle.Turtle()
        New_seg.speed(0)
        New_seg.color("brown")
        New_seg.shape("square")
        New_seg.penup()
        segments.append(New_seg)

        # Speed up the snake comment to turn off
        delay -= 0.0001

        # Increase score
        Score = Score + 10

    # Write new score
    Pen.clear()
    Pen.goto(0, 269)
    Pen.write("Score: {}".format(Score), align="center", font=("Courier", 24, "normal"))
    # Move the end segment first in reverse order

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = Head.xcor()
        y = Head.ycor()
        segments[0].goto(x, y)
    # Movement Function usage
    move()
    # Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(Head) < 20:
            time.sleep(1)
            exit()

    time.sleep(delay)

    wn.update()

wn.mainloop()
