from turtle import Turtle, Screen

crazy = Turtle()
screen = Screen()


def move_forwards():
    crazy.forward(20)


def move_backwards():
    crazy.forward(-20)


def move_left():
    crazy.left(20)


def move_right():
    crazy.right(40)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.exitonclick()
