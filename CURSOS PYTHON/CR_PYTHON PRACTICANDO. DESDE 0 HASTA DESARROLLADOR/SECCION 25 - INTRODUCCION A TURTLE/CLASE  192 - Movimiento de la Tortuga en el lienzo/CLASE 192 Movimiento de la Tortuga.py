import turtle

pantalla = turtle.Screen()
tortuga = turtle.Turtle()

tortuga.goto(100,100)
tortuga.goto(-100,100)
tortuga.home() # lo mismo que tortuga.goto(0,0)


tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)

turtle.done()