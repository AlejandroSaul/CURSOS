import turtle
import random

def crearEscenario():
    pantalla.bgcolor("#e7cfb9")

    tortuga1.hideturtle()
    tortuga2.hideturtle()

    tortuga1.shape("turtle")
    tortuga2.shape("turtle")

    tortuga1.color("green")
    tortuga2.color("blue")

    tortuga1.shapesize(2,2,2)
    tortuga2.shapesize(2,2,2)

    tortuga1.pensize(3)
    tortuga2.pensize(3)

    tortuga1.penup()
    tortuga2.penup()

    tortuga1.sety(60)
    tortuga2.sety(-140)

    tortuga1.setx(200)
    tortuga2.setx(200)


    tortuga1.pendown()
    tortuga2.pendown()
    tortuga1.circle(40)
    tortuga2.circle(40)
    tortuga1.penup()
    tortuga2.penup()

    tortuga1.goto(-200,100)
    tortuga2.goto(-200,-100)

    tortuga1.showturtle()
    tortuga2.showturtle()

def validarPosicion():
    print("Tortuga 1: ",tortuga1.pos())
    print("Tortuga 2: ",tortuga2.pos())

def mover():
    for i in range(200):
        numero1 = random.randint(1,10)
        numero2 = random.randint(1,10)
        tortuga1.forward(numero1)
        tortuga2.forward(numero2)
        validarPosicion()

        if tortuga1.pos() >= (200,60):
            print("T1")
            break
        elif tortuga2.pos() >= (200,-140):
            print("t2")
            break



pantalla = turtle.Screen()
turtle.title("Proyecto 1")
tortuga1 = turtle.Turtle()
tortuga2 = turtle.Turtle()
crearEscenario()
mover()
turtle.done()




