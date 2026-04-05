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
        dado = [1,2,3,4,5,6]
        numero1 = random.randint(1,10)
        numero2 = random.randint(1,10)

        validarPosicion()

        if tortuga1.pos() >= (200,60):
            print("El ganador es la toertuga 1")
            break
        elif tortuga2.pos() >= (200,-140):
            print("El ganador es la toertuga 2")
            break
        else:
            turno1 = input("Presiona la tecla enter")
            turno1 = random.choice(dado)
            print("tu numero es ",turno1," Avanzas: ",turno1*5)
            tortuga1.forward(turno1*5)

            turno2 = input("Presiona la tecla enter")
            turno2 = random.choice(dado)
            print("tu numero es ",turno2," tu numero es: ",turno2*5)
            tortuga2.forward(turno2*5)



pantalla = turtle.Screen()
turtle.title("Proyecto 1")
tortuga1 = turtle.Turtle()
tortuga2 = turtle.Turtle()
crearEscenario()
bandera = True
while(bandera):
    mover()
    letra = input("¿Quiere iniciar nuevamente? S para continuar cualquier otra cosa para salir")
    if letra == 'S' or letra== 's':
        tortuga1.goto(-200,100)
        tortuga2.goto(-200,-100)
    else:
        bandera = False
turtle.done()




