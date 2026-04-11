import turtle
import time

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
serpiente.direction = 'right'
serpiente.color('green')



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
    #s.update()
    time.sleep(retraso)
    movimiento()

turtle.done()