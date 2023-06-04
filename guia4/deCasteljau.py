from turtle import *
import random
def dibujarLineas(dataset):
    pantalla.colormode(255)
    colorPunto = (random.randint(0,255), random.randint(0,255),
        random.randint(0,255))
    colorLinea = (random.randint(0,255), random.randint(0,255),
        random.randint(0,255))
    i = 0
    while i < len(dataset)-1:
        pen.color(colorLinea)
        pen.goto(dataset[i][0], dataset[i][1])
        pen.pendown()
        pen.goto(dataset[i+1][0], dataset[i+1][1])
        pen.penup()
        t_pos = deCasteljau(dataset[i][0], dataset[i][1],
                dataset[i+1][0], dataset[i+1][1])
        pen.goto(t_pos[0], t_pos[1])
        pen.color(colorPunto)
        pen.dot(5)
        i += 1
def deCasteljau(x1, y1, x2, y2):
    t_x = (x1 * (1-funcionT)) + (x2*funcionT)
    t_y = (y1 * (1-funcionT)) + (y2*funcionT)
    t_plot = (t_x, t_y)
    t_coords.append(t_plot)
    return t_plot
pantalla = Screen()
pantalla.screensize(1500,1000)
pantalla.title("Algoritmo de deCasteljau")
pen = Turtle()
pen.speed(5)
pantalla.colormode(255)
pen.penup()
pen.pensize(2)
funcionT = 0.85
t_coords = []
puntosControl = [[(0,0), (200,100), (400, 0)],
                [(0,0), (100,200), (300,200),
                (400,0)],
                [(-100,0), (0, 75), (200,120),
                (350,75), (400,0)],
                [(-100,0), (0, 100), (100,200),
                (200,200), (300, 100), (400,0)]]
for poligono in puntosControl:
    for puntocontrol in poligono:
        pen.goto(puntocontrol[0], puntocontrol[1])
        pen.dot(5)
    for punto in range(0, len(poligono)+1):
        dibujarLineas(poligono)
        poligono = t_coords
        t_coords = []
    pantalla.clearscreen()
pantalla.exitonclick()