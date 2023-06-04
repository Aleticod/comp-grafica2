from turtle import *

def aplicarReglas(ch):
    nuevaCadena = ''
    
    if ch == 'F':
        nuevaCadena = 'F-F++F-F'
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
        if cmd == 'F':
            aTurtle.forward(distancia)
        elif cmd == 'B':
            aTurtle.backward(distancia)
        elif cmd == '+':
            aTurtle.right(angulo)
        elif cmd == '-':
            aTurtle.left(angulo)

def main():
    tracer(0, 0)
    inst = crearSistemaL(4, 'F')
    print(inst)
    t = Turtle()
    wn = Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    dibujarSistemaL(t, inst, 60, 5)
    wn.listen()
    wn.mainloop()

main()