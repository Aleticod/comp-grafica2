# PRACTICA DE COMPUTACION GRAFICA II
# NOMBRE: PFOCCORI QUISPE ALEX HARVEY
# CODIGO: 193837

# Importamos las librerias
from turtle import *
import math

# Ingresamos un vector de puntos vacio
p = []
n_p=int(input("Ingrese el numero de puntos : "))
for i in range(n_p):
    px,py=map(float,input(f"Ingrese las coordenadas del punto {i} : ").split())
    p.append(Vec2D(px, py))

# Invertimos el orden de los puntos
p_i = p[::-1]
tortuga = Turtle()
tortuga.penup()
# Graficamos los puntos
for posicion in p_i:
    tortuga.goto(posicion)
    tortuga.dot()

tortuga.pendown()

n = len(p) - 1
t = 0
while t <= 1:
    # Ecuacion generalizada de Bezier
    posicion = Vec2D(0,0)
    for i in range(len(p)):
        posicion += math.comb(n, i) * (1 - t) ** (n - i) * t ** i * p[i]

    # Grafica de los puntos
    tortuga.setheading(tortuga.towards(posicion))
    tortuga.goto(posicion)
    t += 0.01

screen = Screen()
screen.exitonclick()