import turtle

pantalla = turtle.Screen()
tortuga = turtle.Turtle()

resultado = input("quieres imprimir una figura")
if resultado =="si":

    for i in range (4):
        tortuga.forward(100)
        tortuga.right(90)
    i=10
    while(i<=100):
        tortuga.circle(i)
        i+=10
else:
    print("ok")
turtle.done()