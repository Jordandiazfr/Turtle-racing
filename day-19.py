from turtle import Turtle, Screen

jojo = Turtle()
screen = Screen()


def move_up():
    jojo.setheading(90)
    jojo.forward(10)


def move_down():
    jojo.setheading(270)
    jojo.forward(10)


def move_left():
    jojo.setheading(180)
    jojo.forward(10)


def move_right():
    jojo.setheading(0)
    jojo.forward(10)


# Challenge part
def clear():
    jojo.reset()


def move_fd():
    jojo.forward(10)


def move_back():
    jojo.back(10)


def move_clockwise():
    jojo.right(10)


def move_counter_clock():
    jojo.left(10)


# Bottom
screen.listen()
# screen.onkey(key="z", fun=move_up)
# screen.onkey(key="s", fun=move_down)
# screen.onkey(key="q", fun=move_left)
# screen.onkey(key="d", fun=move_right)
screen.onkey(key="z", fun=move_fd)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="q", fun=move_counter_clock)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
