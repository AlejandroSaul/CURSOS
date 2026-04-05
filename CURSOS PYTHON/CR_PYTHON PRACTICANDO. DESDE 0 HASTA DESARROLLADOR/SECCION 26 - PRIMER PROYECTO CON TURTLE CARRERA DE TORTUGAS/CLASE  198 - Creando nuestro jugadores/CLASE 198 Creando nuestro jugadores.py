import turtle
import random

def crearEscenario():

    tortuga1.shape("turtle")
    tortuga2.shape("turtle")

    tortuga1.color("green")
    tortuga2.color("blue")

    tortuga1.penup()
    tortuga2.penup()

    tortuga1.sety(75)
    tortuga2.sety(-125)

    tortuga1.setx(200)
    tortuga2.setx(200)




turtle.Screen()
turtle.title("Proyecto 1")
tortuga1 = turtle.Turtle()
tortuga2 = turtle.Turtle()
crearEscenario()
turtle.done()




