from turtle import *

def aplicarReglas(ch):
    nuevaCadena = ''
    
    if ch == 'B':
        nuevaCadena = 'BBB'
    elif ch == 'A':
        nuevaCadena = 'ABA'
    else:
        nuevaCadena = ch

    return nuevaCadena

def procesarCadena(cadenaVieja):
    nuevaCadena = ''

    for ch in cadenaVieja:
        nuevaCadena = nuevaCadena + aplicarReglas(ch)

    return nuevaCadena

def crearSistemaL(numIters, axioma):
    cadenaInicio = axioma
    cadenaFin = ''
    
    for i in range(numIters):
        cadenaFin = procesarCadena(cadenaInicio)
        cadenaInicio = cadenaFin
    
    return cadenaFin

def dibujarSistemaL(aTurtle, instrucciones, angulo, distancia):
    for cmd in instrucciones:
        if cmd == 'A':
            aTurtle.forward(distancia)
        elif cmd == 'B':
            aTurtle.penup()
            aTurtle.setpos(aTurtle.xcor() + distancia, aTurtle.ycor())
            aTurtle.pendown()

def main():
    #tracer(0, 0)
    inst = crearSistemaL(3, 'A')
    print(inst)
    t = Turtle()
    wn = Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    dibujarSistemaL(t, inst, 60, 10)
    wn.listen()
    wn.mainloop()

main()
