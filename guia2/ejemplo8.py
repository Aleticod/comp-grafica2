from turtle import *

def aplicarReglas(ch):
    nuevaCadena = ''
    
    if ch == 'F':
        nuevaCadena = 'F+G'
    elif ch == 'G':
        nuevaCadena = 'F-G'
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
    aTurtle.setheading(90)
    for cmd in instrucciones:
        if cmd == 'F':
            aTurtle.forward(distancia)
        elif cmd == 'G':
            aTurtle.forward(distancia)
        elif cmd == '-':
            aTurtle.left(angulo)
        elif cmd == '+':
            aTurtle.right(angulo)

def main():
    inst = crearSistemaL(10, 'F')
    print(inst)
    t = Turtle()
    wn = Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    dibujarSistemaL(t, inst, 90, 8)
    wn.listen()
    wn.mainloop()

main()