import turtle

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("black")
s.title("Culebrita")

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.color('green')


turtle.done()