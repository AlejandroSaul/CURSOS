import turtle
import random

def crearEscenario():

    tortuga1.shape("turtle")
    tortuga2.shape("turtle")

    tortuga1.color("green")
    tortuga2.color("blue")

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




turtle.Screen()
turtle.title("Proyecto 1")
tortuga1 = turtle.Turtle()
tortuga2 = turtle.Turtle()
crearEscenario()
turtle.done()




