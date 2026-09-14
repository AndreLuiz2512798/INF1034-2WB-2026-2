from turtle import *
from time import sleep
from math import sqrt
from random import randint

def calcula_raiz(x):
    return sqrt(x)

def calcula_fracao(x):
    return 1/x

def calcula_2_elevado(x):
    return 2**x

def calcula_menos_5(x):
    return 5-x**2

def calcula_x_quadrado(x):
    return x**2 - 5*x + 6

def calcula_x_elevado_3(x):
    return x**3 - x**2 - x + 1

def corrida(n):
    for x in range(n):
        list(x= Turtle())
        x.shape("turtle")
        x.goto(-200, 100 + (x*10))

    for num in range(30):
        list.fd(randint(5, 10))

t = Turtle()
t.speed(0)

def desenha_plano():
    t.pu()
    t.goto(-300, 0)
    t.pd()
    t.goto(300, 0)
    t.stamp()

    t.pu()
    t.goto(0, -300)
    t.pd()
    t.goto(0, 300)
    t.lt(90)
    t.stamp()
    t.rt(90)

desenha_plano()

t.color("blue")
t.pu()
t.goto(0, calcula_raiz(0))
t.pd()
for x in range(1, 150):
    t.goto(2*x, calcula_raiz(2*x))

sleep(2)
t.clear()

t.color("black")
desenha_plano()

t.color("blue")
t.pu()
t.goto(-100, 100 * calcula_fracao(-100))
t.pd()
for x in range(-100, 0):
    t.goto(x, 100 * calcula_fracao(x))
t.pu()
t.goto(0.1, 100 * calcula_fracao(1))
t.pd()
for x in range(1, 101):
    t.goto(x, 100 * calcula_fracao(x))

sleep(2)
t.clear()

t.color("black")
desenha_plano()

t.color("blue")
t.pu()
t.goto(-60, calcula_2_elevado(-60))
t.pd()
for x in range(-59, 6):
    t.goto(2*x, calcula_2_elevado(2*x))

sleep(2)
t.clear()

t.color("black")
desenha_plano()

t.color("blue")
t.pu()
t.goto(-200, calcula_menos_5(-200))
t.pd()
for x in range(-99, 101):
    t.goto(2*x, calcula_menos_5(2*x))

sleep(2)
t.clear()

t.color("black")
desenha_plano()

t.color("blue")
t.pu()
t.goto(-200, calcula_x_quadrado(-200))
t.pd()
for x in range(-99, 101):
    t.goto(2*x, calcula_x_quadrado(2*x))

sleep(2)
t.clear()

t.color("black")
desenha_plano()

t.color("blue")
t.pu()
t.goto(-100, calcula_x_elevado_3(-100))
t.pd()
for x in range(-99, 101):
    t.goto(x, calcula_x_elevado_3(x))

# sleep(2)
# t.clear()

# t.color("black")

# corrida(3)

mainloop()