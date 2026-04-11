import turtle
import time
import random

retraso = 0.1

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("black")
s.title("Culebrita")

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color('green')

comida = turtle.Turtle()
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

s.listen()
s.onkeypress(arriba,"Up")
s.onkeypress(abajo,"Down")
s.onkeypress(derecha,"Right")
s.onkeypress(izquierda,"Left")


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
    


while True:
    s.update()
    if serpiente.distance(comida) < 20:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        comida.goto(x,y)

    time.sleep(retraso)
    movimiento()

turtle.done()