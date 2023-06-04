from turtle import *
import math
import random
def crear_tortuga(color, x, y):
    tortuga = Turtle(shape='turtle')
    tortuga.color(color)
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.speed(0)
    return tortuga

def dibujar_hiperbola(turtle_izquierda, turtle_derecha):
    a = int(input("Ingrese el valor de 'a': "))
    b = int(input("Ingrese el valor de 'b': "))
    # Dibujar sección izquierda de la hiperbola
    for theta in range(-190, 191, 5):
        rad = math.radians(theta)
        x = a * math.cosh(rad)
        y = b * math.sinh(rad)
        turtle_izquierda.goto(x + origen_x, y + origen_y)

    # Dibujar sección derecha de la hiperbola (inversa de la sección izquierda)
    for theta in range(190, -191, -5):
        rad = math.radians(theta)
        x = -a * math.cosh(rad)
        y = -b * math.sinh(rad)
        turtle_derecha.goto(x + origen_x, y + origen_y)
# Configuración de la ventana y la tortuga
window = Screen()
window.setup(1000, 800)
origen_x1 = 0
origen_x = 0
origen_y = 0
tortuga_izquierda = crear_tortuga('red', origen_x1, origen_y)
tortuga_derecha = crear_tortuga('blue', origen_x, origen_y)
dibujar_hiperbola(tortuga_izquierda, tortuga_derecha)
window.exitonclick()