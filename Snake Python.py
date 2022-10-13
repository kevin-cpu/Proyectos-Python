import turtle
import time
import random

posponer = 0.15

#Marcador
marcador = 0
mayor_puntaje = 0

#configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width=600 ,height=600)
wn.tracer(0)

#configuracion serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("Green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Segmentos / cuerpo serpiente
segmentos = []

#marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Marcador: 0     Mayor Puntaje: 0", align ="center", font = ("courier", 20, "normal"))

#comida serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#funciones

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


def mov ():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    #colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #eliminar segmentos y limpiar lista de segemntos
        [a.hideturtle() for a in segmentos]
        segmentos.clear() 

        #resetear marcador
        marcador = 0
        texto.clear()
        texto.write("Marcador: {}     Mayor Puntaje: {}".format(marcador, mayor_puntaje), 
        align ="center", font = ("courier", 20, "normal"))

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #eliminar segmentos y limpiar lista de segemntos
            [a.hideturtle() for a in segmentos]
            segmentos.clear() 

            #resetear marcador
            marcador = 0
            texto.clear()
            texto.write("Marcador: {}     Mayor Puntaje: {}".format(marcador, mayor_puntaje), 
            align ="center", font = ("courier", 20, "normal"))
            
    #colision comida 
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        #estilo de cuerpo
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("Grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #aumentar marcador
        marcador += 5

        if marcador > mayor_puntaje:
            mayor_puntaje = marcador

        texto.clear()
        texto.write("Marcador: {}     Mayor Puntaje: {}".format(marcador, mayor_puntaje), 
        align ="center", font = ("courier", 20, "normal"))

    #moviento del cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()
    time.sleep(posponer)