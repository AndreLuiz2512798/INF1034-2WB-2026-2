import turtle
from random import randint
import tkinter as tk


def randomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))


def drawSquare(t, size):
  t.pd()
  t.begin_fill()
  t.fillcolor(randomColor())
  for i in range(4):
    t.fd(size)
    t.right(90)
  t.end_fill()
  t.pu()


def drawSquareFractal(t, j, size, step=50):
  if step < 0 or size < 1:
    return
  t.fd(size / 1.5)
  t.pd()
  t.lt(10)

  j.fd(size / 1.5)
  j.pd()
  j.lt(10)

  drawSquare(t, size)
  drawSquare(j, size)
  drawSquareFractal(t, j, size - 1, step - 1)

def drawPentaFractal(t, size):
  if size < 10:
    return
  for i in range(5):
    t.fd(size)
    drawPentaFractal(t, size / 2)
    t.lt(72)


def treeFractal(t, size, angle, nivel):
  if size < 40:
    return

  t.pd()
  t.fd(size)

  # right tree
  t.rt(angle)
  t.fd(size)
  treeFractal(t, size * 0.8, angle, nivel - 1)
  t.back(size)

  t.pencolor(0, 255 // nivel, 0)

  # central tree
  t.lt(angle)
  t.fd(size)
  treeFractal(t, size * 0.8, angle, nivel - 1)
  t.back(size)

  t.pencolor(0, 255 // nivel, 0)

  # left tree
  t.lt(angle)
  t.fd(size)
  treeFractal(t, size * 0.8, angle, nivel - 1)
  t.back(size)

  t.pencolor(0, 255 // nivel, 0)
  t.lt(-angle)
  t.back(size)


t = turtle.Turtle()
j = turtle.Turtle()
turtle.colormode(255)

screen = turtle.Screen()
screen.tracer(0)

desenho = 0

def atualizar(valor):
    valor = int(valor)
    t.clear()
    j.clear()
    t.pu()
    j.pu()

    if desenho == 0:
        t.goto(-100, -200)
        j.goto(100, -200)
        drawSquareFractal(t, j, valor, 60)

    elif desenho == 1:
      j.hideturtle()
      t.goto(-100, -100)
      t.setheading(0)
      t.pd()
      drawPentaFractal(t, valor)

    elif desenho == 2:
        j.hideturtle()
        t.goto(0, -200)
        t.setheading(90)
        treeFractal(t, 80, valor, 20)

    screen.update()


def proximoDesenho():
    global desenho
    desenho = (desenho + 1) % 3

    if desenho == 0:
      slider.config(from_=10, to=100)
      slider.set(40)

    elif desenho == 1:
      slider.config(from_=40, to=150)
      slider.set(100)

    elif desenho == 2:
        slider.config(from_=1, to=60)
        slider.set(40)

    atualizar(slider.get())


tela = screen.getcanvas().master

slider = tk.Scale(
    tela,
    from_=1,
    to=60,
    orient=tk.HORIZONTAL,
    command=atualizar
)
slider.pack(side=tk.BOTTOM)

botao = tk.Button(
    tela,
    text="Próximo desenho",
    command=proximoDesenho
)
botao.pack(side=tk.BOTTOM)

slider.set(40)
atualizar(40)

turtle.mainloop()