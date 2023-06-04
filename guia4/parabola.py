from turtle import *
import math
import random
G = 9.80665
origen_x = -480
origen_y = -180
def crear_tortuga():
    proyecto = Turtle(shape='turtle')
    proyecto.hideturtle()
    proyecto.penup()
    proyecto.goto(origen_x, origen_y)
    proyecto.pendown()
    proyecto.speed(0)
    proyecto.left(45)
    proyecto.showturtle()
    return proyecto

def dibujar_puntos(turtle):
    angulo = int(input("Ingrese el angulo en grados: "))
    potencia = int(input("Ingrese la potencia: "))
    for tiempo in range(1, 200):
        x = potencia * math.cos(math.radians(angulo)) * tiempo + origen_x
        y = potencia * math.sin(math.radians(angulo)) * tiempo - (((tiempo ** 2) * G) / 2) + origen_y
        turtle.goto(x, y)
window = Screen()
window.setup(1000, 400)

for _ in range(3):
    mi_tortuga = crear_tortuga()
    mi_tortuga.color(random.choice(['red', 'green', 'blue', 'purple', 'black']))
    dibujar_puntos(mi_tortuga)

window.exitonclick()