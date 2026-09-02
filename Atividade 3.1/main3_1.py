from turtle import *
from random import randint
from time import sleep

t = Turtle()
# t.shape("turtle")

def desenha_triangulo(x, y, lado, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    for count in range(3):
        t.forward(lado)
        t.left(120)
    t.end_fill()

def desenha_retangulo(x, y, base, altura, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    for count in range(2):
        t.forward(base)
        t.left(90)
        t.forward(altura)
        t.left(90)
    t.end_fill()

def desenha_pentagono(x, y, lado, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    for count in range(5):
        t.forward(lado)
        t.left(72)
    t.end_fill()

def desenha_hexagono(x, y, lado, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    for count in range(6):
        t.forward(lado)
        t.left(60)
    t.end_fill()

def cria_plano():
    t.pu()
    t.goto(-400, 0)
    t.pd()
    t.goto(400,0)
    t.stamp()
    t.pu()
    t.goto(0, -400)
    t.left(90)
    t.pd()
    t.goto(0, 400)
    t.stamp()
    t.pu()
    t.right(90)

def desenha_poligono(x, y, lado, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.fillcolor(cor)
    t.begin_fill()
    for count in range(lado):
        t.forward(tamanho)
        t.left(360/lado)
    t.end_fill()

cria_plano()

#Triangulo
x = randint(0, 400)
y = randint(0, 400)
lado = float(textinput("Escolha do tamanho do lado", "Digite o tamanho do lado do triângulo: "))
var_color = textinput("Escolha da cor", "Digite a cor do triângulo")
desenha_triangulo(x, y, lado, var_color)

#Retangulo
x = randint(-400, 0)
y = randint(0, 400)
lado = float(textinput("Escolha do tamanho da base", "Digite o tamanho da base do retângulo: "))
altura = float(textinput("Escolha do tamanho da altura", "Digite o tamanho da altura do retângulo: "))
var_color = textinput("Escolha da cor", "Digite a cor do retângulo")
desenha_retangulo(x, y, lado, altura, var_color)

#Pentagono
x = randint(-400, 0)
y = randint(-400, 0)
lado = float(textinput("Escolha do tamanho do lado", "Digite o tamanho do lado do pentagono: "))
var_color = textinput("Escolha da cor", "Digite a cor do pentagono")
desenha_pentagono(x, y, lado, var_color)

#Hexagono
x = randint(0, 400)
y = randint(-400, 0)
lado = float(textinput("Escolha do tamanho do lado", "Digite o tamanho do lado do hexagono: "))
var_color = textinput("Escolha da cor", "Digite a cor do hexagono")
desenha_hexagono(x, y, lado, var_color)

#Poligono qualquer
x = randint(-400, 400)
y = randint(-400, 400)
lado = int(textinput("Escolha dos lado", "Digite quantos lados tem o poligono: "))
tamanho = float(textinput("Escolha do tamanho do lado", "Digite o tamanho do lado do poligono: "))
var_color = textinput("Escolha da cor", "Digite a cor do poligono")
desenha_poligono(x, y, lado, tamanho, var_color)

mainloop()