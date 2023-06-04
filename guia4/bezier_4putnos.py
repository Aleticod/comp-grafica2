from turtle import *
p0 = Vec2D(0, -50)
p1 = Vec2D(-300, 50)
p2 = Vec2D(0, 250)
b = lambda t: (1 - t)**2 * p0 + 2*(1 - t)*t * p1 + t**2 * p2
tortuga = Turtle()
tortuga.penup()
for posicion in [p2, p1, p0]:
    tortuga.goto(posicion)
    tortuga.dot()

tortuga.pendown()
t = 0

while t <= 1:
    posicion = b(t)
    tortuga.setheading(tortuga.towards(posicion))
    tortuga.goto(posicion)
    t += 0.01
    
screen = Screen()
screen.exitonclick()
