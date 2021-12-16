from turtle import Turtle, Screen

crazy = Turtle()
screen = Screen()


def move_forwards():
    crazy.forward(20)
    crazy.setheading(45)
    crazy.forward(20)
    crazy.right(90)
    crazy.forward(20)
    crazy.left(135)
    crazy.goto(-200, -100)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
