import turtle

pantalla = turtle.Screen()
tortuga = turtle.Turtle()

tortuga.speed(1)
tortuga.circle(10)
tortuga.speed(10)
tortuga.circle(50)
tortuga.dot(30)

tortuga.hideturtle()
tortuga.speed(1)
tortuga.circle(40)
tortuga.showturtle()
tortuga.circle(100)

tortuga.setx(100)
tortuga.sety(-100)

turtle.done()