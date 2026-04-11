import turtle
import time
import random

pantalla = turtle.Screen()
serpiente = turtle.Turtle()
comida = turtle.Turtle()
cuerpo = [serpiente]
retraso = 0.01
marcador = 0
marcadorMayor = 0

def definicionValoresElementos():
    pantalla.setup(650,650)
    pantalla.bgcolor("#99a681")
    pantalla.title("Culebrita")

    serpiente.speed(1)
    serpiente.shape("square")
    serpiente.penup()
    serpiente.goto(0,0)
    serpiente.direction = 'stop'
    serpiente.color('#050a07')

    comida.shape("square")
    comida.color("#82352d")
    comida.penup()
    comida.goto(0,100)
    comida.speed(0)
    
    global texto
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color('#050a07')
    texto.penup()
    texto.hideturtle()
    texto.goto(0,-260)
    texto.write("Marcador: 0 \t Marcador mas alto: 0", align="center", font=("verdana", 20, "normal"))

def arriba():
    serpiente.direction ='up'
def abajo():
    serpiente.direction ='down'
def derecha():
    serpiente.direction ='right'
def izquierda():
    serpiente.direction ='left'

def movimiento():
    for index in range(totalElementosSerpiente -1 ,0,-1):
        coordXLastElement = cuerpo[index-1].xcor()
        coordYLastElement = cuerpo[index-1].ycor()
        cuerpo[index].goto(coordXLastElement,coordYLastElement)
        cuerpo[index].showturtle()    

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

def comprobarComer():
    global marcador, marcadorMayor
    if serpiente.distance(comida) < 20:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        comida.goto(x,y)

        ultimaPosicionX = cuerpo[len(cuerpo)-1].xcor()
        ultimaPosicionY = cuerpo[len(cuerpo)-1].ycor()
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.hideturtle()
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(ultimaPosicionX,ultimaPosicionY)
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("#050a07")

        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcadorMayor:
            marcadorMayor = marcador
        texto.clear()
        texto.write("Marcador: {} \t Marcador mas alto: {}".format(marcador,marcadorMayor), align="center", font=("verdana", 20, "normal")) 

def reiniciarJuego():
    global marcador
    global texto
    for i in cuerpo[1:]:
        i.clear() #limpiamos el objeto 
        i.hideturtle() #Ocultamos el objeto
    cuerpo.clear() # Limpiamos la lista
    cuerpo.append(serpiente) # añadimos nuevamente el objeto turtle
    serpiente.home()
    serpiente.showturtle()
    serpiente.direction = 'stop'
    marcador = 0
    texto.clear()
    texto.write("Marcador: {} \t Marcador mas alto: {}".format(marcador,marcadorMayor), align="center", font=("verdana", 20, "normal")) 

def colicionPantalla():
    if serpiente.xcor() > 325 or serpiente.xcor() < -325 or serpiente.ycor() > 325 or serpiente.ycor() < -325:
        time.sleep(0.1)
        reiniciarJuego()

def colicionCuerpo():    
    for i in range (1,len(cuerpo)):
        if cuerpo[i].distance(serpiente) < 20:
            reiniciarJuego()
            break

definicionValoresElementos()
pantalla.listen()
pantalla.onkeypress(arriba,"Up")
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(derecha,"Right")
pantalla.onkeypress(izquierda,"Left")

while True:

    totalElementosSerpiente = len(cuerpo)
    
    movimiento()

    colicionPantalla()

    colicionCuerpo()

    comprobarComer()

    pantalla.update()
        
    time.sleep(retraso)

turtle.done()