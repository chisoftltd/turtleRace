from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1050, height=650)
user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet", "brown", "cyan", "olive"]
y_positions = [-130, -100, -70, -40, -10, 20, 50, 80, 110, 140]
turtle_list = []
is_race_on = False

for turtle_index in range(0, 10):
    crazy = Turtle(shape="turtle")
    crazy.speed(turtle_index)
    crazy.color(colors[turtle_index])
    crazy.penup()
    crazy.goto(x=-510, y=y_positions[turtle_index])
    turtle_list.append(crazy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 500:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The winning color is {turtle.pencolor()}.")
            else:
                print(f"You've lost! The winning color is {turtle.pencolor()}.")
        turtle.forward(random.randint(0, 25))

screen.exitonclick()
