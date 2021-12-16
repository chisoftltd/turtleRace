import turtle as t
from turtle import Screen
import random

color_list = [(240, 231, 221), (228, 152, 86), (120, 171, 203), (1, 0, 0), (40, 111, 159), (240, 201, 83)]

benz = t.Turtle()
volvo = t.Turtle()
tesla = t.Turtle()
toyota = t.Turtle()
honda = t.Turtle()
porsche = t.Turtle()
kia = t.Turtle()
mazda = t.Turtle()
jaguar = t.Turtle()

screen = Screen()

t.colormode(255)

benz.color(random.choice(color_list))
volvo.color(random.choice(color_list))
tesla.color(random.choice(color_list))
toyota.color(random.choice(color_list))
honda.color(random.choice(color_list))
porsche.color(random.choice(color_list))
kia.color(random.choice(color_list))
mazda.color(random.choice(color_list))
jaguar.color(random.choice(color_list))

benz.shape("turtle")
volvo.shape("turtle")
tesla.shape("turtle")
toyota.shape("turtle")
honda.shape("turtle")
porsche.shape("turtle")
kia.shape("turtle")
mazda.shape("turtle")
jaguar.shape("turtle")

benz.penup()
volvo.penup()
tesla.penup()
toyota.penup()
honda.penup()
porsche.penup()
kia.penup()
mazda.penup()
jaguar.penup()

benz.goto(-800, -400)
volvo.goto(-800, -300)
tesla.goto(-800, -200)
toyota.goto(-800, -100)
honda.goto(-800, 0)
porsche.goto(-800, 100)
kia.goto(-800, 200)
mazda.goto(-800, 300)
jaguar.goto(-800, 400)

for i in range(75):
    benz.forward(random.randint(0, i))
    volvo.forward(random.randint(0, i))
    tesla.forward(random.randint(0, i))
    toyota.forward(random.randint(0, i))
    honda.forward(random.randint(0, i))
    porsche.forward(random.randint(0, i))
    kia.forward(random.randint(0, i))
    mazda.forward(random.randint(0, i))
    jaguar.forward(random.randint(0, i))

screen.exitonclick()
