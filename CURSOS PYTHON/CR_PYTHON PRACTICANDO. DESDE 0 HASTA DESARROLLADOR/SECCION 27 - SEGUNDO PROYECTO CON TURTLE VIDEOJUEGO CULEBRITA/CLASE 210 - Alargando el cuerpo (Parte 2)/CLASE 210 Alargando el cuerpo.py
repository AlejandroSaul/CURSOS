import turtle
import time
import random

pantalla = turtle.Screen()
serpiente = turtle.Turtle()
comida = turtle.Turtle()
cuerpo = [serpiente]
retraso = 0.01

def definicionValoresElementos():
    pantalla.setup(650,650)
    pantalla.bgcolor("black")
    pantalla.title("Culebrita")

    serpiente.speed(1)
    serpiente.shape("square")
    serpiente.penup()
    serpiente.goto(0,0)
    serpiente.direction = 'stop'
    serpiente.color('green')

    comida.shape("circle")
    comida.color("white")
    comida.penup()
    comida.goto(0,100)
    comida.speed(0)

def arriba():
    serpiente.direction ='up'
def abajo():
    serpiente.direction ='down'
def derecha():
    serpiente.direction ='right'
def izquierda():
    serpiente.direction ='left'

def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x+20)
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x-20)
    for index in range(totalElementosSerpiente -1 ,0,-1):
        coordXLastElement = cuerpo[index-1].xcor()
        coordYLastElement = cuerpo[index-1].ycor()
        cuerpo[index].goto(coordXLastElement,coordYLastElement)
        cuerpo[index].showturtle()    

def comprobarComer():
    if serpiente.distance(comida) < 20:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.hideturtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        cuerpo.append(nuevo_cuerpo)

definicionValoresElementos()

pantalla.listen()
pantalla.onkeypress(arriba,"Up")
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(derecha,"Right")
pantalla.onkeypress(izquierda,"Left")

while True:
    pantalla.update()
    totalElementosSerpiente = len(cuerpo)
    comprobarComer()

    if totalElementosSerpiente == 0 :
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)
    movimiento()
        
    time.sleep(retraso)



turtle.done()