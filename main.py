from turtle import Turtle, Screen

crazy = Turtle()
screen = Screen()


def move_forwards():
    crazy.forward(50)


def move_backwards():
    crazy.backward(50)


def move_left():
    crazy.left(45)


def move_right():
    crazy.right(90)


def clear():
    crazy.clear()
    crazy.penup()
    crazy.home()
    crazy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
