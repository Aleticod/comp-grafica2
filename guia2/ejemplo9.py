from turtle import *
def crearSistemaL(numIters,axioma):
    cadenaInicio = axioma
    cadenaFin = ""
    for i in range(numIters):
        cadenaFin = procesarCadena(cadenaInicio)
        cadenaInicio = cadenaFin
    return cadenaFin

def procesarCadena(cadenaVieja):
    nuevaCadena = ""
    for ch in cadenaVieja:
        nuevaCadena = nuevaCadena + aplicarReglas(ch)
    return nuevaCadena

def aplicarReglas(ch):
    nuevaCadena = ""
    if ch == 'F':
        nuevaCadena = 'FF' # Regla 1
    elif ch == 'X':
        nuevaCadena = 'F+[[X]-X]-F[-FX]+X' # Regla 2
    else:
        nuevaCadena = ch # No se aplica regla, mantenemos el caracter
    return nuevaCadena

def dibujarSistemaL(aTurtle, instrucciones, angulo, distancia):
    aTurtle.penup()
    aTurtle.goto(-200, -300)
    aTurtle.pendown()
    pila = []
    aTurtle.setheading(65)
    for cmd in instrucciones:
        if cmd == "F":
            aTurtle.forward(distancia)
        elif cmd == "-":
            aTurtle.right(angulo)
        elif cmd == "+":
            aTurtle.left(angulo)
        elif cmd == "[":
            pila.append((aTurtle.position(), aTurtle.heading()))
        elif cmd == "]":
            position, heading = pila.pop()
            aTurtle.penup()
            aTurtle.goto(position)
            aTurtle.setheading(heading)
            aTurtle.pendown()

def main():
    tracer(0,0)
    inst = crearSistemaL(6, "X") # crea la cadena
    print(inst)
    t = Turtle() # crea la tortuga
    wn = Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(2)
    dibujarSistemaL(t, inst, 25, 4)
    wn.listen()
    wn.mainloop()
    
main()