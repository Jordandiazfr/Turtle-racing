from turtle import Turtle, Screen
import random

# Set up  for the race
new_turtle = ["red", "blue", "green", "yellow", "purple", "orange"]
screen = Screen()
screen.setup(width=500, height=400)
game_on = False
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle would win the race? , write a color (red, blue, yellow, green, purple, orange) : ")

# Set up for the racers
turtles = []
x = -230
y = 150

# Set up for the finish line
define_the_finish_line = 200
finish_line = Turtle()
finish_line.penup()
finish_line.setposition(x=define_the_finish_line, y=-180)
finish_line.setheading(to_angle=90)
finish_line.pendown()
finish_line.forward(400)

# Create all the new turtles
for color in new_turtle:
    index = new_turtle.index(color)
    new_turtle[index] = Turtle(shape="turtle")
    new_turtle[index].color(color)
    new_turtle[index].penup()
    new_turtle[index].goto(x=x, y=y)
    y = y - 60
    turtles.append(new_turtle[index])


def random_moving(list_of_turtles):
    for turtle in list_of_turtles:
        num = random.randrange(0, 10)
        turtle.forward(num)
    return turtle.xcor()


def select_winner():
    turtles_position = []
    for t in turtles:
        turtles_position.append(int(t.xcor()))
    winner = max(turtles_position)
    index_of_winner = turtles_position.index(winner)
    return turtles[index_of_winner]


def end_game(bet):
    print("Finished")
    champion = select_winner().color()[0]
    print("The winner is %s" % champion)
    if bet == champion:
        print("Congratulations you win! you choosed %s and he won" % bet)
    else:
        print("Sorry you lost this time, you choosed %s and %s won" % (bet, champion))


# The game starts:
if user_bet:
    game_on = True

while game_on:
    stop = random_moving(turtles)
    if stop >= 180:
        end_game(user_bet)
        game_on = False

# Bottom
screen.exitonclick()
