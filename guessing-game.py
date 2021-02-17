# guessing game

import random
import turtle


sr = turtle.Screen()
sr.bgcolor('white')
sr.title('learning')
sr.setup(width= 600, height= 400)
turtle.shape('turtle')

turtle.width(3)
turtle.speed(0)
turtle.colormode(255)

# for x in range(1, 5):
#     turtle.bk(150)
#     turtle.left(90)

turtle.pencolor(0,0,0)

def filled_circle(radius, red, green, blue):
    turtle.fillcolor(red, green, blue)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

# filled_circle(150, 0, 0.5, 0)

# star
def star(size, angle):
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    while size > 0:
        turtle.forward(size)
        turtle.left(angle)
        size = size - 1
        turtle.pencolor(random.randint(0,255), random.randint(0, 255), random.randint(0, 255))

# star(150, 200)

def polka_dot():
    turtle.penup()
    for i in range (1, 400):
        diameter = random.randint(5,30)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.dot(diameter, color)
        turtle.setx(random.randint(-300, 300))
        turtle.sety(random.randint(-200, 200))

def cursor_stamp():
    turtle.penup()
    for i in range (1, 400):
        turtle.stamp()
        turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.setx(random.randint(-300, 300))
        turtle.sety(random.randint(-200, 200))

turtle.hideturtle()
# cursor_stamp()
# polka_dot()
turtle.listen()
cursor_stamp()
turtle.onkey(polka_dot,'y')
# why the above line doesn't work?


turtle.exitonclick()
