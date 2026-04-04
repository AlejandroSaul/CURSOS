import turtle

pantalla = turtle.Screen()
tortuga = turtle.Turtle()

tortuga.begin_fill()
tortuga.circle(100)
tortuga.end_fill()

tortuga.begin_fill()
tortuga.color("white")
tortuga.circle(10)
tortuga.end_fill()

tortuga.color("blue")
tortuga.shape("turtle")
#tortuga.shape("arrow")
#tortuga.shape("square")
#tortuga.shape("triangle")
#tortuga.shape("classic")
#tortuga.shape("circle")
tortuga.speed(1)
tortuga.penup()
tortuga.forward(100)
tortuga.pendown()
tortuga.forward(100)
tortuga.undo()
tortuga.clear()
tortuga.reset()

tortuga.forward(100)
tortuga.stamp()
tortuga.forward(100)
turtle.done()