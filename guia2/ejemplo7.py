from turtle import *

def aplicarReglas(ch):
    nuevaCadena = ''
    
    if ch == 'B':
        nuevaCadena = 'A+B+A'
    elif ch == 'A':
        nuevaCadena = 'B-A-B'
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
    aTurtle.setheading(0)
    for cmd in instrucciones:
        if cmd == 'A':
            aTurtle.forward(distancia)
        elif cmd == 'B':
            aTurtle.forward(distancia)
        elif cmd == '+':
            aTurtle.left(angulo)
        elif cmd == '-':
            aTurtle.right(angulo)

def main():
    inst = crearSistemaL(8, 'A')
    print(inst)
    t = Turtle()
    wn = Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    dibujarSistemaL(t, inst, 60, 1)
    wn.listen()
    wn.mainloop()

main()